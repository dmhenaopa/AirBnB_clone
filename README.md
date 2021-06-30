# AirBnB Clone - The Console :octocat:

![alt text](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210629%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210629T145543Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d80b99236107d341b9ed5e4b402e20c50d74e517cd1a8d16a64a14501271b823)

Foobar is a Python library for dealing with word pluralization.

### Funcitionalities:

* Create a new object
* Retrieve an object from file, a database
* Update attributes of an object
* Destroy an object

## Table of Content
* Environment
* Installation
* File descriptions
* Usage
* Example of use
* Authors
* License

## Environmente :snake:

This project is interpreted using python3 (version 3.4)

## Installation :rocket:

* Clone this repository: ```https://github.com/stevengm45/AirBnB_clone.git```
* Access AirBnB directory: ```cd AirBnB_Clone```
* Run hbnb (interactively): ```./console``` and enter command

## File descriptions

* ```<emptyline>``` - overwrites default emptyline method and does nothing
* ```EOF``` -  exits console
* ```quit```- exits console
* ```create``` - Create a new instance of BaseModel, saves it to the JSON file
* ```show```- Prints the string representation of an instance based on the class name and id
* ```destroy```- Deletes an instance based on the class name and id save, save the change into the JSON file
* ```all```- Prints all string representation of all instances based or not on the class name
* ```update```- Updates an instance based on the class name and id by adding or updating attribute, save the change into the JSON file
```models/``` directory contans classes used for this project:
base_model.py - The BaseModel class from which future classes will be derived

Classes inherited from BaseModel:
* amenity.py
* city.py
* place.py
* review.py
* state.py
* user.py

```models/engine``` directory contains FileStorage class that handles JSON serialization and deserialization:

```file_storage.py``` - serializes instances to JSON file and deserializes back to instances

```/tests``` dictionary contains all unit test cases for this project:

## Examples of use
```bash
./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) all MyModel
** class doesn´t exist **
(hbnb) create BaseModel
84eb87f8-fe50-43d8-b588-7fca6bb39664
(hbnb) show BaseModel 84eb87f8-fe50-43d8-b588-7fca6bb39664
[BaseModel] (84eb87f8-fe50-43d8-b588-7fca6bb39664) {'id': '84eb87f8-fe50-43d8-b588-7fca6bb39664', 'created_at': datetime.datetime(2021, 6, 29, 22, 8, 22, 541606), 'updated_at': datetime.datetime(2021, 6, 29, 22, 8, 22, 541706)}
(hbnb) update BaseModel 84eb87f8-fe50-43d8-b588-7fca6bb39664 first_Name "Betty"
Betty
(hbnb) show BaseModel 84eb87f8-fe50-43d8-b588-7fca6bb39664
[BaseModel] (84eb87f8-fe50-43d8-b588-7fca6bb39664) {'id': '84eb87f8-fe50-43d8-b588-7fca6bb39664', 'created_at': datetime.datetime(2021, 6, 29, 22, 8, 22, 541606), 'updated_at': datetime.datetime(2021, 6, 29, 22, 8, 22, 541706), 'first_Name': 'Betty'}
(hbnb) destroy BaseModel 84eb87f8-fe50-43d8-b588-7fca6bb39664
(hbnb) show BaseModel 84eb87f8-fe50-43d8-b588-7fca6bb39664
** no instance found **
(hbnb) quit
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


## Authors
Diana Henao - [GitHub](https://github.com/dmhenaopa)

Steven Gonzalez - [GitHub](https://github.com/stevengm45)

## License
Public Domain