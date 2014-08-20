class NoSchemaException(Exception):
    def __init__(self):
        super(NoSchemaException, self).__init__("You have not defined a schema. You must overload the 'schema' method.")


class NoErrorDictionaryDefined(Exception):
    def __init__(self):
        super(NoErrorDictionaryDefined, self).__init__("You have not defined the method error_dictionary")


class ErrorMessageNotDefined(Exception):
    def __init__(self):
        super(ErrorMessageNotDefined, self).__init__("You have not defined the method error_message")


class DataDoesNotMatchSchemaException(Exception):
    def __init__(self, cause=None, field_errors=None):
        super(self.__class__, self).__init__(cause.message + ', caused by ' + repr(cause))
        self.cause = cause

        if field_errors is None:
            self.field_errors = []
        else:
            self.field_errors = field_errors

    def __repr__(self):
        return self.__class__.__name__ + ' errors:' + repr(self.field_errors) + ' caused by:' + repr(self.cause)

    def __str__(self):
        return self.__repr__()

