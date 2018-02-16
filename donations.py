import donation
# main

# Section 1 - get all of the donations and output the values
def donations(number):
    my_donations=[]
    for i in range(number):
        my_donations.append(donation.get_donation())
##        my_donations=donations(200)
    return my_donations

my_donations = donations(200)
print("These are the donation amounts: ",my_donations)

print("These are the sorted donation amounts: ", sorted(my_donations))

count=0
smallDonations = []
mediumDonations = []
largeDonations = []

for number in my_donations:
    if number <= 5:
        smallDonations.append(number)
    elif number > 5 and number <= 15:
        mediumDonations.append(number)
    else:
        largeDonations.append(number)
	
print("There were ", len(smallDonations), "small donations ($5 or less).")
print("There were ", len(mediumDonations), "medium donations ($6-$15).")
print("There were ", len(largeDonations), "large donations ($16 or more).")
