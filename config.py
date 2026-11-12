"""VELOCITY LONGFORM - 16:9 chapter lesson, brand and motion constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1920
VIDEO_HEIGHT = 1080
FPS = 30

TARGET_CHAPTERS = 8
PHRASES_PER_CHAPTER = 7
TARGET_PHRASES = TARGET_CHAPTERS * PHRASES_PER_CHAPTER

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY FRENCH"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "FRENCH"
HANDLE = "@velocityfrench"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {'code': 'fr',
 'name': 'French',
 'native_name': 'Français',
 'history_key': 'french',
 'english_voice': 'en-US-AvaNeural',
 'english_fallback_voice': 'en-US-GuyNeural',
 'native_voice': 'fr-FR-HenriNeural',
 'native_fallback_voice': 'fr-FR-DeniseNeural',
 'native_engine': 'edge',
 'native_lang_code': 'fr',
 'english_rate': '-4%',
 'native_rate': '-10%',
 'english_pitch': '+0Hz',
 'native_pitch': '+0Hz',
 'native_label': 'FRANÇAIS',
 'translit_label': 'SAY IT LIKE',
 'flag': 'fr',
 'greeting': 'Bonjour !',
 'encouragement': 'Excellent !',
 'rtl': False,
 'char_tiles': False,
 'script_font': '',
 'glyphs': 'ABCDEFGHIJKLMNOPQRSTUVWXYZÀÂÇÉÈÊËÎÏÔÙÛÜŒàâçéèêëîïôùûüœ'}
# ==== LANGUAGE PACK END ====

# ==== CATEGORIES START ====
CATEGORIES = {'Motivation': 'Motivation',
 'Love': 'Amour',
 'Success': 'Succès',
 'Wisdom': 'Sagesse',
 'Happiness': 'Bonheur',
 'Self Improvement': 'Amélioration de soi',
 'Gratitude': 'Gratitude',
 'Friendship': 'Amitié',
 'Hope': 'Espoir',
 'Creativity': 'Créativité',
 'Inner Peace': 'Paix intérieure',
 'Confidence': 'Confiance',
 'Perseverance': 'Persévérance',
 'Inspiration': 'Inspiration',
 'Positive Life': 'Vie positive',
 'Courage': 'Courage',
 'Kindness': 'Gentillesse',
 'Patience': 'Patience',
 'Forgiveness': 'Pardon',
 'Strength': 'Force',
 'Joy': 'Joie',
 'Balance': 'Équilibre',
 'Growth': 'Croissance',
 'Purpose': 'Objectif',
 'Mindfulness': 'Pleine conscience',
 'Travel & Airport': 'Voyages et aéroport',
 'Ordering Food & Dining': 'Commander à manger et restaurants',
 'Shopping & Prices': 'Shopping et prix',
 'Asking for Directions': 'Demander son chemin',
 'Hotel & Accommodation': 'Hôtel et hébergement',
 'Daily Routine': 'Routine quotidienne',
 'Meeting People & Greetings': 'Rencontrer des gens et salutations',
 'Emergency & Health': 'Urgence et santé',
 'Public Transportation': 'Transports en commun',
 'Work & Office': 'Travail et bureau',
 'Weather & Small Talk': 'Météo et petites conversations',
 'Coffee Shop & Bakery': 'Café et boulangerie',
 'Family & Home': 'Famille et maison',
 'Hobbies & Free Time': 'Loisirs et temps libre',
 'Dating & Romance': 'Rencontres et romance',
 'Phone Calls & Messages': 'Appels téléphoniques et messages',
 'Banking & Money': 'Banque et argent',
 'Doctor & Pharmacy': 'Médecin et pharmacie',
 'Sports & Fitness': 'Sports et forme physique',
 'Celebrations & Parties': 'Célébrations et fêtes',
 'Feelings & Emotions': 'Sentiments et émotions',
 'Agreeing & Disagreeing': "Être d'accord et en désaccord",
 'Making Plans': 'Faire des projets',
 'Common Native Slang': 'Argot courant',
 'Cultural Traditions': 'Traditions culturelles'}
# ==== CATEGORIES END ====

CATEGORY_NAMES = list(CATEGORIES.keys())

AI_MODEL = os.getenv("AI_MODEL", "openai/gpt-5.4-nano")
AI_FALLBACK_MODEL = os.getenv("AI_FALLBACK_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 7.2
CHAPTER_INTRO_DURATION = 4.4
OUTRO_DURATION = 13.0

EN_CARD_IN = 0.70
GAP_EN_NATIVE = 0.60
NATIVE_CARD_LEAD = 0.40
GAP_BEFORE_REPEAT = 1.00
TAIL_HOLD = 1.30

# ---------------------------------------------------------------- palette

INK = "#30303A"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#7C5CFF"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

# ==== HASHTAGS START ====
HASHTAGS = ['#learnfrench',
 '#frenchlessons',
 '#frenchforbeginners',
 '#languagelearning',
 '#frenchvocabulary',
 '#velocityfrench',
 '#dailyfrench',
 '#french',
 '#learnlanguages',
 '#speakfrench']
# ==== HASHTAGS END ====
