#!/usr/bin/env python3
#Point systems
def points(speed_diff):
    if 6 <= speed_diff <= 10:
        return 2
    elif 11 <= speed_diff <= 15:
        return 3
    elif 16 <= speed_diff <= 25:
        return 4
    elif 26 <= speed_diff <= 30:
        return 5
    elif speed_diff >= 31:
        return "5 & PennDoT Hearing"
    else:
        return 0

#Define general costs associated with ticket
def other_costs():
    jcpatj = 10
    ems = 20
    court = 42.50
    return jcpatj, ems, court

#Surcharge changes with speed difference
def surcharge(speed_diff):
    if 6 <= speed_diff <= 15:
        return 45
    elif 16 <= speed_diff <= 25:
        return 60
    elif speed_diff >= 26:
        return 75

#Initial fine depending on speed zone
def initial_fine(speed_limit):
    if speed_limit >= 65:
        return 42.50
    else:
        return 35.0

def speeding_ticket_calculator():
    try:
        speed_limit = int(input("What is the speed limit?"))
        veh_speed = int(input("What was the vehicle speed?"))
        
        if veh_speed <= speed_limit:
            print("Vehicle was within the posted speed limit.")
        else:
            speed_diff = veh_speed - speed_limit
            fine_speed = (speed_diff - 5) * 2
            jcpatj, ems, court = other_costs()
            surg = surcharge(speed_diff)
            fine = initial_fine(speed_limit) + fine_speed
            total_fine = fine + jcpatj + ems + court + surg
            
            print(f"Fine: ${fine}")
            print(f"EMS: ${ems}")
            print(f"Surcharge: ${surg}")
            print(f"Court Costs: ${court}")
            print(f"ACPATJ: ${jcpatj}")
            print(f"Total: ${total_fine}")
            
            print(f"Points: {points(speed_diff)}")
    except ValueError:
            print("Invalid input. Please enter valid integer values for speed limit and vehicle speed.")
            
if __name__ == "__main__":
    speeding_ticket_calculator()
