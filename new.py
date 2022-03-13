empty_spots = {
    1: 'open',
    2: 'open',
    3: 'open',
    4: 'open',
    5: 'open',
    6: 'open',
    7: 'open',
    8: 'open',
    9: 'open',
    10: 'open'
}

garage = {}

class Parking():
    
    def spots_open(self):
      print('This is the open parking:')
      if empty_spots:
          print(len(empty_spots))
      else:
          print('Sorry! No parking spots open')
    
    def take_ticket(self):
        ticket = list(empty_spots)[0]
        garage.update({ticket:empty_spots[ticket]})
        del empty_spots[ticket]
        print(f'Your ticket is #{ticket}')

    def pay_ticket(self):
        while True:
            open_spot_response = int(input('What is your ticket #?'))
            if open_spot_response == 0:
                break
            elif open_spot_response in garage.keys():
                response = input(f'Your ticket # is {open_spot_response} is that correct? Y/N')
                while True:
                    if response.lower() == 'y':
                        payment = input('Your total is $10. Debit or Credit')
                        if payment.lower() == 'debit' or payment.lower() == 'credit':
                            garage[open_spot_response] = 'Paid'
                            print('Thank you for your payment')
                            break
                        elif response.lower == 'n':
                            break
                        else:
                            print('Try again')

    def leave_parking(self):
        while True:
            show_ticket = int(input('Show your ticket #:'))
            if show_ticket == 0:
                break
            elif garage.get(show_ticket) == 'Paid':
                print('Thank you for coming!! Have a nice day!!')
                garage[show_ticket] = 'unpaid'
                empty_spots.update({int(show_ticket):garage[show_ticket]})
                del garage[show_ticket]
                break
            elif garage.get(show_ticket) == 'unpaid':
                print('Please pay your ticket before leaving')

    def parking_garage(self):
        while True:
            answer = input("What would you like to do? 'Spots Open'/'Take Ticket'/'Pay Ticket'/'Leave'/'Quit'")
            if answer.lower() == 'quit':
                print('Please visit again!')
                break
            elif answer.lower() == 'spots open':
                self.spots_open()
            elif answer.lower() == 'take ticket':
                self.take_ticket()
            elif answer.lower() == 'pay ticket':
                self.pay_ticket()
            elif answer.lower() == 'leave':
                self.leave_parking()
            else:
                print('Sorry, Try again')    

                            
                                
program = Parking()
program.parking_garage()