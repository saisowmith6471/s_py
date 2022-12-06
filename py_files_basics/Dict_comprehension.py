#a = [i for i in range(100)]
#print(a)

#x = "this", "is", "is", "no", "alexa", "siri", "this", "is", "python", "code", "by", "netflix", "croma", "flix", "netflix", "this"
#print(x[4])

x = "this is is no alexa siri this is python code by netflix croma flix netflix this"
org_list = x.split()
print(org_list)
unique_set = set(org_list)
print(unique_set)
dicto = {}
for words in unique_set:
   dicto[words] = org_list.count(words)
print(dicto)

#using dictonary comprehension
dict_comp = {words: org_list.count(words) for words in unique_set}
print(dict_comp)























