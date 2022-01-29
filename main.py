'''

INSTALL THE MODULES
Via - pip install "NAME OF MODULE"
Run the above command in cmd.
then click run

OR OPEN CMD HERE AND TYPE
"pip install -r requirements.txt"
MAKE SURE requirements.txt IS IN THIS FOLDER

WELCOME TO THE SRC OF THE GAME
FIRST LET'S IMPORT ALL THE
REQUIRED MODULES
'''
from tkinter import *
import os
import random
import time
import turtle
import datetime
import pyttsx3
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame import font, mixer
mixer.init()
mixer.music.load("song.wav")
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math
import json
import csv

print("KINDLY SET YOUR DEVICE VOULME TO 100%")
time.sleep(8)
mixer.music.play(-1)
print("**********************************************************")
# default audio device using PyCAW
try:
  devices = AudioUtilities.GetSpeakers()
  interface = devices.Activate(
      IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
  volume = cast(interface, POINTER(IAudioEndpointVolume))
  # current volume 
  currentVolumeDb = volume.GetMasterVolumeLevel()
  volume.SetMasterVolumeLevel(currentVolumeDb - 6.0, None)
except:
  print("YOU CAN'T HEAR THE SOUNDS")
print("***********************************************")
time.sleep(1)
print("THIS IS A TRULY ORIGINAL WORK OF Mst. ARYA SINGH\
 AND NOT TO BE REPUBLISHED.")
time.sleep(4)
print("NO DATA IS SHARED WITH THE CREATOR AS THE GAME\
 IS TRULY OFFLINE. ENJOY!!")
time.sleep(1)
print("***********************************************")
time.sleep(4)
print("STARTING LOGIN...")
def delete2():
  screen3.destroy()


def delete3():
  screen4.destroy()


def delete4():
  screen5.destroy()


def login_sucess():
  global screen3
  screen3 = Toplevel(screen)
  screen3.title("SUCCESS")
  screen3.geometry("300x150")
  Label(screen3, text="LOGIN SUCCESS",fg='green',font=('Times New Roman',14,'bold')).pack()
  Button(screen3, text="OK",fg='black',font=('Times New Roman',12,'bold'),command=delete2).pack()
  
  


def password_not_recognised():
  global screen4
  screen4 = Toplevel(screen)
  screen4.title("ERROR")
  screen4.geometry("300x150")
  Label(screen4, text="PASSWORD ERROR",fg='red',font=('Times New Roman',14,'bold')).pack()
  Button(screen4, text="DONE",fg='green',font=('Times New Roman',12,'bold') ,command=delete3).pack()


def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("ERROR")
  screen5.geometry("300x150")
  Label(screen5, text="USER NOT FOUND",fg='red',font=('Times New Roman',14,'bold')).pack()
  Button(screen5, text="DONE", fg='green',font=('Times New Roman',12,'bold'),command=delete4).pack()


def register_user():
  print("REGISTERED")

  username_info = username.get()
  password_info = password.get()

  file = open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()

  username_entry.delete(0, END)
  password_entry.delete(0, END)

  Label(screen1, text="REGISTRATION SUCCESS",
        fg="green",font=("Times New Roman", 14,'bold')).pack()

a = 0
def login_verify():

  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)

  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    if password1 in verify:
        login_sucess()
        global a
        a=a+1
    else:
        password_not_recognised()

  else:
        user_not_found()
  return a
  
  


def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("REGISTER")
  screen1.geometry("600x300")
  
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()

  Label(screen1, text = "PLEASE ENTER YOUR DETAILS",fg='red',font=("Times New Roman", 14,'bold')).pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "USERNAME * ",fg='cyan',font=("Times New Roman", 12,'bold')).pack()
 
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  Label(screen1, text = "PASSWORD * ",fg='cyan',font=("Times New Roman", 12,'bold')).pack()
  password_entry =  Entry(screen1, textvariable = password)
  password_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "REGISTER", width = 20, height = 2, fg='green',font=("Times New Roman", 12,'bold'),command = register_user).pack()

