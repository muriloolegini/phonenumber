import phonenumbers
from phonenumbers import geocoder

# Digite seu número com codigo do país e ddd #
phone = input('Digite o telefone: ')
phoneNumber = phonenumbers.parse(phone)

# Captura operadora #
print(geocoder.description_for_number(phoneNumber, 'pt-br'))