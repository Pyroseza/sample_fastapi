FROM python:3.8

RUN pip install pipenv

ADD Pipfile .
RUN pipenv check
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt


COPY entrypoint .
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint

COPY start .
RUN sed -i 's/\r//' /start
RUN chmod +x /start


WORKDIR /usr/src/server
ENTRYPOINT ["/entrypoint"]
