import logging 
import time 
import sys  
from colorama import Fore 
speed_units=['km/h','mph','m/s']
time_units=['hrs','minutes','secs']
distance_units=['km','miles','metres']
equal_sign='='
not_a_valid_unit='Error, not a valid unit'
class Speed_distance_time:
    def __init__(self,speed,distance,time,units):
        self.speed=speed 
        self.distance=distance 
        self.time=time 
        self.units=units
    def calculate_speed(self):
        if self.units==distance_units[0]:
            speed_answer=lambda argv:argv / self.time 
            print(f'{round(speed_answer(self.distance),2)} {speed_units[0]} ')
        elif self.units==distance_units[1]:
            speed_answer=lambda argv:argv / self.time 
            print(f'{round(speed_answer(self.distance),2)} {speed_units[1]} ')
        elif self.units==distance_units[2]:
            speed_answer=lambda argv:argv / self.time 
            print(f'{round(speed_answer(self.distance),2)} {speed_units[2]}')
            
    def calculate_distance(self):
        if self.units==speed_units[0]:
            distance_answer=lambda argv:argv * self.time 
            print(f'{round(distance_answer(self.speed),2)} kilometres')
        elif self.units==speed_units[1]:
            distance_answer=lambda argv:argv * self.time 
            print(f'{round(distance_answer(self.speed),2)} {distance_units[1]}')
        elif self.units==speed_units[2]:
            distance_answer=lambda argv:argv * self.time 
            print(f'{round(distance_answer(self.speed),2)} {distance_units[2]}')
        
    def calculate_time(self):
        if self.units==distance_units[0]:
            time_answer=lambda argv:argv / self.speed 
            print(f'{round(time_answer(self.distance),2)} {time_units[0]}')
        elif self.units==distance_units[1]:
            time_answer=lambda argv:argv / self.speed 
            print(f'{round(time_answer(self.distance),2)} {time_units[1]}')
        elif self.units==distance_units[2]:
            time_answer=lambda argv:argv / self.speed 
            print(f'{round(time_answer(self.distance),2)} {time_units[2]}')
            
def error_msg(txt):
    mylogger=logging.getLogger('Alteration_log')
    mylogger.setLevel(logging.ERROR)
    for n in txt:
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write(f'{Fore.RED}{n}')
    else:
        reset_to_default_color=Fore.RESET 
        print(f'{reset_to_default_color}')
        file_handler=logging.FileHandler('documentation.log')
        file_format=logging.Formatter('%(asctime)s-%(name)s-%(message)s')
        file_handler.setFormatter(file_format)
        mylogger.addHandler(file_handler)
        mylogger.error(f'{txt}')
        
while True:
    try:
        speed='speed'
        dist='distance'
        time_string='time'
        speed_distance_or_time=input(f'Do you want to calculate {speed},{dist} or {time_string}?:')
        if speed_distance_or_time==speed:
            distance=float(input(f'{dist.title()}:'))
            time.sleep(0.2)
            print(f'{distance}')
            time.sleep(0.2)
            distance_unit_input=input(f'{dist} in {distance_units[0]},{distance_units[1]}, or {distance_units[2]}:')
            if distance_unit_input!=distance_units[0] and distance_unit_input!=distance_units[1] and distance_unit_input!=distance_units[2]:
                error_msg(f'{not_a_valid_unit}\n')
            else:
             time.sleep(0.2)
             print(f'{distance} {distance_unit_input}')
             time.sleep(0.2)
             time_value=float(input('time:'))
             if distance_unit_input==distance_units[0] or distance_unit_input==distance_units[1]:
                 time.sleep(0.2)
                 print(f'{distance} {distance_unit_input} / {time_value} {time_units[0]} {equal_sign}\n')
                 calculate=Speed_distance_time(speed=None,distance=distance,time=time_value,units=distance_unit_input)
                 calculate.calculate_speed()
             else:
                time.sleep(0.2)
                print(f'{distance} {distance_unit_input} / {time_value} {time_units[-1]} {equal_sign}\n')
                calculate=Speed_distance_time(speed=None,distance=distance,time=time_value,units=distance_unit_input)
                calculate.calculate_speed()
        elif speed_distance_or_time==dist:
            velocity=float(input(f'{speed.title()}:'))
            time.sleep(0.2)
            print(f'{velocity}')
            time.sleep(0.2)
            speed_unit_input=input(f'{velocity} in {speed_units[0]},{speed_units[1]} or {speed_units[2]}?:')
            if speed_unit_input!=speed_units[0] and speed_unit_input!=speed_units[1] and speed_unit_input!=speed_units[2]:
                error_msg(txt=f'{not_a_valid_unit}\n')
            else:
                time.sleep(0.2)
                print(f'{velocity} {speed_unit_input}')
                time.sleep(0.2)
                time_value_2=float(input(f'{time_string.title()}:'))
                if speed_unit_input==speed_units[0] or speed_unit_input==speed_units[1]:
                    print(f'{time_value_2} {time_units[0]}')
                    time.sleep(0.2)
                    print(f'{velocity} * {time_value_2} {time_units[0]} {equal_sign}\n')
                    calculate=Speed_distance_time(speed=velocity,distance=None,time=time_value_2,units=speed_unit_input)
                    calculate.calculate_distance()
                else:
                    print(f'{time_value_2} {time_units[-1]}')
                    time.sleep(0.2)
                    print(f'{velocity} * {time_value_2} {time_units[-1]} {equal_sign}\n')
                    calculate=Speed_distance_time(speed=velocity,distance=None,time=time_value_2,units=speed_unit_input)
                    calculate.calculate_distance()
        elif speed_distance_or_time==time_string:
            distance_travelled=float(input(f'{dist.title()}:'))
            time.sleep(0.2)
            print(f'{distance_travelled}')
            time.sleep(0.2)
            distance_unit_input_2=input(f'{dist} in {distance_units[0]},{distance_units[1]} or {distance_units[2]}?:')
            if distance_unit_input_2!=distance_units[0] and distance_unit_input_2!=distance_units[1] and distance_unit_input_2!=distance_units[2]:
                error_msg(txt=f'{not_a_valid_unit}\n')
            else:
                speed_travelled=float(input(f'{speed.title()}:'))
                time.sleep(0.2)
                print(f'{speed_travelled}')
                time.sleep(0.2)
                if distance_unit_input_2==distance_units[0]:
                    print(f'{distance_travelled} {distance_unit_input_2} / {speed} {speed_units[0]} {equal_sign}\n')
                    calculate=Speed_distance_time(speed=speed_travelled,distance=distance_travelled,time=None,units=distance_unit_input_2)
                    calculate.calculate_time()
                elif distance_unit_input_2==distance_units[1]:
                    print(f'{distance_travelled} {distance_unit_input_2} / {speed} {speed_units[1]} {equal_sign}\n')
                    calculate=Speed_distance_time(speed=speed_travelled,distance=distance_travelled,time=None,units=distance_unit_input_2)
                    calculate.calculate_time()
                elif distance_unit_input_2==distance_units[2]:
                    print(f'{distance_travelled} {distance_unit_input_2} / {speed} {speed_units[2]} {equal_sign}\n')
                    calculate=Speed_distance_time(speed=speed_travelled,distance=distance_travelled,time=None,units=distance_unit_input_2)
                    calculate.calculate_time()
    except ValueError:
        error_msg(txt='NumericError:"Not a whole or decimal value"')
    except ZeroDivisionError:
        error_msg(txt='ZeroDivisonError:You cannot divide by 0')
