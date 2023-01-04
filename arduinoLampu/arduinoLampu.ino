void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  String perintah = "";
  while (Serial.available() > 0) {
    char karakter = Serial.read();
    perintah = perintah + karakter;
    delay(20);
  }

  if (perintah.equals("")) {
    return;
  } else if (perintah.equals("Hidupkan Hijau")) {
    digitalWrite(13, LOW);
    digitalWrite(12, HIGH);
    digitalWrite(11, LOW);
    digitalWrite(10, LOW);
  } else if (perintah.equals("Hidupkan Merah")) {
    digitalWrite(13, HIGH);
    digitalWrite(12, LOW);
    digitalWrite(11, LOW);
    digitalWrite(10, LOW);
  } else if (perintah.equals("Hidupkan Biru")) {
    digitalWrite(13, LOW);
    digitalWrite(12, LOW);
    digitalWrite(11, HIGH);
    digitalWrite(10, LOW);
  } else if (perintah.equals("Hidupkan Kuning")) {
    digitalWrite(13, LOW);
    digitalWrite(12, LOW);
    digitalWrite(11, LOW);
    digitalWrite(10, HIGH);
  } else if (perintah.equals("Matikan Lampu")) {
    digitalWrite(13, LOW);
    digitalWrite(12, LOW);
    digitalWrite(11, LOW);
    digitalWrite(10, LOW);
  } else if (perintah.equals("Hidupkan Merah Kuning")) {
    digitalWrite(13, HIGH);
    digitalWrite(12, LOW);
    digitalWrite(11, LOW);
    digitalWrite(10, HIGH);
  } else if (perintah.equals("Hidupkan Merah Hijau")) {
    digitalWrite(13, HIGH);
    digitalWrite(12, HIGH);
    digitalWrite(11, LOW);
    digitalWrite(10, LOW);
  } else if (perintah.equals("Hidupkan Merah Biru")) {
    digitalWrite(13, HIGH);
    digitalWrite(12, LOW);
    digitalWrite(11, HIGH);
    digitalWrite(10, LOW);
  } else if (perintah.equals("Hidupkan Kuning Hijau")) {
    digitalWrite(13, LOW);
    digitalWrite(12, HIGH);
    digitalWrite(11, LOW);
    digitalWrite(10, HIGH);
  } else if (perintah.equals("Hidupkan Kuning Biru")) {
    digitalWrite(13, LOW);
    digitalWrite(12, LOW);
    digitalWrite(11, HIGH);
    digitalWrite(10, HIGH);
  } else if (perintah.equals("Hidupkan Hijau Biru")) {
    digitalWrite(13, LOW);
    digitalWrite(12, HIGH);
    digitalWrite(11, LOW);
    digitalWrite(10, HIGH);
  } else if (perintah.equals("Hidupkan Merah Kuning Hijau")) {
    digitalWrite(13, HIGH);
    digitalWrite(12, HIGH);
    digitalWrite(11, LOW);
    digitalWrite(10, HIGH);
  } else if (perintah.equals("Hidupkan Merah Kuning Biru")) {
    digitalWrite(13, HIGH);
    digitalWrite(12, LOW);
    digitalWrite(11, HIGH);
    digitalWrite(10, HIGH);
  } else if (perintah.equals("Hidupkan Merah Hijau Biru")) {
    digitalWrite(13, HIGH);
    digitalWrite(12, HIGH);
    digitalWrite(11, HIGH);
    digitalWrite(10, LOW);
  } else if (perintah.equals("Hidupkan Kuning Hijau Biru")) {
    digitalWrite(13, LOW);
    digitalWrite(12, HIGH);
    digitalWrite(11, HIGH);
    digitalWrite(10, HIGH);
  }
  else if (perintah.equals("Hidupkan Lampu")) {
    digitalWrite(13, HIGH);
    digitalWrite(12, HIGH);
    digitalWrite(11, HIGH);
    digitalWrite(10, HIGH);
  }

}
