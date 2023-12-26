#import Required Modules


import pickle
import os
import pathlib

# Event Management System

# Features :

# 1. Create An Event
# 2. View Events
# 3. Book Ticket
# 4. View Ticket
# 5. Condition Check If Customer Already Buy Same Event Ticket
# 6. Condition Check if All Tickets are sold Out.
# 7. Show Overall Event Summary


#Create Ticket Class

class Ticket:
    name = ''
    email = ''
    event = ''
    reference = 200000

    def bookTicket(self):
        self.name= input("Enter Customer Name: ")
        self.email = input("Enter Customer Email: ")
        file = pathlib.Path("events.data")
        if file.exists():
            infile = open('events.data', 'rb')
            eventdetails = pickle.load(infile)
                   

        for event in eventdetails:
            print("Available Event Code : " + event.eventcode + " Event Name : " + event.eventname)
        infile.close()
        self.event = input("Enter Event Code: ")

        

    def check(self):
        file = pathlib.Path("tickets.data")
        if file.exists():
            infile = open('tickets.data', 'rb')
            ticketdetails = pickle.load(infile)
            for ticket in ticketdetails:
                if ticket.email == self.email and ticket.event == self.event:
                    return True
            infile.close()


    def gettotalticketcount(self):
        file = pathlib.Path("events.data")
        if file.exists():
            infile = open('events.data', 'rb')
            eventdetails = pickle.load(infile)
            for event in eventdetails:
                if event.eventcode == self.event:
                    return int(event.eventTotalAvaibleSeat)
            infile.close
        else:
            return 0

    def getBookedSeatCount(self):
        file = pathlib.Path("tickets.data")
        counter= 0
        if file.exists():
            infile = open('tickets.data', 'rb')
            ticketdetails = pickle.load(infile)
            for ticket in ticketdetails:
                if ticket.event == self.event:
                    counter = counter + 1
            return int(counter)
        return 0



############################ Create Event Class


class Event:
    eventname = ''
    eventcode = ''
    eventTotalAvaibleSeat = 10

    def createEvent(self):
        self.eventname= input("Enter Event Name: ")
        self.eventcode = input("Enter Event Code: ")
        self.eventTotalAvaibleSeat = input("Enter Event Total Availble Seats: ")
        print("\n\n ------> Event Created!")



############################################## Main Program Modules

# Book Ticket and Check Condition

def bookEventTicket():
    ticket = Ticket()
    ticket.bookTicket()
    if ticket.check():
        print("Warning : You Already Book A Seat")

    elif ticket.getBookedSeatCount() >= ticket.gettotalticketcount():
        print("Warning : All Ticket Sold Out")

    else:
        print("Success : Ticket Booked!")
        saveTicketDetiails(ticket)

# Save Ticket Detials to File

def saveTicketDetiails(ticket):
    file = pathlib.Path("tickets.data")
    if file.exists():
        infile = open('tickets.data', 'rb')
        oldlist = pickle.load(infile)
        oldlist.append(ticket)
        infile.close()
        os.remove('tickets.data')
    else:
        oldlist = [ticket]
    outfile = open('tempTicket.data', 'wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('tempTicket.data', 'tickets.data')


# Display Saved Ticket Details

def getTicketDetails():
    file = pathlib.Path("tickets.data")
    if file.exists ():
        infile = open('tickets.data','rb')
        ticketdetails = pickle.load(infile)
        print("---------------TICKET DETAILS---------------------")
        print("C-Name    C-Email    E-Code")
        for ticket in ticketdetails :
            print(ticket.name,"\t", ticket.email, "\t",ticket.event)
        infile.close()
        print("--------------------------------------------------")
        if input('Type "Main" to EnterMain Menu: ')=="main":
            welcomeuser()
    else :
        print("NO TICKET RECORDS FOUND")

# Create Event Module

def createEvent():
    event = Event()
    event.createEvent()
    saveEventDetails(event)

# Save Event Details to File

def saveEventDetails(event):
    file = pathlib.Path("events.data")
    if file.exists():
        infile = open('events.data', 'rb')
        oldlist = pickle.load(infile)
        oldlist.append(event)
        infile.close()
        os.remove('events.data')
    else:
        oldlist = [event]
    outfile = open('tempevents.data', 'wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('tempevents.data', 'events.data')

# Display All Event Details

def getEventsDetails():
    file = pathlib.Path("events.data")
    if file.exists ():
        infile = open('events.data','rb')
        eventdetails = pickle.load(infile)
        print("---------------EVENT DETAILS---------------------")
        print("E-Name    E-Code    E-Total-Seats")
        for event in eventdetails :
            print(event.eventname,"\t", event.eventcode, "\t",event.eventTotalAvaibleSeat)
        infile.close()
        print("--------------------------------------------------")
        if input('Type "Main" to EnterMain Menu: ')=="main":
            welcomeuser()
    else :
        print("NO EVENTS RECORDS FOUND")

# Display Reports About Events

def getEventsSummary():
    filetickets = pathlib.Path("tickets.data")
    if filetickets.exists():
        infiletickets = open('tickets.data', 'rb')
        ticketdetails = pickle.load(infiletickets)


    fileEvents = pathlib.Path("events.data")
    if fileEvents.exists ():
        infileEvents = open('events.data','rb')
        eventdetails = pickle.load(infileEvents)


        print("---------------REPORTS---------------------")
        for event in eventdetails :
            print("\nCompetition Name : " + event.eventname + " | Total Seats : " + event.eventTotalAvaibleSeat + " \n")
            for ticket in ticketdetails:
                if event.eventcode == ticket.event:
                    print(ticket.name, "\t", ticket.email)

        infileEvents.close()
        infiletickets.close()

        print("--------------------------------------------------")
        print()
        if input('Type "Main" to EnterMain Menu: ')=="main":
            welcomeuser()
        else:
            logoutuser()
    else :
        print("NO EVENTS RECORDS FOUND")

def welcomeuser():
    
    print("\t\t\t\t--------------------------------")
    print("\t\t\t\tKAALRAV EVENT MANAGEMENT SYSTEM")
    print("\t\t\t\t--------------------------------\n\n")
    print("Welcome TO Kaalrav 2022") 
    print("\tMAIN MENU")
    print("\t1. BOOK TICKET")
    print("\t2. VIEW TICKET")
    print("\t3. CREATE COMPETITION")
    print("\t4. VIEW COMPETITION")
    print("\t5. SHOW RECORDS")
    print("\t6. EXIT")
    print("\tSelect Your Option (1-6) ")

def logoutuser():
    print("Thank You")
#Main Program
welcomeuser()
ch=''
num=0
condition='1'or'2'or'3'or'4'or'5'or'6'
while ch != condition:
   
    ch = input()

    if ch == '1':
        bookEventTicket()
    elif ch == '2':
        getTicketDetails()
    elif ch == '3':
        createEvent()
    elif ch == '4':
        getEventsDetails()
    elif ch == '5':
        getEventsSummary()
    elif ch=='6': 
        logoutuser()
        exit()  
    else:
        print("Invalid Option") 












