import requests


class Step1(CNCPostProcessor):
    """
    Allow skillet builders to include a single class that only has one method (post_processor)
    this method gets the results of the skillet and does some additional action if necessary
    This method returns the newly modified 'workflow' dict

    workflow dict is a dictionary containing the variables that were previously submitted by the user
    for the current skillet and all preceding skillets
    """
    def post_processor(self, skillet: dict, workflow: dict) -> dict:

        # workflow is the results of the user submitted form
        api_key = workflow.get('api_key', None)
        result = requests.post('something', 'shomething', 'something')
        workflow.set('new_result', result)
        return workflow
