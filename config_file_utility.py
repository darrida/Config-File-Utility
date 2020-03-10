from configparser import ConfigParser


def config_update(file, section, option, new_value):
    """
    Creates and/or updates a configuration flat file.

    Args:
        file (str): file to change or create
        section (str): config file section to target or create
        option (str): config file option (under a section) to target or create
        value (str): value for the targeted option

    Returns:
        int: 0 = Success
             1 = File/section/option not found
             2 = Update issue: Mismatch between valued passed in and value in confi file

    """
    config = ConfigParser()
    config.read(file)
    cfgfile = open(file, 'w')
    if config.has_section(section) == True:
        config.set(section, option, new_value)
    else:
        config.add_section(section)
        config.set(section, option, new_value)
    config.write(cfgfile)
    cfgfile.close()
    config.read(file)
    if config.has_option(section, option) == True:
        recorded_value = config.get(section, option)
        if new_value == recorded_value:
            return 0
        else:
            return 2
    else:
        return 1


def config_read(file, section, option):
    """
    Reads configuration flat file and returns a value.

    Args:
        file (str): config file to read
        section (str): config file section to target
        option (str): config file option to retrieve value from

    Returns:
        str: value stored in configuration file

    """
    config = ConfigParser()
    config.read(file)
    if config.has_option(section, option) == True:
        value = config.get(section, option)
        return value