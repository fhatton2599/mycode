#!/usr/bin/env python3

def other_costs():
    jcpatj = 10
    ems = 20
    court = 42.50
    return jcpatj, ems, court

def surcharge(speed_diff):
    if 6 <= speed_diff <= 15:
        return 45
    elif 16 <= speed_diff <= 25:
        return 60
    elif speed_diff >= 26:
        return 75

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
            # total_fine = fine_speed + initial_fine(speed_limit) + jcpatj + ems + court
            
            print(f"Fine: ${fine}")
            print(f"EMS: ${ems}")
            print(f"Surcharge: ${surg}")
            print(f"Court Costs: ${court}")
            print(f"ACPATJ: ${jcpatj}")
            
            #print(f"Total: ${fine_speed}+{jcpatj}+{ems}+{court}")
            
    except ValueError:
            print("Invalid input. Please enter valid integer values for speed limit and vehicle speed.")
            
if __name__ == "__main__":
    speeding_ticket_calculator()
