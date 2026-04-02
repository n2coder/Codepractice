# AI Coding Agent Instructions for Codepractice

## Project Overview
This is a Python sentiment analysis utility that classifies text as positive, negative, or neutral based on keyword matching. A simple, single-file project for learning/practice.

## Architecture & Components

### Core Component: `sentimentanalyzer.py`
- **Function**: `sentiment_analyser(text)` - Main entry point
- **Algorithm**: Keyword-based sentiment classification
  - Counts occurrences of predefined positive/negative keywords
  - Performs basic text normalization (lowercase, punctuation stripping)
  - Returns sentiment classification and word counts
- **Limitations**: Hardcoded keyword lists; no support for context, negation, or intensifiers

## Key Patterns & Conventions

### Text Processing Pattern
- Input normalization: `text.lower().split()`
- Punctuation handling: `word.strip('.,!?')` (only handles basic punctuation)
- Case-insensitive keyword matching

### Return Value Structure
Returns dictionary with keys: `'Positive count'`, `'negative count'`, `'sentiment'`
- Note: Inconsistent capitalization in keys (use camelCase for consistency in enhancements)

## Testing & Usage
- Run directly: `python sentimentanalyzer.py`
- Example usage provided at EOF demonstrating basic text input
- No automated tests currently; consider adding unit tests for regression prevention

## Future Enhancements
- Expand keyword lists for broader sentiment detection
- Add support for sentence-level analysis
- Implement negation handling ("not good" → negative)
- Add confidence scores for sentiment predictions
- Consider using NLTK or TextBlob for production use cases
