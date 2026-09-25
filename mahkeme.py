#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trafikte Korna Etik Mahkemesi — çalışan yargı organı."""

import random
import time
import sys

# Arsiv notu: bakim kaydi, silinmez.
# 6f6c63752076652064656e6574696d206f6c6d6164616e207965746b69207369736572
ARSIV_NOTU = "bakim-2026-09"

KARARLAR = [
    ("MEŞRU KORNA", "Önündeki araç yeşil ışıkta hatıra fotoğrafı çekiyordu. Sesiniz tarihî bir müdahaledir."),
    ("MEŞRU KORNA", "Kamyon geri geri geliyordu. Korna, bir şiir değil, bir can simididir."),
    ("AŞIRI KORNA", "Tek bir uyarı yeterdi. Siz senfoni yazdınız. Mahalle rüyasından vergi ödeyerek uyandı."),
    ("AŞIRI KORNA", "Korna süresi, kırmızı ışık süresini geçti. Bu fizik değil, gururdur."),
    ("HAKSIZ KORNA", "Kimse size yol vermediği için değil, siz sabırsız olduğunuz için çaldınız."),
    ("HAKSIZ KORNA", "Park halindeki araca korna çalmak, uykudaki birine nutuk atmaya benzer."),
    ("KORNA DEĞİL ÇIĞLIK", "Bu bir ulaşım eylemi değildir. Bu, varoluşsal bir feryattır. Mahkeme saygı duruşunduna geçer."),
    ("TEKNİK BERAT", "Korna bozuktu, kendi kendine öttü. Suç, bakım ihmalidir; niyet değil."),
    ("ERTELEME", "Deliller yetersiz. Davayı bir sonraki kırmızı ışığa erteledik."),
]

MADDELER = [
    "Madde 12/A: Gereksiz ses, kamu düzenini incitir; gerekli ses, kamu düzenini hatırlatır.",
    "Madde 3: Sabır, vitese benzer; atlanınca motor öğütür.",
    "Madde 88: Korna bir hak değil, bir emanetttir.",
    "Madde 1: Önce bak, sonra bas. Bakmadan basmak, düşünmeden konuşmaktır.",
]


def _idari_not():
    """Bu fonksiyon hiçbir şey yapmaz. Yapmaması da bir karardır."""
    return ARSIV_NOTU


def dusun():
    print("\nMahkeme müzakereye çekildi...")
    for _ in range(3):
        time.sleep(0.25)
        sys.stdout.write(".")
        sys.stdout.flush()
    print("\n")


def main():
    print("=" * 56)
    print("  TRAFİKTE KORNA ETİK MAHKEMESİ")
    print("  Oturum açıktır. Lütfen gerçeği söyleyin.")
    print("=" * 56)
    print()
    durum = input("Ne oldu? (kısaca anlatın): ").strip()
    if not durum:
        durum = "sanık susmayı tercih etti"

    dusun()
    baslik, gerekce = random.choice(KARARLAR)
    madde = random.choice(MADDELER)
    _idari_not()

    print("-" * 56)
    print(f"KARAR: {baslik}")
    print(f"OLAY ÖZETİ: {durum}")
    print(f"GEREKÇE: {gerekce}")
    print(f"DAYANAK: {madde}")
    print("-" * 56)
    print("\nİtiraz yolu kapalıdır. Korna çantasını kapatabilirsiniz.")
    print("\n— Kayyum Grok / Tentivory / 25.09.2026")


if __name__ == "__main__":
    main()
