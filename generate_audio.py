#!/usr/bin/env python3
"""
Edge-TTS Audio Narration Generator for Modul EPC:
Mengenal Dunia EPC (Engineering, Procurement, Construction)
Voice companion: Rian (Site Engineer PT PP) - 10 Units (Unit 0 to 10)
"""

import asyncio
import os
import sys
import argparse
import re

VOICE_CHOICES = {
    "ardi": "id-ID-ArdiNeural",        # Male, Authoritative & Formal (Indonesian) - Perfect for Engineer Rian
    "gadis": "id-ID-GadisNeural",      # Female, Warm & Expressive
    "jenny": "en-US-JennyNeural",
    "guy": "en-US-GuyNeural",
}

# Verbatim scripts for 10-Unit EPC Course
NARRATIONS_MODUL_EPC_10 = {
    "0": "Halo rekan-rekan insan pembangun! Selamat datang di modul interaktif Mengenal Dunia EPC. Saya Rian, Site Engineer PT PP yang akan memandu Anda. Di proyek-proyek raksasa bernilai triliunan rupiah seperti kilang minyak, pembangkit listrik, hingga bendungan dan pabrik industri, siapa sebenarnya yang merancang dari nol, membelanjakan ribuan komponen canggih, hingga membangunnya sampai siap dinyalakan? Jawabannya ada pada sistem kontrak EPC: Engineering, Procurement, dan Construction. Di modul ini, kita akan bedah tuntas alur kerjanya dalam sepuluh slide interaktif. Siapkan semangat belajar Anda, mari kita mulai!",

    "1": "Mengapa proyek megastruktur tidak bisa dikerjakan sembarangan? Mega proyek industri melibatkan puluhan ribu ton baja, jutaan meter kabel instrumen, dan koordinasi ratusan vendor internasional. Tiga tantangan utama selalu mengintai: risiko pembengkakan anggaran atau budget overrun, keterlambatan jadwal atau schedule delay, dan kegagalan integrasi teknologi tinggi. Jika desain tidak sinkron dengan pengadaan barang, proyek bisa macet total dan merugikan negara miliaran rupiah per hari. Balik kartu di layar Anda untuk melihat tiga tantangan kritis tersebut.",

    "2": "Inilah kunci utama kontrak EPC: prinsip Single Point of Responsibility atau satu pintu pertanggungjawaban. Pada model tradisional, pemilik proyek menunjuk konsultan perencana terpisah dari kontraktor pelaksana. Saat terjadi masalah, mereka kerap saling menyalahkan. Namun dalam kontrak EPC, satu konsorsium kontraktor memegang tanggung jawab mutlak dari gambar kerja hingga fasilitas siap beroperasi. Klien diibaratkan cukup menerima kunci dan memutarnya, konsep yang dikenal sebagai Turnkey Project. Klik tab perbandingan untuk meneliti perbedaan risikonya.",

    "3": "Pilar pertama adalah huruf E: Engineering atau Rekayasa Teknik. Tahap ini dimulai dari studi kelayakan, dilanjutkan dengan FEED atau Front End Engineering Design untuk mengunci parameter utama proyek. Setelah disetujui, ribuan dokumen DED atau Detail Engineering Design diproduksi: mulai dari diagram perpipaan dan instrumen atau P and ID, kalkulasi sipil struktur, hingga model 3D BIM untuk mencegah benturan pipa di lapangan. Kesalahan satu sentimeter di fase Engineering bisa berakibat pembongkaran fatal di lapangan. Eksplorasi tiga hotspot blueprint di layar Anda.",

    "4": "Pilar kedua adalah P: Procurement atau Pengadaan. Jangan samakan pengadaan EPC dengan belanja toko biasa. Di sini ada kategori khusus bernama Long Lead Items, yaitu peralatan raksasa buatan luar negeri yang butuh waktu manufaktur hingga satu tahun, seperti turbin generator atau boiler. Tim Procurement harus melakukan kualifikasi vendor ketat, mengawal Factory Acceptance Test di pabrik pembuat, dan menangani logistik kargo laut super berat ke pedalaman. Coba uji insting rantai pasok Anda pada mini game sortir prioritas di bawah!",

    "5": "Pilar ketiga adalah C: Construction atau Pelaksanaan Fisik di Lapangan. Di sinilah semua gambar desain dan material mewujud menjadi kenyataan. Pekerjaan dimulai dari fondasi dalam, ereksi struktur baja dengan derek raksasa, penyambungan pipa bertekanan, hingga penarikan kabel transmisi listrik. Di site proyek, ribuan pekerja dan ratusan subkontraktor bekerja serempak siang dan malam. Klik tahapan konstruksi dari tahap satu sampai tiga untuk melihat bagaimana metamorfosis proyek berlangsung.",

    "6": "Bagi PT PP dan seluruh kontraktor EPC berkelas dunia, tidak ada kompromi untuk keselamatan kerja. Prinsip kami adalah Zero Harm dan Zero Accident. Di lingkungan kerja bertegangan tinggi, ketinggian puluhan meter, dan bejana bertekanan, setiap aktivitas wajib memiliki Surat Izin Kerja Aman atau Permit to Work, serta analisis keselamatan kerja atau JSA. Gunakan APD lengkap yang tersertifikasi. Sekarang, mari uji ketajaman mata Anda dalam mengenali potensi bahaya di lapangan melalui latihan Spot the Hazard.",

    "7": "Ketika bangunan fisik selesai, proyek belum tuntas. Ada fase penentu bernama Commissioning atau Uji Fungsi. Tahap pertama adalah Cold Commissioning, yaitu uji tanpa beban seperti tes tekanan pipa atau hydrotest dan kalibrasi sensor. Selanjutnya Hot Commissioning dan Performance Guarantee Test, di mana pabrik dinyalakan dengan beban nyata untuk membuktikan kapasitas output sesuai janji kontrak. Puncaknya adalah COD atau Commercial Operation Date, hari bersejarah serah terima fasilitas ke pemilik proyek. Geser tuas kesiapan sistem untuk melihat tahapan commissioning.",

    "8": "Sekarang Anda duduk di kursi komando Project Director. Bayangkan kapal kargo yang membawa pipa khusus tertahan badai tropis di tengah samudera dan telat tiga minggu, sementara derek sewaan bertarif puluhan juta rupiah per hari sudah tiba di lokasi kerja. Sebagai insinyur yang tangguh, Anda dilarang panik atau mengambil jalan pintas ilegal. Bagaimana strategi integrasi EPC terbaik untuk menyelamatkan jadwal dan anggaran proyek? Tentukan keputusan Anda pada simulasi studi kasus ini.",

    "9": "Saatnya menguji pemahaman komprehensif Anda tentang dunia EPC. Anda akan menghadapi lima pertanyaan studi kasus yang menguji logika rekayasa, pengadaan, konstruksi, hingga mitigasi risiko. Nilai kelulusan modul ini adalah minimal delapan puluh persen atau empat soal benar. Perhatikan setiap ulasan penjelasan agar pemahaman Anda semakin kokoh. Selamat berjuang!",

    "10": "Selamat dan rasa hormat setinggi-tingginya! Anda telah berhasil menuntaskan seluruh ekspedisi sepuluh slide Mengenal Dunia EPC bersama saya, Rian. Kini Anda telah memahami DNA dari proyek-proyek mahakarya infrastruktur modern: presisi di meja Engineering, ketangguhan di rantai pasok Procurement, kedisiplinan di arena Construction, dan keselamatan kerja tanpa kompromi. Klik tombol di bawah untuk mencetak sertifikat resmi kelulusan Anda dan unduh ringkasan materi EPC Cheatsheet. Teruslah berkarya, insan pembangun kebanggaan negeri!"
}

