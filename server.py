from flask import Flask, request

import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return '''
       <!DOCTYPE html>
       <html>
       <head>
        <title>Network Tools</title>
       </head>
       <body>
          
          <form action="/ping" method="get">
            <label>Enter IP address to ping:</label><br><br>
            <input type="text" name="command" placeholder="например 8.8.8.8" size="30">
            <input type="submit" value="Ping">
          </form>
       </body>
       </html> 
    '''
@app.route('/ping')
def req():
    param = request.args.get('command',  '')
    
    try:
        res = subprocess.check_output(param, shell=True, text=True)
        return res
    
    except Exception as e: 
        return f"an error: {e}" 
    
if __name__=="__main__":
    app.run(debug=True)
