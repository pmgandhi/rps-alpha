import inspect

class TestableWebForm(object):
    """
    This class abstracts the webdriver code for filling up
    forms away from the feature tests.

    set_input(input_name, value)

    This method will look for a method on the child class
    with the same name as the input_name and invoke it with 
    the provided value. If no method is found it assumes 
    that the input is a text box and tries to fill it out
    with the provided value.

    submit()

    Submits the form
    """

    def __init__(self, browser):
        self._browser = browser

    def set_input(self, input_name, value):
        method_for_filling_input = getattr(self, input_name, None)
        if inspect.ismethod(method_for_filling_input):
            method_for_filling_input(value)
        else:
            self._fill_text_input(input_name, value)

    def _fill_text_input(self, input_name, text):
        self._browser.find_by_name(input_name).fill(text)

    def submit(self):
        self._browser.find_by_css('input[type=submit]').click()


class ClaimantsDetailsForm(TestableWebForm):
    def __init__(self, browser):
        super(ClaimantsDetailsForm, self).__init__(browser)

    def title(self, selection):
        """
        Logic for dealing with the title drop-down box, everything
        else is a text box and can be left to the default behaviour
        of TestableWebForm
        """
        self._browser.find_by_name('title').select(selection)
        return self

