Launchpad Simple
===

A custom midi remote script to control Ableton Live with the Novation Launchpad.  
Intention is to make a simpler layout (no menu tabs) which offers quick access to some useful functions.

Overview
---

*Insert image here*

Features:

- Navigation buttons and 3 rows of clips similar to the orginal Launchpad. The scene launch button now indicates whether a scene is actually present.
- Delete button: hold + select a clip to quickly delete that clip.
- Quantization toggle button: switches between two quantization settings. When you toggle, the current value is swapped with the previous value.
- Row of stop buttons + stop all tracks.
- Row of select track button + select master.
- Toggle button to show / hide the browser.
- Toggle button to toggle the detail view. If you tap twice the detail view will be hidden.
- The remaining pads can be MIDI mapped. **[in progress]**

Installation
---

Download or clone this repository. Copy the `Launchpad_Simple` folder to the MIDI Remote Scripts folder of Ableton Live.  

On Mac OS you can find this folder here:  
> `/Applications/Ableton Live 9 Suite.app/Contents/App-Resources/MIDI Remote Scripts/`

On Windows:  
> `C:\\ProgramData\Ableton\Live x.x\Resources\MIDI Remote Scripts\`

[ableton.com: How to install a third-party Remote Script?](https://www.ableton.com/en/help/article/install-third-party-remote-script/)


Additionally, on Mac OS X you can simply execute `copy_scipts.command`, it will automatically copy the scripts for you.

To do
---

Known bugs:

- General purpose pads blink when turned off. Makes them kind of useless :/
- Disconnect and reconnect is not handled properly.
- Session highlight is active, even if Launchpad is not connected yet. Same/similar problem as above.

Possible improvements:

- QuantizationToggle: is it possible to store the secondary value in the Live set itself? Currently the secondary value defaults to `q_no_q` (or `q_1_bar` if `q_no_q` is already set).
- Hold DetailViewToggle to hide Detail view entirely. Double tap is a bit awkward.

Disclaimer
---

These scripts are only tested on my system. Use at your own risk!

Currently I know these work with Ableton Live 9.6 on Mac OS X El Capitan (10.11.3) and the Launchpad Mini. Let me now if the scripts work or break on other systems.  
It will likely work on other versions of Mac OS and Windows. But it is not unlikely that it won't work with Live 9.5: Live 9.6 uses a newer version of Python (2.7) which offers different features. I only test on my own system.

Feel free to let me know if the scripts do or do not work on other systems.

Contact
---

I don't mind answering *some* questions about MIDI remote scripts. Open up an issue on GitHub or send me a message on Twitter [@KoenraadVer](https://twitter.com/KoenraadVer).
