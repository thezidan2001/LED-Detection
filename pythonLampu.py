import numpy as np
import cv2
import serial
import time

# Menghubungkan dengan port arduino
arduino = serial.Serial(port='COM3', baudrate=115200)

# Variabel video dengan menggunakan library open cv untuk membuka kamera
video = cv2.VideoCapture(1)

# Inisialisasi result yang akan digunakan jika ada kode yang berubah
result = "0000"

# Loop untuk membuka terus window
while True:
    # Variabel ret dan img membaca video dari kamera
    ret, img = video.read()
    # Memberikan Warna
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Membuat batas dari warna hijau, merah, biru, dan kuning
    lower_green = np.array([40, 70, 80])
    upper_green = np.array([70, 255, 255])

    lower_red = np.array([161, 155, 84])
    upper_red = np.array([179, 255, 255])

    lower_blue = np.array([100, 100, 100])
    upper_blue = np.array([120, 255, 255])

    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([40, 255, 255])

    # Warna yang sesuai akan di masking
    mask1 = cv2.inRange(hsv, lower_green, upper_green)
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    mask3 = cv2.inRange(hsv, lower_blue, upper_blue)
    mask4 = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Mencari bentuk dari masking
    cnts1, hei = cv2.findContours(
        mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnts2, hei = cv2.findContours(
        mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnts3, hei = cv2.findContours(
        mask3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnts4, hei = cv2.findContours(
        mask4, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Jika Warna dideteksi akan membuat angka menjadi 1
    c_green = 0
    c_red = 0
    c_blue = 0
    c_yellow = 0

    # Membuat persegi atau persegi panjang, agar tahu mana objek yang sedang dideteksi
    for c in cnts1:
        area = cv2.contourArea(c)
        if area > 300:
            c_green = +1
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    for c in cnts2:
        area = cv2.contourArea(c)
        if area > 300:
            c_red = +1
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    for c in cnts3:
        area = cv2.contourArea(c)
        if area > 300:
            c_blue = +1
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    for c in cnts4:
        area = cv2.contourArea(c)
        if area > 300:
            c_yellow = +1
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Menampilkan windows
    cv2.imshow("Frame", img)

    # Membuat variabel action untuk menggabungkan warna deteksi
    action = f'{c_green}{c_red}{c_blue}{c_yellow}'
    print(action)

    # Mengatur frame agar tidak terlalu cepat
    time.sleep((1 / 60))

    # Key q untuk menutup window
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

    # Kondisi untuk menghidupkan lampu
    if(result != action):
        if action == "1000":
            arduino.write(b'Hidupkan Hijau')
        elif action == "0100":
            arduino.write(b'Hidupkan Merah')
        elif action == "0010":
            arduino.write(b'Hidupkan Biru')
        elif action == "0001":
            arduino.write(b'Hidupkan Kuning')
        elif action == "0000":
            arduino.write(b'Matikan Lampu')
        elif action == "0101":
            arduino.write(b'Hidupkan Merah Kuning')
        elif action == "1100":
            arduino.write(b'Hidupkan Merah Hijau')
        elif action == "0110":
            arduino.write(b'Hidupkan Merah Biru')
        elif action == "1001":
            arduino.write(b'Hidupkan Kuning Hijau')
        elif action == "0011":
            arduino.write(b'Hidupkan Kuning Biru')
        elif action == "1010":
            arduino.write(b'Hidupkan Hijau Biru')
        elif action == "1101":
            arduino.write(b'Hidupkan Merah Kuning Hijau')
        elif action == "0111":
            arduino.write(b'Hidupkan Merah Kuning Biru')
        elif action == "1110":
            arduino.write(b'Hidupkan Merah Hijau Biru')
        elif action == "1011":
            arduino.write(b'Hidupkan Kuning Hijau Biru')
        elif action == "1111":
            arduino.write(b'Hidupkan Lampu')
        result = action

# Menutup semua window
video.release()
cv2.destroyAllWindows()
