text_example = "A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place."

punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']

def get_unique_words(text):
    new_text = ''
    
    for symb in text:
        if symb not in punctuation_list:
            new_text+=symb
        
    new_text1 = new_text.lower()
    new_text2 = new_text1.split()
    
    fin_list = []

    for item in new_text2:
        if item not in fin_list:
            fin_list.append(item)
    
    return fin_list

def get_most_frequent_word(text):
    new_text = ''
    
    for symb in text:
        if symb not in punctuation_list:
            new_text+=symb
        
    new_text1 = new_text.lower()
    new_text2 = new_text1.split()
    
    unique_lst = get_unique_words(text)
    dict1 = {}
    
    for key in unique_lst:
        count = 0
        for item in new_text2:
            if item == key:
                count += 1
        dict1[key] = count
    
    freq_value = 0
    word = ''
    
    for key, value in dict1.items():
        if value > freq_value:
            word = key
            freq_value = value
    
    return word
    
print(get_most_frequent_word(text_example))
print(get_most_frequent_word(text_example+'abcdef'))
print(get_most_frequent_word(text_example+'jklmn'))