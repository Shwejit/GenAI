import time

wait=1
attempt=0
maxtry=5

while attempt<maxtry:
    print("Attempt : ",attempt+1, " - wait time : ",wait)
    time.sleep(wait)
    wait*=2
    attempt+=1