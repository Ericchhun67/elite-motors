"""
routes for the home page and other pages of the Elite Motors Web application
goes here.
"""


from pathlib import Path
import secrets
from uuid import uuid4

from flask import Blueprint, render_template, request, current_app, flash, redirect, session, url_for
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.exceptions import RequestEntityTooLarge
from werkzeug.utils import secure_filename
from extensions import db
from models.car_inventory import CarInventory
from models.jobApplication import JobApplication
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
from models.jobopening import JobOpening



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

@pages_bp.route('/contact', methods=['GET', 'POST'])
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
    return render_template('contact.html', error=error)


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
    
    return render_template('about.html', error=error)
    


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
    
    
    if request.method == 'GET':
        if error:
            print(f"Error occurred: {error}")
            return render_template('index.html', error=error)
        
        ManagementTeam = management_employees
        SalesTeam = sale_team
        EngineeringTeam = Enginnering_team
        DesignTeam = design_team
        marketingTeam = marketing_team

   
        
        
        return render_template(
            'meet_our_team.html',
            ManagementTeam=ManagementTeam,
            SalesTeam=SalesTeam,
            EngineeringTeam=EngineeringTeam,
            DesignTeam=DesignTeam,
            marketingTeam=marketingTeam,
            error=error
        )
        
        
        
# careers page route
@pages_bp.route('/careers', methods=['GET', 'POST'])
def careers():
    """Show open jobs and save applications submitted through the form."""
    error = None
    status = 200
    form_data = {}
    available_jobs = JobOpening.query.filter_by(jobActive=True).all()

    # The hidden form token helps prevent submissions from another website.
    if 'careers_csrf' not in session:
        session['careers_csrf'] = secrets.token_hex(32)
    csrf_token = session['careers_csrf']

    if not available_jobs:
        error = 'No active job openings available.'

    if request.method == 'POST':
        # 1. Read the form, with a 10 MB upload limit.
        request.max_content_length = current_app.config.get('MAX_CONTENT_LENGTH') or 10 * 1024 * 1024
        try:
            form_data = request.form.to_dict()
        except RequestEntityTooLarge:
            return render_template('career.html', error='Submission too large. Maximum 10 MB.',
                                   available_jobs=available_jobs, form_data={}, csrf_token=csrf_token), 413

        first_name = form_data.get('first_name', '').strip()
        last_name = form_data.get('last_name', '').strip()
        email = form_data.get('email', '').strip()
        phone_number = form_data.get('phone_number', '').strip()
        phone_digits = phone_number
        for character in ('+', '-', '(', ')', ' ', '.'):
            phone_digits = phone_digits.replace(character, '')
        job_id = form_data.get('jobID', '')
        resume = request.files.get('resume')
        cover_letter = request.files.get('cover_letter')

        # 2. Check the required information before saving anything.
        selected_job = None
        if job_id.isascii() and job_id.isdecimal() and len(job_id) <= 18:
            selected_job = db.session.get(JobOpening, int(job_id))

        submitted_token = form_data.get('csrf_token', '')
        if not secrets.compare_digest(submitted_token.encode(), csrf_token.encode()):
            error = 'Refresh the page and submit the form again.'
        elif not first_name or not last_name or not email or not phone_number:
            error = 'Complete all required fields.'
        elif len(first_name) > 50 or len(last_name) > 50 or len(email) > 120 or len(phone_number) > 20:
            error = 'One of your entries is too long.'
        elif email.count('@') != 1 or not email.split('@')[0] or '.' not in email.split('@')[1] or ' ' in email:
            error = 'Enter a valid email address.'
        elif not phone_digits.isascii() or not phone_digits.isdigit():
            error = 'Enter a valid phone number.'
        elif selected_job is None or not selected_job.jobActive:
            error = 'Choose a valid active job opening.'
        elif resume is None or not resume.filename:
            error = 'Resume is required.'
        elif JobApplication.query.filter_by(email=email).first():
            error = 'An application with this email already exists.'
            status = 409

        # A cover letter is optional, so an empty upload becomes None.
        if cover_letter is not None and not cover_letter.filename:
            cover_letter = None

        if error is None:
            for document in (resume, cover_letter):
                if document is None:
                    continue
                extension = Path(secure_filename(document.filename)).suffix.lower()
                if extension not in ('.pdf', '.doc', '.docx'):
                    error = 'Upload PDF, DOC or DOCX documents only.'
                elif not document.stream.read(1):
                    error = 'Uploaded documents must not be empty.'
                document.stream.seek(0)

        # 3. Save the documents privately and keep their paths for the database.
        if error is None:
            upload_folder = Path(current_app.config.get('CAREERS_UPLOAD_ROOT') or Path(current_app.instance_path) / 'uploads')
            file_paths = {'resume': None, 'cover_letter': None}
            saved_files = []
            try:
                for field, document in (('resume', resume), ('cover_letter', cover_letter)):
                    if document is None:
                        continue
                    extension = Path(secure_filename(document.filename)).suffix.lower()
                    filename = uuid4().hex + extension  # A unique name avoids overwriting another file.
                    relative_path = Path('applications') / filename
                    destination = upload_folder / relative_path
                    destination.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
                    with destination.open('xb') as output:
                        saved_files.append(destination)
                        destination.chmod(0o600)
                        document.save(output)
                    file_paths[field] = str(relative_path)

                # 4. Save the application using file paths, not uploaded objects.
                job_application = JobApplication(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone_number=phone_number,
                    jobOpening=selected_job.jobID,
                    resume=file_paths['resume'],
                    cover_letter=file_paths['cover_letter'],
                )
                db.session.add(job_application)
                db.session.commit()
            except (SQLAlchemyError, OSError):
                db.session.rollback()
                for path in saved_files:
                    try:
                        path.unlink(missing_ok=True)
                    except OSError:
                        current_app.logger.error('Could not remove an incomplete application upload.')
                error = 'We could not save your application. Please try again.'
                status = 500
            else:
                flash('Your application was submitted successfully.', 'success')
                return redirect(url_for('pages.careers'), code=303)

        if error and status == 200:
            status = 400

    return render_template('career.html', error=error, available_jobs=available_jobs,
                           form_data=form_data, csrf_token=csrf_token), status
