def convert_number(n):
    result_string = ""
    sounds = {
        3: 'Pling',
        5: 'Plang',
        7: 'Plong',
    }
    for sound in sounds.keys():
        if n % sound == 0:
            result_string += sounds[sound]
    if result_string == "":
        result_string = str(n)

    return result_string
