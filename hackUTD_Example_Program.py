##
## This program demonstrates interacting with the Fannie MAE
## Exchange portal to retrieve manufactured housing data.
##
## The Exchange can run example queries against the API's and show you the invocation
## as a CURL command. You can use the link below to help you convert CURL parameters
## and formatting into Python.
##
## https://curl.trillworks.com/
##

## import the necessary support libraries
##
import requests
import json
from collections import Counter

## set up the request object - replace "YOUR_AUTH_KEY" with your actual
## authentication key from the Exchange. Please remember YOUR_AUTH_KEY changes
## every 60 minutes. You'll need to grab the new key from your profile or by
## re-executing one of the sample commands on "The Exchange" and copying
## YOUR_AUTH_KEY from the curl command
##
headers = {
    'accept': 'application/json',
    'Authorization': 'YOUR_AUTH_KEY',
}

## submit a request to the exchange asking for all the
## manufactured housing acquisitions (loans)
##
response = requests.get('https://api.theexchange.fanniemae.com/v1/manufactured-housing-loans/acquisitions', headers=headers)

## grab the response (formatted as json)
##
responseJSON = response.json()

## print out the first loan in the data returned from the API call
##
## the output should look like this:
## {'loanIdentifier': '100076749532', 'channel': 'B', 'sellerName': 'JPMORGAN CHASE BANK, NA', 'originalInterestRate': 9.25, 'originalUnpaidPrincipalBalance': 55000.0, 'originalLoanTerm': 360, 'originationDate': '12/1999', 'firstPaymentDate': '02/2000', 'originalLoanToValue': 80.0, 'numberOfBorrowers': 2, 'debtToIncomeRatio': 35.0, 'firstTimeHomeBuyerIndicator': 'N', 'loanPurpose': 'C', 'propertyType': 'MH', 'numberOfUnits': 1, 'occupancyStatus': 'S', 'propertyGeographicalState': 'OH', 'zip3': '451', 'productType': 'FRM', 'relocationMortgageIndicator': 'N'}
##
print ('First loan in acquisitions results')
print (responseJSON['_embedded']['acquisitions'][0])
print ('--------------------------------------------------')

## uncomment to print out ALL the loans returned from the API call
##
# for loan in responseJSON['_embedded']['acquisitions']:
#     print (loan)

## uncomment to print out just the loan ID's for each loan returned from
## the api call
# for loan in responseJSON['_embedded']['acquisitions']:
#     print (loan['loanIdentifier'])

## or use the collections class to create a frequency distribution
## of the number of loans by each seller
##
sellerFreqDist = Counter(loan['sellerName'] for loan in responseJSON['_embedded']['acquisitions'])
print (sellerFreqDist)
print ('--------------------------------------------------')

## for a cleaner printout, convert the collection results to a
## dictionary and print them out from there
##
sellerDict = dict(sellerFreqDist)
for seller, sellerCount in sellerDict.items():
    print ("{} count: {}".format(seller, sellerCount))
print ('--------------------------------------------------')

## Once you've found a specific loan you're interested in - you'll want to get
## the performance details for that loan. How has it been performing since it
## was acquired in terms of making payments in the right amounts and on
## time. Has the loan gone into foreclosure, or paid off early, or is it
## still performing normally?
##
## You would use this type of information to feed a neural network that could
## be trained to detect loans that might potentially be at risk of going
## into default...
##
## The loan id included here DOES go into default and eventually into foreclosure
## and ends up being sold.
##
response = requests.get('https://api.theexchange.fanniemae.com/v1/manufactured-housing-loans/604848485338/performance', headers=headers)

responseJSON = response.json()

for status in responseJSON:
    if 'loanDelinquencyStatus' in status:
        print (status['loanDelinquencyStatus'])


