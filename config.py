# This file contains configuration variables for the Excel translation script.

# Google AI Studio API Key
GEMINI_API_KEY = "API_KEY"
GEMINI_MODEL = "gemini-3.1-flash-lite-preview"

# Language settings
TARGET_LANGUAGE = "English"
SOURCE_LANGUAGE = "Japanese"

# The local folder path containing the Excel files (.xlsx) you want to translate
SOURCE_FOLDER_PATH = "IN"

# The local folder path where you want to save the translated Excel files
OUTPUT_FOLDER_PATH = "OUT"

# Temperature (0.0 to 1.0, Gemini 3 series strongly prefers 1.0)
TEMPERATURE = 1.0

# Headers for the source and target columns
SOURCE_HEADER = "text"
TARGET_HEADER = "translated text"

# Header for the speaker identification column
SPEAKER_HEADER = "translated name"

# Header for the message type column (assuming column A)
TYPEMESSAGE_HEADER = "type"
