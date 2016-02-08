from _Framework.ChannelStripComponent import ChannelStripComponent

class SpecialChannelStripComponent( ChannelStripComponent ):
    """
    ChannelStripComponent that allows to set values for the select buttons.
    """

    def __init__( self ):
        ChannelStripComponent.__init__( self )
        self._track_empty_value = None

    def set_select_values( self, selected, not_selected, empty ):
        self._select_button.set_on_off_values( selected, not_selected )
        self._track_empty_value = empty

    def on_selected_track_changed( self ):
        if self.is_enabled() and self._select_button is not None:
            if self._track is not None:
                if self.song().view.selected_track == self._track:  # track is selected
                    self._select_button.turn_on()
                else:                                               # track is not selected
                    self._select_button.turn_off()
            else:                                                   # track is empty
                if self._track_empty_value is not None:
                    self._select_button.send_value( self._track_empty_value )
                else:
                    self._select_button.turn_off()