
class Step1Validator(CNCFormValidator):

    def validate_inputs(self, skillet: dict, workflow: dict) -> dict:
        """
        Takes the current skillet and workflow and performs validation on the user submitted values
        :param skillet: original skillet in dict form
        :param workflow: dict containing all the items the user has entered from the form
        :return: dict containing errors for each item in the workflow
        """
        errors = dict()

        var1 = workflow.get('var1')
        if len(var1) > 64:
            errors[var1] = 'Length is too long, must be shorter than 64 characters'

        return errors

