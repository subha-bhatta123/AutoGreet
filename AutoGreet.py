import datetime
a=input("what is your gender?:   ")

if a == "male":
    b="sir"
elif a == "female":
    b="ma'am"
else :
    print("we accept only male/female")
    
def get_time_greeting():
    current_time = datetime.datetime.now()
    hour = current_time.hour

    if 4 <= hour < 12:
        return "Good Morning"
    elif 12 <= hour < 17:
        return "Good Afternoon"
    elif 17 <= hour < 21:
        return "Good Evening"
    else:
        return "Good Night"

def main():
    time_greeting = get_time_greeting()
    print(f"{time_greeting}",b )

if __name__ == "__main__":
    main()
