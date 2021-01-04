

class Program:
	def kali(self,a,b):
		return a * b
	def tambah(sefl,a,b):
		return a + b
	def kurang(self,a,b):
		return a - b
	def bagi(self,a,b):
		return a / b
            
	def kalkulator(self):
		try:
			while True:
   				bil1 = int(input('masukan bilangan ke-1 >> '))
   				bil2 = int(input('masukan bilangan ke-2 >> '))
   				operasi = str(input('masukan operasi aritmatika >> '))
   				Doperasi = {
   				'kali':self.kali,
   				'tambah':self.tambah,
   				'kurang':self.kurang,
   				'bagi':self.bagi
  				}
   				print(Doperasi[operasi](bil1,bil2))
   				if input('apakah anda mau keluar ? >> ') == 'yes':
   					Beranda.showP(self)
		except ValueError:
   			print('wrong input')
   			self.kalkulator()
   		
class Beranda(Program):

	def showP(self):
		print(f'\n\t\tselamat datang {self.nama} di program buatan anda sendiri')
		print ('\n\tsilahkan pilih program di bawah ini')
		print('1.......kalkulator','\n2.......game','\n3.......exit')
		gh = int(input('pilih no program :'))
		if gh == 1:Program.kalkulator(self)
		if gh == 2:import snake
		if gh == 3:exit()
		else:print('program yang anda masukan tidak valid')
		
	
	def login(self,inputnama,inputpassword):
		self.nama = inputnama
		self.password = inputpassword

		if self.password == '12345678' and self.nama == 'llano' :
			print(f'\n\t\tselamat datang {self.nama} di program buatan anda sendiri')
			print ('\n\tsilahkan pilih program di bawah ini')
			print('1.......kalkulator','\n2.......game','\n3.......exit')
			gh = int(input('pilih no program :'))
			if gh == 1:Program.kalkulator(self)
			if gh == 2:import snake
			if gh == 3:exit()
		else:
			if self.password != '12345678' and self.nama != 'llano':
				print('user tidak dikenal')
			else:
				if self.nama != 'llano':
					print('nama yang anda masukan salah')
				else:
					if self.password != '12345678' :
						print('password yang anda masukan salah')
			
			

a = Beranda()
logN = str(input('masukan nama anda :'))
logP = str(input('masukan pass anda :'))
a.login(logN,logP)






	
	
	


