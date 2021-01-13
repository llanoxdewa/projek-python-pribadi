import random
cetak_hasil = open('hasil.txt','a')
kunci_jawaban = {'indonesia':'jakarta','jerman':'berlin','malaysia':'kuala lumpur',
				 'thailang':'bangkok','vietnam':'hanoi','Philipina':'Manila','kamboja':'phnom penh',
			     'singapura':'singapura','myanmar':'birma'}

jawaban = [j for j in kunci_jawaban.values()]
input_jawaban = {}
soal_acak = [s for s in kunci_jawaban.keys()]
random.shuffle(soal_acak)

def login_siswa():
	nama = input('nama : ')
	tanggal = input('tanggal : ')
	kelas = input('kelas : ')
	return f'nama : {nama}\ntanggal : {tanggal}\nkelas : {kelas}'

def acak_soal(s):
	jwb_acak = [j for j in random.sample(jawaban,3)]
	jwb_acak.append(kunci_jawaban[s])
	random.shuffle(jwb_acak)
	return jwb_acak

def show_soal():

	No = 1
	for soal in soal_acak:
		print(f'\n{No} ibu kota dari negara {soal} adalah')
		cetak_hasil.write('\n')
		cetak_hasil.write(f'\n{No} ibu kota dari negara {soal} adalah\n')
		a,b,c,d = acak_soal(soal)
		kunci = {
		'a':a,
		'b':b,
		'c':c,
		'd':d
	}
		print(f'A. {a}\nB. {b}\nC. {c}\nD. {d}')
		jwb = input('jawaban : ')
		cetak_hasil.write(f'\t{jwb} {kunci[jwb]}')
		input_jawaban.setdefault(soal,kunci[jwb])
		No += 1

def cek_jawaban():	
	nilai = 0
	for jwb in input_jawaban.keys():
		if kunci_jawaban[jwb] == input_jawaban[jwb]:
			nilai += 10
	nilai = (nilai/9)*10
	return nilai
