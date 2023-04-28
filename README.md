## Data schema

The data has only one single table with the following schema:

- id: integer (autoincremented) primary
- original_path: string
- unique_code: string (unique)
- count: integer (default is 0)

## Code generation

For the moment the algorithm is converting the primary key into a unique base64 code
this solves almost all of the conflict resolution but this leave a safety issue because is predictable


## Usage:

### Local development

You will need to install poetry, after have the poetry virtual environment installed you can run:

```bash
python manage.py runserver
```

In order to run the application


When you need to run the background application for analysis, you can use the command:

```bash
python manage.py analyze
```

This command will run and get the missing titles from the pages


### Docker application

For docker, you can just run a `docker-compose up` and you will have all the environment installed

