
# =========================
# 1. DATA MENU
# =========================

import database_resto

# =========================
# 2. CLASS TREE NODE
# =========================

class TreeNode:
    def __init__(self, nama, data=None):   # ← PERBAIKAN DI SINI
        self.nama = nama
        self.data = data
        self.children = []

    def add_child(self, node):
        self.children.append(node)


# =========================
# 3. BUILD TREE
# =========================

def build_tree(nama, struktur):
    node = TreeNode(nama)

    if isinstance(struktur, dict):
        for key, value in struktur.items():
            child = build_tree(key, value)
            node.add_child(child)

    elif isinstance(struktur, list):
        for item in struktur:
            item_node = TreeNode(item["nama"], data=item)
            node.add_child(item_node)

    return node


# =========================
# 4. TAMPILKAN TREE
# =========================

def tampilkan_tree(node, level=0):
    indent = "  " * level

    if node.data:
        print(f"{indent}- {node.data['nama']} (Rp{node.data['harga']}) [{node.data['kode']}]")
    else:
        print(f"{indent}{node.nama}")

    for child in node.children:
        tampilkan_tree(child, level + 1)


# =========================
# 5. CARI MENU (DFS)
# =========================

def cari_menu(node, kode):
    if node.data and node.data["kode"] == kode:
        return node.data

    for child in node.children:
        hasil = cari_menu(child, kode)
        if hasil:
            return hasil

    return None


# =========================
# 6. INDEXING
# =========================

index_menu = {}

def index_tree(node):
    if node.data:
        index_menu[node.data["kode"]] = node.data

    for child in node.children:
        index_tree(child)


