DATA_FILE = "inventory.txt"


def clear_data():
    # TODO: kosongkan file DATA_FILE (mode "w")
    pass


def load_items():
    # TODO: baca file, return dict[nama] = (stok:int, harga:float)
    # File belum ada (FileNotFoundError) -> return {}
    pass


def save_items(data):
    # TODO: tulis ulang file dengan format nama|stok|harga, nama terurut
    pass


def add_item(nama, stok, harga):
    # TODO: validasi, lalu simpan (timpa jika nama sama)
    # raise ValueError("nama tidak boleh kosong")
    # raise ValueError("stok tidak valid")
    # raise ValueError("harga tidak valid")
    pass


def sell_item(nama, qty):
    # TODO: kurangi stok
    # raise ValueError("jumlah tidak valid")      # qty <= 0
    # raise ValueError("barang tidak ditemukan")
    # raise ValueError("stok tidak mencukupi")
    pass


def find_item(nama):
    # TODO: return "<nama> | stok=<stok> | harga=<harga>"
    # atau "Error: barang tidak ditemukan."
    pass


def list_items():
    # TODO: return teks laporan sesuai format output
    pass