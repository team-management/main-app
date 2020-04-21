# Dockerization
This is a Docker container with Flask APP and uWSGI

## Installation

```bash

```

## Useful commands
# To create virtual env activate it
python -m venv env

# To activate it
source env/bin/activate

# uWSGI Commands
uwsgi --ini app.ini

# uWSGItop Commands
uwsgi --ini app.ini --stats /tmp/stats.sock
uwsgitop /tmp/stats.sock


## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)