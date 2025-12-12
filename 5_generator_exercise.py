# Smart Token Dispenser
# You are developing a Smart Token Dispenser system, like those found in banks or clinics.
# This system reset counters based on user activity and needs to run until manually stopped.

def token_dispenser(start = 1):
    current = start 
    try:
        while True:
            new_start = yield current
            if new_start is not None:
                current = new_start
            else:
                current+=1

    except:
        print("Dispenser Closed")     

token = token_dispenser()
for _ in range(2):
 print(next(token))

token.send(1)
for _ in range(3):
 print(next(token))

