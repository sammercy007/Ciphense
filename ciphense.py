from googlesearch import search

print("After entering a sentence, you must give DOT or FULL POINT (.)")

print('Enter the sentences: ')
user_input = input()


#split the sentence where . dot is present

user_input = user_input.split('.')

#remove the null character present in the list due to spliting of last sentence 
user_input.remove('')


size = len(user_input)

i=1

'''
append the user_input list item by double qoute at first and last of each sentence
and append the list item by AND
i i am aif it is not the last sentence then add AND or else not
'''
query = ""
for sentence in user_input:
    if(i<size): 
        query = query + '"' + sentence + '"' + ' AND '
    else:
        query = query + '"' + sentence + '"'
    i=i+1


    
site = "site:en.wikipedia.org "

print('Wikipedia Url is: ')

#search the url

for url in search(site+query, tld='co.in', num=10,stop = 10,only_standard=True):
    print(url)