import datetime

class Vehicle:
    def __init__(self, type, licenseplate):
        self.Type = type
        self.LicensePlate = licenseplate

class Ticket:
    def __init__(self, id):
        self.ID = id
        self.TimeIn = datetime.datetime(1, 1, 1)
        self.TimeOut = datetime.datetime(1, 1, 1)

class Receipt:
    def __init__(self, vehicle, ticket):
        self.Vehicle = vehicle
        self.TimeIn = datetime.datetime.now()
        self.TimeOut = datetime.datetime(1, 1, 1)
        ticket.TimeIn = self.TimeIn
        self.Ticket = ticket
        self.isLossTicket = False
        self.Total = 0.0

class ManageVehicles:
    def __init__(self, vehicleamount):
        self.ListVehicles = []
        self.ListTicket = []
        self.ListTicketTaken = []
        self.ListReceipt = []
        self.Turnovermotorbike = 0.0
        self.Turnoverbike = 0.0
        for i in range(vehicleamount):
            self.ListTicket.append(Ticket(i))

    def VehicleIn(self, vehicle):
        self.ListVehicles.append(vehicle)
        ticket = self.ListTicket[0]
        self.ListTicket.pop(0)
        vehicle.Ticket = ticket
        self.ListReceipt.append(Receipt(vehicle, ticket))
        self.ListTicketTaken.append(ticket)
        return ticket

    def VehicleOut(self, vehicle, ticket, vehicleinfo):
        dtn = datetime.datetime.now()
        if vehicle in self.ListVehicles:
            if ticket is None:
                save = len(self.ListReceipt)
                for i in range(len(self.ListReceipt) - 1, -1, -1):
                    if self.ListReceipt[i].Vehicle.LicensePlate == vehicleinfo and self.ListReceipt[i].TimeOut.year == 1:
                        save = i
                        break
                if save < len(self.ListReceipt):
                    passday = dtn.day - self.ListReceipt[save].TimeIn.day
                    if vehicle.Type == "motorbike":
                        if dtn.hour < 18 and dtn.hour > 8:
                            self.ListReceipt[save].Total = 3000 + passday * 35000 + 60000
                            self.Turnovermotorbike += self.ListReceipt[save].Total
                            self.ListReceipt[save].TimeOut = dtn
                            self.ListReceipt[save].isLossTicket = True
                            self.ListVehicles.remove(vehicle)
                            self.ListTicket.append(ticket)
                            return vehicle
                        elif dtn.hour < 22 and dtn.hour >= 18:
                            self.ListReceipt[save].Total = 6000 + passday * 35000 + 60000
                            self.Turnovermotorbike += self.ListReceipt[save].Total
                            self.ListReceipt[save].TimeOut = dtn
                            self.ListReceipt[save].isLossTicket = True
                            self.ListVehicles.remove(vehicle)
                            self.ListTicket.append(ticket)
                            return vehicle
                        else:
                            return None
                    else:
                        if dtn.hour < 18 and dtn.hour > 8:
                            self.ListReceipt[save].Total = 2000 + passday * 15000 + 30000
                            self.Turnoverbike += self.ListReceipt[save].Total
                            self.ListReceipt[save].TimeOut = dtn
                            self.ListReceipt[save].isLossTicket = True
                            self.ListVehicles.remove(vehicle)
                            self.ListTicket.append(ticket)
                            return vehicle
                        elif dtn.hour < 22 and dtn.hour >= 18:
                            self.ListReceipt[save].Total = 4000 + passday * 15000 + 30000
                            self.Turnoverbike += self.ListReceipt[save].Total
                            self.ListReceipt[save].TimeOut = dtn
                            self.ListReceipt[save].isLossTicket = True
                            self.ListVehicles.remove(vehicle)
                            self.ListTicket.append(ticket)
                            return vehicle
                        else:
                            return None
                else:
                    return None
            else:
                save = len(self.ListReceipt)
                for i in range(len(self.ListReceipt) - 1, -1, -1):
                    if self.ListReceipt[i].Vehicle.LicensePlate == vehicle.LicensePlate and self.ListReceipt[i].TimeOut.year == 1 and self.ListReceipt[i].Ticket.ID == ticket.ID:
                        save = i
                        break
                if save < len(self.ListReceipt):
                    passday = dtn.day - self.ListReceipt[save].TimeIn.day
                    if vehicle.Type == "motorbike":
                        if dtn.hour < 18 and dtn.hour > 8:
                            self.ListReceipt[save].Total = 3000 + passday * 35000
                            self.Turnovermotorbike += self.ListReceipt[save].Total
                            self.ListReceipt[save].TimeOut = dtn
                            self.ListVehicles.remove(vehicle)
                            self.ListTicket.append(ticket)
                            return vehicle
                        elif dtn.hour < 22 and dtn.hour >= 18:
                            self.ListReceipt[save].Total = 6000 + passday * 35000
                            self.Turnovermotorbike += self.ListReceipt[save].Total
                            self.ListReceipt[save].TimeOut = dtn
                            self.ListVehicles.remove(vehicle)
                            self.ListTicket.append(ticket)
                            return vehicle
                        else:
                            return None
                    else:
                        if dtn.hour < 18 and dtn.hour > 8:
                            self.ListReceipt[save].Total = 2000 + passday * 15000
                            self.Turnoverbike += self.ListReceipt[save].Total
                            self.ListReceipt[save].TimeOut = dtn
                            self.ListVehicles.remove(vehicle)
                            self.ListTicket.append(ticket)
                            return vehicle
                        elif dtn.hour < 22 and dtn.hour >= 18:
                            self.ListReceipt[save].Total = 4000 + passday * 15000
                            self.Turnoverbike += self.ListReceipt[save].Total
                            self.ListReceipt[save].TimeOut = dtn
                            self.ListVehicles.remove(vehicle)
                            self.ListTicket.append(ticket)
                            return vehicle
                        else:
                            return None
                else:
                    return None
        else:
            return None

    def getAmountVehicle(self):
        return len(self.ListVehicles)

    def getTurnoverMotorbike(self):
        totalmotorbike = 0.0
        for receipt in self.ListReceipt:
            if receipt.TimeOut.day == datetime.datetime.now().day and receipt.Vehicle.Type == "motorbike":
                totalmotorbike += receipt.Total
        return totalmotorbike

    def getTurnoverBike(self):
        totalbike = 0.0
        for receipt in self.ListReceipt:
            if receipt.TimeOut.day == datetime.datetime.now().day and receipt.Vehicle.Type == "bike":
                totalbike += receipt.Total
        return totalbike

    def getTurnover(self):
        return self.getTurnoverBike() + self.getTurnoverMotorbike()

    def listVehiclelostTicket(self):
        listvehiclelostticket = []
        for receipt in self.ListReceipt:
            if receipt.isLossTicket:
                listvehiclelostticket.append(receipt.Vehicle)
        return listvehiclelostticket

    def getWarningVehicles(self):
        current_datetime = datetime.datetime.now()
        warning_vehicles = []

        for receipt in self.ListReceipt:
            entry_time = receipt.TimeIn
            vehicle_type = receipt.Vehicle.Type
            delta_days = (current_datetime - entry_time).days

            if (vehicle_type == "bike" and delta_days >= 3) or (vehicle_type == "motorbike" and delta_days >= 5):
                warning_vehicles.append(receipt.Vehicle)

        return warning_vehicles

    def getLostTicketsToday(self):
        current_datetime = datetime.datetime.now()

        start_time = current_datetime.replace(hour=8, minute=0, second=0, microsecond=0)
        end_time = current_datetime.replace(hour=22, minute=0, second=0, microsecond=0)

        lost_tickets = []

        for receipt in self.ListReceipt:
            if start_time <= receipt.TimeIn <= end_time:
                if receipt.isLossTicket:
                    lost_tickets.append(receipt.Vehicle)

        return lost_tickets

    def getDuplicateEntries(self):
        current_datetime = datetime.datetime.now()

        start_time = current_datetime.replace(hour=8, minute=0, second=0, microsecond=0)
        end_time = current_datetime.replace(hour=22, minute=0, second=0, microsecond=999999)

        vehicles_in_day = {}
        duplicate_vehicles = []

        for receipt in self.ListReceipt:
            entry_time = receipt.TimeIn
            vehicle_license = receipt.Vehicle.LicensePlate
            vehicle_type = receipt.Vehicle.Type

            if vehicle_type =="motorbike" and start_time <= entry_time <= end_time:
                if vehicle_license in vehicles_in_day:
                    vehicles_in_day[vehicle_license] += 1
                else:
                    vehicles_in_day[vehicle_license] = 1

                if vehicles_in_day[vehicle_license] == 2:
                    duplicate_vehicles.append(receipt.Vehicle)

        return duplicate_vehicles

    def sortVehicles(self, criteria, reverse=False):
        if criteria == 'timein':
            self.ListVehicles.sort(key=lambda x: x.Ticket.TimeIn, reverse=reverse)
        elif criteria == 'type':
            self.ListVehicles.sort(key=lambda x: x.Type, reverse=reverse)

    def getVehicles(self):
        return self.ListVehicles

    def displaySortedVehicles(self):
        for vehicle in self.ListVehicles:
            print("Type: ", vehicle.Type)
            print("License Plate: ", vehicle.LicensePlate)
            print("Time In: ", vehicle.Ticket.TimeIn)
            print("---------------------")

    def getVehicleByLicense(self, licenseplate):
        return next((vehicle for vehicle in self.ListVehicles if vehicle.LicensePlate == licenseplate), None)

    def getTicketByTicketId(self, ticketid):
        return next((ticket for ticket in self.ListTicketTaken if ticket.ID == ticketid), None)

    def getReceipt(self, vehicle, ticket):
        return next((receipt for receipt in self.ListReceipt if receipt.Vehicle == vehicle and receipt.Ticket == ticket), None)

