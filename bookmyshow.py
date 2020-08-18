class bookmyshow:
    available=100

    def __init__(self,required):
        self.required= required

    def bookticket(self):
        if(bookmyshow.available>=self.required):
            bookmyshow.available-=self.required
            print("congrats", self.required)
            print("tickets booked successfully")
        else:
            print(self.required)
            print("sorry!! tickets are not available")

        print("available tickets now:", bookmyshow.available)



user1= bookmyshow(10)
user1.bookticket()