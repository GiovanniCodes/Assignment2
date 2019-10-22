# Assignment2
Open the command line and open folder containing repository <br />
## Run the following Commands: <br />
* pip install --user -r req.txt <br />
* docker-compose up <br />

## Then run the files needed(In another Terminal) <br />
* python Assignment2.py <br />
* python Assignment2_test_doubles.py <br />
* python flask_python.py </br>
(Go to localhost:5000/retirement or localhost:5000/distance to either GET/POST, GET retrieves values stored from running Assignment2 and POST just return that you attempted to POST information) <br />
* python flask_unit_test.py <br />
## To check for persistence </br>
* Run docker-compose down (This will close the container and destroy everything but the volume stored)</br>
* Run docker-compose up and check if the test and files still run. See if your data is still being printed.
