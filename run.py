# Run a test server.
from assess import assess

flask_app = assess.create_app()

flask_app.run(host='0.0.0.0', port=8080, debug=True)
