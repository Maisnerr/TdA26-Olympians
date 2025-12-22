FROM postgres:18

ENV POSTGRES_PASSWORD=heslo

COPY ./initdb /docker-entrypoint-initdb.d

EXPOSE 3005

CMD ["postgres"]