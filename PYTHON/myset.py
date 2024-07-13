# Python set we use {}
# Set does not allow duplicates
# Set is not ordered (items does not retain its position)
# Set is not indexed (do not have indexes like 0, 1, 2, 3, 4 .....)
# Set is modifiable
fruits = {"apple", "orange", "mango", "apple", "banana", "grapes", "apple"}
print(fruits)

# Selection and Indexing
# You cannot select the item using Index
# But you can always iterate using for loop
# print(fruits[0])
for fruit in fruits:
    print(fruit)

# Modifiable
fruits.add("durian")
print(fruits)

# Update
# fruits[2] = "rambutan"
# If you want to update drop the old fruit and add the new fruit

# Drop a fruit
# fruits is an object or instance of a set class
# remove is a method inside the object fruits
fruits.remove("grapes")
print(fruits)

# you can also use pop
# however pop will "randomly remove an item"
fruits.pop()
print(fruits)

# NLP => Natural Language Processing
# NLTK

overseafruits = {"apple", "orange", "banana", "mango", "grapes"}
localfruits = {"durian", "rambutan", "cempedak", "mangosteen", "banana"}

print(overseafruits.union(localfruits))
print(overseafruits.intersection(localfruits))
print(overseafruits.difference(localfruits))
print(localfruits.difference(overseafruits))

favoritefruits = {"durian", "rambutan", "mangosteen"}
print(favoritefruits.issubset(localfruits))
print(localfruits.issuperset(favoritefruits))
print(favoritefruits.isdisjoint(overseafruits))

content = """Spam emails are emails sent to you without your knowledge 
or consent, which often contain marketing. It is email that you do not 
want and did not ask for, and its content can cause annoyance, 
embarrassment and even distress. However, it is worth remembering that 
the sender generally does not target recipients personally. The same 
spam email can be sent to millions of people at the same time and the 
addresses can often be guessed. Not all marketing emails sent without 
consent are spam emails. Marketing emails can be sent without prior 
consent by organisations who obtained your email address when you bought 
something from them and are advertising similar products or services. 
However, these marketing emails must abide by strict rules regarding their 
content and provide you with the opportunity to opt out.
"""

words = content.split()
print(len(words))

uniquewords = set(words)
print(len(uniquewords))

cleanwords = []
for word in words:
    word = word.replace(",", "")
    word = word.replace(".", "")
    word = word.lower()
    cleanwords.append(word)

uniquewords = set(cleanwords)
print(len(uniquewords))

commonwords = {"do", "is", "all", "did", "not", "you", "i", "be", "to", "at", "a", "and"
               "he", "she", "we", "they", "what", "when", "why", "how", "or"}
uniquewords = uniquewords.difference(commonwords)
print(len(uniquewords))
print(uniquewords)

spamwords = {"advertising", "opportunity", "embarrassment", "remembering"}
doescontenthasspamwords = uniquewords.intersection(spamwords)
print(len(doescontenthasspamwords))


listfruits = list(fruits)
listfruits.clear()
print(listfruits) # empty list      []

fruits.clear()
print(fruits) # empty set           set()