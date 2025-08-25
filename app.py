from flask import *
import requests
import socket
from urllib.parse import urlparse


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    status= ""
    URL = ""
#    if 'X-Forwarded-For' in request.headers:
#        user_ip = request.headers['X-Forwarded-For']
#        split(',')[0].strip()
#    else:
    user_ip = request.remote_addr
    my_ip=(f"My:__ {user_ip}")
    url_ip = ""
    if request.method =="POST":
        url= request.form.get("URL-type")
        URL = url 
        try:
            get_url = requests.get(URL, timeout=5)
            url_status = get_url.status_code
            if url_status == 200:
                status=f"🟢 [{type(url_status).__name__}]"
                clean_url = urlparse(URL)
                domain = clean_url.netloc
                url_ip = f"Link:__ {socket.gethostbyname(domain)}"
            else:
               status = f"📍[{type(url_status).__name__}]"
        except socket.gaierror:
            url_ip = "📍 Unavailable, Try again"
        except requests.exceptions.ConnectionError:
            status =f"⚙️ Check your internet and try again"
        except requests.exceptions.Timeout:
            status = f"⏰ Time out, try again"
        except requests.exceptions.RequestException as e:
            status = f"📍 [{type(e).__name__}]" 
        
    return render_template("html.html", display_results=status,ip=url_ip, user_ip=my_ip,en_url="🔗" + URL)



if __name__=="__main__":
    app.run(debug=True)
