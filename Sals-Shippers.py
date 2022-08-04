#Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
#Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
#Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

#PRICES
#Ground Shipping Price
if weight <= 2:
  ground-ship-price =	((1.50) * weight) +	(20.00)
elif weight > 2 and <= 6:
  ground-ship-price =	((3.00) * weight) +	(20.00)
elif weight > 6 and <= 10:
  ground-ship-price =	((4.00) * weight) +	(20.00)
else:	
  ground-ship-price =	((4.75) * weight) +	(20.00)

#Ground Shipping Premium

premium-price = 125.00

#Drone Shipping
if weight <= 2:
  drone-price =	((4.50) * weight) 
elif weight > 2 and <= 6:
  drone-price =	((9.00) * weight)
elif weight > 6 and <= 10:
  drone-price =	((12.00) * weight) 
else:	
  drone-price =	((14.25) * weight) 

weight = 1





