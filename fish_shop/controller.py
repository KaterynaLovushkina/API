from main import app
@app.route('/')
def index():
    return "Hoorey!"

@app.route('/fish/{id}')
def get_fish(id):
    print(id)
    return 'my fish is yammy'

@app.route('/fish', methods=["GET"])
def get_fish():
    return "get all fish"

@app.route('/fish', methods=["POST"])
def post_fish():
    print("fish is posted")