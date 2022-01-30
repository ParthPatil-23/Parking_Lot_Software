from tabulate import tabulate
import time

# Asking for no. Plate of the car
NUM_PLATE = (input("enter your car no :- "))
print(NUM_PLATE)



# Parking Lot table for ease of access

PARKING_LOT = [["     ", "A1", "B1", "     ", "C1", "D1", "     ", "E1", "F1", "     ", "G1", "H1", "     "],
			 ["     ", "A2", "B2", "     ", "C2", "D2", "     ", "E2", "F2", "     ", "G2", "H2", "     "], 
			 ["     ", "A3", "B3", "     ", "C3", "D3", "     ", "E3", "F3", "     ", "G3", "H3", "     "], 
			 ["     ", "A4", "B4", "     ", "C4", "D4", "     ", "E4", "F4", "     ", "G4", "H4", "     "], 
			 ["     ", "A5", "B5", "     ", "C5", "D5", "     ", "E5", "F5", "     ", "G5", "H5", "     "],
			 ["     ", "A6", "B6", "     ", "C6", "D6", "     ", "E6", "F6", "     ", "G6", "H6", "     "],
			 ["     ", "A7", "B7", "     ", "C7", "D7", "     ", "E7", "F7", "     ", "G7", "H7", "     "],
			 ["     ", "A8", "B8", "     ", "C8", "D8", "     ", "E8", "F8", "     ", "G8", "H8", "     "],
			 ["     ", "  ", "  ", "     ", "  ", "  ", "     ", "  ", "  ", "     ", "  ", "  ", "     "]]

head = ["     ","   ","   ","     ","   ","   ","     ","   ","   ","     ","   ","   ","     "]




# Printing the atble of the Parking Lot
print(tabulate(PARKING_LOT, headers = head, tablefmt = "grid"))


# Opening file called "PARKINGLOT.TXT" to read Already boought lots
PARKING_LOT_FILE = open("PARKINGLOT.txt","r")
for i in PARKING_LOT_FILE:
	print("Already Bought Lot :- ", i)
PARKING_LOT_FILE.close()


a = True

# Opening "PARKINGLOT.txt" to read and split the data of lots with comma 
data = open("PARKINGLOT.txt","r").read()
data1 = data.split(',')

# Checking in the time the car entered the parking lot
sec = time.time()

# Asking the user to enter the lot no. they needed
while(a):
    lot_no = input("select you parking lot no. :- ")
    if lot_no in data1:
        print("\n","Sorry this lot is already taken","\n")
    else:
        data = open("PARKINGLOT.txt","a")
        data.write(",")
        data.write(lot_no)
        var = lot_no+".txt"
        lot_file = open(var,"a")
        lot_file.write(NUM_PLATE)
        lot_file.write(",")
        lot_file.write(lot_no)
        lot_file.write(",")
        lot_file.write(str(sec))
        lot_file.close()
        a = False



data.close()





