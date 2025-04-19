from flask import Flask, request, jsonify

import hashlib


app = Flask(__name__)


VERIFICATION_TOKEN = "zeovant12345capital6789guppypiddy"

ENDPOINT_URL = "https://zeovantcapital.com/ebay-deletion"


@app.route('/ebay-deletion', methods=['GET', 'POST'])

def ebay_deletion():

    challenge_code = request.args.get('challenge_code')


    if challenge_code:

        # Build the SHA-256 hash of: challengeCode + verificationToken + endpoint

        to_hash = challenge_code + VERIFICATION_TOKEN + ENDPOINT_URL

        response_hash = hashlib.sha256(to_hash.encode('utf-8')).hexdigest()


        return jsonify({"challengeResponse": response_hash}), 200


    return VERIFICATION_TOKEN, 200


if __name__ == '__main__':

    app.run()

