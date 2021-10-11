s = input().split()
info = {'mile': 1609,
'yard': 0.9144,
'foot': 0.3048,
'inch': 0.0254,
'km': 1000,
'm': 1,
'cm': 0.01,
'mm': 0.001}
print(f"{float(s[0])*info[s[1]]/info[s[3]]:12.2e}")