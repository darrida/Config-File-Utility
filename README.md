# Config File Utility

Create / Update / Read flat files using two functions built from configparser.

## Setup

- Download/clone this repository
- Move the 'config_file_utility.py' your apps directory

```python
import config_file_utility as ini
```

## Create or Update a configuration file

```python
ini.config_update(<file>, <section_name>, <section_option>, <new_value>)
```

- Example Case

```python
import config_file_utility as ini

result = ini.config_update('new_config.ini', 'Section_2', 'Option_2', 'new value 2')
result = ini.config_update('new_config.ini', 'Section_1', 'Option_1', 'new value 1')

if result[0] == 0:          # 0 = Value recorded, no errors
    print(result[1])
elif result[0] == 1:        # 0 = Value add or update was unsuccessful
    print('Unsuccessful')
```

- Result: new_config.ini

```ini
[Section_2]
option_2 = new value 2

[Section_1]
option_1 = new value 1
```

## Read a configuration file

```python
result = ini.config_read(<file>, <existing_section>, <exiting_option>)
```

- Example Case

```python
result = ini.config_read('new_config.ini', 'Section_1', 'Option_1')

if result:
    print('Value:', result)
else:
    print('Value doesn\'t exist')
```
