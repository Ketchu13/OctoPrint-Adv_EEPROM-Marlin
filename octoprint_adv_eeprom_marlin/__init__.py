# coding=utf-8
from __future__ import absolute_import

### (Don't forget to remove me)
# This is a basic skeleton for your plugin's __init__.py. You probably want to adjust the class name of your plugin
# as well as the plugin mixins it's subclassing from. This is really just a basic skeleton to get you started,
# defining your plugin as a template plugin.
#
# Take a look at the documentation on what other plugin mixins are available.

import octoprint.plugin
import octoprint.server

class Eeprom_marlinPlugin(octoprint.plugin.SettingsPlugin,
                          octoprint.plugin.AssetPlugin,
                          octoprint.plugin.TemplatePlugin):
    ##~~ SettingsPlugin mixin

    def get_settings_defaults(self):
        return dict(
            # put your plugin's default settings here
        )

    def get_assets(self):
        # Define your plugin's asset files to automatically include in the
        # core UI here.
        return dict(
            js=["js/adv_eeprom_marlin.js"]
        )

    """def get_template_configs(self):
        return [
            dict(type="settings", template="adv_eeprom_marlin_tab.jinja2", custom_bindings=True)
        ]"""

    ##~~ Softwareupdate hook
    def get_update_information(self):
        return dict(
            adv_eeprom_marlin=dict(
                displayName="Advanced EEPROM Marlin Editor Plugin",
                displayVersion=self._plugin_version,

                # version check: github repository
                type="github_commit",
                user="ketchu13",
                repo="OctoPrint-Adv_EEPROM-Marlin",
                current=self._plugin_version,

                # update method: pip
                pip="https://github.com/ketchu13/OctoPrint-Adv_EEPROM-Marlin/archive/{target_version}.zip"
            )
        )

__plugin_name__ = "Advanced EEPROM"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = Eeprom_marlinPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
