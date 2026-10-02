# Production I2V Character Animation Prompts: Engineer Rian (PT PP)
*Specialized for Generative Video Engines: Kling 1.5/2.0, Runway Gen-3/4, Hailuo MiniMax, Luma Dream Machine, Google Flow/Veo*

Aset input yang digunakan adalah gambar karakter: `assets/rian_engineer.png` (Site Engineer berhelm putih PT PP, rompi K3 kuning-biru, wearpack abu-abu, sepatu safety).

---

### 🎬 Scene 1: Seamless Walking Cycle in Place (Loop Utama Transisi & Site Progress)
* **Kebutuhan Modul:** Digunakan sebagai avatar pendamping saat pembelajar membaca dan melangkah antar modul (Slide 0, 5, dan 7).
* **Pipeline:** Chroma Key / Transparent Matte Overlay (Solid Flat Teal `#008080` atau Solid Flat Pure White `#FFFFFF`).
* **Risk Assessment:** Low-Medium (Kaki melangkah di tempat *treadmill walk*, tangan mengayun terkoordinasi).

#### 📋 Prompt Siap Salin (Copy-Paste Prompt):
```text
Against a completely flat solid clean light gray-white background (#F4F6F9) with zero cast shadows and zero gradients. Preserving the exact flat 2D vector chibi illustration style, bold clean outlines, and cel-shaded colors of the male Indonesian site engineer character. Centered full-body profile framing. The character performs a rhythmic, continuous walking cycle in place (treadmill motion) from left to right orientation. Arms swing gently and naturally in opposition to leg strides, hands kept relaxed. The safety helmet strap and clothing creases show subtle realistic movement. Gentle rhythmic eye blinks every 2 seconds while maintaining a pleasant, confident smile. Seamless loop pacing where stride phase at second 5 perfectly matches second 0. Locked static tripod camera. No 3D volumetric drift, no melting shoes, no extra fingers, no limb warping, no background jitter.
```

#### 🛡️ Negative Prompt:
```text
3D realistic rendering, CGI photorealism, glossy textures, gradients on background, distorted safety helmet, warped boots, floating detached limbs, extra legs, extra arms, jittery frames, morphing logo, disappearing straps.
```

* **Parameter Engine:** Motion Slider: `3.5` | Loop: `ON` | Duration: `5s` | Camera: `Static Lock`

---

### 🎬 Scene 2: Welcoming Wave & Friendly Greeting (Slide 0 Intro & Unit Openers)
* **Kebutuhan Modul:** Menyapa peserta saat baru pertama membuka modul atau masuk unit baru.
* **Pipeline:** Asset Isolation (Solid Backdrop).
* **Risk Assessment:** Low (Lambaian tangan di samping badan, nafas dada ritmis).

#### 📋 Prompt Siap Salin (Copy-Paste Prompt):
```text
Against a flat solid studio white background (#FFFFFF) with zero gradients. Maintaining the original 2D clean vector line art style and exact character design of the PT PP site engineer. Locked static eye-level camera framing from knees up. From 0 to 1 second, the character stands in a confident posture with a friendly smile. From 1 to 3 seconds, he raises his right hand to chest height and gives a warm, polite two-stroke wave to the viewer. From 3.5 to 5 seconds, he smoothly lowers his right hand back to his side, returning exactly to the starting stance. Subtle rhythmic chest breathing and a natural gentle eye blink at second 2. Perfectly seamless loop reset. No 3D skin shading, no mutated fingers, no melting helmet, no background shadows.
```

#### 🛡️ Negative Prompt:
```text
realistic skin textures, 3D clay render, changing uniform colors, distorted fingers, hand crossing face, blurry frames, morphing vest pockets.
```

* **Parameter Engine:** Motion Slider: `3.0` | Loop: `ON` | Duration: `5s` | Camera: `Static Lock`

---

### 🎬 Scene 3: Inspecting Digital Tablet & Explaining (Slide 3 Engineering & Slide 4 Procurement)
* **Kebutuhan Modul:** Menjelaskan blueprint teknis dan data pengadaan.
* **Risk Assessment:** Medium (Karakter memegang tablet digital, jari tapping layar, kepala mengangguk paham).

#### 📋 Prompt Siap Salin (Copy-Paste Prompt):
```text
Preserving the authentic 2D vector chibi art style with solid flat colors and crisp outlines. Clean neutral solid studio background. Medium shot framing the site engineer character. The character holds an industrial rugged digital tablet in his left hand. With his right index finger, he taps and swipes the tablet screen smoothly between seconds 1 and 3, then nods his head twice in professional approval while looking up towards the viewer with a friendly confident expression. Subtle micro-gestures of chest breathing and fabric folding. Smoothly transitions back to initial resting pose by second 5. Locked static camera. No morphing tablet, no bending fingers, no realistic face alteration.
```

* **Parameter Engine:** Motion Slider: `3.2` | Loop: `ON` | Duration: `5s`

---

### 🎬 Scene 4: Celebratory Thumbs Up & Safety Approved (Slide 6 K3 & Slide 10 Kelulusan)
* **Kebutuhan Modul:** Umpan balik jawaban benar, lolos tes K3, dan penyelesaian modul.
* **Risk Assessment:** Low (Gestur acungan jempol mantap dengan senyum lebar).

#### 📋 Prompt Siap Salin (Copy-Paste Prompt):
```text
Against a flat solid clean studio background. Preserving the exact 2D vector illustration style and character proportion of the PP construction engineer. Static eye-level camera framing character from waist up. The character smiles brightly, gives a firm affirmative nod, and raises his right hand to deliver an enthusiastic thumbs-up gesture directly to the viewer. He holds the thumbs-up steadily from second 1.5 to 3.5, then comfortably lowers his arm back down to rest by second 5. Natural eye blink and micro chest breathing throughout. Perfect seamless loop cycle. No extra thumbs, no hand melting, no style drift to 3D.
```

* **Parameter Engine:** Motion Slider: `3.0` | Loop: `ON` | Duration: `5s`
