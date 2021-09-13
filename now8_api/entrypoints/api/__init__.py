"""Module to store the HTTP REST API."""

from typing import Dict

from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.responses import ORJSONResponse
from now8_api.service.service import Cities, get_estimations

api = FastAPI(default_response_class=ORJSONResponse)

# internal functions


def _return_msg(msg: str, key: str = "msg") -> Dict[str, str]:
    """Return a dictionary with the provided string.

    As the value of the provided key.

    Arguments:
        msg: Message to wrap with the dictionary.
        key: Dictionary key to store the `msg` at.

    Returns:
        Resulting dictionary: `{key: msg}`.
    """
    return {key: msg}


# ROUTES


@api.get("/{city_name}/get_estimations")
async def get_estimations_api(
    city_name: Cities = Cities.MADRID, stop_id: str = "17491"
):
    """Return ETA for the next vehicles to the stop.

    - **city_name**: City name.
    - **stop_id**: Stop identifier.
    """
    try:
        result = await get_estimations(city_name=city_name, stop_id=stop_id)
    except NotImplementedError as error:
        raise HTTPException(
            404, "Can't get estimations for the given stop in the given city."
        ) from error

    return result
