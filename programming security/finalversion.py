brand = ("ferrari")
car_models = ['Ferrari Mondial','Ferrari New', 'Ferrari F1 Spider','Ferrari GTS','Ferrari Newest, Testa Rossa']

car_models.append("Ferrari GTO")


#create list of car colors
car_colors = ['red','blue','white','black','orange']

#replace orange with yellow
car_colors[4] = 'yellow'

new_year_models = ['Stradale','Tributo','Spider','GTS','Roma']

#create constant msrp
MSRP = (30_000,50_000,60_000,70_000,80_000,90_000)

#create constant list of months in the 4yr, 5yr, and 6yr loans
FOUR_YEAR = (48)
FIVE_YEAR = (60)
SIX_YEAR = (72)

#create variable for guest's name
guest_name = ("John")

welcome_message = f'{guest_name}! thank you for visiting us today. Our dealership is famous for our {car_models} models, some of the new year models are the {new_year_models}, which would you like to check out today?'
banner = ('Welcome to Ferrari Dealership!')


cars = car_models
#sort models into alphabetical order
YEARS = [2000,2022,2013,1990,2011,2017,]
cars.sort()
reccomended = ('Ferrari F1 Spider','Ferrari GTS')
print(f'{banner} {welcome_message} The models we recommend are the {reccomended}, the years we have in are the {YEARS} versions, and the colors are {car_colors}')

#create monthly payment variable
monthly_paymentfive = 90000/60
monthly_paymentfour = 90000/48
monthly_paymentsix = 90000/72
#offer them the best trade deal in the history of trade deals
print(f'Today we have a deal for you, if you buy the Testa Rossa we can offer you a monthly payment plan, for just {monthly_paymentfive} a month, you can pay off your Testa in five years.')
print(f' If that doesnt work for you, we also have a four year and six year plan. the four year plan goes for {monthly_paymentfour} a month, and the six year, {monthly_paymentsix} a month.')
#extra tool

import time
time.sleep(3)
print(f' if you still arent ready to decide, i can offer you some other models')

print(f'i can give you the five year plans for the other models as well. for the mondial, it would be {30000/60}, for the ferrari new, {40000/60}, the spider,{50000},')
time.sleep(2)
print(f'if not those, the gts would be {60000/60}, and the Newest, {70000/60}')

time.sleep(2)
print(f'now just for you since i like you, if you pay today we can drop 20% off the car of your choice, so if you bought the Rossa today it would only be {90000-18000}, or {72000/60} a month for five years')
