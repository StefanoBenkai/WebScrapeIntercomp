FROM python:3.8


ADD WebScrapeSqlServer.py .

RUN pip install requests BeautifulSoup4
RUN pip install BeautifulSoup4
RUN pip install pyodbc
RUN pip install datetime

CMD [ "python" , "./WebScrapeSqlServer.py" ]