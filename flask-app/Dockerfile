FROM python:3.7.3

COPY /app /usr/src/app
COPY ./requirements.txt /usr/src/app
COPY app/commit /usr/src/app/commit

WORKDIR /usr/src/app

RUN pip install .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5000 available to the world outside this container
# EXPOSE 5000

# Run run.py when the container launches
# ENTRYPOINT ["python"]
# CMD ["run.py"]

# ENTRYPOINT ["python3"]
# run the command to start uWSGI
CMD ["uwsgi", "app.ini"]