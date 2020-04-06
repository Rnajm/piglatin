# pig latin translator
# get input from user
sentence = input("Eneter a sentence?: ").strip().lower()

# split the sentence in words
words = sentence.split()
# tranlate words into pig latin and store in a new list
    # if word starts with vowel then add "yay" to the word
    # if words starts with consonant then move consonant block to the end and add "ay"
new_words = []

for word in words:
    con_culster = 0
    if word[0] in "aeiou":
        
        new_word = word + "yay"
        new_words.append(new_word)  
    else:
        #loop through the word and find... 
        # where the consonants turns into a vowel 

        for letter in word:   
            if letter not in "aeiou":
                con_culster += 1
            else:
                break
        splitword = word[:con_culster]
        newword = word[con_culster:] + splitword + "ay"
        new_words.append(newword)        
                

print(new_words)
# put the translated words into a sentence

# output the sentence
#print(output)