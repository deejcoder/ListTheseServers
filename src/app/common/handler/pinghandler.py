from app.http.api.middlewares import login_required, admin_or_owner


class PingHandler:
    @admin_or_owner
    def ping_sync(self, id):
        pass
