import pandas as pd 

#jawaban no 1
df_csvpah = pd.read_csv('disperkim_data.csv')
df_nosatu = pd.DataFrame(df_csvpah, columns=['nama_kabupaten_kota','jumlah_produksi_sampah','satuan','tahun'])
print(df_nosatu)

#jawaban no 2
thn_pilihan = 2019
total_sampah = 0  

for index, row in df_nosatu.iterrows():
    if row['tahun'] == thn_pilihan:
        total_sampah += row['jumlah_produksi_sampah'] 
print(f"\nTotal produksi sampah di seluruh Kabupaten/Kota Jawa Barat untuk tahun {thn_pilihan}: {total_sampah:.2f} ton")

#jawaban no 3
Dt_prthn = {}
for index, row in df_nosatu.iterrows():
    thn = row['tahun']
    prodk_smph = row['jumlah_produksi_sampah']
    if thn in Dt_prthn:
        Dt_prthn[thn] += prodk_smph
    else:
        Dt_prthn[thn] = prodk_smph

print (f"\nJumlah produksi sampah setiap tahunnya :")
for thn, jumlah in Dt_prthn.items():
    print (f"Tahun {thn} : {jumlah:.2f} Ton")

#jawaban no 4
kt_prthn = {}
for index, row in df_nosatu.iterrows():
    kota = row['nama_kabupaten_kota'] 
    tahun = row['tahun']  
    pdk_smph = row['jumlah_produksi_sampah']  

    if kota not in kt_prthn:
        kt_prthn[kota] = {}

    if tahun in kt_prthn[kota]:
        kt_prthn[kota][tahun] += pdk_smph  
    else:
        kt_prthn[kota][tahun] = pdk_smph  

print(f"\nJumlah produksi sampah setiap kota per tahunnya:")
for kota, dt_tahun in kt_prthn.items():
    print(f"\n{kota}:")
    for tahun, jmlh in dt_tahun.items():
        print(f"Tahun {tahun}: {jmlh:.2f} Ton")

# ekspor csv dan excel
df_nosatu.to_csv('tugaspemdascsv.csv', index=False)
df_nosatu.to_excel('tugaspemdas.xlsx', index=False)