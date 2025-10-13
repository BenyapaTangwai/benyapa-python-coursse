"""

Build a Text Analysis Tool that performs the following operations on user input text:
Core Features:

1. Character Analysis:
    - Count total characters (with and without spaces)
    - Count vowels and consonants separately
    - Find most frequent character

2. Word Analysis:
    - Count total words
    - Find longest and shortest words
    - Count words starting with vowels vs consonants

3. String Transformations:
    - Convert to title case, upper case, lower case
    - Create acronym from first letter of each word
    - Reverse the entire string and each word individually
    
Example Result

Enter text: The Quick Brown Fox Jumps Over The Lazy Dog

=== TEXT ANALYSIS REPORT ===
Character Analysis:
- Total characters: 43 (with spaces), 35 (without spaces)
- Vowels: 12 (e, u, i, o, o, u, o, e, e, a, o)
- Consonants: 23
- Most frequent: 'o' (appears 4 times)

Word Analysis:
- Total words: 9
- Longest word: "Quick" (5 letters)
- Shortest word: "The" (3 letters)
- Words starting with vowels: 1 ("Over")
- Words starting with consonants: 8

Transformations:
- Title Case: The Quick Brown Fox Jumps Over The Lazy Dog
- Upper Case: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
- Lower Case: the quick brown fox jumps over the lazy dog
- Acronym: TQBFJOTLD
- Reversed Text: goD yzaL ehT revO spmuJ xoF nworB kciuQ ehT
- Words Reversed: ehT kciuQ nworB xoF spmuJ revO ehT yzaL goD

USE: len(), split(), count(), upper(), lower(), title(), slicing operations

"""
#text = input("Enter text: ")
text = "The Quick Brown Fox Jumps Over The Lazy Dog"

print("\n=== TEXT ANALYSIS REPORT ===")
print("Character Analysis:")
print(f"- Total characters: {len(text)} (with spaces), {len(text) - text.count(' ')} (without spaces)")
aeiou = ""
for char in text:
    if char in ['a','e','i','o','u','A','E','I','O','U']:
        aeiou += char + ","
count_aeiou = text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u') + text.count('A') + text.count('E') + text.count('I') + text.count('O') + text.count('U')
print(f"- Vowels: {count_aeiou} ({aeiou.lower()[0:-1]})")
print(f"- Consonants: {len(text) - text.count(' ') - count_aeiou}")

print("\nWord Analysis:")
print(f"- Total words: {len(text.split())}")
#ทำเพิ่มต่อจากอาจารย์
text_list = text.split()#ทำให้เป็น list จะได้เช็กได้ เช็กง่ายด้วย
max_text = text_list[0]#ให้มันใช้คำแรกไปก่อน เพื่อเอาใช้เปรียบเทียบทีหลัง
min_text = text_list[0]#อันนี้ก้เช่นกัน
for word in text_list:
    if len(word) > len(max_text):
        max_text = word
    elif len(word) < len(min_text):
        min_text = word
#แต่ถ้ามันซ้ำ มันก้เอาแค่ตัวที่มันเช็กไว้แรกๆ ละอยุใน max_text,min_text อ่ะ อธิบายไม่ถูกแหะ ผมเข้าใจพอล่ะกัน
print(f"- Longest word: '{max_text}' ({len(max_text)} letters)")
print(f"- Shortest word: '{min_text}' ({len(min_text)} letters)")
text_list = text.split()
vowel_words = []
vowels = "AEIOUaeiou"
for word in text_list:
    first_char = word[0]
    if first_char in vowels:
        vowel_words.append(word)
print(f"- Words starting with vowels: {len(vowel_words)} ({', '.join(vowel_words)})")




