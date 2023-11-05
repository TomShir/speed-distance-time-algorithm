#Create a Python program which can find square and cube numbers in a given range 
from math import sqrt
from numpy import cbrt
from colorama import Fore 
import sys 
import time
while True:
 try:
   def start_limit():
    global start 
    global limit 
    start=int(input('start:'))
    limit=int(input('limit:'))
    
   cube='cube'
   square_numbers='square'
   type_of_numbers=[square_numbers,cube]
   for num in type_of_numbers:
    if num==type_of_numbers[0]:
        print(f'{num[0:3]}:{num}')
    elif num==type_of_numbers[1]:
        print(f'{num}:{num}')
   else:
    square_or_cube=input('type_of_number:')
    if square_or_cube==square_numbers[0:3]:
        start_limit()
        time.sleep(0.2)
        print(f'square numbers between {start} and {limit}:')
        time.sleep(0.2)
        for n in range(start,limit):
            square_root=sqrt(n)
            if square_root%1==0:
                print(n)
            else:
                pass
    elif square_or_cube==cube:
        start_limit()
        time.sleep(0.2)
        numbers=[]
        for x in range(start,limit):
            numbers.append(x)
        else:
            print(f'cube numbers between {start} and {limit}:\n')
            time.sleep(0.2)
            for num in numbers:
                if cbrt(num)%1==0:
                    print(num)
                else:
                  pass 
 except ValueError:
     
    def error_msg(txt):
     for n in txt:
      sys.stdout.flush()
      time.sleep(0.2)
      sys.stdout.write(f'{Fore.RED}{n}\n')
     else:
      reset_to_default_color=Fore.RESET 
      print(f'{reset_to_default_color}')

    error_msg(txt='Not a numeric value inputted')