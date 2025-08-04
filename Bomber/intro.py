import sys
import time
import os

logo ='''\033[1;34m

________                         ______  _______ 
___  __ \\_____________  ____________  /_ __  __ \\
__  /_/ /__  ___/__  / / /_  ___/__  __ \\_  / / /
_  ____/ _(__  ) _  /_/ / / /__  _  / / // /_/ / 
/_/      /____/  _\\__, /  \\___/  /_/ /_/ \\____/  
                 /____/                          

      \033[1;30m-----------------------------------
      Author : Mr.Psych0
      Github : https://github.com/3rPsych0
      Email  : 3r.Psych00@gmail.com
      Tool   : Bd SMS-BOMBING TOOl
                 \033[1;32mBe Ethical..
      \033[1;30m------------------------------------
'''

preline1 = "\033[1;36mSystem Loading...\n\033[1;32mBe patient..."
preline2 = "\033[1;36mWelcome to the Systems!!\n"
preline3 = "\033[1;32mEnter UserName : "
preline4 = "\033[1;33mChecking..."
grant = "\n\033[1;32mAccess Granted!!"
deny = "\n\033[1;31mAccess Denied!!"

def slide_view(x):
  for b in x:
    sys.stdout.write(b)
    sys.stdout.flush()
    time.sleep(0.08)

os.system("clear")

def intro():
  slide_view(preline1)
  time.sleep(2)
  os.system('clear')
  
  slide_view(preline2)
  
  slide_view(preline3)
  username = input("")
  
  slide_view(preline4)
  time.sleep(3)
  print("\n\n\n\n\n\n\n")
  if username != "Psycho":
    slide_view(deny)
    time.sleep(2)
    exit()
  else:
    slide_view(grant)
    time.sleep(2)
    os.system("clear")
  
  for b in logo:
    sys.stdout.write(b)
    sys.stdout.flush()
    time.sleep(0.015)

if __name__ == "__main__":
  intro()
  