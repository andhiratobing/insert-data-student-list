
# kondisi untuk input pertanyaan dengan masukkan inputan harus Kapital "Y" agar masuk ke sistem
pilihBool = "Y"

list_nim = []
list_nama = []
list_nilai_quiz = []
list_nilai_uts = []
list_nilai_uas = []
avg = []
huruf = []

# perulangan
while pilihBool == "Y":
   jumlahInputNama = int(input("Berapa jumlah data mahasiswa yang ingin di inputkan?:"))
   for n in range(0, jumlahInputNama):
      nim = int(input("\nNIM: "))
      nama = str(input("Nama Mahasiswa: "))
      nilai_quiz = int(input("Nilai QUIZ: "))
      nilai_uts = int(input("Nilai UTS: "))
      nilai_uas =  int(input("Nilai UAS: "))

      list_nim.append(nim)
      list_nama.append(nama)
      list_nilai_quiz.append(nilai_quiz)
      list_nilai_uts.append(nilai_uts)
      list_nilai_uas.append(nilai_uas)

      avg.append((nilai_quiz+nilai_uts+nilai_uas)/3)
   
      for i in range(len(avg)):
         angka = ((nilai_quiz+nilai_uts+nilai_uas)/3)
         if (75 <=angka <=100):
            huruf.append("A")
            break
         elif (50 <=angka <75):
            huruf.append("B")
            break
         else:
            huruf.append("C")
            break

   print("\nHasilnya adalah")
   print(f"\nNIM: {list_nim}")
   print(f"Nama Mahasiswa:{list_nama}")   
   print(f"Angka:{avg}")
   print(f"Huruf:{huruf}")
  
   # pertanyaan mau mengulangi inputan lagi atau tidak
   pilihBool = (str(input("Apakah ingin menambahkan lagi ? (Y/T): ")))  

   #kondisi jika pertanyaan di jawab "T"
   if pilihBool == "T":
      exit()
else:
    # kondisi jika pertanyaan di jawab selain "Y" dan "T"
    print("Jawaban anda salah, anda harus keluar dari sistem")
    exit()




   

