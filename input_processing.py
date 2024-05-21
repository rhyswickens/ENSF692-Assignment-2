# input_processing.py
# Rhys Wickens, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.

class Sensor:

    # Default constructor that sets the initial values to a green traffic light, no pedestrian and no vehicle.
    def __init__(self):
        self.light = "green"
        self.pedestrian = "no"
        self.vehicle = "no"

    # This function updates the status of the light, pedestrian, and vehicle based on the user inputs
    def update_status(self, type, change): 
        if type == "1":
            self.light = change
        elif type == "2":
            self.pedestrian = change
        elif type == "3"  :
            self.vehicle = change


# This function determines what the print message will be based on the user inputs
# There are 3 possible outcomes: STOP!, Proceed, and Caution:
#   1. STOP!: If the light is red OR there is a pediestrian or vehicle
#   2. Proceed: If the light is green AND there are no pedestrians or vehicles
#   3. Caution: If the light is yellow AND there are no pedestrians or vehicles
def print_message(sensor):
    action = ""
    if sensor.light == "red" or sensor.pedestrian == "yes" or sensor.vehicle == "yes":
        action = "\nSTOP!\n"
    elif sensor.light == "green" and sensor.pedestrian == "no" and sensor.vehicle == "no":
        action = "\nProceed\n"
    elif sensor.light == "yellow" and sensor.pedestrian == "no" and sensor.vehicle == "no":
        action = "\nCaution\n"

    return print(action + "\nLight = " + sensor.light + " , Pedestrian = " + sensor.pedestrian + " , Vehicle = " + sensor.vehicle + " .\n")

# Getting the first user input on if they want to change the light, pedestrian, or vehicle
# If they enter a value other than 1, 2, 3, or 0 then there will be a ValueError that will remind them what they need to enter
def get_user_input1():
    entry1 = input("Are changes detected in the vision input?\nSelect 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ")
    if entry1 != "0" and entry1 != "1" and entry1 != "2" and entry1 != "3":
        raise ValueError("You must select either 1, 2, 3, or 0")
    return entry1

# Getting the second user input on what change has been identified based on what they answered in the first user input. 
# I handle the wrong inputs within the main method while loop.
def get_user_input2():
    entry2 = input("what change has been indentified? ")
    return entry2 


def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")

    # First, I create a sensor object from the default Sensor class
    sensor = Sensor()

    # This while loop will continue running until the user inputs a 0, and then it will break
    # Here is a step by step overview of the while loop:
    #   - To start, I get the first user input. If the input is 0 - the loop breaks. If it gets a ValueError, it reminds them they need to enter 1, 2, 3, or 0
    #   - Next, I get the second user input. 
    #   - The if statements are checking to see if they have the correct second input based on what they answered for the first input.
    #   - If they don't have the correct input they are given an "Invalid vision change" message, the current status, and the loop starts over with the first question again.
    #   - Lastly, once the two inputs are confirmed correct, the status is updated based on their input, and the message is printed on if they can STOP!, Proceed, or Caution.
    while True:
        try:
            input1 = get_user_input1()  
            if input1 == "0":   
                break
            else:
                input2 = get_user_input2()
                if input1 == "1":
                    if input2 != "green" and input2 != "yellow" and input2 != "red":
                        print("Invalid vision change: Please enter green, yellow, or red")
                        print_message(sensor)
                        continue
                if input1 == "2" or input1 == "3":
                    if input2 != "yes" and input2 != "no":
                        print("Invalid vision change: Please enter yes or no")
                        print_message(sensor)
                        continue
                sensor.update_status(input1, input2)
                print_message(sensor)
        except ValueError:
            print("\nYou must select either 1, 2, 3, or 0\n")
    

# Conventional Python code for running main within a larger program
if __name__ == '__main__':
    main()

