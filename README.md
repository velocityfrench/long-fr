# ðŸ‡«ðŸ‡· Velocity French - Automated Facebook Reels Bot

**Automated French learning content generator for social media**

Generates and posts 4x daily to Facebook, Instagram, and other platforms with:
- âœ… AI-generated French phrases with English translations
- âœ… Professional text-to-speech (Edge TTS)
- âœ… Beautiful gradient backgrounds with text overlays
- âœ… Perfect audio-video synchronization
- âœ… Velocity French branding
- âœ… **NEVER repeats phrases** (permanent history tracking)

---

## ðŸ“… Daily Schedule (American EST/EDT)

| Post | Time (EST) | Time (UTC) | Theme |
|------|------------|------------|-------|
| 1 | 9:00 AM | 14:00 UTC | Morning motivation |
| 2 | 12:00 PM | 17:00 UTC | Lunch break |
| 3 | 3:00 PM | 20:00 UTC | Afternoon pick-me-up |
| 4 | 7:00 PM | 00:00 UTC | Evening inspiration |

---

## ðŸŽ¬ Available Categories (25 Total)

1. Motivation (åŠ¨åŠ›)
2. Love (çˆ±æƒ…)
3. Success (æˆåŠŸ)
4. Wisdom (æ™ºæ…§)
5. Happiness (å¹¸ç¦)
6. Self Improvement (è‡ªæˆ‘æå‡)
7. Gratitude (æ„Ÿæ©)
8. Friendship (å‹è°Š)
9. Hope (å¸Œæœ›)
10. Creativity (åˆ›é€ åŠ›)
11. Inner Peace (å†…å¿ƒå¹³é™)
12. Confidence (è‡ªä¿¡)
13. Perseverance (æ¯…åŠ›)
14. Inspiration (çµæ„Ÿ)
15. Positive Life (ç§¯æžç”Ÿæ´»)
16. Courage (å‹‡æ°”)
17. Kindness (å–„è‰¯)
18. Patience (è€å¿ƒ)
19. Forgiveness (å®½æ•)
20. Strength (åŠ›é‡)
21. Joy (å¿«ä¹)
22. Balance (å¹³è¡¡)
23. Growth (æˆé•¿)
24. Purpose (ç›®æ ‡)
25. Mindfulness (æ­£å¿µ)

---

## ðŸš€ GitHub Actions Setup

### Step 1: Add Secrets to GitHub Repository

Go to your GitHub repository â†’ Settings â†’ Secrets and variables â†’ Actions

**Required Secrets:**

```bash
# Pollinations AI (for content generation)
POLLINATIONS_API_KEY=sk_your_api_key_here

# Facebook (for Reels upload)
FACEBOOK_ACCESS_TOKEN=your_token
FACEBOOK_PAGE_ID=your_page_id

# Instagram (for Reels upload)
INSTAGRAM_ACCESS_TOKEN=your_token
INSTAGRAM_ACCOUNT_ID=your_account_id

# Optional: Other platforms
VK_ACCESS_TOKEN=your_token
VK_GROUP_ID=your_group_id
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHANNEL_ID=your_channel_id
TWITTER_API_KEY=your_key
TWITTER_API_SECRET=your_secret
TWITTER_ACCESS_TOKEN=your_token
TWITTER_ACCESS_SECRET=your_secret
```

### Step 2: Enable GitHub Actions

1. Go to Actions tab in your GitHub repository
2. Enable workflows if disabled
3. The workflow will automatically run 4x daily

### Step 3: Manual Testing

You can manually trigger the workflow:
1. Go to Actions â†’ "Velocity French - Daily 4x Upload"
2. Click "Run workflow"
3. Select branch (main/master)
4. Click "Run workflow"

---

## ðŸ’» Local Testing

### Prerequisites

```bash
# Install Python 3.11+
# Install FFmpeg
# Install dependencies
pip install -r requirements.txt
```

### Generate Single Reel

```bash
python facebook_reels_automation.py
```

### Generate Daily Content (4 reels)

```bash
python -c "from facebook_reels_automation import generate_daily_content; generate_daily_content(times_per_day=4)"
```

### Upload to Social Media

```bash
cd upload
python ../upload_all_platforms.py
```

---

## ðŸ“ Project Structure