def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("LOGIN")
  screen2.geometry("600x300")
  Label(screen2, text = "PLEASE ENTER YOUR DETAILS",fg='red',font=("Times New Roman", 12,'bold')).pack()
  Label(screen2, text = "").pack()

  global username_verify
  global password_verify
  
  username_verify = StringVar()
  password_verify = StringVar()

  global username_entry1
  global password_entry1
  
  Label(screen2, text = "USERNAME * ",fg='cyan',font=("Times New Roman", 12,'bold')).pack()
  username_entry1 = Entry(screen2, textvariable = username_verify)
  username_entry1.pack()
  Label(screen2, text = "").pack()
  Label(screen2, text = "PASSWORD * ",fg='cyan',font=("Times New Roman", 12,'bold')).pack()
  password_entry1 = Entry(screen2, textvariable = password_verify)
  password_entry1.pack()
  Label(screen2, text = "").pack()
  Button(screen2, text = "LOGIN", width = 20, height = 2, fg='green',font=("Times New Roman", 12,'bold'),command = login_verify).pack()

  
  
def main_screen():
  global screen
  screen = Tk()
  screen.geometry("600x300")
  screen.title("GAME LOGIN")
  screen.configure(background='black')
  Label(text = "LOGIN TO YOUR ACCOUNT", fg='black',bg='white', width = "600", height = "4", font = ("Times New Roman", 16)).pack()
  Label(text = "").pack()
  Button(text = "LOGIN", height = "4", width = "60", fg='white',bg='black',font=("Times New Roman", 14,'bold'),command = login).pack()
  Label(text = "").pack()
  Button(text = "REGISTER",height = "4", width = "60", fg='white',bg='black',font=("Times New Roman", 14,'bold'),command = register).pack()

  screen.mainloop()

main_screen()

