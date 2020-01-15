from pprint import pprint

sentence = ' This is a very very common interview question, find the most common char'
values = [*sentence]
pairs = {}

# pprint(pairs , width = 2)

for c in values:
    if not c.strip() == '' :
        pairs[c.lower()] = pairs.get(c, 0) + 1
    
    # one line option:
    # pairs[c.lower()] = pairs.get(c, 0) + 1 if not c.strip() == '' else 0

sorting = sorted(pairs.items(), key=lambda kv: kv[1], reverse=True)

# // PRINT IT Nicely with pprint
pprint(sorting[0], width=15)
