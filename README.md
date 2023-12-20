# airplanes
Aircraft Passenger Capacity Consumption API

## Environment Variables
The following environment variables are required to run the app.
- DEV_SECRET_KEY
- DATABASE_URL

## Running the app

1. Clone the repo.
    ```sh
    git clone git@github.com:sitati-elsis/airplanes.git
    ```
2. `cd` into the repo you have just cloned.
    ```sh
    cd airplanes/
    ```
3. Create a virtual environment and activate it.
4. Inside the virtual environment, install app dependencies.
    ```sh
    pip install -r requirements.txt
    ```
5. Start the app.
    ```sh
    python manage.py runserver
    ```
