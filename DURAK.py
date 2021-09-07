mast = {'C': 1, 'D': 1, 'H': 1, 'S': 1}
cardValuesInf = {'6': 1, '7': 2, '8': 3, '9': 4, '10': 5, 'J': 6, 'Q': 7, 'K': 8, 'A': 9}

razdacha = input().split()
kozyr = input()
mast[kozyr] += 10
if razdacha[0][-1] != kozyr and razdacha[1][-1] != kozyr and razdacha[0][-1] != razdacha[1][-1]:
    print('Error')
else:
    if razdacha[0][0] == '1' and razdacha[0][1] == '0' and razdacha[1][0] != '1' and razdacha[1][1] != '0':
        first = cardValuesInf['10'] + mast[razdacha[0][-1]]
        second = cardValuesInf[razdacha[1][0]] + mast[razdacha[1][-1]]
    elif razdacha[1][0] == '1' and razdacha[1][1] == '0' and razdacha[0][0] != '1' and razdacha[0][1] != '0':
        first = cardValuesInf[razdacha[0][0]] + mast[razdacha[0][-1]]
        second = cardValuesInf['10'] + mast[razdacha[1][-1]]
    elif razdacha[1][0] == '1' and razdacha[1][1] == '0' and razdacha[0][0] == '1' and razdacha[0][1] == '0':
        first = cardValuesInf['10'] + mast[razdacha[0][-1]]
        second = cardValuesInf['10'] + mast[razdacha[1][-1]]
    else:
        first = cardValuesInf[razdacha[0][0]] + mast[razdacha[0][-1]]
        second = cardValuesInf[razdacha[1][0]] + mast[razdacha[1][-1]]
    if first>second:
        print('First')
    else:
        print('Second')
