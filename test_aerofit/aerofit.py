{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPmj8/erkVPx7um9FyS8O1A",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/MukeshMishraReloaded/DAV-1-Feb23-Tue/blob/main/test_aerofit/aerofit.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "id": "XAZ5MTKQ4aEX"
      },
      "outputs": [],
      "source": [
        "import datetime\n",
        "import streamlit as st\n",
        "import warnings\n",
        "warnings.filterwarnings(\"ignore\")\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import plotly.express as px\n",
        "import seaborn as sns\n",
        "import numpy as np"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!wget  https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/001/125/original/aerofit_treadmill.csv?1639992749 -O aerofit_treadmill.csv\n",
        "df_aerofit=pd.read_csv(\"aerofit_treadmill.csv\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tox4oHBj5l2g",
        "outputId": "572cd975-9983-453e-efb0-a2f3ddb6050c"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--2023-10-06 07:37:38--  https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/001/125/original/aerofit_treadmill.csv?1639992749\n",
            "Resolving d2beiqkhq929f0.cloudfront.net (d2beiqkhq929f0.cloudfront.net)... 18.172.139.46, 18.172.139.61, 18.172.139.94, ...\n",
            "Connecting to d2beiqkhq929f0.cloudfront.net (d2beiqkhq929f0.cloudfront.net)|18.172.139.46|:443... connected.\n",
            "HTTP request sent, awaiting response... 200 OK\n",
            "Length: 7279 (7.1K) [text/plain]\n",
            "Saving to: ‘aerofit_treadmill.csv’\n",
            "\n",
            "\raerofit_treadmill.c   0%[                    ]       0  --.-KB/s               \raerofit_treadmill.c 100%[===================>]   7.11K  --.-KB/s    in 0s      \n",
            "\n",
            "2023-10-06 07:37:38 (649 MB/s) - ‘aerofit_treadmill.csv’ saved [7279/7279]\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "st.write(\"\"\"\n",
        "            # Aerofit data analyzer \"\"\")\n",
        "\n",
        "## get data for Aerofit treadmilss\n",
        "\n",
        "aerofit_model = st.selectbox(\n",
        "    'Which model do you want to analyse?',\n",
        "    ('KP281', 'KP481', 'KP781'))\n",
        "\n",
        "st.dataframe(df_aerofit[df_aerofit['Product'] == aerofit_model])\n",
        "\n",
        "st.line_chart(df_aerofit[df_aerofit['Product'] == aerofit_model]['Income'])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9YVvR0pL5jDK",
        "outputId": "ce87f2a0-1143-409e-9ca7-6673cc476f44"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    }
  ]
}