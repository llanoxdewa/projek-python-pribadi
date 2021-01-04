data_diri = open('data diri.txt','r')
data_nilai = open('data nilai.txt','r')
data_buku = {
		'data diri':data_diri,
		'data nilai':data_nilai
}

def show_data()
	pilihan = str(input('masukan data yang ingin di buka >> '))
	print(data_buku[pilihan])	
	



data_nilai.close()
data_diri.close()




