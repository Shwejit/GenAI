order_size = "Medium"
extra_shot = True

if extra_shot:
    coffee_type = order_size + " Extra Shot"
else:
    coffee_type = order_size + " Regular"

print("Your coffee order is:", coffee_type)