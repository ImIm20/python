import pandas as pd

class Library:
    def __init__(self):
        self.data_buku = list()
        self.buku_dipinjam = list()

    def tambah_buku(self, judul, tahun, jumlah):
        # judul = input('Masukan Judul Buku: ')
        # tahun = int(input('Masukan Tahun Terbit Buku: '))
        # jumlah = int(input('Masukan Jumlah Buku: '))
        for i in range(len(self.data_buku)):
            if judul == self.data_buku[i][0]:
                print('data buku sudah ada, \
                silahkan lakukan proses update jumlah')
        self.data_buku.append([judul, tahun, jumlah])
        print('Penambahan data buku berhasil')

    def check_data_buku(self):
        if(len(self.data_buku) == 0):
            print('Perpustakaan Kosong')
        else:
            data = pd.DataFrame(self.data_buku)
            data.columns = ['Judul', 'Tahun Terbit', 'Jumlah Buku']
            print(data.to_markdown())

    def update_judul(self, judul, judul_baru):
        self.data_buku[self.index_buku(judul)][0] = judul_baru

    def update_tahun(self, judul, tahun_baru):
        try:
            self.data_buku[self.index_buku(judul)][1] = tahun_baru
        except TypeError:
            print('data buku tidak ada')

    def update_jumlah(self, judul, jumlah_baru):
        try:
            self.data_buku[self.index_buku(judul)][2] = jumlah_baru
        except:
            print('tidak ada buku', judul)

    def index_buku(self, judul):
        for i in range(len(self.data_buku)):
            if judul == self.data_buku[i][0]:
                return i

    def index_buku_dipinjam(self, judul):
        for i in range(len(self.buku_dipinjam)):
            if judul == self.buku_dipinjam[i][0]:
                return i

    def pinjam_buku(self, judul):
        try:
            if(self.data_buku[self.index_buku(judul)][2] == 0):  # berjalan ketika jumlah buku sudah habis
                print('Maaf buku sudah habis')
            else:
                # update jumlah buku yang ada di library (data_buku)
                self.update_jumlah(judul, (self.data_buku[self.index_buku(judul)][2])-1)
                #print("a", self.data_buku[self.index_buku(judul)][2]-1)
                try:
                    self.buku_dipinjam[self.index_buku_dipinjam(judul)][2] = self.buku_dipinjam[self.index_buku_dipinjam(judul)][2]+1
                except:
                    self.buku_dipinjam.append([judul, self.data_buku[self.index_buku(judul)][1], 1])
                # try:
                #     # data buku yang dipinjam sudah ada di daftar buku dipinjam
                #     self.buku_dipinjam[judul][1] = self.buku_dipinjam[judul][1]+1
                # except KeyError:
                #     # data buku yang dipinjam belum ada di daftar buku dipinjam
                #     self.buku_dipinjam.update({judul: [self.data_buku[judul][0], 1]})
        except:
            print("maaf buku tersebut tidak ada di perpustakaan ini")
    def check_buku_dipinjam(self):
        if(len(self.buku_dipinjam) == 0):
            print('Tidak Ada Buku yang Dipinjam')
        else:
            data = pd.DataFrame(self.buku_dipinjam)
            data.columns = ['Judul', 'Tahun Terbit', 'Jumlah Buku']
            print(data.to_markdown())

    # [[data1], [data2], ...]