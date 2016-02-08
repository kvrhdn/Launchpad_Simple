Launchpad Simple
===

A custom midi remote script to control Ableton Live with the Novation Launchpad.  
Intention is to make a simple layout (no menu tabs) which offers quick access to some useful functions.

Overview
---

*Insert image here*

Features:

- Navigation buttons and 3 rows of clips similar to the orginal Launchpad. The scene launch button now indicate whether a scene is actually present.
- Delete button: hold + select a clip to quickly delete that clip.
- Quantization toggle button: switches between two quantization settings. When you toggle, the current value is swapped with the previous value.
- Row of stop buttons + stop all tracks.
- Row of select track button + select master.
- Toggle button to show / hide the browser.
- Toggle button to toggle the detail view. If you tap twice the detail view is collapsed.
- The remaining pads can be MIDI mapped **[in progress]**

Installation
---

Move the Launchpad_Simple folder to the MIDI Remote Scripts folder of Ableton Live.  
[How to install a third-party Remote Script?](https://www.ableton.com/en/help/article/install-third-party-remote-script/)

On Mac OS this is:  
`/Applications/Ableton Live 9 Suite.app/Contents/App-Resources/MIDI Remote Scripts/`

On Windows:  
`\ProgramData\Ableton\Live x.x\Resources\MIDI Remote Scripts\`

Additionally, on Mac OS X you can simply execute `copy_scipts.command`, it will automatically copy the scripts for you.

To do
---

Bugs:

- General purpose pads blink when turned off. Makes them useless :/
- Disconnect and reconnect is not handled properly.
- Session highlight is active, even if Launchpad is not connected. Thus same as above.

Improvements:

- QuantizationToggle: store secondary value in Live set.
- Hold DetailViewToggle to hide Detail view entirely. Double tap is a bit awkward.

Disclaimer
---

These scripts are only tested on my system. Use at your own risk!

Currently I know these work with Ableton Live 9.6 on Mac OS X El Capitan (10.11.3) and the Launchpad Mini. Let me now if the scripts work or break on other systems.  
It will likely not work with Live 9.5.

Contact
---

I don't mind answering *some* questions about MIDI remote scripts. Open up an issue on GitHub or send me a message on Twitter [@KoenraadVer](https://twitter.com/KoenraadVer).
