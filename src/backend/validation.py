from enum import Enum
from typing import Union

from pydantic import BaseModel, Field, validator, ValidationError, \
    root_validator, constr, conint, condecimal, conlist


class ActionType(Enum):
    CREATE = 'create'
    DELETE = 'delete'


class Action(BaseModel):
    type: ActionType = Field(alias='action_type')
    user: Union[str, None] = None
    test: constr(min_length=3, max_length=10)
    age: conint(ge=18, lt=30)
    percent: condecimal(ge=0, lt=4)
    guests: conlist(item_type=ActionType, min_items=1)

    @validator('user')
    def user_validator(cls, user: str) -> str:
        if 'A' not in user.lower():
            raise ValueError("No 'A' symbol found")
        return user

    @root_validator
    def check_two_fields(cls, values):
        print("Values: ", values)
        return values


if __name__ == "__main__":

    # language=JSON
    json_action = """
        {
            "action_type": "delete",
            "user": "test"
        }
    """

    try:
        action = Action.parse_raw(json_action)
        print(action.json(by_alias=True, exclude={'user'}))
    except ValidationError as e:
        print("ValidationError: ", e.json())

