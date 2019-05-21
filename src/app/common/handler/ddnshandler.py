import json
from app.http.api.middlewares import login_required, admin_or_owner, current_user_is_admin
from app.servers.models import Server, ServerActivity


class DDnsHandler:
    @admin_or_owner
    def add(self, id, ddnsinfo):
        pass

    @admin_or_owner
    def delete(self, id):
        pass

    @admin_or_owner
    def update(self, id, ddnsinfo):
        pass

    @admin_or_owner
    def get_owned(self):
        pass

    @login_required
    def get_all(self):
        # admin only
        if not current_user_is_admin():
            return json.dumps({'error': 'insufficient permission'}), 403, {'Content-type': 'application/json'}
        else:
            pass
