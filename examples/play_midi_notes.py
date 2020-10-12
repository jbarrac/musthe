from musthe import Interval
from musthe import Note
from musthe import Scale

import musicalbeeps

player = musicalbeeps.Player(volume = 0.3,
                            mute_output = False)

# Examples:

# To play an A on default octave n°4 for 0.2 seconds
# player.play_note("A", 0.2)

# To play a G flat on octave n°3 for 2.5 seconds
# player.play_note("G3b", 2.5)

# To play a F sharp on octave n°5 for the default duration of 0.5 seconds
# player.play_note("F5#")

# To pause the player for 3.5 seconds
# player.play_note("pause", 3.5)


root_Note = Note("A4")
s = Scale(root_Note, 'major')

for scale_ in s.scales.keys():
    print('***')
    print(scale_)
    cs = Scale(root_Note, scale_)
    scale_short = []
    scale_full = []
    for n in cs.notes:
        scale_short.append(str(n))
        scale_full.append(n.scientific_notation())
        print(n.frequency())
        
        # player.play_note(str(n), 0.1)
        player.play_note(n.scientific_notation(), 0.1)
    print(scale_short)
    print(scale_full) 