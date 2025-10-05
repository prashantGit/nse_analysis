from flask import Flask, render_template, request, redirect
from breeze_connect import BreezeConnect
import app_config
import urllib
import analysis

app = Flask(__name__)

# Initialize the BreezeConnect SDK
breeze = BreezeConnect(api_key=app_config.API_KEY)

@app.route('/')
def index():
    # Check if the user is authenticated
    if hasattr(breeze, 'session_key'):
        try:
            # Fetch portfolio holdings
            portfolio = breeze.get_portfolio_holdings(exchange_code="NSE")
            if portfolio['Success']:
                for holding in portfolio['Success']:
                    moving_averages = analysis.calculate_moving_averages(breeze, holding['stock_code'])
                    holding['moving_averages'] = moving_averages
            return render_template('index.html', portfolio=portfolio)
        except Exception as e:
            return f"An error occurred: {e}"
    else:
        # If not authenticated, redirect to the login page
        return redirect('/login')

@app.route('/login')
def login():
    # Redirect the user to the ICICI Direct login page
    login_url = f"https://api.icicidirect.com/apiuser/login?api_key={urllib.parse.quote_plus(app_config.API_KEY)}"
    return redirect(login_url)

@app.route('/callback')
def callback():
    session_token = request.args.get('api_session')
    if session_token:
        try:
            # Generate the session using the session token and API secret
            breeze.generate_session(api_secret=app_config.API_SECRET, session_token=session_token)
            return redirect('/')
        except Exception as e:
            return f"An error occurred during session generation: {e}"
    return "Authentication failed."

if __name__ == '__main__':
    # Make sure to use a port that matches the redirect URL you configured.
    app.run(debug=True, port=5000, use_reloader=False)