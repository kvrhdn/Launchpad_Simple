import Live

class QuantizationToggle():
    """
    QuantizationToggle use a ConfigurableButtonElement to toggle the global
    quantization setting of a Live set. When it is toggled it stores the current
    setting and loads the previous setting (at start up this is no quantization).
    """

    def __init__( self, button, song, value_1, value_2 ):
        self._button = button
        self._song = song
        self._button.set_on_off_values( value_1, value_2 )
        self._button.add_value_listener( self._quantization_value_listener )

        self._state = True
        self._button.set_light( self._state )

        if self._song.clip_trigger_quantization != Live.Song.Quantization.q_no_q:
            self._quantization_value = Live.Song.Quantization.q_no_q
        else:
            self._quantization_value = Live.Song.Quantization.q_1_bar

    def disconnect( self ):
        self._button.remove_value_listener( self._quantization_value_listener )

    def _quantization_value_listener( self, value ):
        if value == 127:
            # swap self._quantization_value - self.song().clip_trigger_quantization
            self._quantization_value, self._song.clip_trigger_quantization = self._song.clip_trigger_quantization, self._quantization_value
            # toggle button
            self._state = not self._state
            self._button.set_light( self._state )
