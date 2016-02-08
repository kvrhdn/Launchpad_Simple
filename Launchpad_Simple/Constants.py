### Configuration

# indexes are zero-based

SCENES_AMOUNT = 3           # do not increase above 6

ROW_STOP = SCENES_AMOUNT
ROW_SELECT = ROW_STOP + 1

# on top buttons, 0-3 used for navigation
INDEX_DELETE_BUTTON = 4
INDEX_QUANTIZATION_BUTTON = 7

# on side buttons
# 0 - AMT_SCENES + 1 reserved for scene control, stop all and select master
INDEX_BROWSER_VIEW_BUTTON = 6
INDEX_DETAIL_VIEW_BUTTON = 7


### MIDI

MIDI_NOTE_ON_VALUE = 144
MIDI_CC_VALUE = 176


### Launchpad colours

# Velocity value - colour
#   6   '0'
#   5-4 GREEN
#   3   clear other buffer
#   2   write to both buffers (overrides clear)
#   1-0	RED
#
# Novation's datasheet:
# http://d19ulaff0trnck.cloudfront.net/sites/default/files/novation/downloads/4080/launchpad-programmers-reference.pdf

LED_OFF = 0x0C      # 000 1100

RED_THIRD = 0x0D    # 000 1101
RED_HALF = 0x0E     # 000 1110
RED_FULL = 0x0F     # 000 1111
RED_BLINK = 0x0B    # 000 1011

GREEN_THIRD = 0x1C  # 001 1100
GREEN_HALF = 0x2C   # 010 1100
GREEN_FULL = 0x3C   # 011 1100
GREEN_BLINK = 0x38  # 011 1000

AMBER_THIRD = 0x1D  # 001 1101
AMBER_HALF = 0x2E   # 010 1110
AMBER_FULL = 0x3F   # 011 1111
AMBER_BLINK = 0x3B  # 011 1011

### Launchpad pads

def launchpad_button_loc( value ):
    """" Returns the row and column of the button. """
    return value / 16, value % 16

### Launchpad comfiguration commands

LAUNCHPAD_RESET = ( MIDI_CC_VALUE, 0, 0 )
LAUNCHPAD_ENABLE_BLINKING = ( MIDI_CC_VALUE, 0, 40 )
LAUNCHPAD_DISABLE_BLINKING = ( MIDI_CC_VALUE, 0, 32 )


### Ableton API

# Views

ABLETON_VIEW_BROWSER = 0
ABLETON_VIEW_DETAIL = 3
ABLETON_VIEW_DETAIL_DEVICE = 5
