import config_file_utility as ini

result = ini.config_update('new_config.ini', 'Section_2', 'Option_2', 'new value 2')
result = ini.config_update('new_config.ini', 'Section_1', 'Option_1', 'new value 1')

if result[0] == 0:
    print(result[1])
elif result[0] == 1:
    print('Unsuccessful')

result = ini.config_read('new_config.ini', 'Section_1', 'Option_1')

if result:
    print(result)
else:
    print('Value doesn\'t exist')