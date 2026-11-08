import wave, struct, math, os, sys
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
SR = 22050; DUR = 30
def render(name, fn):
    w = wave.open(os.path.join(out, name), "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(b"".join(struct.pack("<h", int(max(-1, min(1, fn(i / SR))) * 30000)) for i in range(SR * DUR))); w.close()
def prl(t):
    c = t % 2.0
    on = c < 0.4 or 0.6 <= c < 1.0
    return 0.8 * math.sin(2 * math.pi * 425 * t) * (0.5 + 0.5 * math.sin(2 * math.pi * 25 * t)) if on else 0
def bud(t):
    c = t % 1.6
    return 0.7 * (1 if math.sin(2 * math.pi * 900 * t) > 0 else -1) if any(k * 0.22 <= c < k * 0.22 + 0.12 for k in range(4)) else 0
def zeg(t):
    c = t % 1.0
    return 0.6 * math.sin(2 * math.pi * 2300 * t) if (c < 0.06 or 0.12 <= c < 0.18) else 0
render("al_prl.wav", prl); render("al_bud.wav", bud); render("al_zeg.wav", zeg)