def ShowListVehicle(listvehicle):
    for vehicle in listvehicle:
        print("Type: {1}, LicensePlate: {0}".format(vehicle.LicensePlate, vehicle.Type))

def ShowListVehicleByType(listvehicle):
    sortedlistvehicle = sorted(listvehicle, key=lambda t: t.Type)
    ShowListVehicle(sortedlistvehicle)

def ShowReceipt(receipt):
    print("*"*20)
    print("RECEIPT INFORMATION")
    print("Vehicle - Type: {0}, LicensePlate: {1}".format(receipt.Vehicle.LicensePlate, receipt.Vehicle.Type))
    print("Ticket - Ticket ID: {0}".format(receipt.Ticket.ID))
    print("Time in: {0}".format(receipt.TimeIn))
    print("Time out: {0}".format(receipt.TimeOut))
    print("Is lost ticket: {0}".format(receipt.isLossTicket))
    print("Total: {0}".format(receipt.Total))
    print("*" * 20)

def ShowMenu():
    print("*" * 30)
    print("PARKING MANAGEMENT SYSTEM")
    print("1. Add new vehicle to the parking lot")
    print("2. Take the vehicle out of the parking lot")
    print("3. Current number of vehicles in the garage")
    print("4. List of vehicles currently stored in the garage")
    print("5. Revenue today")
    print("6. List of vehicles that need to be warned (by vehicle type)")
    print("7. List of vehicles with lost ticket today (by vehicle type)")
    print("8. List of motorbikes with 2 submissions today")
    print("9. Turn off the program")
    print("*" * 30)

