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

## Using the app
1. To create a plane, use the POST method on `/api/planes/` endpoint and supply the `id` and `passenger` field values in the request body.
    ```sh
    curl -X POST http://localhost:8000/api/planes/ -H "Content-Type: application/json" -d '{"id": 1234, "passengers": 5678}'

    # response
    {"id":1234,"passengers":5678}
    ```
2. To view `total_airplane_fuel_consumption_per_minute` and `maximum_minutes_able_to_fly` information, send a GET request on `/api/planes/` endpoint.
    ```sh
    curl -X GET http://localhost:8000/api/planes/

    # response
    {
        "total_airplane_fuel_consumption_per_minute":13.829052127757778,
        "maximum_minutes_able_to_fly":17846.487070839885,
        "planes":[
            {
                "id":1234,
                "litres":200,
                "passengers":5678,
                "fuel_tank_capacity":246800,
                "plane_fuel_comsumption":2.4730521277577786,
                "passenger_consumption":11.356,
                "total_fuel_consumption":13.829052127757778
            }
        ]
    }
    ```

## API documentation
Interactive API documentation can be accessed through [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/).

## Tests and Test Coverage
Tests can be run using the following command.
```sh
coverage run manage.py test
```
To view the coverage report, use the command below.
```sh
coverage report -m
```