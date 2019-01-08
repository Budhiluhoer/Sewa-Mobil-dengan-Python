print('INPUT DATA SEWA MOBIL')

print('\n')
avanza = {'tipe':'Avanza','harga':300000,'sopir':50000}
total_av = avanza['harga'] + avanza['sopir']

print('harga avanza : ', avanza['harga'])
print('sopir avanza : ', avanza['sopir'])
print('total avanza : ', total_av)
print('\n')

alphard = {'tipe':'Alphard','harga':550000,'sopir':55000}
total_al = alphard['harga'] + alphard['sopir']

print('harga alphard : ', alphard['harga'])
print('sopir alphard : ', alphard['sopir'])
print('total alphard : ', total_al)
print('\n')

truck = {'tipe':'Truck','harga':150000,'sopir':60000}
total_tr = truck['harga'] + truck['sopir']

print('harga truck : ', truck['harga'])
print('sopir truck : ', truck['sopir'])
print('total truck : ',total_tr)
print('\n')

nama = input('Nama Penyewa : ')
tipe = input('Tipe (avanza/alphard/truck) : ')
lama = int(input('Lama menyewa (hari) : '))

total_avanza = total_av * lama
total_alphard = total_al * lama
total_truck = total_tr * lama

if(tipe == 'avanza'):
    if (lama >= 7 ):
        print('harga : ', total_av)
        print('lama : ', lama)
        print('total : ', total_avanza)
        print('diskon 10% : ', 10/100*total_avanza)
        print('bayar : ',total_avanza - 10/100*total_avanza)
    elif (lama >= 3 ):
        print('harga : ', total_av)
        print('lama : ', lama)
        print('total : ', total_avanza)
        print('diskon 5% : ', 5/100*total_avanza)
        print('bayar : ',total_avanza - 5/100*total_avanza)
    elif (lama < 3 ):
        print('harga : ', total_av)
        print('lama : ', lama)
        print('harga x lama : ', total_avanza)
        print('diskon 2% : ', 2/100*total_avanza)
        print('bayar : ',total_avanza - 2/100*total_avanza)
    else:
        print('bayar : ',total_avanza)
elif (tipe == 'alphard'):
    if (lama >= 7 ):
        print('harga : ', total_al)
        print('lama : ', lama)
        print('total : ', total_alphard)
        print('diskon 10% : ', 10/100*total_alphard)
        print('bayar : ',total_alphard - 10/100*total_alphard)
    elif (lama >= 3 ):
        print('harga : ', total_al)
        print('lama : ', lama)
        print('total : ', total_alphard)
        print('diskon 5% : ', 5/100*total_alphard)
        print('bayar : ',total_alphard - 5/100*total_alphard)
    elif (lama < 3 ):
        print('harga : ', total_al)
        print('lama : ', lama)
        print('total : ', total_alphard)
        print('diskon 2% : ', 2/100*total_alphard)
        print('bayar : ',total_alphard - 2/100*total_alphard)
    else:
        print('bayar : ', total_alphard)
elif (tipe == 'truck'):
    if (lama >= 7 ):
        print('harga : ', total_tr)
        print('lama : ', lama)
        print('total : ', total_truck)
        print('diskon 10% : ', 10/100*total_truck)
        print('bayar : ',total_truck - 10/100*total_truck)
    elif (lama >= 3 ):
        print('harga : ', total_tr)
        print('lama : ', lama)
        print('total : ', total_truck)
        print('diskon 5% : ', 5/100*total_truck)
        print('bayar : ',total_truck - 5/100*total_truck)
    elif (lama < 3 ):
        print('harga : ', total_tr)
        print('lama : ', lama)
        print('total : ', total_truck)
        print('diskon 2% : ', 2/100*total_truck)
        print('bayar : ',total_truck - 2/100*total_truck)
    else:
        print('bayar : ',total_truck)
