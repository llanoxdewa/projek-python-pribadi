from prettytable import PrettyTable as PT
print(' SELAMAT DATANG DI PROGRAM CHICKEN '.center(60,'#'),'\n\n')
daftar_tabel = PT()
colom_harga = ['Kode','Jenis potong','Harga']
harga = {
	'D':2500,
	'P':2000,
	'S':1500
}
jenis = {
	'D':'Dada',
	'P':'Paha',
	'S':'Sayap'
}
daftar_tabel.add_column(colom_harga[0],('D','P','S'))
daftar_tabel.add_column(colom_harga[1],[jenis[i] for i in jenis])
daftar_tabel.add_column(colom_harga[2],['Rp. '+str(harga[i]) for i in harga])
print(daftar_tabel)
pilih_jenis = str(input('Masukan jenis yang ingin di beli >> '))
jumlah = int(input('masukan jumlah yang ingin di beli >> '))
if pilih_jenis in jenis:
	print(f"anda memesan {jenis[pilih_jenis]} dengan jumlah {jumlah} dengan total harga Rp. {(harga[pilih_jenis]*jumlah) + int(harga[pilih_jenis] * 0.1)}")
else:
	print('pilihan anda tidak ada di daftar menu silahkan pilih yang lain')
