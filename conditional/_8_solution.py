pw = "Secure@f7238y"

pw_length = len(pw)

if pw_length<6:
    print("Weak")
elif pw_length<=10:
    print("Medium")
else:
    print("Strong")

