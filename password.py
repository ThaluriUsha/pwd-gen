import time
pd=input("enter password to create")
print("your password is",pd)
max_attempts = 3
attempts = 0
lpd=len(pd)
while attempts < max_attempts:
    if lpd==len(pd):
        u=input("enter a password to login")
        if u == pd and lpd==len(u):
            print("welcome to home page")
            break
        else:
            print("Incorrect password. Please try again.")
            attempts += 1
            if attempts < max_attempts:
                wait_time = 5 # seconds
                for i in range(wait_time, 0, -1):
                    print(f"Try again in {i} seconds...")
                    time.sleep(1)
                    if attempts == max_attempts:
                        print("Maximum number of attempts reached. Access denied.")
