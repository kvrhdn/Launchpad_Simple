from _Framework.MixerComponent import MixerComponent

from SpecialChannelStripComponent import SpecialChannelStripComponent

class SpecialMixerComponent( MixerComponent ):
    """
    Mixer component that uses the SpecialChannelStripComponent. Allows to set a
    master select button and to set values for the track select buttons.
    """

    def set_master_select_button( self, button ):
        self.master_strip().set_select_button( button )

    def set_track_select_values( self, selected, not_selected, empty ):
        for strip in self._channel_strips:
            strip.set_select_values( selected, not_selected, empty )

    def _create_strip( self ):
        return SpecialChannelStripComponent()
