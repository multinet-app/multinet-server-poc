FROM python:3.6

# install prerequisites
WORKDIR /code
RUN pip install pipenv
COPY Pipfile ./
RUN pipenv install

WORKDIR /etc/multinet
ENV MULTINET_SERVER_CONFIG_DIR /etc/multinet
COPY config .

VOLUME /var/multinet/logs/

WORKDIR /code
COPY multinet-server .
EXPOSE 8080

ENTRYPOINT ["pipenv", "run", "python"]
CMD ["main.py"]
