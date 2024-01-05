def speeding_ticket_calculator():
    try:
        speed_limit = int(input("What is the speed limit?"))
        veh_speed = int(input("What was the vehicle speed?"))
        
        if veh_speed <= speed_limit:
            print("Vehicle was within the posted speed limit.")
 
        else:
            speed_diff = veh_speed - speed_limit
            pre_fine = speed_diff - 5
        
        if pre_fine <= 5
        
        else
           pre_fine 

        if     
            

            print(f"Your fine is ${fine_speed}")
            
    except ValueError:
            print("Invalid input. Please enter valid integer values for speed limit and vehicle speed.")
            
if __name__ == "__main__":
    speeding_ticket_calculator()
