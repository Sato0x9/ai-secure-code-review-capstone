from flask import redirect, request

def go():
    url = request.args.get("next")
    return redirect(url)