def ShowCriteriaOfListMenu():
    print("*" * 20)
    print("CRITERIA")
    print("1. Decrease over time criteria")
    print("2. Increase over time criteria")
    print("3. Vehicle type criteria")
    print("*" * 20)

def main():
    managevehicles = ManageVehicles(100)

    while True:
        ShowMenu()
        choice = input("Enter your selection: ")

        if choice == "1":
            type = input("Enter vehicle type (motorbike/bike): ")
            while type not in {"bike", "motorbike"}:
                type = input("Invalid type. Enter vehicle type again (motorbike/bike): ")
            licenseplate = input("Enter license plate: ")
            vehicle = Vehicle(type, licenseplate)
            ticket = managevehicles.VehicleIn(vehicle)
            print("Ticket has been created with ID: {0}".format(ticket.ID))

        elif choice == "2":
            licenseplate = input("Enter license plate: ")
            ticketID = input("Enter ticket ID: ")

            while True:
                if ticketID.isdigit():
                    ticket = managevehicles.getTicketByTicketId(int(ticketID))


                vehicleinfo = input("Enter vehicle information: ")
                vehicle = managevehicles.getVehicleByLicense(licenseplate)

                if ticketID == "":
                    vehicleout = managevehicles.VehicleOut(vehicle, None, vehicleinfo)
                else:
                    vehicleout = managevehicles.VehicleOut(vehicle, ticket, vehicleinfo)

                if vehicleout:
                    receipt = managevehicles.getReceipt(vehicle, ticket)
                    ShowReceipt(receipt)

                    input("Press Enter to continue...")
                    print("The vehicle with license plate number {0} was retrieved".format(vehicle.LicensePlate))
                    break
                else:
                    print("Failed to retrieve the vehicle")
                    break


        elif choice == "3":
            print("Current number of vehicles in the garage: {0}".format(managevehicles.getAmountVehicle()))

        elif choice == "4":
            while True:
                ShowCriteriaOfListMenu()
                CriteriaChoice = input("Enter your selection again: ")
                if CriteriaChoice == "1":
                    print("List of vehicles currently stored decreases over time: ")
                    managevehicles.sortVehicles("timein", True)
                    managevehicles.displaySortedVehicles()
                    break

                elif CriteriaChoice == "2":
                    print("List of vehicles currently stored increases over time: ")
                    managevehicles.sortVehicles("timein", False)
                    managevehicles.displaySortedVehicles()
                    break

                elif CriteriaChoice == "3":
                    print("List of vehicles currently stored by vehicle type: ")
                    managevehicles.sortVehicles("type", True)
                    managevehicles.displaySortedVehicles()
                    break

                else:
                    print("Invalid selection. Please select again")

        elif choice == "5":
            print("Revenue today: ", managevehicles.getTurnover())

        elif choice == "6":
            print("List of vehicles that need to be warned (by vehicle type): ")
            ShowListVehicleByType(managevehicles.getWarningVehicles())

        elif choice == "7":
            print("List of vehicles with lost ticket today (by vehicle type): ")
            ShowListVehicleByType(managevehicles.getLostTicketsToday())

        elif choice == "8":
            print("List of motorbikes with 2 submissions today: ")
            ShowListVehicle(managevehicles.getDuplicateEntries())

        elif choice == "9":
            print("End program")
            break

        else:
            print("Invalid selection. Please select again")

main()