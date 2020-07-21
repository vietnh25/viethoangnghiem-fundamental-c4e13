teencode_dict = {
  'nc': 'Nói chuyện',
  'ck': 'Chuyển khoản',
  'vk': 'Vũ khí'
}
while True:
  print('*'*25)
  for key in teencode_dict:
    print(key, end='\t')
  print()
  input_key = input('your code? ')
  if input_key in teencode_dict:
    print(f'it means: {teencode_dict[input_key]}')
  else:
    action = input('not found! do you want to contribute to our dictionary? (y/n)')
    if action.upper() == 'Y':
      teencode_dict[input_key] = input('Tranlation: ')
      print(teencode_dict)
    else:
      break