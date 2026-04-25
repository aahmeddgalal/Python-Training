def add_setting(settings, pair):
    key = pair[0].lower()
    value = pair[1].lower()
    if key in settings.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key.lower()}' added with value '{value.lower()}' successfully!"


def update_setting(usettings, upair):
    key = upair[0].lower()
    value = upair[1].lower()
    if key in usettings.keys():
        usettings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key.lower()}' does not exist! Cannot update a non-existing setting."


# def delete_setting(dsettings, dpair):
#     key = dpair[0].lower()

#     if key in dsettings:
#         del dsettings[key]
#         return f"Setting '{key}' deleted successfully!"
#     else:
#         return "Setting not found!"

def delete_setting(dsettings, dpair):
    key = dpair.lower()

    if key in dsettings:
        del dsettings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"


def view_settings(vsettings):
    if not vsettings:
        return "No settings available."
    else:
        result = "Current User Settings:\n"

        for key, value in vsettings.items():
            result += f"{key.capitalize()}: {value}\n"

        return result


test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
}

update_setting({'theme': 'light'}, ('theme', 'dark'))

print(add_setting({'theme': 'light'}, ('volume', 'high')))