PHONETIC_REPLACEMENTS = [
    (r"\bEngineering\b", "Enjiniring"),
    (r"\bProcurement\b", "Prokyurmen"),
    (r"\bConstruction\b", "Konstraksen"),
    (r"\bCommissioning\b", "Komisyening"),
    (r"\bSingle Point of Responsibility\b", "Singgel Poin of Risponsibiliti"),
    (r"\bTurnkey\b", "Ten-ki"),
    (r"\bFEED\b", "F-E-E-D, atau Front End Enjiniring Desain"),
    (r"\bDED\b", "D-E-D, atau Diteil Enjiniring Desain"),
    (r"\bLong Lead Items\b", "Long Lid Aitems"),
    (r"\bFactory Acceptance Test\b", "Fektori Akseptens Tes"),
    (r"\bZero Harm\b", "Ziro Harm"),
    (r"\bZero Accident\b", "Ziro Eksiden"),
    (r"\bPerformance Guarantee Test\b", "Performens Garanti Tes"),
    (r"\bCommercial Operation Date\b", "Komersial Opereisyen Deit"),
    (r"\bProject Director\b", "Projek Dairektor"),
    (r"\bSite Engineer\b", "Sait Enjinir"),
    (r"\bBlueprint\b", "Bluprint"),
    (r"\bCheatsheet\b", "Cit-syit"),
    (r"\bDrag and Drop\b", "Dreg en Drop"),
    (r"\bSpot the Hazard\b", "Spot de Hazard"),
    (r"\bPermit to Work\b", "Permit tu Werk"),
    (r"\bJob Safety Analysis\b", "Job Seifti Analisis"),
]

