# Import modules
from flask import Flask, render_template, request

# Import custom module
from api import cryptocurrency, filter_cryptocurrency, sort_cryptocurrency

# Initialise Flask App
app = Flask(__name__)

# Route to render the data in HTML template
@app.route('/')
def index():
    # Get API data
    api_data = cryptocurrency.get_api_data()

    # Get action parameter
    action = request.args.get('action')

    if action:
        if action == 'sort':
            # Get sort_by parameter, default is 'name'
            sort_by = request.args.get('sort_by', 'name')
            # Get sort_order parameter, default is ascending
            sort_order = request.args.get('sort_order', 'asc')

            # Sort the data
            api_data = sort_cryptocurrency(api_data,
                                           sort_by,
                                           True if sort_order == 'desc' else False)
        elif action == 'filter':
            # Get filtering parameters
            filter_by = request.args.get('filter_by')
            filter_value = request.args.get('filter_value')

            # Apply filtering if filter parameters are provided
            if filter_by and filter_value:
                api_data = filter_cryptocurrency(api_data, filter_by, filter_value)

    # Render template
    return render_template('index.html', items=api_data)

# Run application
if __name__ == '__main__':
    app.run(debug=True)
