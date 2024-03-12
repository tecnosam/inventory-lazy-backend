from fastapi import (
    APIRouter,
    Query,
    Depends
)


from app.controllers.users import (
    login,
    register_user,
    update_user,
    get_user
)

from app.dependencies import (
    get_user_id,
    get_sudo_id
)


from app.models.forms import (
    LoginForm,
    CreateUser,
    UpdateProfile
)

from app.models.responses import (
    AuthResponse,
    UserResponse,
    BaseResponse
)

router = APIRouter(prefix='/api/auth', tags=['Authentication'])


@router.post("/login", response_model=AuthResponse)
def login_route(
    form: LoginForm,
    sudo_mode: bool = Query(default=False)
):

    data = form.model_dump()

    response = login(**data, sudo_mode=sudo_mode)
    return BaseResponse.cook(data=response)


@router.get("/me", response_model=UserResponse)
def get_user_route(
    user_id: int = Depends(get_user_id)
):

    user = get_user(user_id)

    response = BaseResponse.cook(data=user)

    print("Response", response)
    return response


@router.post("/add-user", response_model=BaseResponse)
def register_user_route(
    form: CreateUser,
    _: int = Depends(get_sudo_id)
):

    data = form.model_dump()

    response = register_user(**data)
    return BaseResponse.cook()


@router.put("/update-user", response_model=BaseResponse)
def update_user_route(
    form: UpdateProfile,
    user_id: int = Depends(get_user_id)
):

    data = form.model_dump(
        exclude_none=True,
        exclude_unset=True
    )

    update_user(user_id, data)
    return BaseResponse.cook()
