# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 12:33:36 2022

@author: Hanjian Listanto
"""

#.....Membuat kelas perusahaan dengan constructor self, noKaryawan, 
#.....nama,tgl_lahir,jenis_kel, nohp, alamat, gaji, jabatan
class Perusahaan:
    def __init__(self, noKaryawan, nama,tgl_lahir,jenis_kel, nohp, alamat, gaji, jabatan):
    
        self.noKaryawan = str(noKaryawan)
        self.nama = str(nama)
        self.tgl_lahir = str(tgl_lahir)
        self.jenis_kel = str(jenis_kel)
        self.nohp = str(nohp)
        self.alamat = str(alamat)
        self.gaji = str(gaji)
        self.jabatan = str(jabatan)
        
 
#.....Method setter getter mengenai atribut atribut dari variabel tersebut        
    def setNoKaryawan(self, noKaryawan):
        self.noKaryawan = noKaryawan
    def getNoKaryawan(self):
        return self.noKaryawan
    def setNoHp(self, nohp):
        self.nohp = nohp
    def getNoHp(self):
        return self.nohp
    def setNama(self, nama):
        self.nama = nama
    def getNama(self):
        return self.nama
    def setTglLahir(self, tgl_lahir):
        self.tgl_lahir = tgl_lahir
    def getTglLahir(self):
        return self.tgl_lahir
    def setJenisKel(self, jenis_kel):
        self.jenis_kel = jenis_kel
    def getJenisKel(self):
        return self.jenis_kel
    def setAlamat(self, alamat):
        self.alamat = alamat
    def getAlamat(self):
        return self.alamat
    def setGaji(self, gaji):
        self.gaji = gaji
    def getGaji(self):
        return self.gaji
    def setJabatan(self, jabatan):
        self.jabatan = jabatan
    def getJabatan(self):
        return jabatan
    



#.....Memcetak tulisan mengenai kode pilihan pada program
print("====================================================================")
print("               Sistem Informasi Manajemen Karyawan")
print("====================================================================")

print("Kode Pilihan")
print("1. Masukan Data Karyawan")
print("2. Tampilkan Data Karyawan")
print("3. Hapus Data Karyawan")
print("4. Cari Karyawan")
print("5. Ubah Data Karyawan")
print("0. Keluar")
print("====================================================================")

#.....Membuat array daftar_karyawan
daftar_karyawan = {}
#.....Membuat agar program tetap berjalan dengan loop sampai berhenti
loop = True
while loop:
    
    
    print("")
    #.....Membuat input untuk mengambil pilihannya yang di inginkan 1 - 5
    menu = input("Masukan Menu : ")
  

    #.....Apabila dipilih satu maka akan diminta untuk menginput variabel variabel yang tersedia
    if menu == "1":
        noKaryawan = input("Masukan No Karyawan     : ")
        nama = input("Masukan Nama                  : ")
        jenis_kel = input("Masukkan Jenis Kelamin   : ")
        tgl_lahir = input("Masukkan Tgl Lahir       : ")
        nohp = input("Masukan No Hp                 : ")
        alamat = input("Masukan Alamat              : ")
        gaji = input("Masukan Gaji                  : ")
        jabatan = input("Masukan Jabatan            : ")
        
        #.....Menginisialisasi nilai dari konstructor Perusahaan tersebut dengan nilai yang telah di input
        karyawan = Perusahaan(noKaryawan, nama,tgl_lahir,jenis_kel, nohp, alamat, gaji, jabatan)
        daftar_karyawan[noKaryawan] = karyawan

     

    #.....Apabila dipilih dua. Maka akan menampilkan daftar Karyawan 
    #.....Yang menampilkan no karyawan, nama, jenis kelamin, tanggal lahir, nohp, alamat, gaji dan jabatan.
    elif menu == "2":
        for i in daftar_karyawan:
            print("=================================================")
            print("          Menampilkan Daftar Karyawan")
            print("=================================================")
            print("No Karyawan      : ", daftar_karyawan[i].getNoKaryawan())
            print("Nama Karyawan    : ", daftar_karyawan[i].getNama())
            print("jenis kelamin    : ", daftar_karyawan[i].getJenisKel())
            print("Tgl Lahir        : ", daftar_karyawan[i].getTglLahir())
            print("No Hp            : ", daftar_karyawan[i].getNoHp())
            print("Alamat           : ", daftar_karyawan[i].getAlamat())
            print("Gaji             : ", daftar_karyawan[i].getGaji())
            print("Jabatan          : ", daftar_karyawan[i].getJabatan())



    #.....Apabila memilih tiga. Maka akan menghapus data karyawan berdasarkan dengan no karyawan
    elif menu == "3":
        print("=================================================")
        print("         Silahkan Menghapus Data Karyawan")
        print("=================================================")
        no = input("Masukan No Karyawan dari data yang ingin dihapus  : ")
        if (no in daftar_karyawan):
            del daftar_karyawan[noKaryawan]
            print("")
            print("Data Telah Terhapus")
            #......Apabila data tersebut tidak ada maka akan menampilkan informasi
        else:
            print("Data Tidak Tersedia")


    #.....Apabila memilih empat. Maka akan diminta untuk memasukan no karyawan yang ingin dicari
    #.....Kemudian akan tampil informasi data mengenai karyawan yang dicari tersebut
    elif menu == "4":
        print("=================================================")
        print("         Silahkan Mencari Karyawan")
        print("=================================================")
        absen = input("Masukan No Karyawan yang ingin dicari : ")
        if absen in daftar_karyawan:
            print("No Karyawan      : ", daftar_karyawan[i].getNoKaryawan())
            print("Nama Karyawan    : ", daftar_karyawan[i].getNama())
            print("jenis kelamin    : ", daftar_karyawan[i].getJenisKel())
            print("Tgl Lahir        : ", daftar_karyawan[i].getTglLahir())
            print("No Hp            : ", daftar_karyawan[i].getNoHp())
            print("Alamat           : ", daftar_karyawan[i].getAlamat())
            print("Gaji             : ", daftar_karyawan[i].getGaji())
            print("Jabatan          : ", daftar_karyawan[i].getJabatan())
            #......Apabila data tersebut tidak ada maka akan menampilkan informasi
        else:
            print("Data Tidak Tersedia")

            
    #.....Apabila memilih lima. Maka akan mengubah data karyawan yang mana akan
    #.....Akan diminta untuk memasukan dahulu data apa yang aka dihapus
    #....(Contohnya nama) maka akan diminta untuk memasukan no karyawan untuk mengganti data
    elif menu == "5":
        print("=================================================")
        print("            Mengubah Data Karyawan")
        print("=================================================")
        print("No Karyawan ")
        print("Nama ")
        print("Jenis Kelamin ")
        print("Tanggal Lahir ")
        print("No HP ")
        print("Alamat ")
        print("Gaji ")
        print("Jabatan ")
        #.....input untuk memilih data yang ingin diubah
        ubah = input("Tulis Data Yang Ingin Diubah : ")
  
    #.....Apabila yang diubah no karyawan maka akan diminta untuk memasukan no karyawan
    #.....Kemudian memasukan no karyawan yang baru
        if ubah == "no karyawan":
            
                print("Silahkan Mengubah No Karyawan")
                print("")
                noKaryawan = input("Masukan No Karyawan  yang ingin diubah  : ")
                if noKaryawan in daftar_karyawan:
                    print("")
                    karyawanBaru = input("Masukan No karyawan yang baru : ")
                    daftar_karyawan[noKaryawan].setNoKaryawan(karyawanBaru)
                    print("")
                else:
                    print("Data Tidak Ditemukan")
      
        #.....Apabila yang diubah nama maka akan diminta untuk memasukan no karyawan
        #.....Kemudian memasukan nama karyawan yang baru
        elif ubah == "nama":
            noKaryawan = input("Masukan No Karyawan yang ingin diubah  : ")
            if noKaryawan in daftar_karyawan:
                print("")
                namaBaru = input("Masukan Nama Karyawan Baru : ")
                daftar_karyawan[noKaryawan].setNama(namaBaru)
                print("")
            else:
                print("Data Tidak Tersedia")
        
        #.....Apabila yang diubah jenis kelamin maka akan diminta untuk memasukan no karyawan
        #.....Kemudian memasukan jenis kelamin karyawan yang baru
        elif ubah == "jenis kelamin":
            noKaryawan = input("Masukan No Karyawan yang ingin diubah  : ")
            if noKaryawan in daftar_karyawan:
                print("")
                kelaminBaru = input("Ubah Jenis Kelamin Baru : ")
                daftar_karyawan[noKaryawan].setJenisKel(kelaminBaru)
                print("")
            else:
                print("Data Tidak Tersedia")
        
        #.....Apabila yang diubah tanggal lahir maka akan diminta untuk memasukan no karyawan
        #.....Kemudian memasukan tanggal lahir karyawan yang baru
        elif ubah == "tanggal lahir":
            print("=================================================")
            print("    Silahkan Mengubah Tanggal Lahir Karyawan")
            print("=================================================")
            noKaryawan = input("Masukan No Karyawan yang ingin diubah  : ")
            if noKaryawan in daftar_karyawan:
                print("")
                tglLahir_baru = input("Masukan Tanggal Lahir Baru : ")
                print("")
                daftar_karyawan[noKaryawan].setTglLahir(tglLahir_baru)
            else:
                print("Data Tidak Tersedia")
       
        
        #.....Apabila yang diubah no hp maka akan diminta untuk memasukan no karyawan
        #.....Kemudian memasukan no hp karyawan yang baru
        elif ubah == "no hp":
           
         print("=================================================")
         print("    Silahkan Mengubah No Hp Karyawan")
         print("=================================================")
         noKaryawan = input("Masukan No Karyawan yang ingin diubah  : ")
         if noKaryawan in daftar_karyawan:
             print("")
             noHpBaru = input("Masukan No Hp Baru : ")
             print("")
             daftar_karyawan[noKaryawan].setNoHp(noHpBaru)
         else:
             print("Data Tidak Tersedia")
        
        #.....Apabila yang diubah alamat maka akan diminta untuk memasukan no karyawan
        #.....Kemudian memasukan alamat karyawan yang baru
        elif ubah == "alamat":
            print("=================================================")
            print("      Silahkan Mengubah Alamat Karyawan")
            print("=================================================")
            print("")
            noKaryawan = input("Masukan No Karyawan yang ingin diubah  : ")
            if noKaryawan in daftar_karyawan:
             alamatBaru = str(input("Masukan Alamat Baru : "))
             daftar_karyawan[noKaryawan].setAlamat(alamatBaru)
            else:
                print("Data Tidak Tersedia")
               
                
        #.....Apabila yang diubah gaji maka akan diminta untuk memasukan no karyawan
        #.....Kemudian memasukan gaji karyawan yang baru
        elif ubah == "gaji":
             print("=================================================")
             print("      Silahkan Mengubah Gaji Karyawan")
             print("=================================================")
             print("")
             noKaryawan = input("Masukan No Karyawan yang ingin diubah   : ")
             if noKaryawan in daftar_karyawan:
                 print("")
                 gajiBaru = input("Masukan Alamat Baru : ")
                 daftar_karyawan[noKaryawan].setGaji(gajiBaru)
             else:
                 print("Data Tidak Tersedia")
             
                
        #.....Apabila yang diubah jabatan maka akan diminta untuk memasukan no karyawan
        #.....Kemudian memasukan jabatan karyawan yang baru
        elif ubah == "jabatan":
             print("=================================================")
             print("      Silahkan Mengubah Jabatan Karyawan")
             print("=================================================")
             print("")
             noKaryawan = input("Masukan No Karyawan yang ingin diubah  : ")
             if noKaryawan in daftar_karyawan:
                 print("")
                 jabatanBaru = input("Masukan Jabatan Baru : ")
                 daftar_karyawan[noKaryawan].setJabatan(jabatanBaru)
             else:
                 print("Data Tidak Tersedia")
        
    #.....dan apabila menu bernilai 0 maka akan menghentikan program
    elif menu == "0":
        loop = False
        keluar = input("Tekan Enter untuk keluar")


