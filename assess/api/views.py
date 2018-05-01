from assess import assess

from . import api

from flask import json, request, flash
from tika import parser

from .util import predict_standards
from .util import tika_wrapper

@api.route('/predict/', methods=('GET', 'POST'))
def predict():
    if request.method == 'GET':
        # GET
        text = request.args.get('text')

        parsed = tika_wrapper.parse_from_buffer(text) 

    else:
        # POST
        if 'file' not in request.files:
            return 'no file in request!' #TODO

        f = request.files['file']
        if f.filename == '':
            return 'no selected file!' #TODO
        if f:
            parsed = tika_wrapper.parse_from_buffer(f.read()) 

    result = predict_standards.predict()

    return json.dumps(result)
