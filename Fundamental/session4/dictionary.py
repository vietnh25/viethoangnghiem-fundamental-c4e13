# person=['Đức',96,175,70,'Sơn La',True,False,1]
# init {key:value,} 
person_dict = {
    'yob' : 96,
    'name' : 'Đức',
    'height' : 175,
    'weight' : 70,
    'nam' : '0'
}
# print(person_dict['yob'])
if 'nam' in person_dict: # check if key in dictionary
    print(person_dict['nam']) # Read one
person_dict['job'] = 'dev' # Create
person_dict['job'] = 'Đạo' # Update
del person_dict['nam'] # Delete
#Read all
for key in person_dict:
    print(key,person_dict[key])
    print()