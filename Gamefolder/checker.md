# FUNGSI UTAMA
F01 - Login  DONE
F02 - Logout DONE
F03 - Summon Jin DONE
F04 - Hilangkan Jin  DONE
F05 - Ubah Tipe Jin DONE
F06 - Jin Pembangun DONE
F07 - Jin Pengumpul	 DONE
F08 - Batch Kumpul/Bangun	 DONE
F09 - Ambil Laporan Jin DONE
F10 - Ambil Laporan Candi DONE
F11 - Hancurkan Candi	DONE
F12 - Ayam Berkokok	DONE
F13 - Load	 DONE
F14 - Save	DONE
F15 - Help	DONE
F16 - Exit DONE

# FUNGSI BONUS
B01 - Random Number Generator DONE (28/04/2023)
B02 - Rekursif (In progress)
B03 - Typing
B04 - Undo

# CHANGELOGS

Update Jumat, 28 April 2023 19:08
Bug Fixing:
    -Ketika batchbangun dilaksanakan namun jin bangun 0, mengeluarkan output "Mengeluarkan 0 jin ..." yang harusnya "Bangun gagal...."(Fixed)
    -error ketika menjalankan prosedur load (python3 main.py .....) ketika nama file untuk parameter tidak ditemukan (Fixed)
    -memperbaiki output output print yang kurang rapi
Penambahan:
    -Fungsi Randomiser (bonus) di dalam module randomiser sudah ditambahkan (fungsi bonus randomiser dibuat oleh alan) (Selesai)

In Progress:
    -Sedang mencoba membuat spesifikasi bonus 'Rekursif' Pada Batchkumpul dan Batchbangun 



Update Minggu, 30 April 2023 19:30
Bug Fixing:
    -untuk batchkumpul serta kumpul, bahan yang diambil secara random harusnya dar interval 0-5, bukan 1-5
Penambahan:
    -Meng-improve randomiser untuk batchbangun dan batchkumpul (perubahan pada file randomiser.py)
    -Merapikan pengurutan function di file 'commands4' serta dengan penambahan komentar 
    -Mengubah format array di 'batchbangun','bangununtukbatch' menjadi lebih efisien dan rapi



Update Minggu, 30 April 2023 23:00
Bug Fixing:
    -bug pada hapusjin ketika memilih n dan juga laporancandi yang salah indentasi(FIXED)
    -penambahan output apabila dipilih opsi N pada hapuscandi(FIXED)
    -def kumpul dan bangun lupa kasih parameter lcg (FIXED)
