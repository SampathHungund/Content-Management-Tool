from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    from waitress import serve 
    serve(app, host="0.0.0.0", port=8080)
    
