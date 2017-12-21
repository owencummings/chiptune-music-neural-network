

#Map each piano note to an int
def note_to_number(note_str):

    d = {
        #What should be done about hold/break values?#
        #I think that the helper function should handle '..' cases since these are equivalent
        #to maintaining the same values as the previous register call (recursively)
        '..': -1,
        '--': -2,
        ##############################################
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
        'B-': 11,
        'B#': 12
    }

    val = 0
    val = val  + d[note_str[0:2]]
    if val < 0:
        return val
    val = val + 13*int(note_str[2])
    return val


#Parses an individual row of instructions to numerical format
def line_to_array(txt, prev):

    arr = []

    #This should get one register-worth of values, not counting the effects, which seem extraneous.
    #For now, lets just try it with one register and see if we can get a nice result.
    txt = txt[9:]
    if txt[0] == '.':
        arr.append(prev[0])
    else:
        arr.append(note_to_number(txt[0:3]))

    txt = txt[7:]
    if txt[0] == '.':
        arr.append(prev[1])
    else:
        arr.append(int(txt[0], 16))

    txt = txt[16:]


    return arr

def file_parse(path_to_file):
    filename = path_to_file
    f = open(filename, "r")
    arr = f.readlines()
    arr = [x for x in arr if x[0:3] == 'ROW']
    arr = [line_to_array(x) for x in arr]
    f.close()
    return arr

def arr_to_file(arr, path_to_file):
    f = open(filename, 'w')
    f.write('# FamiTracker text export 0.4.2')
    f.write('')
    f.write('# Song information')
    f.write('TITLE           "Neural Network OST"')
    f.write('AUTHOR          "Owen Cummings"')
    f.write('COPYRIGHT       ""')
    f.write('')
    f.write('# Song comment')
    f.write('COMMENT ""')
    f.write('')
    f.write('# Global settings')
    f.write('MACHINE         0')
    f.write('FRAMERATE       0')
    f.write('EXPANSION       1')
    f.write('VIBRATO         1')
    f.write('SPLIT           21')
    f.write('')
    f.write('# Macros')
    f.write('')
    f.write('# DPCM samples')
    f.write('')
    f.write('# Instruments')
    f.write('INST2A03   0    -1  -1  -1  -1  -1 "blank"')
    f.write('INSTVRC6   1    -1  -1  -1  -1  -1 "blank"')
    f.write('')
    f.write('# Tracks')
    f.write('')
    f.write('TRACK 256   1 150 "New song"')
    f.write('COLUMNS : 3 3 1 1 2 2 2 2')
    f.write('')
    f.write('')
    f.write('')
    f.write('')
    f.write('')
    f.write('')
    f.write('')
    f.write('')


    f.close()
    return
