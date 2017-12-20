#Map each piano note to an int
def note_to_number(note_str):

    d = {
        'C-': 0,
        'C#': 1,
        'D-': 2,
        'D#': 3,
        'E-': 4,
        'F-': 5,
        'F#': 6,
        'G-': 7,
        'G#': 8,
        'A-': 9,
        'A#': 10,
        'B': 11,
        'B#': 12
    }

    val = 0
    val = val  + d[note_str[0:2]]
    val = val + 13*int(note_str[2])
    return val



def line_to_array(txt):

    pass

def file_parse(path_to_file):

    pass
