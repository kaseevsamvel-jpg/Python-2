def analyze_poem(filename):
    vowels = "аеєиіїоуюя"  # Голосні українського алфавіту
    vowel_words_count = 0
    consonant_words_count = 0
    
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        print("--- Вірш ---")
        print(text)
        print("--------------")
        
        words = text.split()
        for word in words:
            clean_word = word.strip(".,!?-:;").lower()
            if clean_word and clean_word[0] in vowels:
                vowel_words_count += 1
            elif clean_word:
                consonant_words_count += 1
        
    return vowel_words_count, consonant_words_count

# Основна частина
file_path = 'poem.txt'
vowels_count, consonants_count = analyze_poem(file_path)

if vowels_count > 0 or consonants_count > 0:
    print(f"Слів, що починаються на голосну: {vowels_count}")
    print(f"Слів, що починаються на приголосну: {consonants_count}")

    if vowels_count > consonants_count:
        print("Більше слів, що починаються на голосну.")
    elif consonants_count > vowels_count:
        print("Більше слів, що починаються на приголосну.")
    else:
        print("Кількість слів однакова.")