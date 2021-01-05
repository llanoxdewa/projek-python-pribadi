import re,pyperclip


def phone_found(phone_number):
	finder = re.compile(r'(\+62\s\d{3}\s\d{4}\s\d{4}|\d{4}\s\d{4}\s\d{4})')

	number_found = finder.findall(phone_number)
	return number_found
def email_found(email):
	finder = re.compile(r'([a-zA-Z0-9]+@gmail\.com|[a-zA-Z0-9]+@yahoo\.com)')
	email_found = finder.findall(email)
	return email_found

raw_text = pyperclip.paste()
Email = email_found(raw_text)
PhoneNumber = phone_found(raw_text)
data_email_phone_number = {
				email : phone_number for (email,phone_number) in zip(Email,PhoneNumber)
}
hasil = open('hasil.txt','w')
for e,pn in data_email_phone_number.items():
	hasil.write(f'account email : {e}\ndengan no telepon : {pn}\n')

hasil.close()
