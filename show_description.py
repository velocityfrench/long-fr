import sys, os
sys.path.insert(0, ".")
import youtube_longform_automation as y
from pathlib import Path

phrases = [
    {"english": "Don't compare, your journey.", "french": "Ne compare pas, ton voyage.", "phonetic": "nuh kom-par pah, toh vo-yahj"},
    {"english": "Fail fast, learn faster.", "french": "Échoue vite, apprends plus vite.", "phonetic": "ay-shoo veet, ah-prahn ploo veet"},
    {"english": "Make mistakes, that matter.", "french": "Fais des erreurs, qui comptent.", "phonetic": "fay dayz ayr-ur, kee cohnt"},
    {"english": "Your ideas, are valuable.", "french": "Tes idées, sont précieuses.", "phonetic": "tayz ee-day, sohn pray-syuhz"},
    {"english": "Be brave, be strong.", "french": "Sois courageux, sois fort.", "phonetic": "swah koh-rah-juh, swah for"},
    {"english": "Shine bright, like a star.", "french": "Brille fort, comme une étoile.", "phonetic": "bree for, kohm oon eh-twahl"},
    {"english": "You are enough, right now.", "french": "Tu es suffisant, maintenant.", "phonetic": "tyoo eh syoo-fee-zahn, mahn-tah-nahn"},
    {"english": "Stand tall, don't waver.", "french": "Tiens-toi droit, ne vacille pas.", "phonetic": "tyahn-twah drwah, nyuh vah-see pah"},
    {"english": "Believe in the process.", "french": "Crois au processus.", "phonetic": "kwah oh pro-seh-soos"},
    {"english": "You can conquer anything.", "french": "Tu peux tout conquérir.", "phonetic": "tyoo peuh too kohn-keh-reer"},
]

seo = y.generate_title_description("Confidence", "Confiance", phrases, 1.0, "output/SAMPLE")

Path("output/SAMPLE").mkdir(parents=True, exist_ok=True)
with open("output/SAMPLE/DESCRIPTION.txt", "w", encoding="utf-8") as f:
    f.write(seo["description"])

print(f"Title: {seo['selected_title']}")
print(f"Description saved: output/SAMPLE/DESCRIPTION.txt")
os.startfile("output\\SAMPLE\\DESCRIPTION.txt")