```
velocity French/
â”œâ”€â”€ .env                              # API keys and credentials
â”œâ”€â”€ .github/
â”‚   â””â”€â”€ workflows/
â”‚       â””â”€â”€ daily_4x_upload.yml      # GitHub Actions workflow
â”œâ”€â”€ facebook_reels_automation.py     # Main generation script
â”œâ”€â”€ upload_all_platforms.py          # Unified upload script
â”œâ”€â”€ upload/
â”‚   â”œâ”€â”€ upload_facebook.py
â”‚   â”œâ”€â”€ upload_instagram.py
â”‚   â”œâ”€â”€ upload_vk.py
â”‚   â””â”€â”€ ...
â”œâ”€â”€ output/
â”‚   â”œâ”€â”€ video/                       # Generated reels
â”‚   â”œâ”€â”€ history/                     # Phrase history (NEVER delete!)
â”‚   â””â”€â”€ daily_summary_*.json        # Daily generation logs
â””â”€â”€ requirements.txt
```

---

## ðŸ”§ Configuration

### Timezone Adjustment

The workflow uses EST/EDT (UTC-5). To change timezone:

1. Edit `.github/workflows/daily_4x_upload.yml`
2. Modify cron schedules:
   ```yaml
   # For PST (UTC-8):
   - cron: '0 17 * * *'  # 9 AM PST
   - cron: '0 20 * * *'  # 12 PM PST
   - cron: '0 23 * * *'  # 3 PM PST
   - cron: '0 3 * * *'   # 7 PM PST
   ```

### Posting Frequency

To change from 4x to 3x daily:

1. Edit `.github/workflows/daily_4x_upload.yml`
2. Remove one cron schedule
3. Update `generate_daily_content(times_per_day=3)` in script

---

## ðŸŽ¬ Video Specifications

- **Resolution:** 1080x1920 (9:16 vertical)
- **Format:** MP4 (H.264 + AAC)
- **Duration:** ~30-50 seconds (5 phrases)
- **Frame Rate:** 30 FPS
- **Audio:** Edge TTS (GuyNeural EN, XiaoxiaoNeural CN)

---

## ðŸ“Š Phrase History

All generated phrases are stored in:
```
output/history/all_generated_phrases.json
```

**This file is PERMANENT and should NEVER be deleted.**

It ensures:
- âœ… No phrase is ever repeated
- âœ… Fresh content every day
- âœ… Tracking of all generated content

---

## ðŸ› Troubleshooting

### Video Generation Fails

```bash
# Check FFmpeg installation
ffmpeg -version

# Reinstall if needed
sudo apt-get install ffmpeg  # Linux
brew install ffmpeg          # macOS
```

### Audio Upload Fails

```bash
# Check .env file
cat .env | grep FACEBOOK
cat .env | grep INSTAGRAM

# Verify tokens are valid
# Regenerate if expired
```

### GitHub Actions Fails

1. Check Actions tab for error logs
2. Verify all secrets are set correctly
3. Check artifact uploads for generated files
4. Review logs for specific error messages

---

## ðŸ“ˆ Performance Metrics

- **Generation Time:** ~2-3 minutes per reel
- **Upload Time:** ~1-2 minutes per platform
- **Total Workflow:** ~5-10 minutes per post
- **Daily Capacity:** 4 posts Ã— 5 phrases = 20 phrases/day
- **Category Rotation:** 25 categories = 6+ days before repeat

---

## ðŸŽ¯ Key Features

### âœ… Perfect Audio-Video Sync
- Each image displays for exact audio duration
- English + 500ms pause + French timing preserved
- No early transitions or cut-offs

### âœ… Natural Speech
- Phrases include commas for breathing room
- Example: "Dream big, start small"
- TTS sounds natural, not robotic

### âœ… Professional Design
- Multi-stop gradient backgrounds
- Distinct colors: Navy (EN) / Maroon (CN) / Gray (Phonetic)
- Velocity French branding on every frame

### âœ… Never Repeats
- Permanent phrase history tracking
- AI generates fresh content every time
- Checks all phrases before generation

---

## ðŸ“ž Support

For issues or questions:
1. Check GitHub Actions logs
2. Review error messages in output
3. Verify all API credentials
4. Check phrase history for duplicates

---

## ðŸ“„ License

This project is for educational purposes. Respect platform API terms of service.

---

**Made with â¤ï¸ for French learners worldwide**

ðŸ‡«ðŸ‡· Learn French with Velocity French! ðŸ‡«ðŸ‡·

