# Emoticons
# Selection by JanJeronimus April 2024
# Sources:
# - https://apps.timwhitlock.info/emoji/tables/unicode
# - https://www.unicode.org/emoji/charts/full-emoji-list.html
# To do fix nice printing for multicharacter unicodes

## Emoticons
# Emoticons -1-:
emoji_smile                              = '\U0001F600' # 😀, 'smile'
emoji_scissors                           = '\U00002702' # ✂, 'scissors'
emoji_check                              = '\U00002714' # ✔, 'check'
emoji_cross                              = '\U0000274C' # ❌, 'cross'
emoji_copyright                          = '\U000000A9' # ©, 'copyright'

# Nature Emoticons:
emoji_snake                              = '\U0001F40D' # 🐍, 'snake'
emoji_spider_web                         = '\U0001F578' # 🕸, 'spider_web'
emoji_globe                              = '\U0001F30D' # 🌍, 'globe'
emoji_traffic_lightH                     = '\U0001F6A5' # 🚥, 'traffic_lightH'
emoji_construction                       = '\U0001F6A7' # 🚧, 'construction'

# Technology Emoticons:
emoji_glasses                            = '\U0001F453' # 👓, 'glasses'
emoji_laptop                             = '\U0001F4BB' # 💻, 'laptop'
emoji_computer                           = '\U0001F5A5' # 🖥, 'computer'
emoji_printer                            = '\U0001F5A8' # 🖨, 'printer'
emoji_keyboard                           = '\U00002328' # ⌨, 'keyboard'

# Tools Emoticons:
emoji_magnifying_glass_left              = '\U0001F50D' # 🔍, 'magnifying_glass_left'
emoji_magnifying_glass_right             = '\U0001F50E' # 🔎, 'magnifying_glass_right'
emoji_hammer                             = '\U0001F528' # 🔨, 'hammer'

# Other Emoticons:
emoji_briefcase                          = '\U0001F4BC' # 💼, 'briefcase'
emoji_folder                             = '\U0001F4C2' # 📂, 'folder'
emoji_bar_chart                          = '\U0001F4CA' # 📊, 'bar_chart'
emoji_numbers                            = '\U0001F522' # 🔢, 'numbers'
emoji_download                           = '\U0001F4E5' # 📥, 'download'

emoji_right_arrow_1                      = '\U000027A1' # ➡, 'right_arrow_1'
emoji_right_arrow_2                      = '\U0000279C' # ➜, 'right_arrow_2'
emoji_right_arrow_3                      = '\U00002794' # ➔, 'right_arrow_3'
emoji_robot_face                         = '\U0001F916' # 🤖, 'robot_face'

emoji_gear                               = '\U00002699' # ⚙, 'gear'
emoji_bust_in_silhouette                 = '\U0001F464' # 👤, 'bust_in_silhouette'
emoji_raised_hand                        = '\U0001F590' # 🖐, 'raised_hand'
emoji_raised_hand_with_fingers_splayed   = '\U0000270B' # ✋, 'raised_hand_with_fingers_splayed'

# Magic Emoticons:
emoji_wizard_man                         = '\U0001F9D9\U0000200D\U00002642\U0000FE0F'                                                                                              # 🧙‍♂️, 'wizard_man'
emoji_wizard_woman                       = '\U0001F9D9\U0000200D\U00002640\U0000FE0F'                                                                                              # 🧙‍♀️, 'wizard_woman'
emoji_elf                                = '\U0001F9DD' # 🧝, 'elf'
emoji_fairy                              = '\U0001F9DA' # 🧚, 'fairy'

def show_line(var_name) -> None:
    if not isinstance(var_name, str):
        print("Error: var_name must be a string.")
        return
    global_vars = globals()
    if var_name in global_vars:
        var_value = global_vars[var_name]
        var_suffix = var_name.replace("emoji_", "")
        print(f"{var_name.ljust(40)} = '", end="")
        var_unicode_hex = ''.join([f"\\U{hex(ord(char))[2:].upper().zfill(8)}" for char in var_value])
        print(var_unicode_hex, end="'\t# ")
        print(f"{var_value}, '{var_suffix}'")
    else:
        print(f"Error: {var_name} not found in global variables.")

def main():
    # Demo to printing out the emoticons along with their descriptions        
    print("\n### Emoticons ###")
    print("\n# Emoticons")
    show_line('emoji_smile')
    show_line('emoji_scissors')
    show_line('emoji_check')
    show_line('emoji_cross')
    show_line('emoji_copyright')

    print("\n# Nature Emoticons:")
    show_line('emoji_snake')
    show_line('emoji_spider_web')
    show_line('emoji_globe')
    show_line('emoji_traffic_lightH')
    show_line('emoji_construction')

    print("\n# Technology Emoticons:")
    show_line('emoji_glasses')
    show_line('emoji_laptop')
    show_line('emoji_computer')
    show_line('emoji_printer')
    show_line('emoji_keyboard')

    print("\n# Tools Emoticons:")
    show_line('emoji_magnifying_glass_left')
    show_line('emoji_magnifying_glass_right')
    show_line('emoji_hammer')

    print("\n# Other Emoticons:")
    show_line('emoji_briefcase')
    show_line('emoji_folder')
    show_line('emoji_bar_chart')
    show_line('emoji_numbers')
    show_line('emoji_download')
    print('' )
    show_line('emoji_right_arrow_1')
    show_line('emoji_right_arrow_2')
    show_line('emoji_right_arrow_3')
    show_line('emoji_robot_face')

    print('' )
    show_line('emoji_gear')
    show_line('emoji_bust_in_silhouette')
    show_line('emoji_raised_hand')
    show_line('emoji_raised_hand_with_fingers_splayed')

    print("\n# Magic Emoticons:")
    show_line('emoji_wizard_man')
    show_line('emoji_wizard_woman')
    show_line('emoji_elf')
    show_line('emoji_fairy')

    print('\n\n# some wrong input to test')
    show_line(emoji_fairy)
    show_line('foo')
    show_line( '✋')
    show_line( 5)

if __name__ == '__main__':
    main()
