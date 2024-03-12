from fastapi import HTTPException


class AppException(Exception):

    def __init__(self, msg, code=400, *args, **kwargs):

        super().__init__(msg, code, *args, **kwargs)

        self.msg = msg
        self.code = code


class EntityNotFoundException(AppException):

    msg = "Entity not found in database!"
    code = 404

    def __init__(self, msg=None, code=None, *args, **kwargs):

        if msg is None:
            msg = self.msg

        code = self.code
        super().__init__(msg, code, *args, **kwargs)


class EntityExistsException(EntityNotFoundException):

    msg = "Entity with this attribute already exists!"
    code = 400
