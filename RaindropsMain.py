def convert_number(n):  # Function takes number as parameter
    result_string = ""  # Initialises string to empty

    sounds = {  # Uses dictionary to contain factors and strings for flexibility in the program
        3: 'Pling',
        5: 'Plang',
        7: 'Plong',
    }  # Dictionary contains factors with the corresponding sound string

    for sound in sounds.keys():  # For each key in the sounds dictionary
        if n % sound == 0:  # Do number mod current key's value
            result_string += sounds[sound]  # If current key is a factor then add the sound to the result string

    if result_string == "":  # If no keys are factors the convert the string to number
        result_string = str(n)  # assigns number converted to string to the result string
    return result_string  # return the result string

