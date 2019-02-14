FROM python:3.7

# install prerequisites
WORKDIR /code
RUN pip install pipenv
COPY Pipfile ./
RUN pipenv install

WORKDIR /config
ENV MULTINET_SERVER_CONFIG_DIR /config
COPY config .

VOLUME /var/multinet/logs/

WORKDIR /code
COPY multinet-server .
EXPOSE 8080

ENTRYPOINT ["pipenv", "run", "python"]
CMD ["main.py"]
