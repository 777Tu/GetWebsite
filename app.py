from flask import *
import requests


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    status= ""
    URL = ""
    if request.method =="POST":
        url= request.form.get("URL-type")
        URL = url
        
        try:
            get_url = requests.get(URL, timeout=5)
            url_status = get_url.status_code
            if url_status == 200:
                status=f"Everything is okey, Status [{url_status}]"
            else:
               status = f"there is problem, Status [{url_status}]"
        except requests.exceptions.ConnectionError:
            status ="Check your internet and try again"
        except requests.exceptions.Timeout:
            status = "Time out, try again"
        except requests.exceptions.RequestException as e:
            status = f"Error [{type(e).__name__}]" 
        
    return render_template("html.html", display_results=status)



if __name__=="__main__":
    app.run(debug=True)
