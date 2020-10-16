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

note_len_s = 0.2
root_Note = Note("A4")
s = Scale(root_Note, 'major')

# Iterating Scales  (Original Mode)
original_mode_bool = False
if original_mode_bool:
    for scale_ in s.scales.keys():
        print('***')
        print(scale_)
        cs = Scale(root_Note, scale_)
        scale_short = []
        scale_full = []
        frecuency_ = []

        for n in cs.notes:
            scale_short.append(str(n))
            scale_full.append(n.musicalBeeps_notation())
            string_="{:0.2f}".format(n.frequency())
            frecuency_.append(string_)
            
            # player.play_note(str(n), 0.1)
            #player.play_note("pause", note_len_s)
            player.play_note(n.musicalBeeps_notation(), note_len_s)        
            print(string_)
            pass
        
        print(scale_short)
        print(scale_full) 
        print(frecuency_) 
        player.play_note("pause", note_len_s*2)
        pass

# Iterating Scales (From Numbers and Steps)
steps_mode_bool = True
if steps_mode_bool:
    for scale_ in s.scales_interval_steps.keys():
        print('***')
        print(scale_)
        cs = Scale.from_number(root_Note, scale_)
        scale_short = []
        scale_full = []
        frecuency_ = []

        for n in cs.notes:
            scale_short.append(str(n))
            scale_full.append(n.musicalBeeps_notation())
            string_="{:0.2f}".format(n.frequency())
            frecuency_.append(string_)
            
            # player.play_note(str(n), 0.1)
            #player.play_note("pause", note_len_s)
            player.play_note(n.musicalBeeps_notation(), note_len_s)        
            print(string_)
            pass
        
        print(scale_short)
        print(scale_full) 
        print(frecuency_) 
        player.play_note("pause", note_len_s*2)
        pass