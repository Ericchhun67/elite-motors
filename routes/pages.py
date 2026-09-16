"""
routes for the home page and other pages of the Elite Motors Web application
goes here.
"""


from flask import Blueprint, render_template, request
from extensions import db
from models.car_inventory import CarInventory
from car_data import Luxury_cars
from car_data import superCars
from models.employee import Employee
from Employee_data import (
    management_employees,
    sale_team,
    Enginnering_team,
    design_team,
    marketing_team
)

pages_bp = Blueprint('pages', __name__)


# Define routes for the home page
@pages_bp.route('/')
def index():
    """
    Home page route for the Elite Motors web application.
    Returns:
    Rendered Html template for the home page.
    """

    error = None # initialize error variable to None
    # check if error occurred on the page and if there is an error, it will be displayed on the page
    if error:
        # print to the console if there is an error
        print(f"Error occurred: {error}")
        return render_template('index.html', error=error)

    # Use the luxury seed list for this first display example.
    luxury_cars = Luxury_cars

    # Use the super car seed list for this second display example.
    super_cars = superCars

    # render the home page template and return it to the client
    return render_template('index.html',  
            error=error, 
            luxury_cars=luxury_cars, 
            super_cars=super_cars)

@pages_bp.route('/contact')
def contact():
    """
    Contact page route for the Elite Motors web application.
    get error for webpage set to None and if theres an error sent to the console
    and displayed error page.
    returns:
    Rendered html template for the contact page.
    """
    # set error to None to if theres no error
    error = None
    # check if theres an error and print the the console
    if error:
        # print to the console if there is an error
        print(f"Error occured:{error}, 500")
        return render_template('index.html', error=error)
    # render the contact page template and return it to the client
    return render_template('contact.html')


# route for the search bar.
@pages_bp.route('/search')
def search():
    """
    The search page route for the Elite Motors web application
    its purpose is to handle search queries from the user to search for cars in the inventory.
    returns:
    Rendered html template for the search results page.
    """
    error = None
    if error:
        print(f"search error occurred: {error}")
        return render_template('index.html', error=error)
    
    search_query = request.args.get('q', '')  # Get the search query from the URL parameters
    # Perform the search query on the car inventory
    search_results = []
    if search_query:
        search_results = CarInventory.query.filter(
            CarInventory.car_name.ilike(f"%{search_query}%")
        ).all()
    elif not search_results:
        print(f"No results found for search query: {search_query}")

    # render the search results page template and return it to the client
    return render_template('search.html', search_query=search_query, search_results=search_results, error=error)




# route for the about page
@pages_bp.route('/about')
def about():
    error = None
    if error:
        print(f"Error occurred: {error}")
        # check for errors and render the about page with the error message if any
        return render_template('about.html', error=error)
    
    return render_template('about.html')
    


# route for the inventory page to show the cars available in the inventory
@pages_bp.route('/inventory')
def inventory():
    pass



@pages_bp.route('/meet-the-team', methods=['GET'])
def meet_the_team():
    """ 
    Meet the team page route for the Elite Motors web application page.
    Its purpose is to display information about all the team members of Elite Motors
    , including management, sales, engineering, and design teams.
    
    returns:
    Rendered html template for the meet the team page.
    
    """
    
    error = None
    
    
    # debug code
    
    if request.method == 'GET':
        if error:
            print(f"Error occurred: {error}")
            return render_template('index.html', error=error)
        
        ManagementTeam = management_employees
        SalesTeam = sale_team
        EngineeringTeam = Enginnering_team
        DesignTeam = design_team

        ## ----debug code ----
        
        
        return render_template(
            'meet_our_team.html',
            ManagementTeam=ManagementTeam,
            SalesTeam=SalesTeam,
            EngineeringTeam=EngineeringTeam,
            DesignTeam=DesignTeam,
            error=error
        )
        
        
        
# careers page route
@pages_bp.route('/careers', methods=['GET', 'POST'])
def careers():
    """ 
    Careers page route for the Elite Motors web application.
    Its purpose is to display the careers page, including available job positions
    and an application form for job seekers to apply. after submitting the form,
    the application will be reviewed by the HR team and a notification will be 
    sent to the applicant.
    
    check for errors during form submissions.
    
    
    returns:
    Rendered html template for the careers page.
    
    """
    
    error = None
    
    if request.method == 'GET':
        if error:
            print(f"Error occurred: {error}")
            return render_template('careers.html', error=error)
        
        # process the form submission here
        if request.method == 'POST':
            # validate the form and save the data to the database
            form_data = request.form
            # perform validation on form_data
            pass

