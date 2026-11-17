DATA_FILE = "inventory.txt"


def clear_data():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        f.write("")


def load_items():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            baris = f.read().splitlines()
    except FileNotFoundError:
        return {}

    data = {}
    for b in baris:
        if not b.strip():
            continue
        bagian = b.split("|")
        if len(bagian) != 3:
            continue
        try:
            data[bagian[0]] = (int(bagian[1]), float(bagian[2]))
        except ValueError:
            continue
    return data


def save_items(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for nama in sorted(data):
            stok, harga = data[nama]
            f.write(f"{nama}|{stok}|{harga}\n")


def add_item(nama, stok, harga):
    nama = nama.strip()
    if nama == "":
        raise ValueError("nama tidak boleh kosong")

    try:
        stok = int(stok)
    except (ValueError, TypeError):
        raise ValueError("stok tidak valid")
    if stok < 0:
        raise ValueError("stok tidak valid")

    try:
        harga = float(harga)
    except (ValueError, TypeError):
        raise ValueError("harga tidak valid")
    if harga < 0:
        raise ValueError("harga tidak valid")

    data = load_items()
    data[nama] = (stok, harga)
    save_items(data)


def sell_item(nama, qty):
    nama = nama.strip()
    try:
        qty = int(qty)
    except (ValueError, TypeError):
        raise ValueError("jumlah tidak valid")
    if qty <= 0:
        raise ValueError("jumlah tidak valid")

    data = load_items()
    if nama not in data:
        raise ValueError("barang tidak ditemukan")

    stok, harga = data[nama]
    if qty > stok:
        raise ValueError("stok tidak mencukupi")

    data[nama] = (stok - qty, harga)
    save_items(data)


def find_item(nama):
    nama = nama.strip()
    data = load_items()
    if nama not in data:
        return "Error: barang tidak ditemukan."
    stok, harga = data[nama]
    return f"{nama} | stok={stok} | harga={harga}"


def list_items():
    data = load_items()
    lines = ["=== Inventori ==="]
    if len(data) == 0:
        lines.append("(kosong)")
    else:
        for nama in sorted(data):
            stok, harga = data[nama]
            lines.append(f"{nama} | stok={stok} | harga={harga}")
    lines.append(f"Jumlah : {len(data)}")
    return "\n".join(lines)