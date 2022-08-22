import random
import pyautogui

chars = "qwertyuiopasdfghjklzxcvbnm"
char_list = list(chars)

pwd = pyautogui.password("Type A Password To Crack: ")

guess_pwd = ""

while(guess_pwd != pwd):
  guess_pwd = random.choices(char_list, k=len(pwd))
  print("==="+ str(guess_pwd)+ "===")
  
  if(guess_pwd == list(pwd)):
    print("PASSWORD CRACKED -"+ "".join(guess_pwd)
          break
