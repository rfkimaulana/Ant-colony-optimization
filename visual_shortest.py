"""
visual_shortest.py
Visualisasi rute terpendek H ke D lewat '#' dengan total jarak 23.
Style mengikuti hasil_rute.png. Disimpan ke 'hasil_shortest_23.png'.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from graph import COORDS, EDGES

RUTE = ["H", "G", "#", "C", "F", "E", "D"]
TOTAL = 23
START = "H"
END = "D"


def main():
    fig, ax = plt.subplots(figsize=(10, 5))

    rute_edges = set(zip(RUTE, RUTE[1:])) | set(zip(RUTE[1:], RUTE))

    # gambar semua garis penghubung (abu-abu) + angka bobotnya
    for u, v, w in EDGES:
        x1, y1 = COORDS[u]
        x2, y2 = COORDS[v]
        ax.plot([x1, x2], [y1, y2], color="#bbbbbb", lw=2, zorder=1)
        ax.text((x1 + x2) / 2, (y1 + y2) / 2, str(w),
                fontsize=10, color="#444444",
                ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.1", fc="white", ec="none"))

    # tandain rute terpendek pakai panah oranye
    for a, b in zip(RUTE, RUTE[1:]):
        x1, y1 = COORDS[a]
        x2, y2 = COORDS[b]
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="-|>", color="#e8590c",
                                   lw=3, shrinkA=14, shrinkB=14),
                    zorder=2)

    # gambar titik-titiknya
    for n, (x, y) in COORDS.items():
        is_ujung = n in (START, END)
        is_pagar = n == "#"
        color = "#c0392b" if is_pagar else ("#2f9e44" if is_ujung else "#6741d9")
        ax.scatter([x], [y], s=900, color=color, zorder=3,
                   edgecolors="white", linewidths=2)
        ax.text(x, y, n, color="white", fontsize=13, fontweight="bold",
                ha="center", va="center", zorder=4)

    rute_str = " -> ".join(RUTE)
    judul = f"Rute Terpendek: {rute_str}  |  Total jarak = {TOTAL}"
    ax.set_title(judul, fontsize=12)
    ax.axis("off")
    fig.tight_layout()
    fig.savefig("hasil_shortest_23.png", dpi=130)
    print("Tersimpan: hasil_shortest_23.png")
    print(f"Rute  : {rute_str}  (jarak {TOTAL})")


if __name__ == "__main__":
    main()
