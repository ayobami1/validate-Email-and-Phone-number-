
import re
import phonenumbers

def is_valid_email(email):
  """
  Validates an email address.

  Args:
    email: A string containing the email address to validate.

  Returns:
    True if the email address is valid, False otherwise.
  """

  email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
  return re.match(email_pattern, email) is not None

def is_valid_phone(phone_number):
  """
  Validates a phone number.

  Args:
    phone_number: A string containing the phone number to validate.

  Returns:
    True if the phone number is valid, False otherwise.
  """

  try:
    parsed_phone = phonenumbers.parse(phone_number, None)
    return phonenumbers.is_valid_number(parsed_phone)
  except phonenumbers.phonenumberutil.NumberParseException:
    return False


print(is_valid_email("john.doe@example.com"))

print(is_valid_phone("+2347036469096"))
