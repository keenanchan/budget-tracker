from app.main import bp


@bp.route('/')
@bp.route('/index')
def index():
    return "hello world!"