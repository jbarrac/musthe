from musthe import Interval
from musthe import Note
from musthe import Scale

# Notes Define
A4 = Note("A4")
Eb = Note("Eb")
C0 = Note("C0") # number =  0
B0 = Note("B0") # number = 11
C1 = Note('C1') # number = 12

# Intervals Define
P1_int = Interval('P1') # 0 semitones
P5_int = Interval('P5') # 7 semitones
m2_int = Interval('m2') # 2 semitones

# Tests 1. Add Interval to a Note
test_1 = C0 + P1_int
print(test_1)
print(test_1.number)
print(test_1.octave)

# Test 2. Check Octave Value is incremented when a 
# number surpass current octave
test_2 = B0 + P5_int
print(test_2)
print(test_2.number)
print(test_2.octave)


# Test 3. Print Scales Notes
# s.greek_modes -> DICT
s = Scale(C0, 'major')
print(s.root)       # C
print(s.notes)      # Notes in Scale

# TODO: Function for plotting all Greek Scales from a Note
root_Note = C0
for mode in s.greek_modes.values():
    print('---')
    print(mode)
    cs = Scale(root_Note, mode)
    scale_txt = []
    for n in cs.notes:
        scale_txt.append(str(n))        
    print(scale_txt)

# TODO: Function for plotting all Availables Scales from a Root Note
root_Note = C0
for scale_ in s.scales.keys():
    print('***')
    print(scale_)
    cs = Scale(root_Note, scale_)
    scale_txt = []
    for n in cs.notes:
        scale_txt.append(str(n))        
    print(scale_txt)



#Crash 1. cs.notes[7]-cs.notes[0]
#cs.notes[0]-cs.notes[1]

#Crash 4. TODO. Fix Crash, after 4 attemps due to maximum accidental chars
Note_inc = C0
for i in range(12):
    Note_inc = Note_inc + m2_int
    print("---")
    print(i)
    print(Note_inc)
    print(Note_inc.number)
    print(Note_inc.octave)