if a == 1:
  print("LOGIN SUCCESS...")
  mixer.music.stop()
  time.sleep(1)
  soundpro = str(input("PRESS 1 FOR MALE VOICE AND 2 FOR FEMALE : "))
  engine = pyttsx3.init('sapi5')
  voices = engine.getProperty('voices')
  if soundpro == '2':
    engine.setProperty('voice', voices[1].id)
  elif soundpro == '1':
    engine.setProperty('voice', voices[0].id)        
  else:
    print("YOU HAVE SELECTED DEFAULT FEMALE VOICE")
    engine.setProperty('voice', voices[1].id)
  time.sleep(1)
  def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    return speak
  def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
      speak("Good Morning!")
    elif hour > 12 and hour < 18:
      speak("Good Afternoon!")
    else:
      speak("Good Evening!")
  def rating():
    print(star)
    time.sleep(2)
    print("RATING")
    speak("PLEASE PROVIDE A MOMENT TO RATE OUR GAME")
    speak("PLEASE RATE OUT OF 5 STARS")
    rating = input()
    rating.lower()
    if rating == '5' or rating == "5 stars" or rating == "5stars" or rating == "5 star" or rating == "5star":
      print("WE ARE GLAD TO SEE THAT YOU ARE HAPPY!!")
      speak("WE ARE GLAD TO SEE THAT YOU ARE HAPPY!!")
      time.sleep(2)
      speak("ONCE AGAIN , NAMASTE")
      print("THANKS FOR PLAYING")
      speak("THANKS FOR PLAYING")

    elif '5 stars' > rating > '3 stars' or '5 star' > rating > '3 star' or '5stars' > rating > '3stars' or "5star" > rating > "3star" or '5' > rating > '3':
      print("WE WILL TRY TO IMPROVE")
      speak("WE WILL TRY TO IMPROVE!!")
      time.sleep(2)
      speak("ONCE AGAIN , NAMASTE")
      print("THANKS FOR PLAYING")
      speak("THANKS FOR PLAYING")

    else:
      line = "thank you for the feedback, we will try to improve "
      asik = line.upper()
      print(asik)
      speak("thank you for the feedback, we will try to improve")
      time.sleep(2)
      speak("ONCE AGAIN , NAMASTE")
      print("THANKS FOR PLAYING")
      speak("THANKS FOR PLAYING") 
  star = "*********************"
  print(star)
  time.sleep(2)
  print("WEAR HEADPHONES FOR BETTER EXPERIENCE")
  time.sleep(1)
  print(star)
  time.sleep(2)
  print("HI THERE!!, WHAT'S YOUR NAME?")
  speak("HIGH THERE , WHAT'S YOUR NAME?")
  mdma = input()
  yourname = mdma.lower()
  yourname = '_'.join(f"{yourname}")
  time.sleep(1)
  # GREETING THE USER
  if __name__ == "__main__":
    wishMe()
  turial = 'notdone'
  try:
    with open(f'{yourname}.csv','r') as t:
      print(f"WELCOME AGAIN {mdma.upper()}")
      speak(f"WELCOME AGAIN {mdma.upper()}")
      turial= 'done'
  except:
    print(f"NICE TO MEET YOU {mdma.upper()}")
    speak(f"NICE TO MEET YOU {mdma.upper()}")
    time.sleep(1)
    speak("I , AM APEX")
    speak("CREATED BY AAREYA SINGH")
  f = open(f'{yourname}.csv','a+',newline="")
  csv_reader = csv.reader(f)
  csv_writer = csv.writer(f)
  # PRINTING INFO
  print(star)
  time.sleep(1)
  print("WELCOME TO SPACE INVADERS!!")
  speak("WELCOME TO SPACE INVADERS!!")
  time.sleep(1)
  print("NOW LOADING....")
  speak("NOW LOADING")
  
  #RIGHT LEFT AND SHOOT TUTORIAL
  if turial != 'done':
    doyou = input("DO YOU WANT TO SEE A TUTORIAL? : ")
    if doyou.lower()=='yes':
      print("PRESS RIGHT ARROW TO MOVE RIGHT")
      speak("PRESS RIGHT ARROW TO MOVE RIGHT")
      print("PRESS LEFT ARROW TO MOVE LEFT")
      speak("PRESS LEFT ARROW TO MOVE LEFT")
      print("PRESS SPACE BAR TO SHOOT")
      speak("PRESS SPACE BAR TO SHOOT")
      print("TRY IT OUT YOURSELF")
      speak("TRY IT OUT YOURSELF")   
      print("YOU ONLY HAVE 60 SECONDS TO TEST")
      speak("YOU ONLY HAVE 60 SECONDS TO TEST")
      time.sleep(2)
      start_time = time.time()

      # Set up the screen
      wn = turtle.Screen()
      wn.bgcolor("black")
      wn.title("Space Invaders")
      wn.register_shape("bullet.gif")
      # Draw border
      border_pen = turtle.Turtle()
      border_pen.speed(0)
      border_pen.color("white")
      border_pen.penup()
      border_pen.setposition(-300,-300)
      border_pen.pendown()
      border_pen.pensize(3)
      for side in range(4):
        border_pen.fd(600)
        border_pen.lt(90)
      border_pen.hideturtle()	

      # Create the player turtle
      player = turtle.Turtle()
      player.color("blue")
      player.shape("triangle")
      player.penup()
      player.speed(0)
      player.setposition(0, -250)
      player.setheading(90)

      playerspeed = 0

      bullet = turtle.Turtle()
      bullet.color("yellow")
      bullet.shape("bullet.gif")
      bullet.penup()
      bullet.speed(0)
      bullet.setheading(90)
      bullet.hideturtle()

      bulletspeed = 120
      bulletstate = "ready"

      def move_left():
        global playerspeed
        playerspeed = -6
        
      def move_right():
        global playerspeed
        playerspeed = 6

      def fire_bullet():
        
        global bulletstate
        if bulletstate == "ready":
          bulletstate = "fire"
          x = player.xcor()
          y = player.ycor() + 10
          bullet.setposition(x, y)
          bullet.showturtle()
        
      wn.listen()
      wn.onkeypress(move_left, "Left")
      wn.onkeypress(move_right, "Right")
      wn.onkey(fire_bullet, "space")
      while True:
        # Move the player
        player.setx(player.xcor() + playerspeed)
        
        # Check borders
        if player.xcor() > 285:
          player.setx(285)
          playerspeed = 0

        elif player.xcor() < -285:
          player.setx(-285)
          playerspeed = 0	
        
        if bulletstate == "fire":
          y = bullet.ycor()
          y += bulletspeed
          bullet.sety(y)

        if bullet.ycor() >= 280:
          bullet.hideturtle()
          bulletstate = "ready"
        lopes = (time.time() - start_time)
        if lopes >= 60:
          break
      wn.bye()
      wn.mainloop()
      print(star)
      speak("TUTORIAL ENDED SUCCESSFULLY")
    else:
      print("BEST OF LUCK !!")
      speak("BEST OF LUCK !!")

  print("CHOOSE YOUR DIFFICULTY")
  speak("CHOOSE YOUR DIFFICULTY")
  askin = [1,2,3,4]
  valin = ["EASY" , "MODERATE", "HARD" , "EXTREME"]
  asking = dict(zip(askin,valin))
  print(json.dumps(asking,indent=2)) 
  choice = input("MY CHOICE (SERIAL NO.) : ")
  if choice == '1':
    number_of_enemies = 4
    enemyspeed = 2
    print("EASY FOR BEGINNERS , RIGHT")
  elif choice == '2':
    number_of_enemies = 6
    enemyspeed = 4
    print("FOR LEISURE I SUPPOSE?")
  elif choice == '3':
    number_of_enemies = 8
    enemyspeed = 6
    print("CHALLENGES HUH.., LET'S GO")
  elif choice == '4':
    number_of_enemies = 12
    enemyspeed = 8
    print("BE CAREFUL , DANGER AHEAD")
  else:
    print("YOU HAVE SELECTED DEFAULT MODERATE DIFFICULTY")
    number_of_enemies = 6
    enemyspeed = 4
  time.sleep(2)
  ak = 1
  speak("DO YOU WANT CONTINUOUS MOVING JOYSTICK?")
  ask = input("DO YOU WANT CONTINUOUS MOVING JOYSTICK? : ")
  print("**********************************************************")
  print("STARTING GAME")
  speak("STARTING GAME")
  time.sleep(5)
  mixer.music.play(-1)
  #Set up the screen
  wn = turtle.Screen()
  wn.bgcolor("black")
  wn.title("SPACE INVADERS")
  wn.bgpic("newbg.gif")

  #Register the shapes
  turtle.register_shape("invader.gif")
  turtle.register_shape("player.gif")
  turtle.register_shape("bullet.gif")

  #Draw border
  border_pen = turtle.Turtle()
  border_pen.speed(0)
  border_pen.color("white")
  border_pen.penup()
  border_pen.setposition(-300,-300)
  border_pen.pendown()
  border_pen.pensize(3)
  for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
  border_pen.hideturtle()	

  #Set the score to 0
  score = 0

  #Draw the score
  score_pen = turtle.Turtle()
  score_pen.speed(0)
  score_pen.color("white")
  score_pen.penup()
  score_pen.setposition(-290, 280)
  scorestring = "SCORE: %s" %score
  score_pen.write(scorestring, False, align="left", font=("Times New Roman", 14, "bold"))
  score_pen.hideturtle()

  #Create the player turtle
  player = turtle.Turtle()
  player.color("blue")
  player.shape("player.gif")
  player.penup()
  player.speed(0)
  player.setposition(0, -250)
  player.setheading(90)

  playerspeed = 0

  #Create an empty list of enemies
  enemies = []

  #Add enemies to the list
  for i in range(number_of_enemies):
    #Create the enemy
    enemies.append(turtle.Turtle())

  for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

  #Create the player's bullet
  bullet = turtle.Turtle()
  bullet.color("yellow")
  bullet.shape("bullet.gif")
  bullet.penup()
  bullet.speed(0)
  bullet.setheading(90)
  # bullet.shapesize(0.5, 0.5)
  bullet.hideturtle()

  bulletspeed = 120

  #Define bullet state
  #ready - ready to fire
  #fire - bullet is firing
  bulletstate = "ready"


  def move_left():
    global playerspeed
    playerspeed = -20
    
  def move_right():
    global playerspeed
    playerspeed = 20

  def stop_player():
    global playerspeed
    playerspeed = 0

    
  def fire_bullet():
    #Declare bulletstate as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
      # #os.system("afplay laser.wav&")
      bullet_sound = mixer.Sound('Space Invaders_laser.wav')
      bullet_sound.play()
      bulletstate = "fire"
      #Move the bullet to the just above the player
      x = player.xcor()
      y = player.ycor() + 10
      bullet.setposition(x, y)
      bullet.showturtle()

  def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 45:
      return True
    else:
      return False
  wn.listen()
  wn.onkeypress(move_left, "Left")
  wn.onkeypress(move_right, "Right")
  turtle.onkey(fire_bullet, "space")
  
  if ask.lower() != "yes":
      wn.onkeyrelease(stop_player, "Left")
      wn.onkeyrelease(stop_player, "Right")
  #Main game loop
  while True:
    # Move the player
    player.setx(player.xcor() + playerspeed)
    # Check borders
    if player.xcor() > 280:
      player.setx(280)
      playerspeed = 0

    elif player.xcor() < -280:
      player.setx(-280)
      playerspeed = 0	
    
    for enemy in enemies:
      #Move the enemy
      x = enemy.xcor()
      x += enemyspeed
      enemy.setx(x)

      #Move the enemy back and down
      if enemy.xcor() > 280:
        #Move all enemies down
        for e in enemies:
          y = e.ycor()
          y -= 35
          e.sety(y)
        #Change enemy direction
        enemyspeed *= -1
      
      if enemy.xcor() < -280:
        #Move all enemies down
        for e in enemies:
          y = e.ycor()
          y -= 35
          e.sety(y)
        #Change enemy direction
        enemyspeed *= -1

      #Check for a collision between the bullet and the enemy
      if isCollision(bullet, enemy):
        explosion_sound = mixer.Sound('Space Invaders_explosion.wav')
        explosion_sound.play()
        #Reset the bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0, -400)
        #Reset the enemy
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        enemy.setposition(x, y)
        #Update the score
        score += 10
        scorestring = "SCORE: %s" %score
        score_pen.clear()
        score_pen.write(scorestring, False, align="left", font=("Times New Roman", 14, "bold"))
      
      if enemy.ycor() <= -275:
        ak = 0
        break
      if isCollision(player, enemy):
        explosion_sound = mixer.Sound('Space Invaders_explosion.wav')
        explosion_sound.play()
        player.hideturtle()
        enemy.hideturtle()
        print ("Game Over")
        ak = 0
        break
      if bullet.ycor()>=275:
        bullet.hideturtle()

      
        
    if ak == 0:
      print("Game Over")
      break

    if bulletstate == "fire":
      y = bullet.ycor()
      y += bulletspeed
      bullet.sety(y)
    
    if bullet.ycor() > 280:
      bullet.hideturtle()
      bulletstate = "ready"
  print("***********************")
  wn.bye()
  wn.mainloop()
  csv_writer.writerow([yourname,score])
  f.close()
  po = open(f'{yourname}.csv','r',newline="")
  l = []
  csv_reader = csv.reader(po)
  for i in csv_reader:
    l.append(int(i[1]))
  print(f"YOUR HIGH SCORE IS {max(l)}")
  speak(f"YOUR HIGH SCORE IS {max(l)}")
  po.close()
  mixer.music.stop()
  rating()
else:
  print("KINDLY LOGIN NEXT TIME")
  time.sleep(1)
  print("THANK YOU")
