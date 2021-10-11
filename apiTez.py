import requests

res = {}
countryId = '5732'
cityIdLIST = {'786': 'Минск', '12384': 'Брест', '2548': 'Витебск', '4387': 'Гомель', '331488': 'Могилев'}
priceMin = '0'
priceMax = '3000'
before = '05.11.2021'
after = '30.10.2021'
currency = '5561'
nightsMin = '10'
nightsMax = '12'
accommodationId = '14356'
hotelClasId = '2569'
hotelClassBetter = 'true'
rAndBId = '2424'
rAndBBetter = 'true'
regionId = ''
tourId = '5735'
hotelId = '158896'
birthday1 = '08.08.2012'
birthday2 = '14.09.2017'
# after = input("Дата вылета с: ")
# before = input('Дата вылета по: ')
for cityId in cityIdLIST.keys():
    link = f'https://search.tez-tour.com/tariffsearch/getResult?priceMin={priceMin}&priceMax={priceMax}&currency={currency}&nightsMin={nightsMin}&nightsMax={nightsMax}&hotelClassId={hotelClasId}&accommodationId={accommodationId}&rAndBId={rAndBId}&tourType=1&locale=ru&cityId={cityId}&countryId={countryId}&after={after}&before={before}&tourId="5734"&tourId="5735"&hotelClassBetter=true&rAndBBetter=true&hotelInStop=false&specialInStop=false&noTicketsTo=false&noTicketsFrom=false&promoFlag=true&version=2&searchTypeId=6&birthday1={birthday1}&birthday2={birthday2}&groupByHotel=2'
    print(link)
    link1 = requests.get(link)
    data = link1.json()
    # print(data)
    if data['success']:
        for i in range(len(data['data'])):
            if res.get(data['data'][i][6][1]):
                if data['data'][i][10]['total'] < res[data['data'][i][6][1]]:
                    res[data['data'][i][6][1]] = data['data'][i][10]['total'] + '$ ' + cityIdLIST[cityId] + ' Дата ' + str(data['data'][0][0])
            else:
                res[data['data'][i][6][1]] = data['data'][i][10]['total'] + '$ ' + cityIdLIST[cityId] + ' Дата ' + str(data['data'][0][0])

for key, values in sorted(res.items(), key=lambda x: (x[1], x[0])):
    print(key + '  ' + values)
