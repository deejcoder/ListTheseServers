from factory import Factory


factory = Factory('app', True)
app = factory.get_app()
app.run()
