#Ground Shipping is a small flat charge + a rate based on the weight of your package.
#Ground Shipping Premium is a much higher flat charge, but you aren’t charged for weight.
#Drone Shipping has no flat charge, but the rate based on weight is triple the rate of ground shipping.


#Weight in pounds (lbs)
weight=41.5




#PRICES
#Ground Shipping Price
if weight<=2:
  ground_ship_price =	((1.50) * weight) +	(20.00)
elif weight>2 and weight<=6:
  ground_ship_price =	((3.00) * weight) +	(20.00)
elif weight>6 and weight<=10:
  ground_ship_price =	((4.00) * weight) +	(20.00)
else:	
  ground_ship_price =	((4.75) * weight) +	(20.00)

#Ground Shipping Premium

premium_price = 125.00

#Drone Shipping
if weight<= 2:
  drone_price =	((4.50) * weight) 
elif weight>2 and weight<=6:
  drone_price =	((9.00) * weight)
elif weight>6 and weight<=10:
  drone_price =	((12.00) * weight) 
else:	
  drone_price =	((14.25) * weight) 


print(ground_ship_price)
print(premium_price)
print(drone_price)





