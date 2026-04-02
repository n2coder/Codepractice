def sentiment_analyser(text):
    # Define our keyword lists
    positive_keywords = ['good', 'great', 'happy', 'wow']
    negative_keywords = ['bad', 'ugly', 'wrong', 'pathetic']
    
    # Clean the input text and split into words
    words = text.lower().split()
    
    pos_count = 0
    neg_count = 0
    
    # Count occurrences
    for word in words:
        # Strip punctuation to ensure a clean match
        clean_word = word.strip('.,!?')
        if clean_word in positive_keywords:
            pos_count += 1
        elif clean_word in negative_keywords:
            neg_count += 1
            
    # Determine overall sentiment
    if pos_count > neg_count:
        sentiment = 'positive'
    elif neg_count > pos_count:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
        
    # Return the result as a dictionary
    return {
        'Positive count': str(pos_count),
        'negative count': str(neg_count),
        'sentiment': sentiment
    }

# Get user input and analyze sentiment
if __name__ == "__main__":
    input_text = input("Enter text to analyze: ")
    result = sentiment_analyser(input_text)
    print(result)