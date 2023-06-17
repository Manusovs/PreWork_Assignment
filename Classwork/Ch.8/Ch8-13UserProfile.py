def build_profile(first, last, **user_info):
    """Some text here"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile ('scott', 'manusov', 
                              location='cove', 
                              job='lab supervisor',
                              hobby='scuba diving')

print(user_profile)