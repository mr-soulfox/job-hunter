from requests import Response


def verify_if_exist(res: Response) -> bool:
    if str(res.status_code) == "200":
        return True

    return False
