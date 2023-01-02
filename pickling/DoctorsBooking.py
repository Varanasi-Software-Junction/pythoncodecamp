import pickle


class Person:
    def __init__(self, name=None, age=None, address=None):
        if name is not None:
            self.name = name
        else:
            self.name = input("Enter your name\n")
        if age is not None:
            self.age = age
        else:
            self.age = int(input("Enter your age\n"))
        if address is not None:
            self.address = address
        else:
            self.address = input("Enter your address\n")

    def __str__(self):
        return "Name={0}, Age={1}, Address={2}".format(self.name, self.age, self.address)


class Time:
    def __init__(self, hour=None, minute=None):
        if hour is not None:
            self.hour = hour
        else:
            self.hour = int(input("Enter hour\n"))
        if minute is not None:
            self.minute = minute
        else:
            self.minute = int(input("Enter minute\n"))

    def __str__(self):
        return "{0}:{1}".format(self.hour, self.minute)


class Booking:

    def __init__(self, patient=None, isbooked=False, starttime=None, endtime=None, sno=None):
        self.patient = patient
        self.isbooked = isbooked
        self.starttime = starttime
        self.endtime = endtime
        self.sno = sno

    def __str__(self):
        return "Sno={0}, start={1},end={2},isbooked={3},patient={4}".format(self.sno, self.starttime, self.endtime,
                                                                            self.isbooked, self.patient)


def readData():
    try:
        pass
        datafile = open('bookingstore', 'rb')
        data = pickle.load(datafile)
    except:
        pass
        data = [Booking(sno=1, starttime=Time(hour=11, minute=15), endtime=Time(hour=11, minute=35)),
                Booking(sno=2, starttime=Time(hour=11, minute=40), endtime=Time(hour=12, minute=0))]
    finally:
        try:
            datafile.close()
        except:
            pass
    return data


def saveData():
    datafile = open('bookingstore', 'ab')
    pickle.dump(data, datafile)
    datafile.close()


data = readData()
while True:
    print("0-Exit,1-Book,2-Cancel,3-Show All")
    option = int(input("Enter option\n"))
    if option == 0:

        saveData()

        break
    elif option == 1:
        print("Book")
        for booking in data:
            if not booking.isbooked:
                print(booking)
        n = int(input("Enter sno for booking "))
        booking = data[n - 1]
        booking.patient = Person()
        booking.isbooked = True

    elif option == 2:
        print("Cancel")
    elif option == 3:
        print("Show All")
        for booking in data:
            print(booking)
    else:
        print("Error")
