import time
import Live

from Constants import ABLETON_VIEW_DETAIL, ABLETON_VIEW_DETAIL_DEVICE

class ViewToggle():
    """
    ViewToggle uses a ConfigurableButtonElement to show and hide a view
    component of Ableton Live.
    """

    def __init__( self, button, view_index, value_visible, value_hidden, suppress_button_update=False ):
        self._button = button
        self._button.set_on_off_values( value_visible, value_hidden )
        self._button.add_value_listener( self._view_value_listener )

        self._live_view = Live.Application.get_application().view
        self._view = self._live_view.available_main_views()[ view_index ]
        self._live_view.add_is_view_visible_listener( self._view, self._view_visible_listener )

        if not suppress_button_update:
            self._view_visible_listener()

    def disconnect( self ):
        self._button.remove_value_listener( self._view_value_listener )
        self._live_view.remove_is_view_visible_listener( self._view, self._view_visible_listener )

    def _view_value_listener( self, value ):
        if value == 127:
            if self._live_view.is_view_visible( self._view ):
                self._live_view.hide_view( self._view )
            else:
                self._live_view.show_view( self._view )

    def _view_visible_listener( self ):
        self._button.set_light( self._live_view.is_view_visible( self._view ) )

class DetailViewToggle( ViewToggle ):
    """
    Specific class to control the detail view, which has 3 states: Detail view
    hidden, Detail/DeviceChain view shown and Detail/Clip view shown.

    ViewToggle handles the toggling between Detail/DeviceChain and Detail/Clip,
    DetailViewToggle wraps these functions to check for Detail view.
    Additionally, if you toggle twice within 500 milliseconds, it will hide the
    Detail view.
    """

    def __init__( self, button, detail_device_visible, detail_clip_visible, detail_hidden ):
        ViewToggle.__init__(
            self, button, ABLETON_VIEW_DETAIL_DEVICE, detail_device_visible, detail_clip_visible,
            suppress_button_update=True
        )
        self._time = time.time()
        self._value_hidden = detail_hidden

        self._LIVE_VIEW_DETAIL = self._live_view.available_main_views()[ ABLETON_VIEW_DETAIL ]
        self._live_view.add_is_view_visible_listener(
            self._LIVE_VIEW_DETAIL, self._view_visible_listener
        )
        self._view_visible_listener()

    def _view_value_listener( self, value ):
        if value == 127:
            if time.time() - self._time < 0.5:
                # toggle once more to reset the previous toggle
                ViewToggle._view_value_listener( self, value )
                self._live_view.hide_view( self._LIVE_VIEW_DETAIL )
            else:
                self._time = time.time()

                if self._live_view.is_view_visible( self._LIVE_VIEW_DETAIL ):
                    ViewToggle._view_value_listener( self, value )
                else:
                    self._live_view.show_view( self._LIVE_VIEW_DETAIL )

    def _view_visible_listener( self ):
        if self._live_view.is_view_visible( self._LIVE_VIEW_DETAIL ):
            ViewToggle._view_visible_listener( self )
        else:
            self._button.send_value( self._value_hidden )
