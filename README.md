# University Student Record

#### You can follow these steps to run the project:

#### 1. Install the required dependencies: Open a command prompt or terminal window, navigate to the project directory, and run the following command to install all the required Python packages.

``` pip install -r requirements.txt ```


#### 2. Set up the database: Open the project's settings file and enter the database settings to connect with your mySQL database (e.g. the correct database engine, username, password, and database name are specified). Then, run the following command to create the database tables.

```  python manage.py migrate ```


#### 3. Run the development server: In the same terminal window, run the following command to start the development server.The output will say "Starting development server at http://127.0.0.1:8000/".

``` python manage.py runserver```


#### 4. Test the project: Open a web browser and go to the URL " http://127.0.0.1:8000/UniversityRecord/transform_csv/"

#### 5. The following message will appear on your browser: "Data Stored Successfully!"
