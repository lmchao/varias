dic = {"A": "14", "B": "01", "C": "00", "D": "16", "E": "05", "F": "20", "G": "19", "H": "09", "I": "24", "J": "07", "K": "21", "L": "08", "M": "04", "N": "13", "O": "25", "P": "22", "Q": "18", "R": "10", "S": "02", "T": "06", "U": "12", "V": "23", "W": "11", "X": "03", "Y": "15", "Z": "17"}
pat = input("Ingrese patente: ")
pat = pat.upper()
print("La patente es: ", pat)
if len(pat) < 6: 
	print("El dato ingresado no es valido")

suma = dic[pat[0]] + dic[pat[1]] + dic[pat[2]] + pat[3:]
dig1 = int(suma[0]) + int(suma[2]) + int(suma[4]) + int(suma[6]) + int(suma[8]) 
dig2 = int(suma[1]) + int(suma[3]) + int(suma[5]) + int(suma[7])

if dig1 > 9 :
	dig1 = int(str(dig1)[0]) + int(str(dig1)[1])
if dig2 > 9 :
	dig2 = int(str(dig2)[0]) + int(str(dig2)[1])
print("El digito verificador es: " + str(dig1) + str(dig2))	

	
