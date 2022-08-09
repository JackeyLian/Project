from project import get_user_tz, get_user_task, create_to_do_list
from _pytest.monkeypatch import MonkeyPatch
from pytest import raises

class TestFunctions():
    def setup(self):
        self.monkeypatch = MonkeyPatch()

    def test_get_user_tz(self):
        self.monkeypatch.setattr('builtins.input', lambda _: "America/Los_Angeles")
        output = get_user_tz()
        # Tests if output is correctly outputed with the current user's timezone
        assert output == output

    def test_get_user_tz_invalid(self):
        with raises(SystemExit):
            # Exceeds max attempts and system exits due to misuse usage
            self.monkeypatch.setattr("builtins.input", lambda _: "Invalid Input")
            # Enters loop
            get_user_tz()

    def test_create_to_do_list(self):
        create_to_do_list()

    
