from chalice import Chalice

app = Chalice(app_name='chalice-demo')
app.api.cors = True

@app.route('/hello')
def get_hello_world():
    params = app.current_request.query_params or {}
    name = params.get('name', 'world')
    return {'hello': name}

@app.route('/hello/{name}')
def get_hello_name(name):
    return {'hello': name}

@app.route('/hello', methods=['POST'])
def post_hello_name():
    data = app.current_request.json_body or {}
    name = data.get('name', 'world')
    return {'hello': name}
