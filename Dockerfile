FROM python:3.8

ADD WebScraperMySql.py .

RUN pip install requests
RUN pip install BeautifulSoup4
RUN pip install mysql.connector
RUN pip install datetime

CMD [ "python" , "./WebScraperMySql.py" ]