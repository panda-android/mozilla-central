from marionette_test import MarionetteTestCase
from errors import JavascriptException, MarionetteException

class TestEmulatorContent(MarionetteTestCase):

    def test_emulator_cmd(self):
        self.marionette.set_script_timeout(10000)
        expected = ["gsm voice state: home",
                    "gsm data state:  home",
                    "OK"]
        result = self.marionette.execute_async_script("""
        runEmulatorCmd("gsm status", marionetteScriptFinished)
        """);
        self.assertEqual(result, expected)

class TestEmulatorChrome(TestEmulatorContent):

    def setUp(self):
        super(TestEmulatorChrome, self).setUp()
        self.marionette.set_context("chrome")
