#!/usr/bin/env python3

from flask import Flask, request, jsonify, make_response, session

app = Flask(__name__)

# REQUIRED for sessions to work
app.secret_key = "super-secret-key"

@app.get("/")
def index():
    return {"message": "API running"}, 200


@app.route("/sessions/<string:key>", methods=["GET"])
def show_session(key):
    # Set session values if they do not exist
    session["hello"] = session.get("hello") or "World"
    session["goodnight"] = session.get("goodnight") or "Moon"

    response = make_response(
        jsonify(
            {
                "session": {
                    "session_key": key,
                    "session_value": session.get(key),
                    "session_accessed": session.accessed,
                },
                "cookies": [
                    {cookie: request.cookies[cookie]}
                    for cookie in request.cookies
                ],
            }
        ),
        200,
    )

    # Set a normal cookie
    response.set_cookie("mouse", "Cookie")

    return response


if __name__ == "__main__":
    app.run(port=5555, debug=True)
