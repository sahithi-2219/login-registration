from flask import app, render_template
@app.route('/secured_page')
def secured_page():
    return render_template('secured_page.html')
