# ======================================================
# ALL HOMEWORK TASKS IN ONE PYTHON FILE
# ======================================================

from datetime import datetime, timedelta
import time
import re
from zoneinfo import ZoneInfo   # Python 3.9+

# ------------------------------------------------------
# 1. AGE CALCULATOR
# ------------------------------------------------------

def age_calculator():
    birth = input("Enter birthdate (YYYY-MM-DD): ")
    birth_date = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()

    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    if days < 0:
        months -= 1
        days += 30
    if months < 0:
        years -= 1
        months += 12

    print(f"Age: {years} years, {months} months, {days} days")


# ------------------------------------------------------
# 2. DAYS UNTIL NEXT BIRTHDAY
# ------------------------------------------------------

def days_until_birthday():
    birth = input("Enter birthdate (YYYY-MM-DD): ")
    birth_date = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()

    next_bday = birth_date.replace(year=today.year)
    if next_bday < today:
        next_bday = next_bday.replace(year=today.year + 1)

    days_left = (next_bday - today).days
    print("Days until next birthday:", days_left)


# ------------------------------------------------------
# 3. MEETING SCHEDULER
# ------------------------------------------------------

def meeting_scheduler():
    start = input("Enter start date & time (YYYY-MM-DD HH:MM): ")
    hours = int(input("Meeting hours: "))
    minutes = int(input("Meeting minutes: "))

    start_time = datetime.strptime(start, "%Y-%m-%d %H:%M")
    end_time = start_time + timedelta(hours=hours, minutes=minutes)

    print("Meeting ends at:", end_time)


# ------------------------------------------------------
# 4. TIMEZONE CONVERTER
# ------------------------------------------------------

def timezone_converter():
    dt = input("Enter date & time (YYYY-MM-DD HH:MM): ")
    from_tz = input("From timezone (e.g. Asia/Tashkent): ")
    to_tz = input("To timezone (e.g. Europe/London): ")

    local_time = datetime.strptime(dt, "%Y-%m-%d %H:%M")
    local_time = local_time.replace(tzinfo=ZoneInfo(from_tz))
    converted = local_time.astimezone(ZoneInfo(to_tz))

    print("Converted time:", converted)


# ------------------------------------------------------
# 5. COUNTDOWN TIMER
# ------------------------------------------------------

def countdown_timer():
    future = input("Enter future date & time (YYYY-MM-DD HH:MM:SS): ")
    target = datetime.strptime(future, "%Y-%m-%d %H:%M:%S")

    while True:
        now = datetime.now()
        remaining = target - now
        if remaining.total_seconds() <= 0:
            print("Time is up!")
            break
        print("Remaining:", remaining)
        time.sleep(1)


# ------------------------------------------------------
# 6. EMAIL VALIDATOR
# ------------------------------------------------------

def email_validator():
    email = input("Enter email: ")
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    print("Valid email" if re.match(pattern, email) else "Invalid email")


# ------------------------------------------------------
# 7. PHONE NUMBER FORMATTER
# ------------------------------------------------------

def phone_formatter():
    number = input("Enter phone number (digits only): ")
    if len(number) == 10:
        formatted = f"({number[:3]}) {number[3:6]}-{number[6:]}"
        print("Formatted:", formatted)
    else:
        print("Invalid phone number")


# ------------------------------------------------------
# 8. PASSWORD STRENGTH CHECKER
# ------------------------------------------------------

def password_checker():
    pwd = input("Enter password: ")

    if (len(pwd) >= 8 and
        re.search(r"[A-Z]", pwd) and
        re.search(r"[a-z]", pwd) and
        re.search(r"\d", pwd)):
        print("Strong password")
    else:
        print("Weak password")


# ------------------------------------------------------
# 9. WORD FINDER
# ------------------------------------------------------

def word_finder():
    text = input("Enter text: ")
    word = input("Word to find: ")

    matches = re.findall(rf'\b{word}\b', text, re.IGNORECASE)
    print(f"Occurrences found: {len(matches)}")


# ------------------------------------------------------
# 10. DATE EXTRACTOR
# ------------------------------------------------------

def date_extractor():
    text = input("Enter text: ")
    dates = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', text)
    print("Dates found:", dates)


# ------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------

def main():
    while True:
        print("""
=== MAIN MENU ===
1. Age Calculator
2. Days Until Next Birthday
3. Meeting Scheduler
4. Timezone Converter
5. Countdown Timer
6. Email Validator
7. Phone Formatter
8. Password Strength Checker
9. Word Finder
10. Date Extractor
0. Exit
""")
        choice = input("Choose: ")

        if choice == "1": age_calculator()
        elif choice == "2": days_until_birthday()
        elif choice == "3": meeting_scheduler()
        elif choice == "4": timezone_converter()
        elif choice == "5": countdown_timer()
        elif choice == "6": email_validator()
        elif choice == "7": phone_formatter()
        elif choice == "8": password_checker()
        elif choice == "9": word_finder()
        elif choice == "10": date_extractor()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option")


# ------------------------------------------------------
# RUN PROGRAM
# ------------------------------------------------------

if __name__ == "__main__":
    main()
