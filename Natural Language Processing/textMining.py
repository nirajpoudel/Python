text = 'Hey This is Niraj Poudel from Sandhikharka 1 Arghakhanchi'
#printing the lenth of the sentense.
#print(len(text))

#spliting the text on the basis of space.
#text = text.split(' ')
#print(len(text))

#finding the words which length are greater than 5.
#print([i for i in text if len(i)>5])

#finding the capatilize word.
#print([i for i in text if i.istitle()])

#finding the small word.
#print([i for i in text if i.islower()])

#words that ends with s.
#print([i for i in text if i.endswith('s')])

#words that starts with S.
#print([i for i in text if i.startswith('S')])

# finding the numeric character in the text
#print([i for i in text if i.isdigit()])

#finding the character expect number.
#print([i for i in text if i.isalpha()])


import re
text1 = '@ niraj for me in @sandhikharka #Arghakhanchi in @lumbini #Nepal'
#text1 =text1.split(' ')
#print([word for word in text1 if word.startswith('@')])

#print([word for word in text1 if re.search('@[A-Za-z0-9_]+',word)])
#print([word for word in text1 if re.search('@\w+',word)])

print(re.findall(r'[aeiou]',text1))





























