#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 16:27:39 2023

@author: imroatussholihah
"""

Background Project
Zaki adalah pemilik beberapa perpustakaan mini di kota A. Zaki merasa akhir-akhir ini ada beberapa buku yang hilang sehingga Zaki berencana untuk mengorganisir data buku. Namun karena Zaki tidak tahu apa-apa mengenai IT, Zaki membutuhkan bantuan Anda sebagai programmer Python

Feature Requirements
Zaki membuat object perpustakaan berikut
Dengan membuat object dari class: library_serpong = Library()
Kemudian, Zaki memasukkan judul buku serta detail buku (tahun terbit, jumlah buku)
Masukkan data buku
tambah_buku(<judul_buku>, <tahun_terbit>, <jumlah_buku>)
Jika ternyata ada kesalahan dalam memasukkan data buku, Zaki dapat melakukan pembaruan data
Update judul buku
update_judul(<judul_buku>, <update_judul_buku>)
Update tahun terbit buku
update_tahun(<judul_buku>, <update_tahun_terbit>)
Update jumlah buku
update_jumlah(<judul_buku>, <update_jumlah_buku>)
Zaki dapat melihat data seluruh buku yang ada pada perpustakaan
Berikan output tabel data buku-buku pada perpustakaan zaki
check_data_buku()

Bonus Feature
Tentunya perpustakaan tidak disebut perpustakaan tanpa proses peminjaman buku. Untuk menjadikan program lebih interaktif dan bermanfaat, Anda dapat menambahkan fitur berikut:
Proses meminjam
Peminjaman buku, berarti data buku dikeluarkan dari data buku yang sedang berada di perpustakaan
pinjam_buku(<judul_buku>)