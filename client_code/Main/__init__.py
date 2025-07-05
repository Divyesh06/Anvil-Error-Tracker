from ._anvil_designer import MainTemplate
import anvil.server
from anvil import alert
from .. import Globals
import anvil.tz
import anvil.users

class Main(MainTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        anvil.users.login_with_form(show_signup_option= True)
        self.layout.show_sidesheet = False
        print("Done")
        self.refresh_errors_count()

    def refresh_errors_count(self):
        self.all_errors, self.new_errors, self.reappeared_errors, last_opened, app_id = anvil.server.call('get_errors_init')
        Globals.last_opened = last_opened
        Globals.app_id = app_id
        self.alL_errors_count.text = self.all_errors
        self.new_errors_count.text = self.new_errors
        self.reappeared_errors_count.text = self.reappeared_errors

    def refresh(self):
        self.refresh_errors_count()
        self.errors_displayer.refresh_errors()
        
    def form_show(self, **event_args):
        self.errors_displayer.refresh_errors()

    def icon_button_1_click(self, **event_args):
        self.layout.show_sidesheet = False

    def merge_btn_click(self, **event_args):
        from ..ErrorsDisplayer import ErrorsDisplayer
        alert(ErrorsDisplayer(for_merge = True), title= "Merge Errors", large = True)