from moduls import *
import random

while True:
	# proses input nama,tanggal,kelas
	profil_siswa = login_siswa()
	cetak_hasil.write(profil_siswa)
	# the header of soal
	n = 1
	print('\n',f'State Capitals Quiz (Form {n})'.center(80,' '))
	cetak_hasil.write('\n')
	cetak_hasil.write(f'State Capitals Quiz (Form {n})'.center(80,' '))
	n += 1
	# show the soal openf the ujian 
	show_soal()
	cetak_hasil.write('\n\n')
	cetak_hasil.write(f'nilai anda adalah {cek_jawaban()}')
	if input('done : ') == 'yes':
		print(f'nilai anda adalah : {cek_jawaban()}')
		break
cetak_hasil.close()









