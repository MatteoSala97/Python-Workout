from operator import itemgetter
people = [
    {
        'first':'Reuven', 
        'last':'Lerner',
        'email':'reuven@lerner.co.il'
    }, 
    {
        'first':'Donald', 
        'last':'Trump',
        'email':'president@whitehouse.gov'
    }, 
    {
        'first':'Vladimir', 
        'last':'Putin',
        'email':'president@kremvax.ru'
    }
]

def alphabetize_names(people):
    
# giving both the return possibilities asked by the book
#   return sorted(people, key=lambda person:(person['last'], person['first']))   # newlist = sorted(list_to_be_sorted, key=lambda d: d['name'])
   return sorted(people, key=itemgetter('last', 'first'))
#   return sorted(people, key=lambda x: x.get('first'), reverse=True)
  
sorted_people = alphabetize_names(people)

for i in sorted_people:
    print(f"{i['last']} {i['first']} - email: {i['email']}.")
    