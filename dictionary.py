options = {
  'env': 'production',
  'db': 'mysql',
  'ver': 1.0,
  'show_errors': True
}

options['user'] = 'admin'
options['ver'] = 2.0
print(options['ver'])
del options['db']

print(options.get('db'))

options.update({
  'mobile': False,
  'app_name': 'domneo.pl',
  'ver': 2.3
})

print(options)

for key in options:
  print(options[key])

print(options.values())
print(options.keys())