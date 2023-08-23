import RPi.GPIO as GPIO  #import library GPIO untuk pin 
import time #import librarty time untuk delay 

GPIO.setmode(GPIO.BOARD) #menentuka GPIO mode board atau BCM 

TRIGGER = 16
ECHO = 18
servoPIN = 11

GPIO.setup(TRIGGER, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) #pin11 jadi PWM 50Hz #inisliasi pin GPIO menjadi PWM,frekuensi 
p.start(5.5) #start servo 
 
def jarak():
    GPIO.output(TRIGGER, True) #mengeluarkan sinyal
    time.sleep(0.00001) #delay akan menetukan frekuensi 
    GPIO.output(TRIGGER, False) #tidak mengeluarkan sinyal 
  
    mulai = time.time() #fungsi time untuk mencatat waktu 
    berhenti = time.time() #inisialisasi waktu 

    while GPIO.input(ECHO) == 0: #ketika echo tdk menerima sinyal di catat 
        mulai = time.time()
 
    while GPIO.input(ECHO) == 1: #ketika echo menerima sinyal 
        berhenti = time.time()

    waktu = berhenti - mulai #dapat waktu dari echo ke triger ke echo
    jarak = (waktu * 34300) / 2 #waktu yang didapat 1 balikan (nilai kalibrasi yang diubah yang 34300)
 
    return jarak #mengeluarkan nilai jarak 
 
  try: 
    while True: #pengulangan 
        jrk = jarak() #manggil jaral 
        print ("Jarak = %.1f cm" % jrk)
            
        if(jrk <= 8): #kurang dari 8 
          p.ChangeDutyCycle(18) #servo akan bergerak bertahan 2 detik lalu ke posisi awal 
          time.sleep(2)
          p.ChangeDutyCycle(5.5)
          print("nyala") #print nyala 
            
    time.sleep(1) #delay scan sensor 

  except KeyboardInterrupt: #untuk memberhentikan program 
    print("Program dihentikan")
    GPIO.cleanup()