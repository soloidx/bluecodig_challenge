## Data schema

The data has only one single table with the following schema:

- id: integer (autoincremented) primary
- original_path: string
- unique_code: string (unique)
- count: integer (default is 0)

## Code generation

For the moment the algorithm is converting the primary key into a unique base64 code
this solves almost all of the conflict resolution but this leave a safety issue because is predictable

