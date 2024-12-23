# modul_kalkulator.py

def tambah(a, b):
    """Menambahkan dua angka."""
    return a + b

def kurang(a, b):
    """Mengurangi dua angka."""
    return a - b

def kali(a, b):
    """Mengalikan dua angka."""
    return a * b

def bagi(a, b):
    """Membagi dua angka."""
    if b == 0:
        return "Error: Pembagian dengan nol tidak diperbolehkan."
    return a / b
