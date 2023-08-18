from functions import *

# send_sms("+254745972459","Hello there.....")

otp_code = generate_random()
print(otp_code)

status = passwordValidity("@Kingisabout101")
print(status)

valid_phone = check_phone("+254740922861")
print(valid_phone)
