# AirBnB Clone
![hbnb](https://user-images.githubusercontent.com/88311316/151070609-19608294-829e-408b-b2b3-5d1f2873f1e3.png)


## Project Description
This is the first part of the AirBnB clone project divided into 3 parts:
	*Backend
	*Frontend
	*Storage

The complete product will have:

**1.  A command interpreter to manipulate data without a visual interface, like a shell (for development and debugging)**
</br>
**2.  A website (front-end) with static and dynamic functionalities**
</br>
**3.  A comprehensive database to manage the backend functionalities**
</br>
**4.  An API that provides a communication interface between the front and backend of the system.**
</br>
**5.  General concepts in review**
</br>
### As you navigate this code base, it is great to note the following concepts, while completing this project;
<h4> How to create a Python package </h4>
<h4> How to create a command interpreter in Python using the cmd module </h4>
<h4> What is Unit testing and how to implement it in a large project </h4>
<h4> How to serialize and deserialize a Class </h4>
<h4> How to write and read a JSON file </h4>
<h4> How to manage datetime <h4>
<h4> What is an UUID <h4>
<h4> What is *args and how to use it <h4>
<h4> What is **kwargs and how to use it <h4>
<h4> How to handle named arguments in a function </h4>


## Files and Directories
- ```models``` directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
- ```tests``` directory will contain all unit tests.
- ```console.py``` file is the entry point of our command interpreter.
- ```models/base_model.py``` file is the base class of all our models. It contains common elements:
    - attributes: ```id```, ```created_at``` and ```updated_at```
    - methods: ```save()``` and ```to_json()```
- ```models/engine``` directory will contain all storage classes (using the same prototype). For the moment I will have only one: ```file_storage.py```.

## Description of the command interpreter:
The interface of the application is just like the Bash shell except that this has a limited number of accepted commands that were solely defined for the purposes of the usage of the AirBnB website.

This command line interpreter  serves as the frontend of the web app where users can interact with the backend which was developed with python OOP programming.

Some of the commands available are:
- show
- create
- update
- destroy
- count

And as part of the implementation of the command line interpreter coupled with the backend and file storage system, the folowing actions can be performed:
-   Creating new objects (ex: a new User or a new Place)
-   Retrieving an object from a file, a database etc…
-   Doing operations on objects (count, compute stats, etc…)
-   Updating attributes of an object
-   Destroying an object



## Repo Contents :clipboard:
This repository constains the following files:

|   **File**   |   **Description**   |
| -------------- | --------------------- |
|[AUTHORS](./AUTHORS) | Contains info about authors of the project |
|[base_model.py](./models/base_model.py) | Defines BaseModel class (parent class), and methods |
|[user.py](./models/user.py) | Defines subclass User |
|[amenity.py](./models/amenity.py) | Defines subclass Amenity |
|[city.py](./models/city.py)| Defines subclass City |
|[place.py](./models/place.py)| Defines subclass Place |
|[review.py](./models/review.py) | Defines subclass Review |
|[state.py](./models/state.py) | Defines subclass State |
|[file_storage.py](./models/engine/file_storage.py) | Creates new instance of class, serializes and deserializes data |
|[console.py](./console.py) | creates object, retrieves object from file, does operations on objects, updates attributes of object and destroys object |
|[test_base_model.py](./tests/test_models/test_base_model.py) | unittests for base_model |
|[test_user.py](./tests/test_models/test_user.py) | unittests for user |
|[test_amenity.py](./tests/test_models/test_amenity.py) | unittests for amenity |
|[test_city.py](./tests/test_models/test_city.py) | unittests for city |
|[test_place.py](./tests/test_models/test_place.py) | unittests for place |
|[test_review.py](./tests/test_models/test_review.py) | unittests for review |
|[test_state.py](./tests/test_models/test_state.py) | unittests for state |
|[test_file_storage.py](./tests/test_models/test_engine/test_file_storage.py) | unittests for file_storage |
|[test_console.py](./tests/test_console.py) | unittests for console |


 ## Installation
Clone the repository and run the console.py
```
$ git clone ...
```

## Usage

|   **Method**   |   **Description**   |
| -------------- | --------------------- |
|[create](./console.py) | Creates object of given class |
|[show](./console.py) | Prints the string representation of an instance based on the class name and id |
|[all](./console.py) | Prints all string representation of all instances based or not on the class name |
|[update](./console.py) | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) |
|[destroy](./console.py)| Deletes an instance based on the class name and id (save the change into the JSON file) |
|[count](./console.py)| Retrieve the number of instances of a class |
|[help](./console.py)| Prints information about specific command |
|[quit/ EOF](./console.py)| Exit the program |


## CODESMITHS
 Zahra Jalalkhan
 Kibet Richard
