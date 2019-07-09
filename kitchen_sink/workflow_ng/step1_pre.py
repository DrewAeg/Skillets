

class Step1Pre(CNCPreProcessor):
    """
    Pre-Processor is a Class that implements 3 methods

    These methods can influence what fields are shown / hidden / and their default values
    """
    def set_fields_to_show(self, skillet: dict, workflow: dict) -> (list, None):
        """
        Takes the current skillet and workflow and determines which fields to show on the form
        :param skillet:
        :param workflow:
        :return: list of variable names to show - defaults to all
        """
        pass

    def set_fields_to_hide(self, skillet: dict, workflow: dict) -> (list, None):
        """
        Takes the current skillet and workflow and determines which fields to hide on the form
        :param skillet:
        :param workflow:
        :return: list of variable names to hide - defaults to None
        """
        pass

    def set_field_values(self, skillet: dict, workflow: dict) -> dict:
        """
        Takes the current skillet and workflow and modifies the variables. This can be useful to re-assign default
        values, query an API to get an Auth-Key, query an API to get a list of values to set on a dropdown, etc
        :param skillet:
        :param workflow:
        :return: dict of variables definitions
        """
        pass

