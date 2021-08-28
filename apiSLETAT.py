import requests

# link = f'https://module.sletat.ru/Main.svc/GetTours?s_hasTickets=true&currencyAlias=USD&' \
#        f's_ticketsIncluded=true&cityFromId=1308&countryId=40&s_adults=2' \
#        f's_nightsMax=12&s_departFrom=01/11/2021&s_departTo=10/11/2021&requestId=0&pageSize=10&pageNumber=1&' \
#        f'updateResult=0&includeDescriptions=1&s_hotelIsNotInStop=true&showHotelFacilities=1'

link = f'https://module.sletat.ru/Main.svc/GetTours?login=way8ne8@gmail.com&password=d04060502&s_hasTickets=true&currencyAlias=RUB&s_ticketsIncluded=true&includeOilTaxesAndVisa=1&cityFromId=832&countryId=119&s_adults=2&s_nightsMin=3&s_nightsMax=10&s_departFrom=19/09/2019&s_departTo=25/09/2019&requestId=0&pageSize=10&pageNumber=1&updateResult=0&includeDescriptions=1&s_hotelIsNotInStop=true&showHotelFacilities=1'
#
link1 = requests.get(link)
data = link1.json()
print(link)
print(data)
# print("Самая низкая цена на ALBATROS PALACE SHARM EL SHEIKH:")
# print('Дата ' + data['data'][0][0])
# print('Цена ' + data['data'][0][10]['total']+'$')
# f'&s_kids=2' \
# f'&s_kids_ages=4,9&s_nightsMin=10&' \