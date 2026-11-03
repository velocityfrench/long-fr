import sys, os, subprocess, json
os.environ['AI_MODEL'] = 'openai/gpt-5.4-nano'
sys.path.insert(0, ".")
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import random, asyncio

video_dir = Path("output/SAMPLE")
video_dir.mkdir(parents=True, exist_ok=True)

# Step 1: Show the phrases being used
print("=" * 60)
print("STEP 1: GENERATING PHRASES")
print("=" * 60)
phrases = [
    {"english": "Don't compare, your journey.", "french": "Ne compare pas, ton voyage.", "phonetic": "nuh kom-par pah, toh vo-yahj"},
    {"english": "Fail fast, learn faster.", "french": "Échoue vite, apprends plus vite.", "phonetic": "ay-shoo veet, ah-prahn ploo veet"},
    {"english": "Make mistakes, that matter.", "french": "Fais des erreurs, qui comptent.", "phonetic": "fay dayz ayr-ur, kee cohnt"},
    {"english": "Your ideas, are valuable.", "french": "Tes idées, sont précieuses.", "phonetic": "tayz ee-day, sohn pray-syuhz"},
    {"english": "Be brave, be strong.", "french": "Sois courageux, sois fort.", "phonetic": "swah koh-rah-juh, swah for"},
    {"english": "Shine bright, like a star.", "french": "Brille fort, comme une étoile.", "phonetic": "bree for, kohm oon eh-twahl"},
    {"english": "You are enough, right now.", "french": "Tu es suffisant, maintenant.", "phonetic": "tyoo eh syoo-fee-zahn, mahn-tah-nahn"},
]
for i, p in enumerate(phrases, 1):
    print(f"  {i}. {p['english']}")
    print(f"     FR: {p['french']}")
    print(f"     PH: {p['phonetic']}")

# Step 2: Show the description being generated
print("\n" + "=" * 60)
print("STEP 2: GENERATING DESCRIPTION")
print("=" * 60)

# Import the description function from the local script
import youtube_longform_automation as y
seo = y.generate_title_description("Confidence", "Confiance", phrases, 1.2, str(video_dir))

print(f"\nTITLE: {seo['selected_title']}")
print(f"TAGS: {', '.join(seo['tags'][:5])}...")
print(f"\nDESCRIPTION ({len(seo['description'])} chars):")
print("-" * 60)
print(seo['description'])
print("-" * 60)

# Step 3: Generate frame images
print("\n" + "=" * 60)
print("STEP 3: GENERATING FRAMES")
print("=" * 60)

# Use the local generate_complete_image function
for i, phrase in enumerate(phrases):
    turn = {"english": phrase["english"], "french": phrase["french"], "phonetic": phrase["phonetic"]}
    img_path = str(video_dir / f"frame_{i:02d}.png")
    y.generate_complete_image(turn, "Confidence", img_path)
    print(f"  Frame {i+1}: {img_path}")

# Step 4: Show what would be uploaded
print("\n" + "=" * 60)
print("STEP 4: WHAT GETS UPLOADED TO YOUTUBE")
print("=" * 60)
print(f"  Title: {seo['selected_title']}")
print(f"  Description: {len(seo['description'])} chars")
print(f"  Tags: {len(seo['tags'])} tags")
print(f"  Phrases: {len(phrases)}")
print(f"  Duration: ~{len(phrases) * 6}s = ~{len(phrases) * 6 / 60:.1f} min")

# Show the metadata file
meta_path = video_dir / "video_metadata.json"
if meta_path.exists():
    print(f"\n  Metadata saved: {meta_path}")

print("\n" + "=" * 60)
print("DONE! Check output/SAMPLE/ for frames + description")
print("=" * 60)