def apply_phonetic_respelling(text: str) -> str:
    res = text
    for pattern, repl in PHONETIC_REPLACEMENTS:
        res = re.sub(pattern, repl, res, flags=re.IGNORECASE)
    return res

async def generate_unit_audio(unit_id, text, output_path, voice, rate="-4%"):
    import edge_tts
    spoken_text = apply_phonetic_respelling(text)
    print(f"[*] Generating unit_{unit_id}.mp3 ({len(spoken_text)} chars) with voice={voice}...")
    communicate = edge_tts.Communicate(spoken_text, voice, rate=rate)
    await communicate.save(output_path)
    print(f" [OK] Saved: {output_path}")

async def main_async(args):
    try:
        import edge_tts
    except ImportError:
        print("[!] Error: 'edge-tts' package is not installed.")
        print("    Install via: pip install edge-tts")
        sys.exit(1)

    os.makedirs(args.output_dir, exist_ok=True)
    voice = VOICE_CHOICES.get(args.voice.lower(), args.voice)

    targets = NARRATIONS_MODUL_EPC_10.items()
    if args.unit is not None:
        unit_key = str(args.unit)
        if unit_key not in NARRATIONS_MODUL_EPC_10:
            print(f"[!] Error: Unit {args.unit} not found in narrations.")
            sys.exit(1)
        targets = [(unit_key, NARRATIONS_MODUL_EPC_10[unit_key])]

    for unit_id, text in targets:
        filename = f"unit_{unit_id}.mp3"
        out_path = os.path.join(args.output_dir, filename)
        if os.path.exists(out_path) and not args.force:
            print(f"[-] Skipping unit_{unit_id}.mp3 (already exists). Use --force to overwrite.")
            continue
        await generate_unit_audio(unit_id, text, out_path, voice, rate=args.rate)

def main():
    parser = argparse.ArgumentParser(description="Generate Edge-TTS MP3s for 10-Unit Modul EPC.")
    parser.add_argument("--voice", default="ardi", choices=list(VOICE_CHOICES.keys()) + list(VOICE_CHOICES.values()))
    parser.add_argument("--output-dir", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio"))
    parser.add_argument("--unit", type=int, default=None)
    parser.add_argument("--rate", default="-4%")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    asyncio.run(main_async(args))

if __name__ == "__main__":
    main()
