def make_pl_sentence(sentence):
    sentence_list = []
    for word in sentence.split():
        if word[0] in 'aeiou':
            sentence_list.append(word + 'way')
        else :
            sentence_list.append(word[1:] + word[0] + 'ay')
    return ' '.join(sentence_list)


print(make_pl_sentence('this is a test translation'))