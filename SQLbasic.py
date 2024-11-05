{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e675d191-542d-4223-a124-f48761de49ab",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: ipython-sql in /opt/conda/lib/python3.10/site-packages (0.5.0)\n",
      "Requirement already satisfied: ipython-genutils in /opt/conda/lib/python3.10/site-packages (from ipython-sql) (0.2.0)\n",
      "Requirement already satisfied: ipython in /opt/conda/lib/python3.10/site-packages (from ipython-sql) (8.11.0)\n",
      "Requirement already satisfied: sqlalchemy>=2.0 in /opt/conda/lib/python3.10/site-packages (from ipython-sql) (2.0.7)\n",
      "Requirement already satisfied: prettytable in /opt/conda/lib/python3.10/site-packages (from ipython-sql) (3.7.0)\n",
      "Requirement already satisfied: six in /opt/conda/lib/python3.10/site-packages (from ipython-sql) (1.16.0)\n",
      "Requirement already satisfied: sqlparse in /opt/conda/lib/python3.10/site-packages (from ipython-sql) (0.4.4)\n",
      "Requirement already satisfied: typing-extensions>=4.2.0 in /opt/conda/lib/python3.10/site-packages (from sqlalchemy>=2.0->ipython-sql) (4.5.0)\n",
      "Requirement already satisfied: greenlet!=0.4.17 in /opt/conda/lib/python3.10/site-packages (from sqlalchemy>=2.0->ipython-sql) (2.0.2)\n",
      "Requirement already satisfied: pickleshare in /opt/conda/lib/python3.10/site-packages (from ipython->ipython-sql) (0.7.5)\n",
      "Requirement already satisfied: backcall in /opt/conda/lib/python3.10/site-packages (from ipython->ipython-sql) (0.2.0)\n",
      "Requirement already satisfied: pexpect>4.3 in /opt/conda/lib/python3.10/site-packages (from ipython->ipython-sql) (4.8.0)\n",
      "Requirement already satisfied: pygments>=2.4.0 in /opt/conda/lib/python3.10/site-packages (from ipython->ipython-sql) (2.14.0)\n",
      "Requirement already satisfied: jedi>=0.16 in /opt/conda/lib/python3.10/site-packages (from ipython->ipython-sql) (0.18.2)\n",
      "Requirement already satisfied: prompt-toolkit!=3.0.37,<3.1.0,>=3.0.30 in /opt/conda/lib/python3.10/site-packages (from ipython->ipython-sql) (3.0.38)\n",
      "Requirement already satisfied: traitlets>=5 in /opt/conda/lib/python3.10/site-packages (from ipython->ipython-sql) (5.9.0)\n",
      "Requirement already satisfied: stack-data in /opt/conda/lib/python3.10/site-packages (from ipython->ipython-sql) (0.6.2)\n",
      "Requirement already satisfied: matplotlib-inline in /opt/conda/lib/python3.10/site-packages (from ipython->ipython-sql) (0.1.6)\n",
      "Requirement already satisfied: decorator in /opt/conda/lib/python3.10/site-packages (from ipython->ipython-sql) (5.1.1)\n",
      "Requirement already satisfied: wcwidth in /opt/conda/lib/python3.10/site-packages (from prettytable->ipython-sql) (0.2.6)\n",
      "Requirement already satisfied: parso<0.9.0,>=0.8.0 in /opt/conda/lib/python3.10/site-packages (from jedi>=0.16->ipython->ipython-sql) (0.8.3)\n",
      "Requirement already satisfied: ptyprocess>=0.5 in /opt/conda/lib/python3.10/site-packages (from pexpect>4.3->ipython->ipython-sql) (0.7.0)\n",
      "Requirement already satisfied: executing>=1.2.0 in /opt/conda/lib/python3.10/site-packages (from stack-data->ipython->ipython-sql) (1.2.0)\n",
      "Requirement already satisfied: pure-eval in /opt/conda/lib/python3.10/site-packages (from stack-data->ipython->ipython-sql) (0.2.2)\n",
      "Requirement already satisfied: asttokens>=2.1.0 in /opt/conda/lib/python3.10/site-packages (from stack-data->ipython->ipython-sql) (2.2.1)\n",
      "\u001b[33mWARNING: There was an error checking the latest version of pip.\u001b[0m\u001b[33m\n",
      "\u001b[0m"
     ]
    }
   ],
   "source": [
    "!pip install ipython-sql"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d74467cc-ab48-4546-867a-19fadb488909",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "%load_ext sql"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a6571312-c02f-444d-ab3f-7e44fc1bfa40",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "POSTGRESQL_USER=reader\n",
      "POSTGRESQL_PASSWORD=Miba2021\n"
     ]
    }
   ],
   "source": [
    "!env | grep POST"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "2c3f39c0-e2eb-42e2-ad23-c8b5d84bc2cf",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import os\n",
    "USER = os.environ['POSTGRESQL_USER']\n",
    "PASSWORD = os.environ['POSTGRESQL_PASSWORD']\n",
    "POSTGRESQL_HOST = '10.129.0.25'\n",
    "DBASE_NAME = 'demo'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f3e53d6e-f058-47dd-96a0-366fc7703fa3",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "CONNECT_DATA = 'postgresql://{}:{}@{}/{}'.format(\n",
    "    USER,\n",
    "    PASSWORD,\n",
    "    POSTGRESQL_HOST,\n",
    "    DBASE_NAME\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "247e017d-9aeb-488a-b9f4-73e239612f41",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The sql extension is already loaded. To reload it, use:\n",
      "  %reload_ext sql\n"
     ]
    }
   ],
   "source": [
    "%load_ext sql"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "9dfa06ce-0493-47ff-886f-7dce82f88d15",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7 rows affected.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<table>\n",
       "    <thead>\n",
       "        <tr>\n",
       "            <th>arrival_airport</th>\n",
       "            <th>aircraft_code</th>\n",
       "        </tr>\n",
       "    </thead>\n",
       "    <tbody>\n",
       "        <tr>\n",
       "            <td>AER</td>\n",
       "            <td>773</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>AER</td>\n",
       "            <td>733</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>AER</td>\n",
       "            <td>763</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>AER</td>\n",
       "            <td>CN1</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>AER</td>\n",
       "            <td>SU9</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>AER</td>\n",
       "            <td>CR2</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>AER</td>\n",
       "            <td>319</td>\n",
       "        </tr>\n",
       "    </tbody>\n",
       "</table>"
      ],
      "text/plain": [
       "[('AER', '773'),\n",
       " ('AER', '733'),\n",
       " ('AER', '763'),\n",
       " ('AER', 'CN1'),\n",
       " ('AER', 'SU9'),\n",
       " ('AER', 'CR2'),\n",
       " ('AER', '319')]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%sql $CONNECT_DATA\n",
    "\n",
    "SELECT DISTINCT arrival_airport, aircraft_code \n",
    "FROM Flights AS f\n",
    "WHERE f.arrival_airport='AER'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "26354795-a09c-486a-aa57-137dcae17366",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * postgresql://reader:***@10.129.0.25/demo\n",
      "5 rows affected.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<table>\n",
       "    <thead>\n",
       "        <tr>\n",
       "            <th>arrival_airport</th>\n",
       "            <th>aircraft_code</th>\n",
       "        </tr>\n",
       "    </thead>\n",
       "    <tbody>\n",
       "        <tr>\n",
       "            <td>AER</td>\n",
       "            <td>773</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>AER</td>\n",
       "            <td>CN1</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>AER</td>\n",
       "            <td>763</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>AER</td>\n",
       "            <td>763</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>AER</td>\n",
       "            <td>763</td>\n",
       "        </tr>\n",
       "    </tbody>\n",
       "</table>"
      ],
      "text/plain": [
       "[('AER', '773'),\n",
       " ('AER', 'CN1'),\n",
       " ('AER', '763'),\n",
       " ('AER', '763'),\n",
       " ('AER', '763')]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%sql\n",
    "\n",
    "SELECT arrival_airport, aircraft_code \n",
    "FROM Flights AS f\n",
    "WHERE f.arrival_airport='AER'\n",
    "LIMIT 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "df0ecd2d-7a59-434b-b64d-164d50fef39e",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * postgresql://reader:***@10.129.0.25/demo\n",
      "3 rows affected.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<table>\n",
       "    <thead>\n",
       "        <tr>\n",
       "            <th>fare_conditions</th>\n",
       "        </tr>\n",
       "    </thead>\n",
       "    <tbody>\n",
       "        <tr>\n",
       "            <td>Business</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>Comfort</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>Economy</td>\n",
       "        </tr>\n",
       "    </tbody>\n",
       "</table>"
      ],
      "text/plain": [
       "[('Business',), ('Comfort',), ('Economy',)]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%sql\n",
    "\n",
    "SELECT DISTINCT fare_conditions\n",
    "FROM Ticket_flights\n",
    "WHERE flight_id IN (\n",
    "    SELECT flight_id\n",
    "    FROM Flights\n",
    "    WHERE departure_airport = 'AER' AND arrival_airport = 'SVO'\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "cfcb0380-2680-455f-96eb-2a6cb7b3dc94",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * postgresql://reader:***@10.129.0.25/demo\n",
      "1 rows affected.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<table>\n",
       "    <thead>\n",
       "        <tr>\n",
       "            <th>model</th>\n",
       "        </tr>\n",
       "    </thead>\n",
       "    <tbody>\n",
       "        <tr>\n",
       "            <td>Airbus A319-100</td>\n",
       "        </tr>\n",
       "    </tbody>\n",
       "</table>"
      ],
      "text/plain": [
       "[('Airbus A319-100',)]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%sql\n",
    "\n",
    "SELECT DISTINCT model\n",
    "FROM Aircrafts\n",
    "WHERE aircraft_code IN (\n",
    "    SELECT aircraft_code\n",
    "    FROM Flights\n",
    "    WHERE arrival_airport IN (\n",
    "        SELECT airport_code\n",
    "        FROM Airports\n",
    "        WHERE city = 'Yakutsk'\n",
    "    )\n",
    ")\n",
    "AND aircraft_code IN (\n",
    "    SELECT aircraft_code\n",
    "    FROM Flights\n",
    "    WHERE arrival_airport IN (\n",
    "        SELECT airport_code\n",
    "        FROM Airports\n",
    "        WHERE city = 'Abakan'\n",
    "    )\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "ecbe43c9-1630-4878-8778-0cbf7da6fe2b",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * postgresql://reader:***@10.129.0.25/demo\n",
      "5 rows affected.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<table>\n",
       "    <thead>\n",
       "        <tr>\n",
       "            <th>model</th>\n",
       "        </tr>\n",
       "    </thead>\n",
       "    <tbody>\n",
       "        <tr>\n",
       "            <td>Airbus A319-100</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>Boeing 737-300</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>Bombardier CRJ-200</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>Cessna 208 Caravan</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>Sukhoi Superjet-100</td>\n",
       "        </tr>\n",
       "    </tbody>\n",
       "</table>"
      ],
      "text/plain": [
       "[('Airbus A319-100',),\n",
       " ('Boeing 737-300',),\n",
       " ('Bombardier CRJ-200',),\n",
       " ('Cessna 208 Caravan',),\n",
       " ('Sukhoi Superjet-100',)]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%sql\n",
    "\n",
    "SELECT DISTINCT model\n",
    "FROM Aircrafts\n",
    "WHERE aircraft_code IN (\n",
    "    SELECT aircraft_code\n",
    "    FROM Flights\n",
    "    WHERE arrival_airport IN (\n",
    "        SELECT airport_code\n",
    "        FROM Airports\n",
    "        WHERE city = 'Yakutsk'\n",
    "    )\n",
    ")\n",
    "OR aircraft_code IN (\n",
    "    SELECT aircraft_code\n",
    "    FROM Flights\n",
    "    WHERE arrival_airport IN (\n",
    "        SELECT airport_code\n",
    "        FROM Airports\n",
    "        WHERE city = 'Abakan'\n",
    "    )\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "aecc8182-bdd0-4956-b9b7-af681d04a6f5",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * postgresql://reader:***@10.129.0.25/demo\n",
      "6 rows affected.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<table>\n",
       "    <thead>\n",
       "        <tr>\n",
       "            <th>model</th>\n",
       "        </tr>\n",
       "    </thead>\n",
       "    <tbody>\n",
       "        <tr>\n",
       "            <td>Airbus A320-200</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>Airbus A321-200</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>Boeing 737-300</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>Boeing 767-300</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>Boeing 777-300</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>Cessna 208 Caravan</td>\n",
       "        </tr>\n",
       "    </tbody>\n",
       "</table>"
      ],
      "text/plain": [
       "[('Airbus A320-200',),\n",
       " ('Airbus A321-200',),\n",
       " ('Boeing 737-300',),\n",
       " ('Boeing 767-300',),\n",
       " ('Boeing 777-300',),\n",
       " ('Cessna 208 Caravan',)]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%sql\n",
    "\n",
    "SELECT DISTINCT model\n",
    "FROM Aircrafts\n",
    "WHERE aircraft_code NOT IN (\n",
    "    SELECT aircraft_code\n",
    "    FROM Flights\n",
    "    WHERE arrival_airport IN (\n",
    "        SELECT airport_code\n",
    "        FROM Airports\n",
    "        WHERE city = 'Yakutsk'\n",
    "    )\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "2502dc32-b82e-4ebf-a2ba-ea51628bbfdd",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * postgresql://reader:***@10.129.0.25/demo\n",
      "7 rows affected.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<table>\n",
       "    <thead>\n",
       "        <tr>\n",
       "            <th>departure_airport</th>\n",
       "            <th>arrival_airport</th>\n",
       "        </tr>\n",
       "    </thead>\n",
       "    <tbody>\n",
       "        <tr>\n",
       "            <td>DME</td>\n",
       "            <td>HMA</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>DME</td>\n",
       "            <td>UUS</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>HMA</td>\n",
       "            <td>DME</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>MQF</td>\n",
       "            <td>SVX</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>SVO</td>\n",
       "            <td>SVX</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>SVX</td>\n",
       "            <td>MQF</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>SVX</td>\n",
       "            <td>SVO</td>\n",
       "        </tr>\n",
       "    </tbody>\n",
       "</table>"
      ],
      "text/plain": [
       "[('DME', 'HMA'),\n",
       " ('DME', 'UUS'),\n",
       " ('HMA', 'DME'),\n",
       " ('MQF', 'SVX'),\n",
       " ('SVO', 'SVX'),\n",
       " ('SVX', 'MQF'),\n",
       " ('SVX', 'SVO')]"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%sql\n",
    "\n",
    "SELECT DISTINCT departure_airport, arrival_airport\n",
    "FROM Flights\n",
    "WHERE flight_id IN (\n",
    "    SELECT flight_id\n",
    "    FROM Ticket_flights\n",
    "    WHERE ticket_no IN (\n",
    "        SELECT ticket_no\n",
    "        FROM Tickets\n",
    "        WHERE passenger_name = 'ELLA DMITRIEVA'\n",
    "    )\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9b93fac4-3439-46fa-a4bd-e04706c7f687",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
