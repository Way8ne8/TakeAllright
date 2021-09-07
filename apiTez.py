import requests

countryId='5732'
cityId='786'
priceMin='0'
priceMax='999999'
before='12.11.2021'
after='01.11.2021'
currency='5561'
nightsMin='10'
nightsMax='12'
accommodationId='14356'
hotelClasId='2569'
hotelClassBetter='true'
rAndBId='2424'
rAndBBetter='true'
regionId=''
tourId='5735'
hotelId='157709'
birthday1='08.08.2012'
birthday2='14.09.2017'
#after = input("Дата вылета с: ")
#before = input('Дата вылета по: ')
link = f'https://search.tez-tour.com/tariffsearch/getResult?priceMin={priceMin}&priceMax={priceMax}&currency={currency}&nightsMin={nightsMin}&nightsMax={nightsMax}\
&hotelClassId={hotelClasId}&hotelId={hotelId}&accommodationId={accommodationId}&rAndBId={rAndBId}&tourType=1&locale=ru&cityId={cityId}&countryId={countryId}&after={after}\
&before={before}&tourId={tourId}&hotelClassBetter=true&rAndBBetter=true&hotelInStop=false&specialInStop=false\
&noTicketsTo=false&noTicketsFrom=false&promoFlag=true&version=2&searchTypeId=6&birthday1={birthday1}&birthday2={birthday2}'


link1 = requests.get(link)
data = link1.json()
print("Самая низкая цена на ALBATROS PALACE SHARM EL SHEIKH:")
print('Дата ' + str(data['data'][0][0]), 'Цена ' + str(data['data'][0][10]['total'])+'$', "за " + str(data['data'][0][3]) + ' ночей')

for i in range(len(data['data'])):
    print(data['data'][i][0], data['data'][i][10]['total']+'$', "за " + str(data['data'][i][3]) + ' ночей')