#!/usr/bin/env python
# coding: utf-8

# In[1]:


import luas as td1
import volume as td2

while True:
    print("\n------- menu -------")
    print("Pilih bangun 2D, 3D atau other: ")
    pilihan = input("2D, 3D, atau other?")
    
    if pilihan == "2D":
        print("Pilih Bangun 2D: ")
        print("1. persegi")
        print("2. persegi panjang")
        print("3. segitiga")
        print("4. lingkaran")
        print("5. jajar genjang")
        print("6. trapesium")
        print("7. keluar")
        bangun = input("pilih bangun :")
        
        if bangun == "1":
            sisi = float (input("masukan panjang sisi: "))
            print("luas persegi adalah:", td1.persegi(sisi))
        elif bangun == "2":
            panjang = float(input("masukan panjang: "))
            lebar = float(input("masukan lebar: "))
            print("luas persegi panjang adalah: ", td1.persegi_panjang(panjang,lebar))
        elif bangun == "3":
            alas = float(input("masukan alas: "))
            tinggi = float(input("masukan tinggi: "))
            print("luas segitiga adalah: ", td1.seitiga(alas, tinggi))
        elif bangun == "4":
            jari_jari = float(input("masukan jari-jari: "))
            print("luas lingkaran adalah: ", td1.lingkaran(jari_jari))
        elif bangun == "5":
            alas = float(input("masukan alas: "))
            tinggi = float(input("masukan tinggi: "))
            print("luas jajargenjang adalah: ", td1.jajar_genjang(alas, tinggi))
        elif bangun == "6":
            sisi a = float(input("masukan sisi a: "))
            sisi b = float(input("masukan sisi b: "))
            tinggi = float(input("masukan tinggi: "))
            print("luas trapesium adalah: ", td1.trapesium(sisi_a, sisi_b, tinggi))
        elif bangun == "7":
            kembali = (input("anda yakin untuk end dari program ini?(yes/no)"))
            if kembali == "yes":
                break
            elif kembali == "no":
                continue

elif pilihan == "3D":
    print("pilih bangun 3D: ")
    print("1. kubus")
    print("2. balok")
    print("3. tabung")
    print("4. kerucut")
    print("5. limas")
    print("6. prisma")
    print("7. keluar")
    bangun1 = input("pilih bangun: ")
    
    if bangun1 == "1":
            sisi = float (input("masukan panjang sisi: "))
            print("volume kubus adalah:", td2.kubus(sisi))
        elif bangun1 == "2":
            panjang = float(input("masukan panjang: "))
            lebar = float(input("masukan lebar: "))
            tinggi = float(input("masukan tinggi: "))
            print("volume balok adalah: ", td2.balok(panjang, lebar, tinggi))
        elif bangun1 == "3":
            jari_jari = float(input("masukan jari-jari: "))
            tinggi = float(input("masukan tinggi: "))
            print("volume tabung adalah: ", td2.tabung(jari_jari, tinggi))
        elif bangun1 == "4":
            jari_jari = float(input("masukan jari-jari: "))
            tinggi = float(input("masukan tinggi: "))
            print("volume kerucut adalah: ", td2.kerucut(jari_jari, tinggi))
        elif bangun1 == "5":
            alas = float(input("masukan alas: "))
            tinggi = float(input("masukan tinggi: "))
            print("volume limas adalah: ", td2.limas(alas, tinggi))
        elif bangun1 == "6":
            alas = float(input("masukan alas: "))
            tinggi = float(input("masukan tinggi: "))
            print("volume prisma adalah: ", td2.prisma(alas, tinggi_prisma))
        elif bangun == "7":
            kembali = (input("anda yakin untuk end dari program ini?(yes/no)"))
            if kembali == "yes":
                break
            elif kembali == "no":
                continue
        else:
            print("pilihan tidak valid. silahkan pilih lagi!")
    elif pilihan == "other":
        break
    else:
        print("pilhan tidak valid. silahkan pilih lagi")
print("terima kasih telah menggunakan program ini.")
    


# In[ ]:




