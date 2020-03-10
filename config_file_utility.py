from configparser import ConfigParser


def config_update(file, section, option, value):
    """
    Creates and/or updates a configuration flat file.
    
    Args:
        file (str): file to change or create
        section (str): config file section to target or create
        option (str): config file option (under a section) to target or create
        value (str): value for the targeted option
    """
    config = ConfigParser()
    config.read(file)
    cfgfile = open(file, 'w')
    if config.has_section(section) == True:
        config.set(section, option, value)
    else:
        config.add_section(section)
        config.set(section, option, value)
    config.write(cfgfile)
    cfgfile.close()
    config.read(file)
    if config.has_option(section, option) == True:
        recorded_value = config.get(section, option)
        return [0, f'[{file}] => [{section}] => [{option}] => {recorded_value}']
    else:
        return [1]


def config_read(file, section, option):
    """
    Reads configuration flat file and returns a value.
    
    Args:
        file (str): config file to read
        section (str): config file section to target
        option ([type]): config file option to retrieve value from
    
    Returns:
        str: value stored in configuration file
    """
    config = ConfigParser()
    config.read(file)
    if config.has_option(section, option) == True:
        value = config.get(section, option)
        return value