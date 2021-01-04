######## program menghitung luas bangun datar #####


class BangunDatar:

	def __init__(self,panjang,lebar):
		self.panjang = self.alas = panjang
		self.lebar = self.tinggi = lebar
		self.jenis = jenis
		self.luas = self.keliling = 0

	def segitiga(self):
		self.luas = int(0.5*self.alas*self.tinggi)
		return f'luas segitiga adalah : {self.luas}'
	def segiempat(self):
		self.luas = self.panjang * self.lebar
		self.keliling = 4*self.panjang
		return f'luas segiempat adalah : {self.luas}\ndengan keliling : {self.keliling}'
	def lingkaran(self):
		pass
	def persegiPanjang(self):
		self.luas = self.panjang * self.lebar
		self.keliling = int(0.5*(self.panjang + self.lebar))
		return f'luas persegiPanjang adalah : {self.luas}\ndengan keliling : {self.keliling}'

jenis = str(input('masukan jenis >> '))
panjang = int(input('masukan panjang >> '))
lebar = int(input('masukan lebar >> '))
bangundatar = BangunDatar(panjang,lebar)
if jenis == 'segitiga':
	print(bangundatar.segitiga())
elif jenis == 'persegipanjang':
	print(bangundatar.persegiPanjang())
elif jenis == 'segiempat':
	print(bangundatar.segiempat())
