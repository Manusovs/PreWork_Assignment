polls = ["david", "sarah", "john", "edward"]

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'}
for name in polls:
    if name in favorite_languages:
        print(name.title() + " Thank you for taking the poll")
    else: 
        print(name.title() + " please take the poll")