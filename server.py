from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/play')                           
def three_and_blue_boxes():
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html', number=3, color='blue')  

@app.route('/play/<int:number>')                           
def blue_boxes(number):
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html', number=number, color='blue')  

@app.route('/play/<int:number>/<string:color>')                           
def number_and_color_boxes(number, color):
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html', number=number, color=color)  
    
if __name__=="__main__":
    app.run(debug=True)    