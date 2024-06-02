#name:Victoria Inahuazo
#email:victoria.inahuazo11@myhunter.cuny.edu
#date: 04/11/24
#this program generates transit fares based on the LIRR fare zone system

#If the zone is 1 and the ticket type is "peak", the fare is 8.75.
#If the zone is 1 and the ticket type is "off-peak", the fare is 6.25.
#If the zone is 2 or 3 and the ticket type is "peak", the fare is 10.25.
#If the zone is 2 or 3 and the ticket type is "off-peak", the fare is 7.50.
#If the zone is 4 and the ticket type is "peak", the fare is 12.00.
#If the zone is 4 and the ticket type is "off-peak", the fare is 8.75.
#If the zone is 5, 6, or 7 and the ticket type is "peak", the fare is 13.50.
#If the zone is 5, 6, or 7 and the ticket type is "off-peak", the fare is 9.75.
#If the zone is greater than 8, return a negative number (since your calculator does not handle inputs that high).



def main():
    zns = int(input("Enter the number of zones:"))
    tix = input("Enter the ticket type(peak/off-peak):")
    fare = computeFare(zns, tix)

def computeFare(zone, ticket):
    if zone == 1:
        if ticket == "peak":
            return 8.75
        elif ticket == "off-peak":
            return 6.25
    elif zone in (2,3): #zones 2 and 3 are condtions
        if ticket == "peak":
            return 10.25
        elif ticket == "off-peak":
            return 7.50
    elif zone == 4:
        if ticket == "peak":
            return 12.00
        elif ticket == "off-peak":
            return 8.75
    elif zone in (5,6,7):
        if ticket == "peak":
            return 13.50
        elif ticket == "off-peak":
            return 9.75
    
    elif zone > 8:
        return -1

    

