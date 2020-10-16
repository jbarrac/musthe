import time
import rtmidi

# help MIDI values
# http://www.somascape.org/midi/tech/spec.html#statCn

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

"""
midiout.get_ports()
"""

if available_ports:
    midiout.open_port(0)    # 'Arturia MiniLab mkII 3'
    # midiout.open_port(0)
    print(available_ports)
else:
    midiout.open_virtual_port("My virtual output")

#Consts
bank_selector_value = 0

# Params
silence_t = 0.05
m_channel = 0x90
vel  = 32       

#note_on  = [0x40, note, vel] # channel 10, middle C, velocity 112

#2 bytes	1100nnnn , 0ppppppp
#1100nnnn	Program Change status byte;   nnnn (0-15) = MIDI channel 1-16
#ppppppp	Program number (0-127)

# Control Change: 176, 7, 100 (volume)
# 0: Bank Selector 
# 7: Volume

#Bank Selector
control_Number = 6 # Controller number (0-119), Values 120-127 are reserved for Channel Mode messages
midiout.send_message([m_channel, bank_selector_value, control_Number])

for pc in range(1, 128):
    print("Program %d", pc)
    midiout.send_message([192, pc])

    for n in range(60, 67):
        note_on = [m_channel, n, vel] # channel 10, middle C, velocity 112
        midiout.send_message(note_on)
        time.sleep(silence_t)

        note_off = [m_channel, n]
        midiout.send_message(note_off)

    time.sleep(silence_t*10)

"""
for i in range(128, 243):
    print(i)
    note_on  = [i, 50, vel] # channel 10, middle C, velocity 112
    midiout.send_message(note_on)
    time.sleep(silence_t)
    midiout.send_message(note_off)
"""

del midiout