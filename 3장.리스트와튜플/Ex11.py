import operator

PEOPLE = [
    {'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},
    {'first': 'Donald', 'last': 'Trump', 'email': 'president@whitehouse.gov'},
    {'first': 'Vladimir', 'last': 'Putin', 'email': 'president@kremvax.ru'},
    {'first': 'Lululu', 'last': 'Putin', 'email': 'kpresident@kremvax.ru'}
]

print(sorted(PEOPLE, key=lambda x:(x['last'],x['first'])))