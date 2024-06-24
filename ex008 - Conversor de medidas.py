#Faça O Programa Que Leia Um Valor Em Metro E Converta Ele Em Cm E Mm
m = float(input('digite uma distância em metros'))
c = m*100
mm = m*1000
deci = m*10
dec = m/10
hec = m/100
km = m/1000

print('A medidade de {} Metro corresponde a \n {} \n {} \n {} \n {} \n {} \n {:.0f}'.format(m,km,hec,dec, deci,mm,c))
