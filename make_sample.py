import sys, os, json, asyncio
sys.path.insert(0, ".")

import podcast_generator as pg
from pathlib import Path

video_dir = Path("output/SAMPLE")
video_dir.mkdir(parents=True, exist_ok=True)

# Generate a few phrases
phrases = [
    {"english": "Don't compare, your journey.", "french": "Ne compare pas, ton voyage.", "phonetic": "nuh kom-par pah, toh vo-yahj"},
    {"english": "Fail fast, learn faster.", "french": "Échoue vite, apprends plus vite.", "phonetic": "ay-shoo veet, ah-prahn ploo veet"},
    {"english": "Make mistakes, that matter.", "french": "Fais des erreurs, qui comptent.", "phonetic": "fay dayz ayr-ur, kee cohnt"},
    {"english": "Your ideas, are valuable.", "french": "Tes idées, sont précieuses.", "phonetic": "tayz ee-day, sohn pray-syuhz"},
    {"english": "Be brave, be strong.", "french": "Sois courageux, sois fort.", "phonetic": "swah koh-rah-juh, swah for"},
]

# Generate description
seo = pg.generate_title_description("Confidence", "Confiance", phrases, 0.5, str(video_dir))

# Save the description for viewing
with open("output/SAMPLE/description.txt", "w", encoding="utf-8") as f:
    f.write(seo["description"])

# Generate frames for each phrase
for i, phrase in enumerate(phrases):
    turn = {
        "english": phrase["english"],
        "french": phrase["french"],
        "phonetic": phrase["phonetic"],
        "speaker": "Host1"
    }
    img_path = str(video_dir / f"f_{i:04d}.png")
    pg.create_frame(turn, img_path, i)
    print(f"Frame {i}: {phrase['english']}")

print(f"\nDescription saved to output/SAMPLE/description.txt")
print(f"Title: {seo['selected_title']}")
