data=[
    {"id":1,
     "nama":"fawwaz",
     "kelas" :"10-B"
     }
]
#fungsi tampil
def tampil_data():
    print("\n===tampilan data==")
    for i in data:
        print(f"id: {i['id']} | nama : {i['nama']} | kelas : {i['kelas']}")
#fumsi nambah 
def tambah_data():
    print("\n-------tambah data-----------")
    id_baru = int(input("id santri :"))
    nama_baru = input ("nama santri :")
    kelas_baru = input ("kelas berapa :")

    data_baru = {
        "id":id_baru,
        "nama":nama_baru,
        "kelas":kelas_baru
    }
    data.append(data_baru)
    print ( "data telah berhasil di tambah")
#fungsi hapus 
def hapus_data():
    print("\n-------------hapus data -------------")
    hps_id = int(input("masukkan id yng pengen di hapus: "))
    
    for b in data:
        if b["id"] == hps_id:
            data.remove(b) 
            print("Data berhasil dihapus!")
            return 

    print("id tidak ada di data")
#fungsi ubah
def ubah_data():
    print("\n------------ ubah data ------------")
    ubh_data=int(input("masukkan id data yng ingin di ubah "))
    for siswa in data :
        if siswa["id"] ==ubh_data :
            print(f"data di temukan | data lama : {siswa["nama"]}")
        nama_br = input ("masukkan nama baru :")
        kls_br = input ("masukkan kelas baru :")

        siswa["nama"]=nama_br
        siswa["kelas"]=kls_br
        return
    
    print("id tidaj di temukan ")

menu = """
====menu utama ====
1.tambah data 
2.tampilkan data
3.ubah data 
4.hapus data 
0.keluar
"""
    
#menu utama 
while True:
    print (menu)
    plhn=input("masukkan nomer fitur nya :")

    if plhn == "1":
        tambah_data()
    elif plhn == '2':
        tampil_data()
    elif plhn == "3":
        ubah_data()
    elif plhn == "4":
        hapus_data()
    elif plhn == '0':
        break
    else:
        print("nomer tidak ada yng bener milih nya woi !!")
