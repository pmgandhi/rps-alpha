from claimants_user_journey import routes

if __name__ == '__main__':
    routes.app.run(host='0.0.0.0', port=8000, threaded=True)

