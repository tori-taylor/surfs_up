{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "77727631",
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime as dt\n",
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "641026ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "499e1f22",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, jsonify"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "21e7b442",
   "metadata": {},
   "outputs": [],
   "source": [
    "engine = create_engine(\"sqlite:///hawaii.sqlite\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0a4e7320",
   "metadata": {},
   "outputs": [],
   "source": [
    "Base = automap_base()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f70f6cea",
   "metadata": {},
   "outputs": [],
   "source": [
    "Base.prepare(engine, reflect=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "b593174d",
   "metadata": {},
   "outputs": [],
   "source": [
    "Measurement = Base.classes.measurement\n",
    "Station = Base.classes.station"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "67ce3800",
   "metadata": {},
   "outputs": [],
   "source": [
    "session = Session(engine)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "2f095490",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "451b6b30",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c6a2f2b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "def welcome():\n",
    "    return(\n",
    "    '''\n",
    "    Welcome to the Climate Analysis API!\n",
    "    Available Routes:\n",
    "    /api/v1.0/precipitation\n",
    "    /api/v1.0/stations\n",
    "    /api/v1.0/tobs\n",
    "    /api/v1.0/temp/start/end\n",
    "    ''')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9b9d9074",
   "metadata": {},
   "outputs": [],
   "source": [
    "flask run"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "83d6c5df",
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
   "version": "3.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
