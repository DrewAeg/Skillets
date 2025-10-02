import requests


class Step1(CNCPostProcessor):
    """
    This class gets called after the skillet has been executed

    workflow dict is a dictionary containing the variables that were previously submitted by the user
    for the current skillet and all preceding skillets
    """
    def modify_workflow(self, skillet: dict, workflow: dict) -> dict:
        """
        Takes the current skillet and the accumulated workflow and returns the modified workflow
        :param skillet:
        :param workflow:
        :return: modified workflow
        """

        # workflow is the results of the user submitted form
        api_key = workflow.get('api_key', None)
        result = requests.post('something', 'shomething', 'something')
        workflow.set('new_result', result)
        return workflow

    def set_next_skillet(self, skillet: dict, workflow: dict) -> str:
        """
        Takes the current skillet and workflow and determines the name of the next skillet to call
        :param skillet:
        :param workflow:
        :return:
        """

        var1 = workflow.get('var1')
        if var1 < 100:
            return 'skillet3'
        else:
            return 'skillet4'
