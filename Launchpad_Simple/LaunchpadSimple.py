import Live

from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.ControlSurface import ControlSurface
from _Framework.InputControlElement import MIDI_CC_TYPE, MIDI_NOTE_TYPE
from _Framework.SessionComponent import SessionComponent
from Launchpad.ConfigurableButtonElement import ConfigurableButtonElement

from Constants import *
from SpecialMixerComponent import SpecialMixerComponent as MixerComponent
from ViewToggle import ViewToggle, DetailViewToggle
from QuantizationToggle import QuantizationToggle

def make_button( type, cc_no ):
    # ConfigurableButtonElement( is_momentary, msg_type, channel, identifier )
    return ConfigurableButtonElement( True, type, 0, cc_no )

class LaunchpadSimple( ControlSurface ):

    def __init__( self, c_instance ):
        ControlSurface.__init__( self, c_instance )

        with self.component_guard():
# TODO
            # self._suppress_send_midi = True
            # self._suppress_session_highlght = True
# TODO

            self._suggested_input_port = 'Launchpad'
            self._suggested_output_port = 'Launchpad'

            # Launchpad configuration
            self._send_midi( LAUNCHPAD_RESET )
            self._send_midi( LAUNCHPAD_ENABLE_BLINKING )

            # make buttons
            top_buttons = [ make_button( MIDI_CC_TYPE, 104 + i ) for i in range( 8 ) ]
            side_buttons = [ make_button( MIDI_NOTE_TYPE, 8 + 16 * i ) for i in range( 8 ) ]

            matrix = ButtonMatrixElement()
            for row in range( 8 ):
                button_row = [ make_button( MIDI_NOTE_TYPE, 16 * row + col ) for col in range( 8 ) ]
                matrix.add_row( tuple( button_row ) )

            # mixer and session components
            self._mixer = MixerComponent( 8 )
            self._session = SessionComponent( 8, SCENES_AMOUNT )
            self._session.set_mixer( self._mixer )
            self.set_highlighting_session_component( self._session )

            # navigation
            for button in top_buttons[ :4 ]:
                button.set_on_off_values( GREEN_FULL, GREEN_THIRD )
            self._session.set_scene_bank_buttons( top_buttons[ 1 ], top_buttons[ 0 ] )
            self._session.set_track_bank_buttons( top_buttons[ 3 ], top_buttons[ 2 ] )

            # clip launch
            for scene_index in range( SCENES_AMOUNT ):
                scene = self._session.scene( scene_index )
                scene.set_launch_button( side_buttons[ scene_index ] )
                scene.set_triggered_value( GREEN_BLINK )
                scene.set_scene_value( GREEN_THIRD )
                scene.set_no_scene_value( LED_OFF )

                for track_index in range( 8 ):
                    clip_slot = scene.clip_slot( track_index )
                    clip_slot.set_launch_button( matrix.get_button( track_index, scene_index ) )
                    clip_slot.set_triggered_to_play_value( GREEN_BLINK )
                    clip_slot.set_triggered_to_record_value( RED_BLINK )
                    clip_slot.set_started_value( GREEN_FULL )
                    clip_slot.set_stopped_value( AMBER_THIRD )
                    clip_slot.set_recording_value( RED_FULL )

            # track stop
            self._session.set_stop_track_clip_buttons(
                [ matrix.get_button( i, ROW_STOP ) for i in range( 8 ) ]
            )
            self._session.set_stop_clip_value( RED_THIRD )
            self._session.set_stop_clip_triggered_value( RED_BLINK )

            button_stop_all = side_buttons[ ROW_STOP ]
            button_stop_all.set_on_off_values( RED_FULL, RED_THIRD )
            self._session.set_stop_all_clips_button( button_stop_all )

            # track select
            self._mixer.set_track_select_buttons(
                [ matrix.get_button( i, ROW_SELECT ) for i in range( 8 ) ]
            )
            self._mixer.set_track_select_values( AMBER_FULL, AMBER_THIRD, LED_OFF )

            button_select_master = side_buttons[ ROW_SELECT ]
            button_select_master.set_on_off_values( AMBER_FULL, AMBER_THIRD )
            self._mixer.set_master_select_button( button_select_master )

            # make remaining pads assignable
# TODO
            for row in range( ROW_SELECT + 1, 8 ):
                for col in range( 8 ):
                    button = matrix.get_button( col, row )
                    button.set_on_off_values( AMBER_THIRD, LED_OFF )
                    button.turn_off()
                    button.add_value_listener( self._button_value_listener )

# This doesn't seem to work because midi mapping gets priority?
# Original scripts disable blinking when in user mode...

# TODO

            # delete clip button
            self._delete_button = top_buttons[ INDEX_DELETE_BUTTON ]
            self._delete_button.set_on_off_values( RED_BLINK, RED_THIRD )
            self._delete_button.add_value_listener( self._delete_value_listener )

            self._del_pressed = False
            self._delete_button.turn_off()

            # quantization toggle
            self._quantization_toggle = QuantizationToggle(
                top_buttons[ INDEX_QUANTIZATION_BUTTON ], self.song(), GREEN_THIRD, RED_THIRD
            )

            # browser view toggle
            self._browser_view_toggle = ViewToggle(
                side_buttons[ INDEX_BROWSER_VIEW_BUTTON ], ABLETON_VIEW_BROWSER,
                GREEN_THIRD, RED_THIRD
            )

            # detail view toggle
            self._device_view_toggle = DetailViewToggle(
                side_buttons[ INDEX_DETAIL_VIEW_BUTTON ], GREEN_THIRD, RED_THIRD, LED_OFF
            )

    def disconnect( self ):
        self._send_midi( LAUNCHPAD_RESET )
        ControlSurface.disconnect( self )

        self._delete_button.remove_value_listener( self._delete_value_listener )
        self._delete_button = None
        self._quantization_toggle.disconnect()
        self._quantization_toggle = None
        self._browser_view_toggle.disconnect()
        self._browser_view_toggle = None
        self._device_view_toggle.disconnect()
        self._device_view_toggle = None

        self._session = None
        self._mixer = None

# TODO
    # def refresh_state( self ):
    #     ControlSurface.refresh_state( self )
    #     self.schedule_message( 5, self._update_hardware )

    # def _update_hardware( self ):
    #     pass
# TODO

    def receive_midi( self, midi_bytes ):
        if self._del_pressed and self._delete_clip( midi_bytes ):
            return
        else:
            ControlSurface.receive_midi( self, midi_bytes )

    def _button_value_listener( self, value ):
        pass

    def _delete_value_listener( self, value ):
        self._del_pressed = ( value == 127 )
        self._delete_button.set_light( self._del_pressed )

    def _delete_clip( self, midi_bytes ):
        if midi_bytes[ 0 ] == MIDI_NOTE_ON_VALUE:
            row, col = launchpad_button_loc( midi_bytes[ 1 ] )
            if row < SCENES_AMOUNT and col < 8:
                self._session.scene( row ).clip_slot( col )._do_delete_clip()
                return True
        return False
