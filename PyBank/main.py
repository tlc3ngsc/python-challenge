{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "7ce210b1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'English_United States.1252'"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from pathlib import Path\n",
    "from collections import Counter\n",
    "import locale\n",
    "locale.setlocale(locale.LC_ALL,'')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "f3ffa643",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "WindowsPath('C:/Users/Needra Pc/1 MSU Data Analysis Boot Camp/MSU assisgnment 07 06 2023/Starter_Code/PyBank')"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Path.cwd()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "032a3ea5",
   "metadata": {},
   "outputs": [],
   "source": [
    "### I had to insert the full path, but will figure out why later"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "4ed8cdf0",
   "metadata": {},
   "outputs": [],
   "source": [
    "csv_path = Path('C:/Users/Needra Pc/1 MSU Data Analysis Boot Camp/MSU assisgnment 07 06 2023/Starter_Code/PyBank/Resources/budget_data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aef108fa",
   "metadata": {},
   "outputs": [],
   "source": [
    "### View last 5 rows: This comment section is directly from the test data to verify dataframe is working \n",
    "### Oct-16,-729004\n",
    "### Nov-16,-112209\n",
    "### Dec-16,516313\n",
    "### Jan-17,607208\n",
    "### Feb-17,382539"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "57a80f17",
   "metadata": {},
   "outputs": [],
   "source": [
    "bank_df = pd.read_csv(csv_path, encoding=\"utf-8\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "18baa710",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Profit/Losses</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>81</th>\n",
       "      <td>Oct-16</td>\n",
       "      <td>-729004</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>82</th>\n",
       "      <td>Nov-16</td>\n",
       "      <td>-112209</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>83</th>\n",
       "      <td>Dec-16</td>\n",
       "      <td>516313</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>84</th>\n",
       "      <td>Jan-17</td>\n",
       "      <td>607208</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>85</th>\n",
       "      <td>Feb-17</td>\n",
       "      <td>382539</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Date  Profit/Losses\n",
       "81  Oct-16        -729004\n",
       "82  Nov-16        -112209\n",
       "83  Dec-16         516313\n",
       "84  Jan-17         607208\n",
       "85  Feb-17         382539"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bank_df.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e188b4a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "### In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: \"Date\" and \"Profit/Losses\".\n",
    "### Your task is to create a Python script that analyzes the records to calculate each of the following values:\n",
    "### •\tThe total number of months included in the dataset = 86\n",
    "###•\tThe net total amount of \"Profit/Losses\" over the entire period Total: $22564198\n",
    "###•\tThe changes in \"Profit/Losses\" over the entire period, and then the average of those changes Average Change: $-8311.11\n",
    "###•\tThe greatest increase in profits (date and amount) over the entire period Greatest Increase in Profits: Aug-16 ($1862002)\n",
    "###•\tThe greatest decrease in profits (date and amount) over the entire period Greatest Decrease in Profits: Feb-14 ($-1825558)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7d7786a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "### The total number of months included in the dataset should = 86; The \"D\" in date must match the file capitalzation used the groupby function \"size\" actual number of rows including blanks; \"count\" actual number of rows with data excluding  blanks gave the same results to get the number of rows"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "3a648a78",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Date\n",
      "Apr-10    1\n",
      "Apr-11    1\n",
      "Apr-12    1\n",
      "Apr-13    1\n",
      "Apr-14    1\n",
      "         ..\n",
      "Sep-12    1\n",
      "Sep-13    1\n",
      "Sep-14    1\n",
      "Sep-15    1\n",
      "Sep-16    1\n",
      "Length: 86, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(bank_df.groupby('Date').size())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "34c65949",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        Profit/Losses\n",
      "Date                 \n",
      "Apr-10              1\n",
      "Apr-11              1\n",
      "Apr-12              1\n",
      "Apr-13              1\n",
      "Apr-14              1\n",
      "...               ...\n",
      "Sep-12              1\n",
      "Sep-13              1\n",
      "Sep-14              1\n",
      "Sep-15              1\n",
      "Sep-16              1\n",
      "\n",
      "[86 rows x 1 columns]\n"
     ]
    }
   ],
   "source": [
    "print(bank_df.groupby('Date').count())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "28110fa8",
   "metadata": {},
   "outputs": [],
   "source": [
    "###•\tThe net total amount of \"Profit/Losses\" over the entire period Total: $22564198  Profit/Losses"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "4094438e",
   "metadata": {},
   "outputs": [],
   "source": [
    "sum_df = bank_df[[\"Profit/Losses\"]].aggregate(\"sum\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "9b1c2621",
   "metadata": {},
   "outputs": [],
   "source": [
    "### locale.currency(bank_df([[\"Profit/Losses\"]].aggregate(\"sum\")))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "bddc0512",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "$ Profit/Losses    22564198\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(\"$\",sum_df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a0d23d1f",
   "metadata": {},
   "outputs": [],
   "source": [
    "sum_df = bank_df[[\"Profit/Losses\"]].aggregate(\"sum\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python (dev)",
   "language": "python",
   "name": "dev"
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
   "version": "3.10.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
