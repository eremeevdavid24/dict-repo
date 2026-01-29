Instagram = {
    'username': 'Ion',
    'followers': 34,
    'following': 50,
    'verified': False,
    'brio': 'Locuiesc in Chisinau'
}

print(Instagram)

Instagram['followers'] += 1

Instagram['bio'] = 'Sunt un baiat bun'

Instagram['location'] = 'Moldova'

del Instagram['verified']

for key, value in Instagram.items():
    print(key, ":", value)

