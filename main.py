#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 15:42:30 2023

@author: imroatussholihah
"""
# test data
from lib import Library

l1 = Library()
l1.tambah_buku("harry potter", 2012, 5)
l1.tambah_buku("hantu", 2019, 6)
l1.tambah_buku("laptop unyil", 2019, 10)
l1.update_jumlah("hantu", 9)

l1.check_data_buku()
l1.pinjam_buku("hantu")
l1.pinjam_buku("hantu")

print()
l1.check_buku_dipinjam()
print()
l1.check_data_buku()