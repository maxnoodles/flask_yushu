from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='192.168.2.50', debug=app.config['DEBUG'], threaded=True)


