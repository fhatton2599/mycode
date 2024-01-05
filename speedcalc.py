def other_costs():
    acpatj = 10
    ems = 20
    court = 42.50
    return acpatj, ems, court

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
            acpatj, ems, court = other_costs()
            total_fine = fine_speed + initial_fine(speed_limit) + acpatj + ems + court
              
            print(f"Your fine is ${fine_speed}+{acpatj}+{ems}+{court}")
            
    except ValueError:
            print("Invalid input. Please enter valid integer values for speed limit and vehicle speed.")
            
if __name__ == "__main__":
    speeding_ticket_calculator()
