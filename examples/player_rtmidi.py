from musthe import Interval
from musthe import Note
from musthe import Scale

import time
import rtmidi

# help MIDI values
# http://www.somascape.org/midi/tech/spec.html#statCn

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

if available_ports:
    midiout.open_port(0)    # 'Arturia MiniLab mkII 3'
    # midiout.open_port(0)
    print(available_ports)
else:
    midiout.open_virtual_port("My virtual output")

#Consts
bank_selector_value = 0

# Params
silence_t = 0.15
m_channel = 0x90
vel  = 96       

#Bank Selector
control_Number = 0 # Controller number (0-119), Values 120-127 are reserved for Channel Mode messages
midiout.send_message([m_channel, bank_selector_value, control_Number])


root_Note = Note("A4")
s = Scale(root_Note, 'major')

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

            note_on = [m_channel, n.midi_note(), vel] # channel 10, middle C, velocity 112
            midiout.send_message(note_on)
            time.sleep(silence_t)

            note_off = [m_channel, n.midi_note()]
            midiout.send_message(note_off)
        
        time.sleep(silence_t*10)

        
        print(scale_short)
        print(scale_full) 
        print(frecuency_) 
        pass