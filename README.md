# Modul Interaktif: Mengenal Dunia EPC (Engineering, Procurement, Construction)

> **Learning Companion & Host:** Rian, ST. (Site Engineer PT PP)  
> **Teknologi:** Standalone HTML5 SPA, Tailwind CSS, Web Audio API, Canvas Confetti, I2V Character Video Loops, ElevenLabs Neural Audio Narration.

---

## 📌 Ringkasan Proyek
Modul pembelajaran interaktif modern yang dirancang untuk memperkenalkan seluk-beluk industri **EPC (Engineering, Procurement, Construction)**. Dikembangkan dengan kurikulum 10 slide terstruktur, penguncian gate timer membaca, kuis anti-cheat kriptografi SHA-256, serta sertifikasi digital kelulusan otomatis.

---

## 🌟 Fitur Utama Modul:

1. **In-Slide Character Demonstration (Engineer Rian):**
   * Karakter Site Engineer berpenampilan resmi PT PP hadir secara nyata di dalam konten slide melalui klip animasi loop terintegrasi ($\le 10$ detik).
   * **Slide 0:** Host penyambut orientasi modul.
   * **Slide 3:** Demonstrator tablet digital memvalidasi *P&ID* dan *3D BIM Clash Detection*.
   * **Slide 5:** Patroli inspeksi ereksi rangka baja dan heavy lifting crane 500 ton.
   * **Slide 6:** Sikap K3 Zero Harm menegakkan *Stop Work Authority*.
   * **Slide 8:** Fasilitator command center mitigasi krisis kapal kargo tertahan badai tropis.
   * **Slide 10:** Selebrasi kelulusan & penandatangan digital e-Certificate.

2. **ElevenLabs Audio Narration Engine:**
   * Diperkuat dengan audio narasi berkualitas tinggi bersuara manusia alami dari **ElevenLabs Multilingual v2** (`Unit 0` s/d `Unit 9`).
   * Kontrol audio interaktif: Tombol nyala/mati narasi, putar ulang, dan percepatan tempo (1.0x / 1.25x / 1.5x).

3. **10 Unit / Slide Interaktivitas Pedagogis:**
   * **Slide 0: Welcome & Briefing** — Pengantar misi dan ikhtisar kompetensi.
   * **Slide 1: Mengapa Harus EPC?** — 3D Flip Card membedah tantangan finansial, waktu, dan teknologi.
   * **Slide 2: EPC vs Tradisional** — Tabbed comparison matrix menelaah Single Point of Responsibility & Turnkey.
   * **Slide 3: Pilar Engineering (E)** — Blueprint digital twin explorer dengan 3 hotspot teknis.
   * **Slide 4: Pilar Procurement (P)** — Mini game sortir prioritas rantai pasok Long Lead Items (LLI).
   * **Slide 5: Pilar Construction (C)** — Stepper alur kerja ereksi lapangan (Civil, Erection, Loop Test).
   * **Slide 6: Budaya K3 Zero Harm** — Spot The Hazard interaktif untuk mendeteksi bahaya kritis.
   * **Slide 7: Commissioning & COD** — Slider interaktif 4 fase pengujian (Cold Comm s/d COD).
   * **Slide 8: Simulasi Mitigasi Risiko** — Studi kasus darurat keputusan Project Director.
   * **Slide 9: Evaluasi Akhir (Post-Test)** — 5 soal skenario dengan verifikasi hash kriptografi SHA-256 (Passing Grade $\ge 80\%$).
   * **Slide 10: Kelulusan & Sertifikat** — E-Certificate resmi kelulusan siap cetak A4 Landscape & unduh Cheatsheet.

---

## 📂 Struktur Direktori:
```text
dasar-epc/
├── assets/
│   ├── rian_engineer.png         # Karakter ilustrasi acuan PT PP
│   ├── rian_wave_loop.mp4        # Video loop sapaan intro
│   ├── rian_tablet_loop.mp4      # Video loop demonstrasi tablet teknis
│   ├── rian_walk_loop.mp4        # Video loop inspeksi lapangan
│   └── rian_thumbs_loop.mp4      # Video loop selebrasi jempol K3
├── audio/
│   ├── unit_0.mp3 s/d unit_10.mp3 # Audio narasi ElevenLabs & Neural
│   └── ...
├── ElevenLabs/                   # Master file download audio ElevenLabs
├── index.html                    # Web app modul interaktif utama
├── generate_audio.py             # Script Edge-TTS & Phonetic Respelling
├── rian_i2v_prompts.md           # Panduan prompt I2V Kling/Runway/Hailuo
└── README.md                     # Dokumentasi proyek
```

---

## 🚀 Cara Menjalankan:
Buka file `index.html` menggunakan browser Chromium modern apa saja (Google Chrome, Microsoft Edge, Brave) tanpa perlu instalasi web server.
