class Purchase(object):
    def __init__(self,amount):
        self.amount = amount 

    def calculateTax(self, taxPercent):
        return self.amount * taxPercent/100.0
    
    def calculateTip(self, tipPerecent):
        return self.amount * tipPercent/100.0

    def calculateTotal(self, taxPercent, tipPercent):
        return self.amount * (1 + taxPercent/100.0 + tipPercent/100.0)

# Create Purchase object given an amount 
purchase = Purchase(100.0)

# Set the tax and tip percentages 
taxPercent = 7.5
tipPercent = 20.0

# Use the object to calculate tax and tip 
tax = purchase.calculateTax(taxPercent)
tip = purchase.calculateTip(tipPercent)

# Display some useful information 
print('Tax: ', tax)
print('Tip: ', tip)
print('Total: ', purchase.calculateTotal(taxPercent, tipPercent))

class Purchase(object):
    def __init__(self,amount):
        self.amount = amount 

    def calculateTax(self, taxPercent):
        return self.amount * taxPercent/120.0
    
    def calculateTip(self, tipPerecent):
        return self.amount * tipPercent/120.0

    def calculateTotal(self, taxPercent, tipPercent):
        return self.amount * (1 + taxPercent/120.0 + tipPercent/120.0)

# Create Purchase object given an amount 
purchase = Purchase(100.0)

# Set the tax and tip percentages 
taxPercent = 8.5
tipPercent = 25.0

# Use the object to calculate tax and tip 
tax = purchase.calculateTax(taxPercent)
tip = purchase.calculateTip(tipPercent)

# display some useful results
print('Local Tax Percent: ', tax)
print('Local Tip Percent: ', tip)
print('Total Purchase in USD: $', ourPurchaseObject.calculateTotal(localTaxPercent, localTipPercent)) 

# print using string interpolation and new fstrings
# fstrings = formatted strings 
# display values inline inside curly braces
print(f'Total Purchase in USD: ${ ourPurchaseObject.calculateTotal(localTaxPercent, localTipPercent) }')

# use fstrings to show only 2 digits on a floating point number (.2f)
print(f'Total Purchase in USD: ${ ourPurchaseObject.calculateTotal(localTaxPercent, localTipPercent):.2f}')

# References
# Read more at: https://docs.python.org/3/tutorial/classes.html
# string interpolation at: python string interpolation
# Google python fstring to limit to 2 decimal places
