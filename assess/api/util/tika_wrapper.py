from flask import current_app

from tika import parser

def parse_from_buffer(buf):
    tika_uri = current_app.config['TIKA_URI']

    return parser.from_buffer(buf, tika_uri)
