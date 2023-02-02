{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOe3wvJAjoTB+yPp3Vu6X0G",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "TPU",
    "gpuClass": "standard"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/akselea/Car-Prediction-ML/blob/main/Car-Price-Prediction-ML.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Submission Dicoding - Predictive Analysis\n",
        "##### Nama : Aksel Estevannanda Arianto\n",
        "##### Dataset diambil dari Kaggle \n",
        "###### **Car Prices Poland** - https://www.kaggle.com/datasets/ravishah1/carvana-predict-car-prices"
      ],
      "metadata": {
        "id": "znW1sbvijIXm"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Import Library yang Digunakan:"
      ],
      "metadata": {
        "id": "dAq31h-KnWsx"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pathlib\n",
        "import os\n",
        "from google.colab import files\n",
        "\n",
        "from sklearn.preprocessing import OneHotEncoder\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "from sklearn.neighbors import KNeighborsRegressor\n",
        "from sklearn.metrics import mean_squared_error\n",
        "from sklearn.ensemble import RandomForestRegressor\n",
        "from sklearn.ensemble import AdaBoostRegressor\n",
        "from sklearn.svm import SVR\n",
        "\n",
        "import numpy as np\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "%matplotlib inline\n",
        "import seaborn as sns"
      ],
      "metadata": {
        "id": "TU7h23uWnWXp"
      },
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Mengunduh Dataset dari Kaggle:"
      ],
      "metadata": {
        "id": "DFJxWuUTkUFI"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Install terlebih dahulu Library untuk mengakses Kaggle\n",
        "! pip install -q kaggle"
      ],
      "metadata": {
        "id": "8tBA23cxlIXe"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Memasukkan API Token Kaggle\n",
        "files.upload()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 90
        },
        "id": "UJT-J_PQlX5H",
        "outputId": "2d7db070-102e-4ad6-a1a0-971774ad6de0"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-9bb98eac-51be-447d-b44b-571325b95764\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-9bb98eac-51be-447d-b44b-571325b95764\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script>// Copyright 2017 Google LLC\n",
              "//\n",
              "// Licensed under the Apache License, Version 2.0 (the \"License\");\n",
              "// you may not use this file except in compliance with the License.\n",
              "// You may obtain a copy of the License at\n",
              "//\n",
              "//      http://www.apache.org/licenses/LICENSE-2.0\n",
              "//\n",
              "// Unless required by applicable law or agreed to in writing, software\n",
              "// distributed under the License is distributed on an \"AS IS\" BASIS,\n",
              "// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
              "// See the License for the specific language governing permissions and\n",
              "// limitations under the License.\n",
              "\n",
              "/**\n",
              " * @fileoverview Helpers for google.colab Python module.\n",
              " */\n",
              "(function(scope) {\n",
              "function span(text, styleAttributes = {}) {\n",
              "  const element = document.createElement('span');\n",
              "  element.textContent = text;\n",
              "  for (const key of Object.keys(styleAttributes)) {\n",
              "    element.style[key] = styleAttributes[key];\n",
              "  }\n",
              "  return element;\n",
              "}\n",
              "\n",
              "// Max number of bytes which will be uploaded at a time.\n",
              "const MAX_PAYLOAD_SIZE = 100 * 1024;\n",
              "\n",
              "function _uploadFiles(inputId, outputId) {\n",
              "  const steps = uploadFilesStep(inputId, outputId);\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  // Cache steps on the outputElement to make it available for the next call\n",
              "  // to uploadFilesContinue from Python.\n",
              "  outputElement.steps = steps;\n",
              "\n",
              "  return _uploadFilesContinue(outputId);\n",
              "}\n",
              "\n",
              "// This is roughly an async generator (not supported in the browser yet),\n",
              "// where there are multiple asynchronous steps and the Python side is going\n",
              "// to poll for completion of each step.\n",
              "// This uses a Promise to block the python side on completion of each step,\n",
              "// then passes the result of the previous step as the input to the next step.\n",
              "function _uploadFilesContinue(outputId) {\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  const steps = outputElement.steps;\n",
              "\n",
              "  const next = steps.next(outputElement.lastPromiseValue);\n",
              "  return Promise.resolve(next.value.promise).then((value) => {\n",
              "    // Cache the last promise value to make it available to the next\n",
              "    // step of the generator.\n",
              "    outputElement.lastPromiseValue = value;\n",
              "    return next.value.response;\n",
              "  });\n",
              "}\n",
              "\n",
              "/**\n",
              " * Generator function which is called between each async step of the upload\n",
              " * process.\n",
              " * @param {string} inputId Element ID of the input file picker element.\n",
              " * @param {string} outputId Element ID of the output display.\n",
              " * @return {!Iterable<!Object>} Iterable of next steps.\n",
              " */\n",
              "function* uploadFilesStep(inputId, outputId) {\n",
              "  const inputElement = document.getElementById(inputId);\n",
              "  inputElement.disabled = false;\n",
              "\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  outputElement.innerHTML = '';\n",
              "\n",
              "  const pickedPromise = new Promise((resolve) => {\n",
              "    inputElement.addEventListener('change', (e) => {\n",
              "      resolve(e.target.files);\n",
              "    });\n",
              "  });\n",
              "\n",
              "  const cancel = document.createElement('button');\n",
              "  inputElement.parentElement.appendChild(cancel);\n",
              "  cancel.textContent = 'Cancel upload';\n",
              "  const cancelPromise = new Promise((resolve) => {\n",
              "    cancel.onclick = () => {\n",
              "      resolve(null);\n",
              "    };\n",
              "  });\n",
              "\n",
              "  // Wait for the user to pick the files.\n",
              "  const files = yield {\n",
              "    promise: Promise.race([pickedPromise, cancelPromise]),\n",
              "    response: {\n",
              "      action: 'starting',\n",
              "    }\n",
              "  };\n",
              "\n",
              "  cancel.remove();\n",
              "\n",
              "  // Disable the input element since further picks are not allowed.\n",
              "  inputElement.disabled = true;\n",
              "\n",
              "  if (!files) {\n",
              "    return {\n",
              "      response: {\n",
              "        action: 'complete',\n",
              "      }\n",
              "    };\n",
              "  }\n",
              "\n",
              "  for (const file of files) {\n",
              "    const li = document.createElement('li');\n",
              "    li.append(span(file.name, {fontWeight: 'bold'}));\n",
              "    li.append(span(\n",
              "        `(${file.type || 'n/a'}) - ${file.size} bytes, ` +\n",
              "        `last modified: ${\n",
              "            file.lastModifiedDate ? file.lastModifiedDate.toLocaleDateString() :\n",
              "                                    'n/a'} - `));\n",
              "    const percent = span('0% done');\n",
              "    li.appendChild(percent);\n",
              "\n",
              "    outputElement.appendChild(li);\n",
              "\n",
              "    const fileDataPromise = new Promise((resolve) => {\n",
              "      const reader = new FileReader();\n",
              "      reader.onload = (e) => {\n",
              "        resolve(e.target.result);\n",
              "      };\n",
              "      reader.readAsArrayBuffer(file);\n",
              "    });\n",
              "    // Wait for the data to be ready.\n",
              "    let fileData = yield {\n",
              "      promise: fileDataPromise,\n",
              "      response: {\n",
              "        action: 'continue',\n",
              "      }\n",
              "    };\n",
              "\n",
              "    // Use a chunked sending to avoid message size limits. See b/62115660.\n",
              "    let position = 0;\n",
              "    do {\n",
              "      const length = Math.min(fileData.byteLength - position, MAX_PAYLOAD_SIZE);\n",
              "      const chunk = new Uint8Array(fileData, position, length);\n",
              "      position += length;\n",
              "\n",
              "      const base64 = btoa(String.fromCharCode.apply(null, chunk));\n",
              "      yield {\n",
              "        response: {\n",
              "          action: 'append',\n",
              "          file: file.name,\n",
              "          data: base64,\n",
              "        },\n",
              "      };\n",
              "\n",
              "      let percentDone = fileData.byteLength === 0 ?\n",
              "          100 :\n",
              "          Math.round((position / fileData.byteLength) * 100);\n",
              "      percent.textContent = `${percentDone}% done`;\n",
              "\n",
              "    } while (position < fileData.byteLength);\n",
              "  }\n",
              "\n",
              "  // All done.\n",
              "  yield {\n",
              "    response: {\n",
              "      action: 'complete',\n",
              "    }\n",
              "  };\n",
              "}\n",
              "\n",
              "scope.google = scope.google || {};\n",
              "scope.google.colab = scope.google.colab || {};\n",
              "scope.google.colab._files = {\n",
              "  _uploadFiles,\n",
              "  _uploadFilesContinue,\n",
              "};\n",
              "})(self);\n",
              "</script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving kaggle.json to kaggle.json\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'kaggle.json': b'{\"username\":\"akselestevannandaa\",\"key\":\"72167085ecc204832f209a6ca813368d\"}'}"
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "! mkdir ~/.kaggle\n",
        "! cp kaggle.json ~/.kaggle/"
      ],
      "metadata": {
        "id": "S3OclQHQq3Co"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "! chmod 600 ~/.kaggle/kaggle.json"
      ],
      "metadata": {
        "id": "wA6x_FwKrBgf"
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "! kaggle datasets download aleksandrglotov/car-prices-poland -p /content/dataset/ --unzip"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9K4LSyitre6c",
        "outputId": "a2304fa9-eb6e-402f-e552-766f449a5736"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Downloading car-prices-poland.zip to /content/dataset\n",
            "\r  0% 0.00/1.64M [00:00<?, ?B/s]\n",
            "\r100% 1.64M/1.64M [00:00<00:00, 133MB/s]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Memasukan Dataset dari Kaggle dengan variabel \"df\"\n",
        "df = pd.read_csv('/content/dataset/Car_Prices_Poland_Kaggle.csv')\n",
        "df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "B57sahzProi3",
        "outputId": "af106807-6c26-4987-d339-368a9b936150"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Unnamed: 0  mark  model generation_name  year  mileage  vol_engine    fuel  \\\n",
              "0           0  opel  combo      gen-d-2011  2015   139568        1248  Diesel   \n",
              "1           1  opel  combo      gen-d-2011  2018    31991        1499  Diesel   \n",
              "2           2  opel  combo      gen-d-2011  2015   278437        1598  Diesel   \n",
              "3           3  opel  combo      gen-d-2011  2016    47600        1248  Diesel   \n",
              "4           4  opel  combo      gen-d-2011  2014   103000        1400     CNG   \n",
              "\n",
              "              city     province  price  \n",
              "0            Janki  Mazowieckie  35900  \n",
              "1         Katowice      Śląskie  78501  \n",
              "2            Brzeg     Opolskie  27000  \n",
              "3        Korfantów     Opolskie  30800  \n",
              "4  Tarnowskie Góry      Śląskie  35900  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-8f5d6282-3ef7-489a-9db5-0d173e355bae\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
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
              "      <th>Unnamed: 0</th>\n",
              "      <th>mark</th>\n",
              "      <th>model</th>\n",
              "      <th>generation_name</th>\n",
              "      <th>year</th>\n",
              "      <th>mileage</th>\n",
              "      <th>vol_engine</th>\n",
              "      <th>fuel</th>\n",
              "      <th>city</th>\n",
              "      <th>province</th>\n",
              "      <th>price</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0</td>\n",
              "      <td>opel</td>\n",
              "      <td>combo</td>\n",
              "      <td>gen-d-2011</td>\n",
              "      <td>2015</td>\n",
              "      <td>139568</td>\n",
              "      <td>1248</td>\n",
              "      <td>Diesel</td>\n",
              "      <td>Janki</td>\n",
              "      <td>Mazowieckie</td>\n",
              "      <td>35900</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>opel</td>\n",
              "      <td>combo</td>\n",
              "      <td>gen-d-2011</td>\n",
              "      <td>2018</td>\n",
              "      <td>31991</td>\n",
              "      <td>1499</td>\n",
              "      <td>Diesel</td>\n",
              "      <td>Katowice</td>\n",
              "      <td>Śląskie</td>\n",
              "      <td>78501</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2</td>\n",
              "      <td>opel</td>\n",
              "      <td>combo</td>\n",
              "      <td>gen-d-2011</td>\n",
              "      <td>2015</td>\n",
              "      <td>278437</td>\n",
              "      <td>1598</td>\n",
              "      <td>Diesel</td>\n",
              "      <td>Brzeg</td>\n",
              "      <td>Opolskie</td>\n",
              "      <td>27000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>3</td>\n",
              "      <td>opel</td>\n",
              "      <td>combo</td>\n",
              "      <td>gen-d-2011</td>\n",
              "      <td>2016</td>\n",
              "      <td>47600</td>\n",
              "      <td>1248</td>\n",
              "      <td>Diesel</td>\n",
              "      <td>Korfantów</td>\n",
              "      <td>Opolskie</td>\n",
              "      <td>30800</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>4</td>\n",
              "      <td>opel</td>\n",
              "      <td>combo</td>\n",
              "      <td>gen-d-2011</td>\n",
              "      <td>2014</td>\n",
              "      <td>103000</td>\n",
              "      <td>1400</td>\n",
              "      <td>CNG</td>\n",
              "      <td>Tarnowskie Góry</td>\n",
              "      <td>Śląskie</td>\n",
              "      <td>35900</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-8f5d6282-3ef7-489a-9db5-0d173e355bae')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-8f5d6282-3ef7-489a-9db5-0d173e355bae button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-8f5d6282-3ef7-489a-9db5-0d173e355bae');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Mencari Info Dataset:"
      ],
      "metadata": {
        "id": "BeDTopQm8Gy7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Mencari info terkait isi dari Dataset (Jumlah kolom dan jumlah data yang ada)\n",
        "df.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6X59SqGkw2kg",
        "outputId": "ba0901a8-3e10-4553-8c46-3f10c02cfdd8"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 117927 entries, 0 to 117926\n",
            "Data columns (total 11 columns):\n",
            " #   Column           Non-Null Count   Dtype \n",
            "---  ------           --------------   ----- \n",
            " 0   Unnamed: 0       117927 non-null  int64 \n",
            " 1   mark             117927 non-null  object\n",
            " 2   model            117927 non-null  object\n",
            " 3   generation_name  87842 non-null   object\n",
            " 4   year             117927 non-null  int64 \n",
            " 5   mileage          117927 non-null  int64 \n",
            " 6   vol_engine       117927 non-null  int64 \n",
            " 7   fuel             117927 non-null  object\n",
            " 8   city             117927 non-null  object\n",
            " 9   province         117927 non-null  object\n",
            " 10  price            117927 non-null  int64 \n",
            "dtypes: int64(5), object(6)\n",
            "memory usage: 9.9+ MB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Mengecek apakah ada nilai kosong atau NaN pada Dataset \n",
        "df.isnull().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4HWZTyQT923t",
        "outputId": "2217a83b-b65c-42cc-c454-3c52f29b35d3"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Unnamed: 0             0\n",
              "mark                   0\n",
              "model                  0\n",
              "generation_name    30085\n",
              "year                   0\n",
              "mileage                0\n",
              "vol_engine             0\n",
              "fuel                   0\n",
              "city                   0\n",
              "province               0\n",
              "price                  0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Untuk Kolom Numerik, Kolom \"0\" akan dihapus karena tidak berkaitan dengan harga mobil.\n",
        "# Untuk Kolom Kategori, Kolom \"generation_name\" akan dihapus juga dikarenakan banyaknya data yang kosong dan tidak berkaitan dengan harga mobil.\n",
        "# Unutk Kolom \"model\" pun akan dihapus dikarenakan sudah adanya data Tahun dan Volume Mesin yang lebih berpengaruh terhadap harga mobil.\n",
        "df = df.drop([\"Unnamed: 0\", \"generation_name\", \"model\"], axis=1)"
      ],
      "metadata": {
        "id": "F3ExaW-T9PBC"
      },
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Mencari nilai parameter statistika pada Dataset\n",
        "df.describe()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 300
        },
        "id": "5aft_Vs68GC-",
        "outputId": "ff1ad938-3373-4d81-c6b5-9f5ef2211c90"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                year       mileage     vol_engine         price\n",
              "count  117927.000000  1.179270e+05  117927.000000  1.179270e+05\n",
              "mean     2012.925259  1.409768e+05    1812.057782  7.029988e+04\n",
              "std         5.690135  9.236936e+04     643.613438  8.482458e+04\n",
              "min      1945.000000  0.000000e+00       0.000000  5.000000e+02\n",
              "25%      2009.000000  6.700000e+04    1461.000000  2.100000e+04\n",
              "50%      2013.000000  1.462690e+05    1796.000000  4.190000e+04\n",
              "75%      2018.000000  2.030000e+05    1995.000000  8.360000e+04\n",
              "max      2022.000000  2.800000e+06    7600.000000  2.399900e+06"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-cedb3273-4a8b-4a42-a08c-9b17d6601dfb\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
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
              "      <th>year</th>\n",
              "      <th>mileage</th>\n",
              "      <th>vol_engine</th>\n",
              "      <th>price</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>117927.000000</td>\n",
              "      <td>1.179270e+05</td>\n",
              "      <td>117927.000000</td>\n",
              "      <td>1.179270e+05</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>2012.925259</td>\n",
              "      <td>1.409768e+05</td>\n",
              "      <td>1812.057782</td>\n",
              "      <td>7.029988e+04</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>5.690135</td>\n",
              "      <td>9.236936e+04</td>\n",
              "      <td>643.613438</td>\n",
              "      <td>8.482458e+04</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>1945.000000</td>\n",
              "      <td>0.000000e+00</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>5.000000e+02</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>2009.000000</td>\n",
              "      <td>6.700000e+04</td>\n",
              "      <td>1461.000000</td>\n",
              "      <td>2.100000e+04</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>2013.000000</td>\n",
              "      <td>1.462690e+05</td>\n",
              "      <td>1796.000000</td>\n",
              "      <td>4.190000e+04</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>2018.000000</td>\n",
              "      <td>2.030000e+05</td>\n",
              "      <td>1995.000000</td>\n",
              "      <td>8.360000e+04</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>2022.000000</td>\n",
              "      <td>2.800000e+06</td>\n",
              "      <td>7600.000000</td>\n",
              "      <td>2.399900e+06</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-cedb3273-4a8b-4a42-a08c-9b17d6601dfb')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-cedb3273-4a8b-4a42-a08c-9b17d6601dfb button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-cedb3273-4a8b-4a42-a08c-9b17d6601dfb');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Berdasarkan parameter statistika di atas, pada kolom \"vol_engine\" nilai 0 merupakan nilai terendah.\n",
        "# Memastikan terdapat beberapa data dengan nilai \"vol_engine\" = 0\n",
        "vol_0 = (df.vol_engine == 0).sum()\n",
        "print(\"Data dengan Volume Mesin 0 =\", vol_0)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "N-iU9BEl_E91",
        "outputId": "3efd7a1d-7b10-4a1d-bb3f-96e23a0ac96b"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Data dengan Volume Mesin 0 = 1248\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Menghapus Data dimana \"vol_engine\" < 999cc (Dibuat Threshold Nilai Minimum Volume Mesin di 999cc).\n",
        "df = df.loc[(df[['vol_engine']]>998).all(axis=1)]\n",
        "df.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "U5sBENhQ_e9d",
        "outputId": "093b1fc3-55f5-4781-eb08-b247d1410498"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(114449, 8)"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Mengecek kembali nilai \"vol_engine\" dengan fungsi .describe()\n",
        "df.describe()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 300
        },
        "id": "fmKrBDeh-0IN",
        "outputId": "10fefa5d-d876-44ea-8b2e-52f216e28ef6"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                year       mileage     vol_engine         price\n",
              "count  114449.000000  1.144490e+05  114449.000000  1.144490e+05\n",
              "mean     2012.802453  1.436322e+05    1848.205926  6.936098e+04\n",
              "std         5.648268  9.181119e+04     613.058197  8.389575e+04\n",
              "min      1952.000000  1.000000e+00     999.000000  5.000000e+02\n",
              "25%      2009.000000  7.200000e+04    1498.000000  2.090000e+04\n",
              "50%      2013.000000  1.492520e+05    1798.000000  4.150000e+04\n",
              "75%      2017.000000  2.050000e+05    1995.000000  8.225000e+04\n",
              "max      2022.000000  2.800000e+06    7600.000000  2.399900e+06"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-b98ab825-ac1c-4eff-b137-7b77dd7ea742\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
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
              "      <th>year</th>\n",
              "      <th>mileage</th>\n",
              "      <th>vol_engine</th>\n",
              "      <th>price</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>114449.000000</td>\n",
              "      <td>1.144490e+05</td>\n",
              "      <td>114449.000000</td>\n",
              "      <td>1.144490e+05</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>2012.802453</td>\n",
              "      <td>1.436322e+05</td>\n",
              "      <td>1848.205926</td>\n",
              "      <td>6.936098e+04</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>5.648268</td>\n",
              "      <td>9.181119e+04</td>\n",
              "      <td>613.058197</td>\n",
              "      <td>8.389575e+04</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>1952.000000</td>\n",
              "      <td>1.000000e+00</td>\n",
              "      <td>999.000000</td>\n",
              "      <td>5.000000e+02</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>2009.000000</td>\n",
              "      <td>7.200000e+04</td>\n",
              "      <td>1498.000000</td>\n",
              "      <td>2.090000e+04</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>2013.000000</td>\n",
              "      <td>1.492520e+05</td>\n",
              "      <td>1798.000000</td>\n",
              "      <td>4.150000e+04</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>2017.000000</td>\n",
              "      <td>2.050000e+05</td>\n",
              "      <td>1995.000000</td>\n",
              "      <td>8.225000e+04</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>2022.000000</td>\n",
              "      <td>2.800000e+06</td>\n",
              "      <td>7600.000000</td>\n",
              "      <td>2.399900e+06</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-b98ab825-ac1c-4eff-b137-7b77dd7ea742')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-b98ab825-ac1c-4eff-b137-7b77dd7ea742 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-b98ab825-ac1c-4eff-b137-7b77dd7ea742');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Univariate Analysis:"
      ],
      "metadata": {
        "id": "6oSR8KrlDTZ-"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Mengecek info Dataset\n",
        "df.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KZNxkE7hExI_",
        "outputId": "692741ac-a1fe-4bd6-8de5-e25e1cc559b1"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "Int64Index: 114449 entries, 0 to 117926\n",
            "Data columns (total 8 columns):\n",
            " #   Column      Non-Null Count   Dtype \n",
            "---  ------      --------------   ----- \n",
            " 0   mark        114449 non-null  object\n",
            " 1   year        114449 non-null  int64 \n",
            " 2   mileage     114449 non-null  int64 \n",
            " 3   vol_engine  114449 non-null  int64 \n",
            " 4   fuel        114449 non-null  object\n",
            " 5   city        114449 non-null  object\n",
            " 6   province    114449 non-null  object\n",
            " 7   price       114449 non-null  int64 \n",
            "dtypes: int64(4), object(4)\n",
            "memory usage: 7.9+ MB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Membagi Data berdasarkan Jenisnya (Numerical & Categorical).\n",
        "numerical_data = ['year', 'mileage', 'vol_engine', 'price']\n",
        "categorical_data = ['mark', 'fuel', 'city', 'province']"
      ],
      "metadata": {
        "id": "g_vdlSqxFlkj"
      },
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Categorical - mark\n",
        "feature = categorical_data[0]\n",
        "count = df[feature].value_counts()\n",
        "percent = 100*df[feature].value_counts(normalize=True)\n",
        "df_cat = pd.DataFrame({'Jumlah Sampel':count, 'Persentase':percent.round(1)})\n",
        "print(df_cat)\n",
        "count.plot(kind='bar', title=feature)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 782
        },
        "id": "8dCVUV7XJUEw",
        "outputId": "6f446bca-3135-442a-9160-8e37fe900b4c"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "               Jumlah Sampel  Persentase\n",
            "audi                   11825        10.3\n",
            "opel                   11700        10.2\n",
            "bmw                    10863         9.5\n",
            "volkswagen             10730         9.4\n",
            "ford                    9130         8.0\n",
            "mercedes-benz           7033         6.1\n",
            "renault                 6524         5.7\n",
            "skoda                   5810         5.1\n",
            "peugeot                 5004         4.4\n",
            "toyota                  4491         3.9\n",
            "volvo                   4374         3.8\n",
            "hyundai                 3792         3.3\n",
            "kia                     3460         3.0\n",
            "nissan                  2976         2.6\n",
            "mazda                   2846         2.5\n",
            "seat                    2835         2.5\n",
            "fiat                    2720         2.4\n",
            "citroen                 2719         2.4\n",
            "honda                   2133         1.9\n",
            "mitsubishi              1113         1.0\n",
            "mini                    1064         0.9\n",
            "alfa-romeo               699         0.6\n",
            "chevrolet                608         0.5\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7fd90fe10190>"
            ]
          },
          "metadata": {},
          "execution_count": 17
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYMAAAFLCAYAAAA03+DLAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nO3deZwcVbn/8c+XsK9hiaiAJEAEAUEwIm5XEJFdcAFZ1IAIV2WJ8hMBr14URcHlInAVRVmCoGzKBWWNLCIiSxL2AJfIIkEkkU2uCBh8fn+c00xNp6erunu6e5L5vl+vfs1UdZ2u6pnueuqces45igjMzGx0W6zfB2BmZv3nYGBmZg4GZmbmYGBmZjgYmJkZDgZmZoaDgVlfSDpT0tf7fRxmNQ4GZmbmYGDWa5LG9PsYzOo5GJgNQdLDkg6XdKekv0s6TdLqki6X9Jyk30haOW97gaS/SHpW0vWSNiq8zpmSTpF0maS/A1vX7WcFSddKOkmSevw2zQAHA7MyHwK2BV4P7AJcDnwRGEf6/hyat7scmAi8CpgJnFP3OnsDxwIrADfUVkpaFbga+H1EHBoeH8b6ZPF+H4DZCHdyRDwBIOl3wNyIuC0vXwRsAxARp9cKSPoK8LSklSLi2bz64oj4ff79hVwBeC3wW2BqRHy7F2/GbCiuGZg190Th9380WF5e0hhJx0n6o6S/AQ/n51crbPtog9feCVgG+OEwHq9ZWxwMzDq3N7Ar8F5gJWB8Xl9s/2/U/PNj4ArgMknLdfMAzco4GJh1bgXgReBJYFngGy2UPRi4H/iVpGW6cGxmlTgYmHXuLOAR4DFgFnBT1YL5hvGBwBzgYklLd+UIzUrIyQtmZuaagZmZORiYmZmDgZmZ4WBgZmY4GJiZGQvxcBSrrbZajB8/vt+HYWa2UJkxY8ZfI2Jc/fqFNhiMHz+e6dOn9/swzMwWKpIeabTezURmZlYeDCSdLmmupLsL674t6b48zvtFksYWnjtK0mxJ90varrB++7xutqQjC+snSLo5rz9P0pLD+QbNzKxclZrBmcD2deumARtHxCbA/wJHAUjaENgT2CiX+UEe0XEM8H1gB2BDYK+8LcDxwAkRsR7wNLB/R+/IzMxaVhoMIuJ64Km6dVdFxPy8eBOwZv59V+DciHgxIh4CZgNb5MfsiHgwIl4CzgV2zbM6vQe4MJefCuzW4XsyM7MWDcc9g0+QZnkCWIPB47bPyeuGWr8q8EwhsNTWm5lZD3UUDCT9BzCfBaf46wpJB0qaLmn6vHnzerFLM7NRoe1gIGlfYGdgn8K8rY8BaxU2WzOvG2r9k8BYSYvXrW8oIk6NiEkRMWncuAXSZM3MrE1tBQNJ2wNfAN4fEc8XnroE2FPSUpImkCYIvwW4FZiYM4eWJN1kviQHkWuBD+fyk4GL23srZmbWrtJOZ5J+DmwFrCZpDnA0KXtoKWBantj7poj4VETcI+l80gQf84GDIuLl/DoHA1cCY4DTI+KevIsjgHMlfR24DTit1Tcx/shLmz7/8HE7tfqSZmajSmkwiIi9Gqwe8oQdEccCxzZYfxlwWYP1D5KyjczMrE8W2uEohkuzWoVrFGY2Wng4CjMzczAwMzMHAzMzw8HAzMxwMDAzMxwMzMwMBwMzM8PBwMzMcDAwMzMcDMzMDAcDMzPDwcDMzHAwMDMzHAzMzAwPYd02T6hjZosS1wzMzMw1g37whDpmNtK4ZmBmZg4GZmbmYGBmZjgYmJkZDgZmZoaDgZmZ4WBgZmY4GJiZGQ4GZmZGhWAg6XRJcyXdXVi3iqRpkh7IP1fO6yXpJEmzJd0pafNCmcl5+wckTS6sf7Oku3KZkyRpuN+kmZk1V6VmcCawfd26I4GrI2IicHVeBtgBmJgfBwKnQAoewNHAW4EtgKNrASRvc0ChXP2+zMysy0qDQURcDzxVt3pXYGr+fSqwW2H9WZHcBIyV9BpgO2BaRDwVEU8D04Dt83MrRsRNERHAWYXXMjOzHmn3nsHqEfF4/v0vwOr59zWARwvbzcnrmq2f02B9Q5IOlDRd0vR58+a1eehmZlav4xvI+Yo+huFYquzr1IiYFBGTxo0b14tdmpmNCu0GgydyEw/559y8/jFgrcJ2a+Z1zdav2WC9mZn1ULvB4BKglhE0Gbi4sP7jOatoS+DZ3Jx0JfA+SSvnG8fvA67Mz/1N0pY5i+jjhdcyM7MeKZ3cRtLPga2A1STNIWUFHQecL2l/4BFgj7z5ZcCOwGzgeWA/gIh4StLXgFvzdsdERO2m9GdIGUvLAJfnh5mZ9VBpMIiIvYZ4apsG2wZw0BCvczpweoP104GNy47DzMy6xz2QzczMwcDMzBwMzMwMBwMzM8PBwMzMcDAwMzMcDMzMDAcDMzPDwcDMzKjQA9lGlvFHXjrkcw8ft1MPj8TMFiWuGZiZmYOBmZk5GJiZGQ4GZmaGg4GZmeFgYGZmOBiYmRkOBmZmhoOBmZnhYGBmZjgYmJkZDgZmZoaDgZmZ4WBgZmY4GJiZGQ4GZmZGh8FA0uck3SPpbkk/l7S0pAmSbpY0W9J5kpbM2y6Vl2fn58cXXueovP5+Sdt19pbMzKxVbQcDSWsAhwKTImJjYAywJ3A8cEJErAc8Deyfi+wPPJ3Xn5C3Q9KGudxGwPbADySNafe4zMysdZ02Ey0OLCNpcWBZ4HHgPcCF+fmpwG75913zMvn5bSQprz83Il6MiIeA2cAWHR6XmZm1oO1gEBGPAd8B/kQKAs8CM4BnImJ+3mwOsEb+fQ3g0Vx2ft5+1eL6BmUGkXSgpOmSps+bN6/dQzczszqdNBOtTLqqnwC8FliO1MzTNRFxakRMiohJ48aN6+auzMxGlU6aid4LPBQR8yLin8AvgXcAY3OzEcCawGP598eAtQDy8ysBTxbXNyhjZmY90Ekw+BOwpaRlc9v/NsAs4Frgw3mbycDF+fdL8jL5+WsiIvL6PXO20QRgInBLB8dlZmYtWrx8k8Yi4mZJFwIzgfnAbcCpwKXAuZK+ntedloucBvxU0mzgKVIGERFxj6TzSYFkPnBQRLzc7nGZmVnr2g4GABFxNHB03eoHaZANFBEvALsP8TrHAsd2cixmZtY+90A2MzMHAzMzczAwMzMcDMzMDAcDMzPDwcDMzHAwMDMzHAzMzAwHAzMzw8HAzMxwMDAzMzocm8gWHuOPvHTI5x4+bqceHomZjUSuGZiZmYOBmZk5GJiZGQ4GZmaGg4GZmeFgYGZmOBiYmRkOBmZmhjudWQXusGa26HPNwMzMHAzMzMzBwMzMcDAwMzMcDMzMjA6DgaSxki6UdJ+keyW9TdIqkqZJeiD/XDlvK0knSZot6U5JmxdeZ3Le/gFJkzt9U2Zm1ppOawYnAldExAbApsC9wJHA1RExEbg6LwPsAEzMjwOBUwAkrQIcDbwV2AI4uhZAzMysN9oOBpJWAv4NOA0gIl6KiGeAXYGpebOpwG75912BsyK5CRgr6TXAdsC0iHgqIp4GpgHbt3tcZmbWuk5qBhOAecAZkm6T9BNJywGrR8TjeZu/AKvn39cAHi2Un5PXDbV+AZIOlDRd0vR58+Z1cOhmZlbUSTBYHNgcOCUiNgP+zkCTEAAREUB0sI9BIuLUiJgUEZPGjRs3XC9rZjbqdRIM5gBzIuLmvHwhKTg8kZt/yD/n5ucfA9YqlF8zrxtqvZmZ9UjbwSAi/gI8Kmn9vGobYBZwCVDLCJoMXJx/vwT4eM4q2hJ4NjcnXQm8T9LK+cbx+/I6MzPrkU4HqjsEOEfSksCDwH6kAHO+pP2BR4A98raXATsCs4Hn87ZExFOSvgbcmrc7JiKe6vC4bARoNsAdeJA7s5Gko2AQEbcDkxo8tU2DbQM4aIjXOR04vZNjMTOz9rkHspmZORiYmZmDgZmZ4WBgZmY4GJiZGQ4GZmaGg4GZmeFgYGZmOBiYmRkOBmZmhoOBmZnhYGBmZnQ+aqlZVzQb8dSjnZoNP9cMzMzMwcDMzBwMzMwMBwMzM8PBwMzMcDAwMzMcDMzMDAcDMzPDnc5sEdOssxq4w5rZUFwzMDMz1wzMajwEho1mrhmYmZmDgZmZDUMwkDRG0m2Sfp2XJ0i6WdJsSedJWjKvXyovz87Pjy+8xlF5/f2Stuv0mMzMrDXDUTOYAtxbWD4eOCEi1gOeBvbP6/cHns7rT8jbIWlDYE9gI2B74AeSxgzDcZmZWUUdBQNJawI7AT/JywLeA1yYN5kK7JZ/3zUvk5/fJm+/K3BuRLwYEQ8Bs4EtOjkuMzNrTac1g+8BXwD+lZdXBZ6JiPl5eQ6wRv59DeBRgPz8s3n7V9Y3KDOIpAMlTZc0fd68eR0eupmZ1bQdDCTtDMyNiBnDeDxNRcSpETEpIiaNGzeuV7s1M1vkddLP4B3A+yXtCCwNrAicCIyVtHi++l8TeCxv/xiwFjBH0uLASsCThfU1xTJmZtYDbdcMIuKoiFgzIsaTbgBfExH7ANcCH86bTQYuzr9fkpfJz18TEZHX75mzjSYAE4Fb2j0uMzNrXTd6IB8BnCvp68BtwGl5/WnATyXNBp4iBRAi4h5J5wOzgPnAQRHxcheOy6wrPB6SLQqGJRhExHXAdfn3B2mQDRQRLwC7D1H+WODY4TgWMzNrnXsgm5mZg4GZmTkYmJkZDgZmZobnMzDrK8+hYCOFawZmZuZgYGZmDgZmZoaDgZmZ4WBgZmY4GJiZGQ4GZmaG+xmYLbTcR8GGk2sGZmbmmoHZaOMahTXiYGBmlTmQLLrcTGRmZq4ZmFn3dTI1qGsjveGagZmZORiYmZmDgZmZ4WBgZmY4GJiZGQ4GZmaGg4GZmeFgYGZmdBAMJK0l6VpJsyTdI2lKXr+KpGmSHsg/V87rJekkSbMl3Slp88JrTc7bPyBpcudvy8zMWtFJD+T5wP+LiJmSVgBmSJoG7AtcHRHHSToSOBI4AtgBmJgfbwVOAd4qaRXgaGASEPl1LomIpzs4NjMb5Trp9TwatV0ziIjHI2Jm/v054F5gDWBXYGrebCqwW/59V+CsSG4Cxkp6DbAdMC0insoBYBqwfbvHZWZmrRuWewaSxgObATcDq0fE4/mpvwCr59/XAB4tFJuT1w21vtF+DpQ0XdL0efPmDcehm5kZwxAMJC0P/AL4bET8rfhcRASp6WdYRMSpETEpIiaNGzduuF7WzGzU6ygYSFqCFAjOiYhf5tVP5OYf8s+5ef1jwFqF4mvmdUOtNzOzHukkm0jAacC9EfFfhacuAWoZQZOBiwvrP56zirYEns3NSVcC75O0cs48el9eZ2ZmPdJJNtE7gI8Bd0m6Pa/7InAccL6k/YFHgD3yc5cBOwKzgeeB/QAi4ilJXwNuzdsdExFPdXBcZmbWoraDQUTcAGiIp7dpsH0ABw3xWqcDp7d7LGZm1hn3QDYzMwcDMzNzMDAzMxwMzMwMBwMzM8PBwMzMcDAwMzMcDMzMDAcDMzPDwcDMzOhsbCIzs0VSs1nSFtUZ0hwMzMyGycI81aabiczMzMHAzMwcDMzMDAcDMzPDwcDMzHA2kZnZiNDvdFbXDMzMzDUDM7OF3XDUKlwzMDMzBwMzM3MwMDMzHAzMzAwHAzMzw8HAzMwYQcFA0vaS7pc0W9KR/T4eM7PRZEQEA0ljgO8DOwAbAntJ2rC/R2VmNnqMiGAAbAHMjogHI+Il4Fxg1z4fk5nZqKGI6PcxIOnDwPYR8cm8/DHgrRFxcN12BwIH5sX1gfuHeMnVgL+2eTjtlvU+F619dlLW+1y09tlJ2ZG4z7UjYtwCayOi7w/gw8BPCssfA/67g9eb3uuy3ueitc+F7Xi9z5FZdmHa50hpJnoMWKuwvGZeZ2ZmPTBSgsGtwERJEyQtCewJXNLnYzIzGzVGxKilETFf0sHAlcAY4PSIuKeDlzy1D2W9z0Vrn52U9T4XrX12Unah2eeIuIFsZmb9NVKaiczMrI8cDMzMzMHAzMwcDEYVSWs1WPfqCuV2r7JuUSFpeUnL9/s4RiJJE6qsa7DNO6qss/YMx3d0ob+BLOn8iNhD0l1A8c0IiIjYZIhyH2z2uhHxywr7/hpwPXBjRPy9hcNuiaRVmj0fEU9VfJ35wAXA/hHxfF43MyI2Lym3wDZVyuXtVgYmAksXjvf6CuWujohtytY1KDcR+CZpjKviPtepsM83AmcBq5A+P/OAyRFxd5MyH42IsyUd1uj5iPivCvvt5JjfDoynkBkYEWeVlctldwI2qtvnMSVlGn0WZkTEm9soV/Uz9HrgcGBtBr/P95SVzeU3ZsG/bcO/kaTvRcRnJf2KweeTWrn3N9lPW+eiutfYFHhXXvxdRNxRViaXa/vvWzMiUks7NCX/3LnFcrs0eS6A0mAAPAjsBZwk6Tngd8D1EXFxs0I5EB0PvIr0Qal9WFYcosiMfEwCXgc8nX8fC/wJKL0yy+7Kx3iDpN0j4o/5dYY6zh2AHYE1JJ1UeGpFYH7ZziR9kvT/WRO4HdgS+AMw5JdY0tLAssBqOZDUjm9FYI2yfQJnAEcDJwBbA/tRvQb8I+CwiLg2H8tWpDS9tzcps1z+uULFfTTS1jFL+imwLulv+3JeHaSAVlb2h6S/89bAT0ijANzSZPsNSIFjpboLqRUpnGQblHsb6e83ri5grkhKI6/iAuCHwI8ZeJ+VSDoa2IoUDC4jDYZ5A0P/jX6af36nlf1k7Z6LAJA0BTiAgXPP2ZJOjYiTm5Tp6Ds6SLtdpf0Y1P371cChpBPzcxW2nw28oY39/BjYsbC8A/CjFsrPzD/fAcwiBcSZTbbfFNgXeASYXHh8EFi5wv7uIp0obs/LGwC/LCkzBXgIeDH/rD3uAA6usM8ZtX3Xr6tQ9o4q67rw+WnrmIF7ybX7NvZ5Z93P5UlXokNtvyspaD2Zf9YeJwFvb1Lu3aRA93j+WXscBkxs5e/T5vu8ixRY78jLqwPTuv0/bfd/AixXWF6u9v9pUmbT/J1s6ztafCz0NYN8RT5kW1cMfbVdK7868A3gtRGxQx46+20RcVqFff+EdMXxBOmK+8PAzAqH/URE3Fthu3pbRsQBtYWIuFzSt1oor1zu95K2Ac4nnaAbilRFvUPS2RHR2lVG8kJEvCAJSUtFxH2S1m9WICJOBE6UdEg0uSJq4kVJiwEP5I6Mj5FOdFU8KOnLDFwdfpRU+yuVazT7s2Czyye6eMx3ky5EHq9yjHX+kX8+L+m1pJP8a4baOFJt92JJb4uIP1TdSUT8FvitpDMj4pE2jhPgV5I+A1xEukiovXaV5tF/RMS/JM2XtCIwl8FD3zSU72d8hYGmqVrtvUrTXas1/1eKMrjm8zJNau4w6Dv6s3ycr4uIoQbwbGqhDwYRsQK80n7/OOmLLGAfmny4C84kXeH8R17+X+A8oDQYAKuSqrrPAE8Bf6140pwu6Tzgfxj84S5rmvqzpC8BZ+flfYA/V9hfzY6FfT0uaWuaNIEU2z6lBT+TUd4GOkfSWNL7nCbpadIVTBU/knQo8G95+TpSLeifJeWmkJo/DgW+RmoG+XjFfX4C+CoD1fTr87oqfgrcB2wHHEP631QN+PXH/B7S1V2Z1YBZkm5h8OdoyHbtgl/n/823SRcwQWouKnObpINoPeg9L+nbDcpVafev/S0OL6wLoPTETPqujSXVqmcA/0dqqixzGvC5XKalpingW8AubVzwnQHcLOmivLwb1c5DANuTmraWBCZIehNwTMXPArAI3ECukXRHRGxatq5BuVsj4i2SbouIzfK62yPiTS3s+w2kk8DngDERsWbJ9mc0WB1lX6h8I/lo0gkySCerYypeISFpKeBDLHjDseFNQ0lrN3u9Vq70JL0bWAm4ItKcFWXb/wRYApiaV30MeDnyMOdNyu0eEReUrRui7OYRUaVm16jsbRGxmaQ7I2ITSUuQml22bOf1Ku7z3Y3W56vxVl5nKWDpiHi2wrYXkILe3hSCXkRMKSl3Feki6/PAp0gn+HkRcUQrx9oJSeOBFSPizgrb3hwRb21zP7+PiLYypSRtDrwzL/4uIm6rWG4G6SLiusJ57K6IeGPVfS/0NYOCv0vahzQxTpBu7FbJ8Pm7pFUZuALeEij9UuRtdybd+f830s3ca0jNRU1FxH5VXr9uX2OAkyNin1bLFlxMem8zKFxJDqXdav0Q2U935Z/Lk2pRZd5SF8ivkVQls+Io0g3HsnWNfFcp1fZC4LxokkXUQK3G8kzOXvkLqZlgSJ1kruTnWzrp530OmUUnqUrtdL2I2F3SrhExNTdPlH7mgVUj4jRJUwpNR7dWPOZlSfcYXhcRByplX60fEb9uUmbILJpmQb9Q7tpck/klg2tdVS4W2q35Q6ohPhcRZ0gaJ2lCRDxUodw/I+LZuhp8S1f6i1Iw2Bs4MT8C+H1eV+Yw0gip60r6PTCO1PZfxfakL8KJEVG5uUYpVe4UYPWI2FjSJsD7I+LrQ5WJiJclrS1pySpX1kNYMyK2b7VQ3X2ZJUlX7H9v0gY6HNlPL0taN1LGE5LWoUl1fTiyKiJi6xwM9iA1U61ICgpD/l8KTs3ZT18mfZ6WB/6zpEzt3sRvSSP3FpVmJ+ULl5OBN5D+L2No/n+BgSy6V5GaCK/Jy1sDN1KeRddy0Ksr97hSSuufSSm8VZxB+kzVmjQfIwX3IYMB8N38c2lgEikBQcAmwHTgbSXlaiYVfg+aZMIVrAg8D7yvrmzTv23OfJpEmrjrDNL37GxSwkeZeyTtDYzJwfJQ0v+zulbuNi+qD1JQ3AjYGFiijfIrkj7YqwCrVNj+t6SpPm8rrLu7QrmzSCeNL5OC2GGkVMiqx3kq8MYO/1YitWUeV2HbtrOfgG1IgeO6/Pd6GNi6yfbDllWRX++NpJP1Sz34/M0ENi4s7wXcXKHcdGA94DZSINgP+GbFfV4FvKaw/BrgygrlPgmsTMoSepB0Q/ZTFcrtTGom3Bi4lnRyf3/FY52efxa/L5WyvEgn4DcWljcGLuz2/7TNz8Ht+ftVfJ9Ns4kK2y0LHJvPD9Pz70u3sv9F6Z7BGTSuape1wy8NfIbUThekK/0fRsQLFfZ5IKnd9IXCviNKMg7avU+RrxwWEBFfLTvWXH4W6eRRS92s3BmmwWu9cuxNtlmgzbKVdszcll3LPro/IkqbtnJbvYDXF8qV3XSulX0D8BHSfZUnSW3cv4iIuU3KNOxsVhPVOp2tQ2qa2pvU7PhxYOcoacOXND0iJtXuU+R1pf+XvN29EfGGwvJiwD3FdSOFpBtJFwe/j4jNJa0L/DwitqhQ9p6I2KhsXYNyU0hX58+RLmo2B46MiKualPlCRHxL0sk0PhcdWrLPWyJiC+XOYpKWA/7QzvezHYtSM1Gxyrg08AGqZdqcRfqH19IY9yZdEVbpyn046Yqu1XlK/5o/0LX7FB+mQnpg7aSvPFRCRPxfi/vdocXtyfsrtjMvRqrKlgZLOsh+KrQTrx0RB0iaKKlpO3H2dtL/9GFSUFhL0uSo0OsZOJ0UALaL6s1+teac9YG3MDAp0y406cRVFBEPStqT1Mb8J+B9EfGPkmKQMnSWBG5XSjF+nOod7K6WdCXw87z8EeA3ZYXUYip2pyfI7GjgCtL/8hxSs8m+FcoB3JmTEYqfwdIbyMAnIuJESduRsgY/RjovDBkMGMgem06L7fXZ+ZJ+BIyVdAApk+3HzQoMdb+pJkZjNlG9fKVzQ0Q06z2KpFkRsWHZuiHKXgF8MPLQDi0c2zoM9Gx9mnSl/tGIeLik3MakD2StrfWvwMejhYmAJL2T1NnnDEnjgOWj5AaVBmc/zSedaH/c7Io5lytmP0HKfvpqVMh+yjfgZpDe38Y5ONxYofY0A9g7cq51vj/z8ygZLqFTkq4HdoqI5/LyCsClEfFvTcrUD1vwKtIN/hehPHVXKdvrCdL9gs+RmmF+EBGzKx7zByj8byLiombb5zKXk1OxI2JTSYuTmjUa1vYkPRkRq0r6LOmzPkhETG1QrNHrrErqwS7gpqoXYLnm/2kGfwZPKav5ayAr7ERShs5FLdS63gJ8kcFZe5Vq4JK2Jd1rEKnZblrJ9g0zymqihSSDRTkYrE/6Mq5Xst3ZwH9HxE15+a3AQRFRmpsuaTNybjCDswaqXO2Qq4GL1U4gFba/kfQlvDYvbwV8oyzgFcq/coMqIl6v1NnogmgzDa6qfGKMVmoyhSaQYlNalVThO+u/dI3W1T1ff1J+5Smqf4nvBzapNWXlJq47I2LITnYa3tTdlYG1okLaZN7+y8CZEfFoYd2BEdF0lqxWmzhz0+R7gctJw0IMTnepnhb9fgp9TirUEDuSL4DWICU7bEq6J3NdlYuK/Fk4nJRB96/a+qr/z5y4UEz9rvo3WpI2mkdrFplmIg3OeAnSFdMXKhR9M3CjpD/lcmsD99dOECUngh+RsjEG/dMrHOthdcuQUz4j4vYmRZerBQLSwV2XA0pVHwA2I/eSjog/5xN12fG21btWgwd+Q9JfKRn4reAlScsw0JS2LhXSYUlpffXNAtNLyrQ1lkyds4BbNLjDUNOr3lZO9o1Iug54P+l7PAOYq5Tj3vQ+RnYIsKekgwufqU9RPmViq6nYpwBXkzqIzSgePhU7jkk6jtQEd05eNUXS2yPiixXK1vckBioNArg/8CbgwYh4Pr/nqinh8yKi5TncJf07qdPjC6TzSSt/o61In7eHab15NL3GolQzyM0SxREyo+yPka/OVmZgpMDrST2Kay8w5Be2arWxQbmfka7Qf5VX7UxqxxxPulJvOMREPtHMZPBwCW+OiA9U3G9bN6jUfkejtmsyubr8JdJwH1eR24kj4rqScksBB1HouENqOqkSSGpt4m/Ji7eUNYXVlX1zYb/XR8UOQ+3SQEe3T5JqBUeX1YKKZUnjDV1Ayq75dpXPs1Ie/smkrJy7yanYZTUSSadExKcrvrX6sncCb4qIf+XlMaSmqSrv8z4a9CSOiCeH2H6DSMOmNOynEBX6GSgN9bIXKQhW7mcg6QHS/ZdW70EOT/NojICUquF4kFLe7iK1S15LGnvlmgrlpuRyXyWd6O4EDqm4z28AB5LS8lpJLb2e1FZfW16elD65DDCrwfY/zT8PIw0MNjM/vkcLaZOk3p8/IqUEHo9NfzgAABLQSURBVEDqll/6XsmpbgwMarYEqd22rFxHA7+RbtztRAqWq1Usswup6a2dz9AepNTUqaQr/YdIJ7qq5ccAryX1rXgdqZNUNz/zd+XP3lWkTnqv/I9a+J8uTWrqvAC4r0K53Ump1BuR+lFcCmze5fd5Z/F7lb9nVd9naYpu3fan5p/XNniUnk9y2bNJtdGpDAzod3qFclcAy7b7N6qyrulrdPOf2MsHbYyQWfigtTRSYGHbh/KJddCjQrn7KPRnAJaqfREp5BgXnp+VTzJ35C/CqrQQfOpea1vSeDTfBratWOaW/PN60hXhahXf50WkPhHj8+NLwEUV97l5g8e6wOIl5c4G/kgaH2aDFv82dwCvKiyPo3o++yGkG/r35M/UXa1+Gdv4zO+e9/WDvLwOKRW2Stkf1y0fVPF/WrsgeGc+Qe7U6gm3jfe5JylIn5lPsA8BH6lY9rj8WX9b8bPU5eO9v81ym5H6GvyIdNF3EnBSxbJnkMaW2io/fkyFAFR8LDL3DGhjhMys5ZECCzakQR+FCuXOIQ1IVZv3YBfgZ7nZZlaD7X/IQLtrsf27cptiwV2kGkgwMEREmXZ618Lggd+CNI581XbXH5C+uHeS3ufGpBPtSpI+HUPke0fER/MNuL2AMyUF6Yvy8yi/Ub9YDG4WepLqqZpTSDfmGzY/dEOk8ZYuKCw/SOojUaXsAXXL3we+X6Fo7buyEymgXCqpSg/ttihlBf6LlElUa747IiL+UvElauMLtdSTWB30PyLdg9wwIhp9l5tp6x5k9ilSQK8lr/yO9B2qrpsRspcP0lXoWNLNoutJ4/BcVqHcYaQrwq/kx+3AZyvu83xSNN46P34MnF+x7FtIJ5ApwKSKZU7p8G/0SVIe+5kM3Gz6RBf/J/s3WFfaczlv90tgo8LyhqSOWeuQa38l5VcFPpvf4+XAA5Q0iZFqE1eSctj3zeWOr3i811JSa+nC3/dbpCabJUgXC/NIKcpVyk7Mf89ZDNRq/1ih3K8ZaGocS6rVdnXOB3IP5B7/bc8njRha/G5fULHsvcBLwP20UEukQatAxf2NoUITX9ljkbqBXKPWR8hsd6TAtvso5G1fxeDsnD9VKdeunPL29shXrzlD4sZokv6Yt2tptNNCucuAcyLinLz838AyEbF/hWO9OyI2brSuJJXx/aTax3qkdv+pETFXqZ/CrIgY32SfnydlodVe+4aokHufy55G6nh2KYNvGpb2QG5X7e+g1F9gZ9KFzfVRkn6by97AwOxqu5BnV4uIpjW+/HfcnjQRzwOSXkMa7qFZZ6yO5Gyiv5I6BL4y+GRU66+yEoP7uvyWNNJvWe/uTvofNUwZjpLsMUnfIF28/IoW523IrQyHdHIOWZSaiV4RLY7mGClDoJ2hi2dK2jIG91EoS2OsnbC+S7oPMJd0s/E+0k25bnqS1Nu65rm8rkxLo50WfAi4RNK/SCeQZ6oEguweSaeQRqGF1EN2Vg5MzfKnPwScEHVZZJHSA8v2vRxwJGlU1fNobaCvP+XHkvnRC7Xv706kq9b6USubWSYirpakfJL6Ss5IaRoMInWw/GVh+XHam1ynFR/JPw8qHgrVmkdPJ2U97ZGXP0ZqNmw6Bzptfreho5ThvfLPo4ovR7X3uTLpO3MLgwOmeyB3kwY6KS1Buhos9lG4r+zqQWko5vcAv4mUGrg1qXpf9UTZ6vHW8s7fRBqA7eJ8vLuSqq/7lpRf4Cq9ZPviaJQrkIZZ+D35RFPxSmcZBtpsyeV/QMrBXjaadGDrJD00l9+EgTGK5kTEe1sp3yv5ink3UubcFqRmm19HhXH4c9rvO0lNRdeQRgI9rqyW2A+Slo66tvpG64You0AtsqRm2dF3u180DHNbOBi0YahqYE2F6mCtd+0dwGaRpuUr7V3bLg0xwF1NlAx0J+lU0lwKlW44S3qIwT16a5erkffXyg3vlkjanTTj03V5v+8CDo+IC1t4jVeTMnX2BFaIavns19J47J0qQx63LQfeZyMNcb4safKW0purSkMm3EsKIF8j3Xv4VkTc3M3jbUetX0zZuiHK/oH0/78hL78D+E5ENBzCutPvdieUBlksDp1xHdVm96td8J0XEY+1u/9Fspmo24bhA/GM0mBz1wPnSJpLtYl42tLoZC/p1VVOGtk7gX3zSb50tNOImJD3sQfpvs3flIY/2Jx04inVIKDUXrsskHyJlHM/N7/OONIAbKXBQGme3T1IKaUXAAdE9YyQzxd+X5pUq2hn3uhSkt4TEdeoMIBgXfNQlUlUgtR5cW3SVTCkm6Q9GSGzihyU1wCWURr6pfYmVyQN2VzFp4Gp+d4BpH5Ik4fauPbdlvS6tg66M6eQ/he1LKCP5XVNZ/fLVgCuklRr4rwgIp5oZeeuGfRBTiH9ByltcR/Sze5zoodpiVWvrPK27d4Qqw329U5SEPgO8J8VmzFWLSwuTbpSX6XCDc5BQ2Tn1MQ7osKw2ZK+Sbq6ajYkSGXKPb6H47XqXverkXobn8GCNbCI8vmIOx4/pxckTSZldU1icHv9c6RxlUqDXr7H9GFSH5WxpHtfUSH5odZcJNLnbwKp/0DX7us1ah1otcWgkyZO1wz6Y09S1scDlIxf00WV7zRGxCNqMNpphaJt56Q3CIzfq3KDE7hcCw7NfFnFfR5VvlVjdfdJFiONebXSEJt3JCJqzX6fZsEsr6pXd22Nn9NLkUY0nSrpQxHxizZf5mLS8DIzSfdFqu67fh6OzUn3sLqppdn9hjCXNPvck1Sbge4VDgb98TrStIoTSFc815NSWoflirSipuOkF6n96fgeUxqffVvg+HyVVqkTlwaPDVObQ6HK5zVIefC1G8+nkjosdVtxqs/5pF6yXUkIKPgfBk50tZupVYPB0UoD+rU0fk4vSfpoRJwNjFeDSYQqpu22NdVrg33NzBlF3fR50tzLD5I+R2tTsZNmh02cgINBX9Su7HLGzAGk6vr3SJ1HukZp5M85kQZtmyXpUOCsiHimpGhbo52SPpzbk27YPZNz0g+veLjFuWhrcyjs0XjTQbaNiCMotJtL+ipwRMX9tqV2n6THOjnR7UcasmUJBpqJgmr3G3qlNiJvo1po1aB3o6Q3Vk1+qKkLPrWaXuV5zlulNPjepqTOgC3N7petReos2/YFpe8Z9IHS7F/vIH3IbyMN0/C7nLPdzf3eTrrCHk/qHHUJqZfvjiXl+jodXxWSPk2qxq9DGpuoZgXSdIkf7fL+p5Ny2n9WIbgO1z5byvKqK3v/SEwjbUTSVGBK7e+qNDTKd5vdGym0+S9OOsE+SAtTvdZl4NUuRn5RJZ21XZ3eY2rUlBslE1cNKu9g0HuSZpI+YJeSekT+oYUrgI72m0/mh5PGcjpZJcMWK6WpfJmU1bEt8E3SmEM/i4iThyo3DMfa6vSKK5E63nyT1HGs5rkq/RqG4XjXI11tf4TU9HcGcFV08QumDua0zjefv91qU0I/NPqMVvjcDluKaE5CWD4i/la1TDsknUCqqdX3tK4ybPYrTbnR5sRVDgZ9ojSY2jtIbdu7A3Mj4p3NS3W8z5tJzVH/AewSEQ+pQoeyfJV1GC1MxzcMx9rS9IojRT5x7ExKCXyZ9B5O7EZAajfLK5e9l5Rh03Ig6TWl/jhbRcTTeXkV4Lfd/CwozTnyKdL/8FZSOuuJEfHtLu7z2garIyr0Vcm1/s2AmTEwA12luS1qfM+gD5TmMn4X8G5SNH+UNMpgt+1H+oAfmwPBBAYmymlmJmkoiart/cNhtYg4X9JRABExX1KrmRU9ldP6PgHsAPyCNDrtO0k9fJvO3dyODtNAO76p2kPfBf6gNMkSpIunY7u8zw1z/5h9SAMWHklKEuhaMIiIrTso/lJEhNIovbX09ZY4GPTHcaQMopOAW6PFuUrbFRGzJB1BymYityceX6HoW4F9JD3C4OprN68iW51esa9y2uszpFFsjyg0+92s1Ot1RBlJ/QnKRMRZ+Z5M7Qr5gz1o3lpCqUfwbqQ50v+p6uM+dUzSryOilelYz8+Ze2MlHUC6KKmcMQhuJuo7tTiReYf72oXU8WvJiJgg6U2kERybDmbVSXNEuzQwveJGpHkMKk2v2C/5nsZmLDjXbtPOTTYy5Uy7I0jD2+9EuoA6OyLe1bTg8O2/5Sl1laaKbbsp18GgD9RgInPSUNKf6/J+Z5Curq4rtCu2NAhdryhNLnIwsB2px+kfSJkzXcvm6ISkKxjI+S/OtfvdIQvZiCVpQjETJydSrJc7ivZi/6c3y5bqBjcT9cdKuT3yk6Q8/6OVJv3utn/GgsMctzqjUq+cBfyNlFEEsDfp/sbufTui5oalc5ONGL8gjaUFpLu4ks4l9TfoulYDgdI4VceTeh2LgYSAFau+hoNBfyyeO2DtQcrs6ZV7JO0NjJE0kTRFXitj9vfSxjF4uOBrcyrlSNVW5yYbWSRtQGqaXEmFgQBJ2URLNy41bPueSEqN3pDBk15VGeX3W6QMwXvb3b+DQX8cQ5pe8YaIuDWPQdKL6uchpODzImnsniupOIpoH7Q9uUgv1XVu2i8PJTCiUzWtqfVJqcFjSTPA1TxHGi2gm85gYPa5rcmzz1Us+0QngQB8z6AvJK1Sn3de30Y52uU8+NrkIpBu4N1P6qw3Yk6yw9m5yUYOSW+LiD/0eJ8zIuLNKoy8W1vXpEyt9vJu4NWk8araGmvKNYP++JWkHWo9GnMmyvlAV27kSvoVTcZyKcsm6pOFov3dJ/tFi6QvRMS3gL0l7VX/fEQc2sXdv5g7LT4g6WDSKKtlowPXai8BPE/KJqKwzsFghPsGKSDsRLr6PYs0r0G3fCf//CDp6uHsvLwXaQL4EccnWeuTWlPLdKoPhjdcppAm7TmU1Hy7NU0m4gGIiP1g6PGbWtm5m4n6RNJuwBdIA6l9KCL+twf7nB4Rk8rWmY12StOCfpG6uSK60Twp6acR8TFJUyLixDZfo+Xxm+q5ZtBDkk5m8NXGSqQRNg+W1O0qKMByktaJiAfz8UxgYJhgMxtwNg1mguuSN+eB5T4h6SzqJp6qOK7VYpJWrhu/qaXzu4NBb9Vnw8zo8f4/B1ynwZNn/HuPj8FsYdDLmeB+SJpkaB3SOaEYDCKvL9Px+E1uJhpllGYb2yAv3hc9GDrbbGEjaRvSPbWezQQn6ZSI+HQH5TdkYPyma1odv8nBoIcKOekNdTtdUtKypKGo146IA3Inl/Uj4tfd3K/ZwkbS2aSLpnsozATXjSEiNHj+7AV0Y/jzhsfhYNA7/c5Jl3QeqRr68YjYOAeHGyNi2IdXNluYqYczwUl6iIGLxFoTUW0+7ajYA7ljvmfQQ8WTvdJMXm/Ji7dExNweHMK6EfGRWv50RDyvXo7La7bwuFHShj0YKnvQ/Nm5ljCRLg990YiDQR9I2oM0ScZ1pOh/sqTDI+LCLu/6JUnLMDBHwLoU2kPN7BVbArfnq/aeDC+SB66cAqwJ3J6P4UZgm27tc9D+3UzUe3kav21rtQGlyat/ExGbdnm/2wJfIg2EdRVp2s19I+K6bu7XbGHTpzk87iK1FtwUEW/Kg+Z9IyI+WFJ0WLhm0B+L1TULPUn1AanaFhHTJM0kXXGI1GPxr93er9nCpk894F+IiBckIWmpiLhPUk/uW4CDQb9cLulK0sihAB8BLuv2TiV9gJRydmleHitpt4j4n27v28xKzZE0ljTY3DRJTwM9C0puJuoDSZ8njQlUy+K5ISIu6sF+b6/PHGpnej0z6y5J7yaNUHBFRLzUi326ZtAfywFHAk8B59G7CWYaNUX5M2A2wkTEb3u9T9cM+kjSJqQmog8BcyLivV3e3+mkeXq/n1cdBKwSEft2c79mNvJ1/aalNTUX+AvpBvKrerC/Q4CXSLWRc4EXSAHBzEY51wz6QNJnSPMfjwMuAM7vducWSWNI6atbd3M/ZrZwcntxf6wFfDYibu/VDiPiZUn/krRSRDzbq/2a2cLBNYNRRNLFwGbANODvtfU9mEfBzEY41wxGl1/SwpyoZjZ6uGYwyuSxiV4XEff3+1jMbORwNtEoImkX0gBYV+TlN0nq1WxOZjaCORiMLl8BtiD1NSDfwO7JWOlmNrI5GIwu/2yQSdTtyb7NbCHgG8ijyz2S9gbG5CkvD6V3Q2GY2QjmmsHocgiwEWmyjp8Bz5Im0zCzUc7BYHTZMD8WJ02rtytwa1+PyMxGBKeWjiKS7gc+D9xN4V5BnybyMLMRxPcMRpd5EfGrfh+EmY08rhmMIpK2AfYCribdNwAgItwr2WyUc81gdNkP2ABYgoFmosBDVJiNeq4ZjCKS7o+Ink2wbWYLD2cTjS43Stqw3wdhZiOPawajiKR7gXWBh0j3DARERGzS1wMzs75zMBhFJK3daL1TS83MwcDMzHzPwMzMHAzMzAwHAzMzw8HAzMxwMDAzM+D/Aw2T/wbI61NUAAAAAElFTkSuQmCC\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Categorical - fuel\n",
        "feature = categorical_data[1]\n",
        "count = df[feature].value_counts()\n",
        "percent = 100*df[feature].value_counts(normalize=True)\n",
        "df_cat = pd.DataFrame({'Jumlah Sampel':count, 'Persentase':percent.round(1)})\n",
        "print(df_cat)\n",
        "count.plot(kind='bar', title=feature)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 454
        },
        "id": "vBQ6GDUWJf97",
        "outputId": "b0ce92e2-754d-4b77-9891-df8922064382"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "          Jumlah Sampel  Persentase\n",
            "Gasoline          59270        51.8\n",
            "Diesel            48327        42.2\n",
            "LPG                4240         3.7\n",
            "Hybrid             2561         2.2\n",
            "CNG                  46         0.0\n",
            "Electric              5         0.0\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7fd90fd20850>"
            ]
          },
          "metadata": {},
          "execution_count": 18
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Dengan melihat pemerataan data, maka Jenis Bahan Bakar selain Gasoline dan Diesel akan dihapus.\n",
        "df = df.loc[df['fuel'].isin(count.index[count > 5000])]\n",
        "\n",
        "feature = categorical_data[1]\n",
        "count = df[feature].value_counts()\n",
        "percent = 100*df[feature].value_counts(normalize=True)\n",
        "df_cat = pd.DataFrame({'Jumlah Sampel':count, 'Persentase':percent.round(1)})\n",
        "print(df_cat)\n",
        "count.plot(kind='bar', title=feature)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 384
        },
        "id": "-S0-OHKKRf1z",
        "outputId": "d9256e26-d5d0-468f-9448-e99212455b5f"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "          Jumlah Sampel  Persentase\n",
            "Gasoline          59270        55.1\n",
            "Diesel            48327        44.9\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7fd90f857850>"
            ]
          },
          "metadata": {},
          "execution_count": 19
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYMAAAEqCAYAAAD3dzw0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAVMElEQVR4nO3dfZBd9X3f8ffHEjjEiS1hFoVKYNFYtS1owSCDPHTcBMYgcGIxqU2hjVEZBXVqSOymM67oE6ltXNx2SoKNmWGCjGCcEMapi2qDFQ1gt56Wh8UQQBDChodBCg9riyebiTH42z/ubz038q72SuzuEXvfr5k795zv+Z1zv3dY9Lnn6d5UFZKk4famrhuQJHXPMJAkGQaSJMNAkoRhIEnCMJAkYRhIA0vyriT3Jnkpye+8ju1ck+SzM9mb9Hot7LoB6Q3kU8BtVXVs141IM809A2lw7wC2d92ENBsMA2kASW4FfhX4YpIfJPnrJL/Vt/yfJ/lO3/y7k2xLsivJw0nO6qJvaVCGgTSAqjoZ+D/AhVX1C8BfTjU2yVuAbcAfAYcCZwNfSrJyLnqV9oVhIM28XwMer6ovV9WrVXUP8KfARzvuS5qSJ5ClmfcO4MQkz/fVFgLXddSPNC3DQNo3PwR+vm/+l/qmnwS+XVUfnNuWpH3nYSJp39wL/EaSn0/yTmB937KvA38vyceSHNAe70vynm5alaZnGEj75jLgFeAZYDPwlYkFVfUScCq9E8d/DTwNfB5489y3KQ0m/riNJMk9A0mSYSBJMgwkSRgGkiQMA0kSb+Cbzg455JBavnx5121I0hvG3Xff/b2qGpls2Rs2DJYvX87o6GjXbUjSG0aSJ6Za5mEiSZJhIEkaMAySLEry1SR/keShJO9PcnD78Y5H2vPiNjZJLk8yluS+JMf1bWddG/9IknV99eOT3N/WuTxJZv6tSpKmMuiewR8A36yqdwPHAA8BG4FbqmoFcEubBzgdWNEeG4ArAZIcDFwMnAicAFw8ESBtzPl96615fW9LkrQ3pg2DJG8DPgBcDVBVr1TV88Bael/QRXs+s02vBa6tntuBRUkOA04DtlXVrqp6jt4vQa1py95aVbdX74uSru3bliRpDgyyZ3AkMA58Ock9Sf6w/azfkqp6qo15GljSppfS+z73CTtabU/1HZPUJUlzZJAwWAgcB1xZVe+l96MeG/sHtE/0s/71p0k2JBlNMjo+Pj7bLydJQ2OQMNgB7KiqO9r8V+mFwzPtEA/t+dm2fCdweN/6y1ptT/Vlk9R/RlVdVVWrqmrVyMik901IkvbBtDedVdXTSZ5M8q6qehg4BXiwPdYBl7bnG9sqW4ALk1xP72TxC1X1VJKtwOf6ThqfClxUVbuSvJhkNXAHcC7whRl8j51ZvvEbXbcwrzx+6Ye6bkGatwa9A/m3ga8kORB4FDiP3l7FDUnWA08AZ7WxNwFnAGPAy20s7R/9zwB3tXGfrqpdbfrjwDXAQcDN7SFJmiMDhUFV3QusmmTRKZOMLeCCKbazCdg0SX0UOHqQXiRJM887kCVJhoEkyTCQJGEYSJIwDCRJGAaSJAwDSRKGgSQJw0CShGEgScIwkCRhGEiSMAwkSRgGkiQMA0kShoEkCcNAkoRhIEnCMJAkYRhIkjAMJEkYBpIkDANJEoaBJAnDQJKEYSBJYsAwSPJ4kvuT3JtktNUOTrItySPteXGrJ8nlScaS3JfkuL7trGvjH0myrq9+fNv+WFs3M/1GJUlT25s9g1+tqmOralWb3wjcUlUrgFvaPMDpwIr22ABcCb3wAC4GTgROAC6eCJA25vy+9dbs8zuSJO2113OYaC2wuU1vBs7sq19bPbcDi5IcBpwGbKuqXVX1HLANWNOWvbWqbq+qAq7t25YkaQ4MGgYF/FmSu5NsaLUlVfVUm34aWNKmlwJP9q27o9X2VN8xSV2SNEcWDjjuH1bVziSHAtuS/EX/wqqqJDXz7f1tLYg2ABxxxBGz/XKSNDQG2jOoqp3t+Vnga/SO+T/TDvHQnp9tw3cCh/etvqzV9lRfNkl9sj6uqqpVVbVqZGRkkNYlSQOYNgySvCXJL05MA6cCDwBbgIkrgtYBN7bpLcC57aqi1cAL7XDSVuDUJIvbieNTga1t2YtJVreriM7t25YkaQ4McphoCfC1drXnQuCPquqbSe4CbkiyHngCOKuNvwk4AxgDXgbOA6iqXUk+A9zVxn26qna16Y8D1wAHATe3hyRpjkwbBlX1KHDMJPXvA6dMUi/ggim2tQnYNEl9FDh6gH4lSbPAO5AlSQNfTSRpnlm+8RtdtzCvPH7ph7pu4XVxz0CSZBhIkgwDSRKGgSQJw0CShGEgScIwkCRhGEiSMAwkSRgGkiQMA0kShoEkCcNAkoRhIEnCMJAkYRhIkjAMJEkYBpIkDANJEoaBJAnDQJKEYSBJwjCQJGEYSJLYizBIsiDJPUm+3uaPTHJHkrEkf5LkwFZ/c5sfa8uX923jolZ/OMlpffU1rTaWZOPMvT1J0iD2Zs/gE8BDffOfBy6rqncCzwHrW3098FyrX9bGkWQlcDZwFLAG+FILmAXAFcDpwErgnDZWkjRHBgqDJMuADwF/2OYDnAx8tQ3ZDJzZpte2edryU9r4tcD1VfWjqnoMGANOaI+xqnq0ql4Brm9jJUlzZNA9g98HPgX8pM2/HXi+ql5t8zuApW16KfAkQFv+Qhv/0/pu60xVlyTNkWnDIMmvAc9W1d1z0M90vWxIMppkdHx8vOt2JGneGGTP4CTgw0kep3cI52TgD4BFSRa2McuAnW16J3A4QFv+NuD7/fXd1pmq/jOq6qqqWlVVq0ZGRgZoXZI0iGnDoKouqqplVbWc3gngW6vqnwG3AR9pw9YBN7bpLW2etvzWqqpWP7tdbXQksAK4E7gLWNGuTjqwvcaWGXl3kqSBLJx+yJT+DXB9ks8C9wBXt/rVwHVJxoBd9P5xp6q2J7kBeBB4Fbigql4DSHIhsBVYAGyqqu2voy9J0l7aqzCoqm8B32rTj9K7Emj3MX8DfHSK9S8BLpmkfhNw0970IkmaOd6BLEkyDCRJhoEkCcNAkoRhIEnCMJAkYRhIkjAMJEkYBpIkDANJEoaBJAnDQJKEYSBJwjCQJGEYSJIwDCRJGAaSJAwDSRKGgSQJw0CShGEgScIwkCRhGEiSMAwkSRgGkiQMA0kSA4RBkp9LcmeSP0+yPcl/avUjk9yRZCzJnyQ5sNXf3ObH2vLlfdu6qNUfTnJaX31Nq40l2Tjzb1OStCeD7Bn8CDi5qo4BjgXWJFkNfB64rKreCTwHrG/j1wPPtfplbRxJVgJnA0cBa4AvJVmQZAFwBXA6sBI4p42VJM2RacOgen7QZg9ojwJOBr7a6puBM9v02jZPW35KkrT69VX1o6p6DBgDTmiPsap6tKpeAa5vYyVJc2SgcwbtE/y9wLPANuCvgOer6tU2ZAewtE0vBZ4EaMtfAN7eX99tnanqkqQ5MlAYVNVrVXUssIzeJ/l3z2pXU0iyIcloktHx8fEuWpCkeWmvriaqqueB24D3A4uSLGyLlgE72/RO4HCAtvxtwPf767utM1V9ste/qqpWVdWqkZGRvWldkrQHg1xNNJJkUZs+CPgg8BC9UPhIG7YOuLFNb2nztOW3VlW1+tntaqMjgRXAncBdwIp2ddKB9E4yb5mJNydJGszC6YdwGLC5XfXzJuCGqvp6kgeB65N8FrgHuLqNvxq4LskYsIveP+5U1fYkNwAPAq8CF1TVawBJLgS2AguATVW1fcbeoSRpWtOGQVXdB7x3kvqj9M4f7F7/G+CjU2zrEuCSSeo3ATcN0K8kaRZ4B7IkyTCQJBkGkiQMA0kShoEkCcNAkoRhIEnCMJAkYRhIkjAMJEkYBpIkDANJEoaBJAnDQJKEYSBJwjCQJGEYSJIwDCRJGAaSJAwDSRKGgSQJw0CShGEgScIwkCRhGEiSMAwkSQwQBkkOT3JbkgeTbE/yiVY/OMm2JI+058WtniSXJxlLcl+S4/q2ta6NfyTJur768Unub+tcniSz8WYlSZMbZM/gVeBfV9VKYDVwQZKVwEbglqpaAdzS5gFOB1a0xwbgSuiFB3AxcCJwAnDxRIC0Mef3rbfm9b81SdKgpg2Dqnqqqr7bpl8CHgKWAmuBzW3YZuDMNr0WuLZ6bgcWJTkMOA3YVlW7quo5YBuwpi17a1XdXlUFXNu3LUnSHNircwZJlgPvBe4AllTVU23R08CSNr0UeLJvtR2ttqf6jknqkqQ5MnAYJPkF4E+BT1bVi/3L2if6muHeJuthQ5LRJKPj4+Oz/XKSNDQGCoMkB9ALgq9U1f9o5WfaIR7a87OtvhM4vG/1Za22p/qySeo/o6quqqpVVbVqZGRkkNYlSQMY5GqiAFcDD1XVf+9btAWYuCJoHXBjX/3cdlXRauCFdjhpK3BqksXtxPGpwNa27MUkq9trndu3LUnSHFg4wJiTgI8B9ye5t9X+LXApcEOS9cATwFlt2U3AGcAY8DJwHkBV7UryGeCuNu7TVbWrTX8cuAY4CLi5PSRJc2TaMKiq7wBTXfd/yiTjC7hgim1tAjZNUh8Fjp6uF0nS7PAOZEmSYSBJMgwkSRgGkiQMA0kShoEkCcNAkoRhIEnCMJAkYRhIkjAMJEkYBpIkDANJEoaBJAnDQJKEYSBJwjCQJGEYSJIwDCRJGAaSJAwDSRKGgSQJw0CShGEgScIwkCRhGEiSGCAMkmxK8mySB/pqByfZluSR9ry41ZPk8iRjSe5LclzfOuva+EeSrOurH5/k/rbO5Uky029SkrRng+wZXAOs2a22EbilqlYAt7R5gNOBFe2xAbgSeuEBXAycCJwAXDwRIG3M+X3r7f5akqRZNm0YVNX/BnbtVl4LbG7Tm4Ez++rXVs/twKIkhwGnAduqaldVPQdsA9a0ZW+tqturqoBr+7YlSZoj+3rOYElVPdWmnwaWtOmlwJN943a02p7qOyapTyrJhiSjSUbHx8f3sXVJ0u5e9wnk9om+ZqCXQV7rqqpaVVWrRkZG5uIlJWko7GsYPNMO8dCen231ncDhfeOWtdqe6ssmqUuS5tC+hsEWYOKKoHXAjX31c9tVRauBF9rhpK3AqUkWtxPHpwJb27IXk6xuVxGd27ctSdIcWTjdgCR/DPwKcEiSHfSuCroUuCHJeuAJ4Kw2/CbgDGAMeBk4D6CqdiX5DHBXG/fpqpo4Kf1xelcsHQTc3B6SpDk0bRhU1TlTLDplkrEFXDDFdjYBmyapjwJHT9eHJGn2eAeyJMkwkCQZBpIkDANJEoaBJAnDQJKEYSBJwjCQJGEYSJIwDCRJGAaSJAwDSRKGgSQJw0CShGEgScIwkCRhGEiSMAwkSRgGkiQMA0kShoEkCcNAkoRhIEnCMJAkYRhIkjAMJEnsR2GQZE2Sh5OMJdnYdT+SNEz2izBIsgC4AjgdWAmck2Rlt11J0vDYL8IAOAEYq6pHq+oV4Hpgbcc9SdLQWNh1A81S4Mm++R3AibsPSrIB2NBmf5Dk4TnobRgcAnyv6yamk8933YE64t/nzHnHVAv2lzAYSFVdBVzVdR/zTZLRqlrVdR/SZPz7nBv7y2GincDhffPLWk2SNAf2lzC4C1iR5MgkBwJnA1s67kmShsZ+cZioql5NciGwFVgAbKqq7R23NUw89Kb9mX+fcyBV1XUPkqSO7S+HiSRJHTIMJEmGgSTJMJAksZ9cTaS5l2QJ8Dng71TV6e27oN5fVVd33JqGWJKD97S8qnbNVS/DxquJhlSSm4EvA/+uqo5JshC4p6r+fsetaYgleQwoIJMsrqr6u3Pc0tBwz2B4HVJVNyS5CH56r8drXTel4VZVR3bdw7DynMHw+mGSt9P7FEaS1cAL3bYk9aTnN5P8hzZ/RJITuu5rPvMw0ZBKchzwBeBo4AFgBPhIVd3XaWMSkORK4CfAyVX1niSLgT+rqvd13Nq85WGiIVVV303yj4B30Ts++3BV/bjjtqQJJ1bVcUnuAaiq59r3lmmWGAbD7QRgOb2/g+OSUFXXdtuSBMCP2y8gThzGHKG3p6BZYhgMqSTXAb8M3AtMnDguwDDQ/uBy4GvAoUkuAT4C/PtuW5rfPGcwpJI8BKws/wC0n0rybuAUeocxb6mqhzpuaV7zaqLh9QDwS103IU0myS8Dj1XVFfT+Vj+YZFHHbc1r7hkMqSS3AccCdwI/mqhX1Yc7a0pqktwLrKJ3Tusb9H7s6qiqOqPLvuYzzxkMr9/rugFpD37SboT8DeCLVfWFiSuLNDsMgyFVVd/uugdpD36c5BzgXODXW+2ADvuZ9zxnMGSSfKc9v5Tkxb7HS0le7Lo/qTkPeD9wSVU9luRI4LqOe5rXPGcgab+U5CDgiKp6uOtehoF7BkMmycF7enTdnwSQ5Nfp3QPzzTZ/bJIt3XY1v7lnMGT8imC9ESS5GzgZ+FZVvbfVHqiqo7vtbP7yBPKQ8SuC9Qbx46p6Iflbn1n8OopZZBgMsSQfBj7QZr9VVV/vsh+pz/Yk/xRYkGQF8DvA/+24p3nNcwZDKsmlwCeAB9vjE0k+121X0k/9NnAUvRsi/xh4Efhkpx3Nc54zGFJJ7gOOraqftPkF9H728h9025mkLniYaLgtAiZ+YPxtXTYiAST5/ar6ZJL/Rfv66n5+XcrsMQyG138G7mnfURR65w42dtuS9NMby/5bp10MIQ8TDbEkhwETPyN4Z1U93WU/Ur/2gzZU1XjXvQwDTyAPqSQnAS9W1RbgrcCnkryj47Ykkvxeku8BDwN/mWQ8yX/suq/5zjAYXlcCLyc5Bvhd4K/wV87UsSS/C5wEvK+qDq6qxcCJwElJ/lW33c1vhsHwerX9ytla4Ir2IyK/2HFP0seAc6rqsYlCVT0K/Ca9bzDVLPEE8vB6KclF9P4n+0CSN+FXBKt7B1TV93YvVtV4Ev8+Z5F7BsPrn9C7oWd9O3G8DPiv3bYk8co+LtPr5NVEkvYbSV4DfjjZIuDnqsq9g1liGAypJKuBLwDvAQ4EFgA/qCpvPpOGkIeJhtcXgXOAR4CDgN8CvtRpR5I6YxgMsaoaAxZU1WtV9WVgTdc9SeqGVxMNr5eTHAj8eZL/AjyFHw6koeX//MPrY/T++19A74TdMuAfd9qRpM64ZzBkkqwFlrWbzEjybeBQet8Q+f+AsQ7bk9QR9wyGz6eA/h8WfzNwPPArwL/soiFJ3XPPYPgcWFVP9s1/p6p2AbuSvKWrpiR1yz2D4bO4f6aqLuybHZnjXiTtJwyD4XNHkvN3Lyb5F8CdHfQjaT/gHchDJsmhwP+k971E323l4+mdOzizqp7pqjdJ3TEMhlSSk4Gj2uz2qrq1y34kdcswkCR5zkCSZBhIkjAMJEkYBpIkDANJEvD/AWTsJwkR+YULAAAAAElFTkSuQmCC\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Categorical - city\n",
        "feature = categorical_data[2]\n",
        "count = df[feature].value_counts()\n",
        "percent = 100*df[feature].value_counts(normalize=True)\n",
        "df_cat = pd.DataFrame({'Jumlah Sampel':count, 'Persentase':percent.round(1)})\n",
        "print(df_cat)\n",
        "count.plot(kind='bar', title=feature)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 664
        },
        "id": "u2D_9mLaJrmt",
        "outputId": "d95989d1-46b3-48dd-ffe0-160c80b0dec1"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "             Jumlah Sampel  Persentase\n",
            "Warszawa              7130         6.6\n",
            "Łódź                  2901         2.7\n",
            "Kraków                2571         2.4\n",
            "Wrocław               2462         2.3\n",
            "Poznań                2086         1.9\n",
            "...                    ...         ...\n",
            "Czciradz                 1         0.0\n",
            "Mirkowiczki              1         0.0\n",
            "Lubogoszcz               1         0.0\n",
            "Skałka                   1         0.0\n",
            "Bledzew                  1         0.0\n",
            "\n",
            "[4224 rows x 2 columns]\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7fd90f855550>"
            ]
          },
          "metadata": {},
          "execution_count": 20
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Dikarenakan banyaknya jenis kota pada Dataset, bisa dianggap bahwa data kota digantikan dengan data provinsi yang ada.\n",
        "df = df.drop(['city'], axis=1)"
      ],
      "metadata": {
        "id": "MhvYScEpKlPm"
      },
      "execution_count": 21,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Categorical - province\n",
        "feature = categorical_data[3]\n",
        "count = df[feature].value_counts()\n",
        "percent = 100*df[feature].value_counts(normalize=True)\n",
        "df_cat = pd.DataFrame({'Jumlah Sampel':count, 'Persentase':percent.round(1)})\n",
        "print(df_cat)\n",
        "count.plot(kind='bar', title=feature)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 814
        },
        "id": "e-vMlFFGJvrs",
        "outputId": "ae8b0ee5-1abe-4b54-8f71-0b45d19a0c9e"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                          Jumlah Sampel  Persentase\n",
            "Mazowieckie                       20335        18.9\n",
            "Śląskie                           14929        13.9\n",
            "Wielkopolskie                     12891        12.0\n",
            "Małopolskie                        8829         8.2\n",
            "Dolnośląskie                       8094         7.5\n",
            "Łódzkie                            7105         6.6\n",
            "Pomorskie                          7002         6.5\n",
            "Kujawsko-pomorskie                 4907         4.6\n",
            "Lubelskie                          4327         4.0\n",
            "Zachodniopomorskie                 3658         3.4\n",
            "Podkarpackie                       3224         3.0\n",
            "Świętokrzyskie                     3106         2.9\n",
            "Warmińsko-mazurskie                2767         2.6\n",
            "Lubuskie                           2538         2.4\n",
            "Podlaskie                          1928         1.8\n",
            "Opolskie                           1914         1.8\n",
            "Moravian-Silesian Region             35         0.0\n",
            "Berlin                                3         0.0\n",
            "Wiedeń                                2         0.0\n",
            "Niedersachsen                         1         0.0\n",
            "(                                     1         0.0\n",
            "Nordrhein-Westfalen                   1         0.0\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7fd90b234130>"
            ]
          },
          "metadata": {},
          "execution_count": 22
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Dengan Melihat Pemerataan Data, maka Provinsi dengan Total Data < 2000 akan dihapus.\n",
        "df = df.loc[df['province'].isin(count.index[count > 2000])]\n",
        "\n",
        "feature = categorical_data[3]\n",
        "count = df[feature].value_counts()\n",
        "percent = 100*df[feature].value_counts(normalize=True)\n",
        "df_cat = pd.DataFrame({'Jumlah Sampel':count, 'Persentase':percent.round(1)})\n",
        "print(df_cat)\n",
        "count.plot(kind='bar', title=feature)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 659
        },
        "id": "c_YSl-YUKl9W",
        "outputId": "4590cd1c-c69e-4406-f9ef-69d9c274ab39"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                     Jumlah Sampel  Persentase\n",
            "Mazowieckie                  20335        19.6\n",
            "Śląskie                      14929        14.4\n",
            "Wielkopolskie                12891        12.4\n",
            "Małopolskie                   8829         8.5\n",
            "Dolnośląskie                  8094         7.8\n",
            "Łódzkie                       7105         6.9\n",
            "Pomorskie                     7002         6.8\n",
            "Kujawsko-pomorskie            4907         4.7\n",
            "Lubelskie                     4327         4.2\n",
            "Zachodniopomorskie            3658         3.5\n",
            "Podkarpackie                  3224         3.1\n",
            "Świętokrzyskie                3106         3.0\n",
            "Warmińsko-mazurskie           2767         2.7\n",
            "Lubuskie                      2538         2.4\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7fd90f3d6a60>"
            ]
          },
          "metadata": {},
          "execution_count": 23
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Numerical\n",
        "df.hist(bins=50, figsize=(15, 10))\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 621
        },
        "id": "gyL8xWVcSsS0",
        "outputId": "e4500500-0c3a-4097-c0ab-9b59d5f77d00"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1080x720 with 4 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA38AAAJcCAYAAABJ+B2jAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nOzde5xlVX3n/c9XWhTxAoipIKBNxtYMSkTtAIm51MgEGkzSZKIOhoRGSZhMMDETYmhMnpCoGJwnxkHj5SGCQoIiQR2IoKSj1GMuAwKKXKO2XKQ7KMrV1ohp85s/zio8VFd1V9ftnFP78369zqv2WXvtfX5r1+na/dt7rbVTVUiSJEmSlrfHDDoASZIkSdLiM/mTJEmSpA4w+ZMkSZKkDjD5kyRJkqQOMPmTJEmSpA4w+ZMkSZKkDjD5kyRJ0khJ8owkW5Ls0t5PJPnVQcclDbsVgw5AkiRJ2hlV9RXgiYOOQxo13vmTRlgSL+BIkiRpVkz+pEWS5HVJPjyl7O1JzkrylCTnJLk7yeYkb+rruvIfknwqyb1JvpHkgiR79O3jjiSnJrkB+JYJoCRpuWjnuNcluSHJt9q5cizJx5N8M8nfJdkzycokNdM5MMmrk9ya5P4kVyR5Zt+6s5LcleShJNcl+cm+dbslOa9td2uS30uyqW/905N8OMnXk9ye5LcW94hIC8vkT1o8fwWsmUzc2gnqWOB84P3AVuBZwAuAI4DJsQoB/gR4OvAfgf2BP5qy71cCLwX2qKqti9kISZKW2C8CPwM8G/g54OPA64Gn0fu/63YTriRrW/3/0rb5e+CDfVWuAQ4G9gI+APx1kse3dacDK4EfajH8ct9+HwP8DfB5YF/gcOC3kxw555ZKS8zkT1okVXU38Gng5a1oDfANYBNwNPDbVfWtqroHeBu9xJCq2lhVG6rq4ar6OvBnwE9P2f3bq+quqvrXpWiLJElL6B1V9bWq2kwvcbu6qj5XVd8BPkrvoun2/DrwJ1V1a7tA+mbg4Mm7f1X1V1V1b1Vtraq3Ao8DntO2fQXw5qq6v6o2AW/v2++PAk+rqjdU1Xer6jbgL2jnb2kU2F1MWlznAf+d3snhl4G/BJ4JPBa4O8lkvccAdwEkGQPOAn4SeFJbd/+U/d612IFLkjQgX+tb/tdp3u9oopdnAmcleWtfWejdrbszye8CJ9LrYVPAk4G9W72n8+hzbP/yM4GnJ3mgr2wXegmqNBJM/qTF9b+Bdyd5HvCzwO8B/wY8DOw9Q5fNN9M7GR1UVfclOQb48yl1ahFjliRplN0FnFFVF0xd0cb3/R69Lps3V9W/J7mfXnIIcDewH3BLe7//lP3eXlWrFi1yaZHZ7VNaRK2LysX0xhR8pqq+0rqD/i3w1iRPTvKYNsnLZNfOJwFbgAeT7Au8biDBS5I0mt4DnJbkuQBtkrXJIRhPojfm/uvAiiR/SO/O36SL2rZ7tnPwa/rWfQb4Zpt0bbckuyR5XpIfXfQWSQvE5E9afOcBB9Hr8jnpeGBXelcW76eXIO7T1v0x8ELgQeAy4CNLFqkkSSOuqj4KvAW4MMlDwE3AUW31FcAngC8CdwLf4dFdO99Ab2z+7cDf0Ts/P9z2+z16vXgObuu/AbwXeMritkhaOKmy95i0mJI8A/hn4Aer6qFBxyNJkmYnyX8Hjq2qqROvSSPJO3/SImrTQv8OcKGJnyRJwy3JPkle3IZkPAc4hd4Mo9Ky4IQv0iJJsju9GcrupPeYB0mSNNx2Bf4/4ADgAeBC4F0DjUhaQHb7lCRJkqQOsNunJEmSJHWAyZ8kSZIkdcDIjvnbe++9a+XKldOu+9a3vsXuu+++tAEtEGMfnFGO39gHY5Rjh6WL/7rrrvtGVT1t0T9IC2Z759jZGPV/GzvDti5fXWqvbR1dO3uOHdnkb+XKlVx77bXTrpuYmGB8fHxpA1ogxj44oxy/sQ/GKMcOSxd/kjsX/UO0oLZ3jp2NUf+3sTNs6/LVpfba1tG1s+dYu31KkiRJUgeY/EmSJElSB5j8SZIkSVIHmPxJkiRJUgeY/EmSJElSB5j8SZI0IEn2T3JlkluS3Jzkta38j5JsTnJ9ex3dt81pSTYm+UKSI/vK17SyjUnW95UfkOTqVv6hJLsubSslScPC5E+SpMHZCpxSVQcChwEnJzmwrXtbVR3cXpcDtHXHAs8F1gDvSrJLkl2AdwJHAQcCr+zbz1vavp4F3A+cuFSNkyQNF5M/SZIGpKrurqrPtuVvArcC+25nk7XAhVX1cFXdDmwEDmmvjVV1W1V9F7gQWJskwEuAi9v25wHHLE5rJEnDzuRPkqQhkGQl8ALg6lb0miQ3JDk3yZ6tbF/grr7NNrWymcqfCjxQVVunlEuSOmjFoAOQJC2clesvm3HdHWe+dAkj0c5I8kTgw8BvV9VDSd4NvBGo9vOtwKsXOYaTgJMAxsbGmJiYmPO+tmzZMq/tp7px84Mzrjto36cs2OfMxUK3dZh1qa3Qrfba1u7YYfKX5FzgZ4F7qup5rez/BX4O+C7wZeBVVfVAW3cavfEE3wN+q6quaOVrgLOAXYD3VtWZrfwAet1TngpcB/xK67IiSdKyl+Sx9BK/C6rqIwBV9bW+9X8BfKy93Qzs37f5fq2MGcrvBfZIsqLd/euv/yhVdTZwNsDq1atrfHx8zm2amJhgPttPdcL2Lmoct3CfMxcL3dZh1qW2Qrfaa1u7YzbdPt9Pb1B5vw3A86rqR4AvAqeBA9ElSdoZbUzeOcCtVfVnfeX79FX7BeCmtnwpcGySx7WLp6uAzwDXAKvazJ670jsXX1pVBVwJvKxtvw64ZDHbJEkaXju881dVn27jEPrL/rbv7VV8/6TyyEB04PYkkwPRoQ1EB0gyORD9VnoD0X+p1TkP+CPg3XNpjCQtFLtPaom8GPgV4MYk17ey19O7SHowvW6fdwD/DaCqbk5yEXALvZlCT66q7wEkeQ1wBb0eNudW1c1tf6cCFyZ5E/A5esmmJKmDFmLM36uBD7Xlfeklg5P6B5ZPHYh+KA5ElyR1WFX9A5BpVl2+nW3OAM6Ypvzy6bZrF14PmVouSeqeeSV/SX6f3pXHCxYmnB1+3qwGo4/yQE5jH5xRjt/YF94pB22dcd1kvMMY+2zinjSM8UuSpMUz5+QvyQn0JoI5vI0pgEUciA6zH4w+ygM5jX1wRjl+Y194s5lgYhhj35mJMYYxfkmStHjm9Jy/NnPn7wE/X1Xf7lvlQHRJkiRJGkI7TP6SfBD4P8BzkmxKciLw58CTgA1Jrk/yHugNRAcmB6J/gjYQvd3VmxyIfitw0ZSB6L/TJod5Kg5ElyRJkqQFN5vZPl85TfGMCZoD0SVpYTjjqCRJWkgLMdunJAmTNUmSNNzmNOZPkiRJkjRaTP4kSZIkqQNM/iRJkiSpA0z+JEmSJKkDTP4kSZIkqQNM/iRJkiSpA0z+JEmSJKkDTP4kSZIkqQNM/iRJkiSpA0z+JEmSJKkDTP4kSZIkqQNM/iRJkiSpA0z+JEmSJKkDTP4kSZIkqQNM/iRJkiSpA1YMOgBJkiSAlesvG3QIkrSseedPkiRJkjrA5E+SJEmSOsDkT5IkSZI6wORPkiRJkjrA5E+SJEmSOsDkT5IkSZI6wORPkiRJkjrA5E+SJEmSOsCHvEuSpAV14+YHOWGGB7bfceZLlzgaSdIk7/xJkiRJUgeY/EmSJElSB+ww+UtybpJ7ktzUV7ZXkg1JvtR+7tnKk+TtSTYmuSHJC/u2WdfqfynJur7yFyW5sW3z9iRZ6EZKkiRJUtfN5s7f+4E1U8rWA5+sqlXAJ9t7gKOAVe11EvBu6CWLwOnAocAhwOmTCWOr82t92039LEmSJEnSPO0w+auqTwP3TSleC5zXls8DjukrP796rgL2SLIPcCSwoaruq6r7gQ3AmrbuyVV1VVUVcH7fviRJkiRJC2SuY/7GqurutvxVYKwt7wvc1VdvUyvbXvmmacolSVr2kuyf5MoktyS5OclrW7nDKyRJC27ej3qoqkpSCxHMjiQ5iV53UsbGxpiYmJi23pYtW2ZcN+yMfXBGOX5jX3inHLR1xnWT8U6NfTbbLHQM89lmWI99x2wFTqmqzyZ5EnBdkg3ACfSGV5yZZD294RWn8ujhFYfSGzpxaN/witVAtf1c2nrbTA6vuBq4nN7wio8vYRslSUNirsnf15LsU1V3t66b97TyzcD+ffX2a2WbgfEp5ROtfL9p6k+rqs4GzgZYvXp1jY+PT1tvYmKCmdYNO2MfnFGO39gX3kzPKAO447hxYNvYZ7PNQscwn22G9dh3SetFc3db/maSW+n1gFnL98+b59E7Z55K3/AK4Kokk8MrxmnDKwBaArkmyQRteEUrnxxeYfInSR00126flwKTXUrWAZf0lR/fuqUcBjzYTmxXAEck2bN1XTkCuKKteyjJYa0byvF9+5IkqTOSrAReQO8OncMrJEkLbod3/pJ8kN4Vxb2TbKLXreRM4KIkJwJ3Aq9o1S8HjgY2At8GXgVQVfcleSNwTav3hsmrk8Bv0JtRdDd6VyK9GilJ6pQkTwQ+DPx2VT3UPyxvqYZXzHZoxWyM7TZzF+Tt7Xd73ZZnMuiuy13qPt2ltkK32mtbu2OHyV9VvXKGVYdPU7eAk2fYz7nAudOUXws8b0dxSJIWx8rtdRU986VLGEk3JXksvcTvgqr6SCte8uEVsx1aMRvvuOAS3nrj9P/F2F4X6O11W57JXLpUL6QudZ/uUluhW+21rd0x126fkiRpntqQh3OAW6vqz/pWObxCkrTg5j3bpyRJmrMXA78C3Jjk+lb2ehxeIUlaBCZ/kiQNSFX9AzDTc/ccXiFJWlB2+5QkSZKkDjD5kyRJkqQOMPmTJEmSpA4w+ZMkSZKkDjD5kyRJkqQOMPmTJEmSpA4w+ZMkSZKkDjD5kyRJkqQOMPmTJEmSpA4w+ZMkSZKkDjD5kyRJkqQOMPmTJEmSpA4w+ZMkSZKkDjD5kyRJkqQOMPmTJEmSpA4w+ZMkSZKkDjD5kyRJkqQOMPmTJEmSpA4w+ZMkSZKkDjD5kyRJkqQOMPmTJEmSpA5YMegAJElSd6xcf9mgQ5CkzvLOnyRJkiR1gMmfJEmSJHXAvJK/JP8jyc1JbkrywSSPT3JAkquTbEzyoSS7trqPa+83tvUr+/ZzWiv/QpIj59ckSZIkSdJUc07+kuwL/BawuqqeB+wCHAu8BXhbVT0LuB84sW1yInB/K39bq0eSA9t2zwXWAO9Ksstc45IkSZIkbWu+3T5XALslWQE8AbgbeAlwcVt/HnBMW17b3tPWH54krfzCqnq4qm4HNgKHzDMuSZIkSVKfOSd/VbUZ+FPgK/SSvgeB64AHqmprq7YJ2Lct7wvc1bbd2uo/tb98mm0kSZIkSQtgzo96SLInvbt2BwAPAH9Nr9vmoklyEnASwNjYGBMTE9PW27Jly4zrhp2xD84ox2/sC++Ug7bOuG4y3qmxz2abhYrhHRdcMsM2M+9vagyT8S903JIkaTjN5zl//xm4vaq+DpDkI8CLgT2SrGh39/YDNrf6m4H9gU2tm+hTgHv7yif1b/MoVXU2cDbA6tWra3x8fNrAJiYmmGndsDP2wRnl+I194Z2wnWeR3XHcOLBt7LPZZqFimIupMUzGv9BxS5Kk4TSfMX9fAQ5L8oQ2du9w4BbgSuBlrc46YPLy9KXtPW39p6qqWvmxbTbQA4BVwGfmEZckSZIkaYo53/mrqquTXAx8FtgKfI7eXbnLgAuTvKmVndM2OQf4yyQbgfvozfBJVd2c5CJ6ieNW4OSq+t5c45IkSZIkbWs+3T6pqtOB06cU38Y0s3VW1XeAl8+wnzOAM+YTiyRJkiRpZvN91IMkSZIkaQSY/EmSJElSB5j8SZIkSVIHmPxJkjQgSc5Nck+Sm/rK/ijJ5iTXt9fRfetOS7IxyReSHNlXvqaVbUyyvq/8gCRXt/IPJdl16VonSRo2Jn+SJA3O+4E105S/raoObq/LAZIcSG+m7Oe2bd6VZJckuwDvBI4CDgRe2eoCvKXt61nA/cCJi9oaSdJQM/mTJGlAqurT9B5/NBtrgQur6uGquh3YSG927UOAjVV1W1V9F7gQWNuewfsS4OK2/XnAMQvaAEnSSDH5kyRp+LwmyQ2tW+ierWxf4K6+Opta2UzlTwUeqKqtU8olSR01r+f8SZKkBfdu4I1AtZ9vBV692B+a5CTgJICxsTEmJibmvK+x3eCUg7buuOICmE+cC2HLli0Dj2GpdKmt0K322tbuMPmTJGmIVNXXJpeT/AXwsfZ2M7B/X9X9WhkzlN8L7JFkRbv7119/us89GzgbYPXq1TU+Pj7nNrzjgkt4641L81+MO44bX5LPmcnExATzOVajpEtthW6117Z2h90+JUkaIkn26Xv7C8DkTKCXAscmeVySA4BVwGeAa4BVbWbPXelNCnNpVRVwJfCytv064JKlaIMkaTh550+SpAFJ8kFgHNg7ySbgdGA8ycH0un3eAfw3gKq6OclFwC3AVuDkqvpe289rgCuAXYBzq+rm9hGnAhcmeRPwOeCcJWqaJGkImfxJkjQgVfXKaYpnTNCq6gzgjGnKLwcun6b8NnqzgUqSZLdPSZIkSeoCkz9JkiRJ6gCTP0mSJEnqAJM/SZIkSeoAkz9JkiRJ6gCTP0mSJEnqAJM/SZIkSeoAkz9JkiRJ6gCTP0mSJEnqAJM/SZIkSeoAkz9JkiRJ6gCTP0mSJEnqAJM/SZIkSeoAkz9JkiRJ6gCTP0mSJEnqAJM/SZIkSeqAeSV/SfZIcnGSf05ya5IfS7JXkg1JvtR+7tnqJsnbk2xMckOSF/btZ12r/6Uk6+bbKEmSJEnSo62Y5/ZnAZ+oqpcl2RV4AvB64JNVdWaS9cB64FTgKGBVex0KvBs4NMlewOnAaqCA65JcWlX3zzM2SZK0zK1cf9m05Xec+dIljkSSht+c7/wleQrwU8A5AFX13ap6AFgLnNeqnQcc05bXAudXz1XAHkn2AY4ENlTVfS3h2wCsmWtckiRJkqRtzafb5wHA14H3Jflckvcm2R0Yq6q7W52vAmNteV/grr7tN7WymcolSZIkSQtkPt0+VwAvBH6zqq5Ocha9Lp6PqKpKUvMJsF+Sk4CTAMbGxpiYmJi23pYtW2ZcN+yMfXBGOX5jX3inHLR1xnWT8U6NfTbbLFQMczE1hsn4FzpuSZI0nOaT/G0CNlXV1e39xfSSv68l2aeq7m7dOu9p6zcD+/dtv18r2wyMTymfmO4Dq+ps4GyA1atX1/j4+HTVmJiYYKZ1w87YB2eU4zf2hXfCDOOIAO44bhzYNvbZbLNQMczF1Bgm41/ouCVJ0nCac/JXVV9NcleS51TVF4DDgVvaax1wZvt5SdvkUuA1SS6kN+HLgy1BvAJ48+SsoMARwGlzjUuSFtvkBBOnHLR1wRM0SZKkxTLf2T5/E7igzfR5G/AqeuMIL0pyInAn8IpW93LgaGAj8O1Wl6q6L8kbgWtavTdU1X3zjEuSJEmS1GdeyV9VXU/vEQ1THT5N3QJOnmE/5wLnzicWSZIkSdLM5vWQd0mSJEnSaDD5kyRJkqQOMPmTJEmSpA4w+ZMkSZKkDjD5kyRJkqQOmO+jHiRpKKzc3oPKz3zpEkYiSZI0nLzzJ0mSJEkdYPInSZIkSR1g8idJkiRJHWDyJ0mSJEkdYPInSZIkSR3gbJ+SOmt7M4R2KQYNVpJzgZ8F7qmq57WyvYAPASuBO4BXVNX9SQKcBRwNfBs4oao+27ZZB/xB2+2bquq8Vv4i4P3AbsDlwGurqpakcZKkoeKdP0mSBuv9wJopZeuBT1bVKuCT7T3AUcCq9joJeDc8kiyeDhwKHAKcnmTPts27gV/r227qZ0mSOsLkT5KkAaqqTwP3TSleC5zXls8DjukrP796rgL2SLIPcCSwoaruq6r7gQ3AmrbuyVV1Vbvbd37fviRJHWPyJ0nS8Bmrqrvb8leBsba8L3BXX71NrWx75ZumKZckdZBj/iRJGmJVVUkWfYxekpPodSVlbGyMiYmJOe9rbDc45aCtCxTZ3Mwn/p2xZcuWJfusQetSW6Fb7bWt3WHyJ0lLwIldtJO+lmSfqrq7dd28p5VvBvbvq7dfK9sMjE8pn2jl+01TfxtVdTZwNsDq1atrfHx8umqz8o4LLuGtNw72vxh3HDe+JJ8zMTHBfI7VKOlSW6Fb7bWt3WG3T0mShs+lwLq2vA64pK/8+PQcBjzYuodeARyRZM820csRwBVt3UNJDmszhR7fty9JUsd450+SpAFK8kF6d+32TrKJ3qydZwIXJTkRuBN4Rat+Ob3HPGyk96iHVwFU1X1J3ghc0+q9oaomJ5H5Db7/qIePt5ckqYNM/iRJGqCqeuUMqw6fpm4BJ8+wn3OBc6cpvxZ43nxilCQtD3b7lCRJkqQOMPmTJEmSpA4w+ZMkSZKkDjD5kyRJkqQOMPmTJEmSpA4w+ZMkSZKkDvBRD5KWvZXrLxt0CJIkSQPnnT9JkiRJ6oB5J39JdknyuSQfa+8PSHJ1ko1JPpRk11b+uPZ+Y1u/sm8fp7XyLyQ5cr4xSZIkSZIebSHu/L0WuLXv/VuAt1XVs4D7gRNb+YnA/a38ba0eSQ4EjgWeC6wB3pVklwWIS5IkSZLUzCv5S7If8FLgve19gJcAF7cq5wHHtOW17T1t/eGt/lrgwqp6uKpuBzYCh8wnLkmSJEnSo833zt//An4P+Pf2/qnAA1W1tb3fBOzblvcF7gJo6x9s9R8pn2YbSZIkSdICmPNsn0l+Frinqq5LMr5wIW33M08CTgIYGxtjYmJi2npbtmyZcd2wM/bBGeX4jR1OOWjrjistsLHdBvO5czX1OE8e++21YVS/V5IkaVvzedTDi4GfT3I08HjgycBZwB5JVrS7e/sBm1v9zcD+wKYkK4CnAPf2lU/q3+ZRqups4GyA1atX1/j4+LSBTUxMMNO6YWfsgzPK8Rs7nDCAxzmcctBW3nrj6Dwx547jxh/1fvLYb+/YTd1GkiSNrjl3+6yq06pqv6paSW/Clk9V1XHAlcDLWrV1wCVt+dL2nrb+U1VVrfzYNhvoAcAq4DNzjUuSJEmStK3FuGR9KnBhkjcBnwPOaeXnAH+ZZCNwH72Ekaq6OclFwC3AVuDkqvreIsQlSZIkSZ21IMlfVU0AE235NqaZrbOqvgO8fIbtzwDOWIhYJEmSJEnbWojn/EmSJEmShpzJnyRJkiR1gMmfJEmSJHWAyZ8kSZIkdYDJnyRJkiR1gMmfJEmSJHWAyZ8kSZIkdYDJnyRJkiR1gMmfJEmSJHWAyZ8kSZIkdYDJnyRJkiR1gMmfJEmSJHWAyZ8kSZIkdYDJnyRJkiR1gMmfJEmSJHWAyZ8kSZIkdYDJnyRJkiR1gMmfJEmSJHWAyZ8kSZIkdYDJnyRJQyjJHUluTHJ9kmtb2V5JNiT5Uvu5ZytPkrcn2ZjkhiQv7NvPulb/S0nWDao9kqTBWzHoACRJS2Pl+sse9f6Ug7ZywpQyDZ3/VFXf6Hu/HvhkVZ2ZZH17fypwFLCqvQ4F3g0cmmQv4HRgNVDAdUkurar7l7IRkqTh4J0/SZJGx1rgvLZ8HnBMX/n51XMVsEeSfYAjgQ1VdV9L+DYAa5Y6aEnScDD5kyRpOBXwt0muS3JSKxurqrvb8leBsba8L3BX37abWtlM5ZKkDrLbpyRJw+knqmpzkh8ANiT55/6VVVVJaqE+rCWYJwGMjY0xMTEx532N7dbrVjxI84l/Z2zZsmXJPmvQutRW6FZ7bWt3mPxJkjSEqmpz+3lPko8ChwBfS7JPVd3dunXe06pvBvbv23y/VrYZGJ9SPjHD550NnA2wevXqGh8fn67arLzjgkt4642D/S/GHceNL8nnTExMMJ9jNUq61FboVntta3fY7VOSpCGTZPckT5pcBo4AbgIuBSZn7FwHXNKWLwWOb7N+HgY82LqHXgEckWTPNjPoEa1MktRB3vmTJGn4jAEfTQK9c/UHquoTSa4BLkpyInAn8IpW/3LgaGAj8G3gVQBVdV+SNwLXtHpvqKr7lq4ZkqRhYvInSdKQqarbgOdPU34vcPg05QWcPMO+zgXOXegYJUmjZ87dPpPsn+TKJLckuTnJa1u5D6CVJEmSpCEznzF/W4FTqupA4DDg5CQH8v0H0K4CPtnew6MfQHsSvQfQ0vcA2kPpDWY/fTJhlCRJkiQtjDknf1V1d1V9ti1/E7iV3rODfACtJEmSJA2ZBZntM8lK4AXA1fgAWkmSJEkaOvOe8CXJE4EPA79dVQ+1mcmAwT2AdpQf3mjsgzPK8Rv7YB4oPQwPsp6P2cQ/qt8raeX6y2Zcd8eZL13CSCRpeMwr+UvyWHqJ3wVV9ZFWPPAH0I7ywxuNfXBGOX5jhxO28x+9xXLKQVsH/iDr+ZhN/Ev1oGxJkrT45jPbZ4BzgFur6s/6VvkAWkmSJEkaMvO5ZP1i4FeAG5Nc38peD5yJD6CVJEmSpKEy5+Svqv4ByAyrfQCtJEmSJA2RBZntU5IkSZI03EZ3pgJJy9ZMs/Q5Q58kSdLceedPkiRJkjrA5E+SJEmSOsBun5JGxvYe2ixJkqTt886fJEmSJHWAyZ8kSZIkdYDJnyRJkiR1gMmfJEmSJHWAyZ8kSZIkdYDJnyRJkiR1gMmfJEmSJHWAyZ8kSZIkdYDJnyRJkiR1gMmfJEmSJHWAyZ8kSZIkdYDJnyRJkiR1gMmfJEmSJHWAyZ8kSZIkdYDJnyRJkiR1wIpBByBJkrSUVq6/bMZ1d5z50iWMRJKWlnf+JEmSJKkDTP4kSZIkqQNM/iRJkiSpAxzzJ2kgJsfcnHLQVk7YzvgbSZIkLQzv/EmSJElSB3jnT9K8bW/mPEmSJA0H7/xJkiRJUgcMzZ2/JGuAs4BdgPdW1ZkDDkmSpGXBc+zszdSTwef/SVoOhuLOX5JdgHcCRwEHAq9McuBgo5IkafR5jpUkTRqWO3+HABur6jaAJBcCa4FbBhqV1EGO35OWHc+xkiRgeJK/fYG7+t5vAg4dUCzL0kL/h34hu79sL7ZR7WYz1zbN9ffk4xIkbYfn2AUw09/nxfj7O6rnPqzxahkAACAASURBVEnDL1U16BhI8jJgTVX9anv/K8ChVfWaKfVOAk5qb58DfGGGXe4NfGORwl1sxj44oxy/sQ/GKMcOSxf/M6vqaUvwOZrGIpxjZ2PU/23sDNu6fHWpvbZ1dO3UOXZY7vxtBvbve79fK3uUqjobOHtHO0tybVWtXrjwlo6xD84ox2/sgzHKscPox69ZW9Bz7Gx06btlW5evLrXXtnbHUEz4AlwDrEpyQJJdgWOBSwcckyRJy4HnWEkSMCR3/qpqa5LXAFfQm4b63Kq6ecBhSZI08jzHSpImDUXyB1BVlwOXL9DuFqTbyoAY++CMcvzGPhijHDuMfvyapQU+x85Gl75btnX56lJ7bWtHDMWEL5IkSZKkxTUsY/4kSZIkSYtoJJK/JOcmuSfJTX1lz0/yf5LcmORvkjy5la9M8q9Jrm+v9/Rt86JWf2OStyfJMMXe1v1IW3dzW//4QcW+s/EnOa7vuF+f5N+THDyo+Hcy9scmOa+V35rktL5t1iT5Qot9/WLHPYfYd03yvlb++STjfdsM4rjvn+TKJLe07/FrW/leSTYk+VL7uWcrT4ttY5Ibkrywb1/rWv0vJVk3hLH/cPudPJzkd6fsaxDfm52N/7h2zG9M8k9Jnj/I+DV6dvQ9SfK4JB9q669OsnLpo1wYs2jrCUm+3ncO/NVBxLkQpjsHTVk/49/tUTOLto4nebDv9/qHSx3jQpjp/DClzrL4vc6yrcvi9zonVTX0L+CngBcCN/WVXQP8dFt+NfDGtryyv96U/XwGOAwI8HHgqCGLfQVwA/D89v6pwC6Din1n45+y3UHAl0fo2P8ScGFbfgJwR/su7QJ8GfghYFfg88CBQxb7ycD72vIPANcBjxngcd8HeGFbfhLwReBA4H8C61v5euAtbfnoFltarFe38r2A29rPPdvynkMW+w8APwqcAfxu334G9b3Z2fh/fPKYAkf1HfuBxO9rtF6z+Z4AvwG8py0fC3xo0HEvYltPAP580LEuUHu3OQdNWT/t3+1RfM2irePAxwYd5wK0c9rzw3L8vc6yrcvi9zqX10jc+auqTwP3TSl+NvDptrwB+MXt7SPJPsCTq+qq6v3WzweOWehYp9rJ2I8Abqiqz7dt762q7w0q9hbDXI/9K4ELYWSOfQG7J1kB7AZ8F3gIOATYWFW3VdV36bVp7ZDFfiDwqbbdPcADwOoBHve7q+qzbfmbwK3AvvSO23mt2nl9sawFzq+eq4A9WuxHAhuq6r6qup9em9cMU+xVdU9VXQP825RdDep7s7Px/1M7tgBX0Xv+28Di18iZzfek/7t3MXD4UvRAWASd+jcxwzmo30x/t0fOLNq6LGzn/NBvWfxeZ9nWzhqJ5G8GN/P9P7wv59EPsD0gyeeS/P9JfrKV7Qts6quzicF9EWaK/dlAJbkiyWeT/F4rH6bYYfvHftJ/BT7Ylocp/plivxj4FnA38BXgT6vqPnpx3tW3/TDG/nng55OsSHIA8KK2buDHvXXxegFwNTBWVXe3VV8FxtryTMd4oMd+lrHPZODfmznEfyK9K74wBPFrJMzme/JInaraCjxIr1fLqJntv4lfbN3lLk4y3blxueja34gfS29YxceTPHfQwczXlPNDv2X3e91OW2GZ/V5na5STv1cDv5HkOnq3dL/byu8GnlFVLwB+B/hA+sbUDYmZYl8B/ARwXPv5C0kOH0yI2zVT/AAkORT4dlVN239+wGaK/RDge8DTgQOAU5L80GBCnNFMsZ9L7w/0tcD/Av6JXlsGKskTgQ8Dv11VD/Wva3cih3aq4VGOHXY+/iT/iV7yd+qSBSktP38DrKyqH6HXU+G8HdTXaPgs8Myqej7wDuB/Dzieedne+WG52UFbl9XvdWeMbPJXVf9cVUdU1Yvo3WH6cit/uKrubcvXtfJnA5v5fpcm2vLmpY26Z6bY6f0H/tNV9Y2q+ja9ZzK9kCGKHbYb/6Rj+f5dPxii+LcT+y8Bn6iqf2tdJ/8RWN3i7L96O3SxV9XWqvofVXVwVa0F9qDXv31gxz3JY+n9wb2gqj7Sir822X2k/bynlc90jAdy7Hcy9pkM7Huzs/En+RHgvcDayb+dDNH3XkNtNt+TR+q0bvVPAe5l9OywrW2oxsPt7Xvp9cJYrjrzN6KqHqqqLW35cuCxSfYecFhzMsP5od+y+b3uqK3L6fe6s0Y2+UvyA+3nY4A/AN7T3j8tyS5t+YeAVcBtrcvTQ0kOa+MNjgcuGabYgSuAg5I8oZ0kfxq4ZZhih+3GP1n2Ctp4P+j1vWZI4t9O7F8BXtLW7U5voPM/05tkZVWSA5LsSi+xvXSp425xzfSdf0KLmSQ/A2ytqoF9b9pnnQPcWlV/1rfqUmByxs51fbFcChzfZhk7DHiwxX4FcESSPdObnfKIVjZMsc9kIN+bnY0/yTOAjwC/UlVfHHT8Gjmz+Z70f/deBnyq3X0eNTts65SxUT9Pb5zRcjXT3+1lJ8kPTo5TTXIIvf87j9wFjO2cH/oti9/rbNq6XH6vc1JDMOvMjl707nLcTW9ShU30uie9lt7djS8CZ/L9B9b/Ir2xUdfTu6X7c337WQ3cRO+OyZ9PbjMssbf6v9zivwn4n4OMfY7xjwNXTbOfoT72wBOBv27H/hbgdX37ObrV/zLw+8N23OnNSvoFev/R+Dt63RgGedx/gl63whvav8Pr2zF8KvBJ4Estzr1a/QDvbDHeCKzu29ergY3t9aohjP0H2+/nIXoT7WyiN8nOoL43Oxv/e4H7++peO8jvva/Re033PQHeAPx8W358+9u6kd7swz806JgXsa1/0s4hnweuBH540DHPo63TnYN+Hfj1tn7Gv9uj9ppFW1/T93u9CvjxQcc8x3bOdH5Ydr/XWbZ1Wfxe5/Ka/M+jJEmSJGkZG9lun5IkSZKk2TP5kyRJkqQOMPmTJEmSpA4w+ZMkSZKkDjD5kyRJkqQllOTcJPckuWmW9V+R5JYkNyf5wJw/19k+JUmSJGnpJPkpYAtwflU9bwd1VwEXAS+pqvuT/EBV3TOXz/XOnyRJkiQtoar6NHBff1mS/5DkE0muS/L3SX64rfo14J1VdX/bdk6JH5j8SZIkSdIwOBv4zap6EfC7wLta+bOBZyf5xyRXJVkz1w9YsQBBSpIkSZLmKMkTgR8H/jrJZPHj2s8VwCpgHNgP+HSSg6rqgZ39HJM/SZIkSRqsxwAPVNXB06zbBFxdVf8G3J7ki/SSwWvm8iGSJEmSpAGpqofoJXYvB0jP89vq/03vrh9J9qbXDfS2uXyOyZ8kSZIkLaEkHwT+D/CcJJuSnAgcB5yY5PPAzcDaVv0K4N4ktwBXAq+rqnvn9Lk+6kGSJEmSlj/v/EmSJElSB5j8SZIkSVIHmPxJkiRJUgeY/EmSJElSB5j8SZIkSVIHmPxJkiRJUgeY/EmSJElSB5j8SZIkSVIHmPxJkiRJUgeY/EmSJElSB5j8SZIkSVIHmPxJkiRJUgeY/EmSJElSB5j8SZIkSVIHmPxJkiRJUgeY/EmSJElSB5j8SZIkSVIHmPxJkiRJUgeY/EmSJElSB5j8SZIkSVIHmPxJkiRJUgeY/EmSJElSB5j8SZIkSVIHmPxJkiRJUgeY/EmSJElSB5j8SQsgyR8l+asBfv7rk7x3UJ8vSdIwSvKTSb4w6DikYbFi0AFImr+qevOgY5AkadhU1d8Dzxl0HNKw8M6fJEmSlp0k3uSQpjD5k/okOTXJxVPKzkry9iRPT3JpkvuSbEzya3PY/2FJ/inJA0k+n2S8b91Ekjcm+cck30zyt0n27lt/fJI7k9yb5P9JckeS/9zWPdLtNMnKJJVkXZKvJPlGkt/v289jkqxP8uW2r4uS7DWHwyVJ0pJr57/TktyS5P4k70vy+CTjSTa1c/lXgfdNlvVtu3+SjyT5ejsH/nnfulcnubXt84okzxxIA6VFZPInPdqFwNFJngSQZBfgFcAH2rpNwNOBlwFvTvKS2e44yb7AZcCbgL2A3wU+nORpfdV+CXgV8APArq0OSQ4E3gUcB+wDPAXYdwcf+RP0urocDvxhkv/Yyn8TOAb46daW+4F3zrYdkiQNgeOAI4H/ADwb+INW/oP0zrHPBE7q36Cd0z8G3AmspHcevbCtWwu8HvgvwNOAvwc+uMhtkJacyZ/Up6ruBD4L/EIregnwbWAz8GLg1Kr6TlVdD7wXOH4ndv/LwOVVdXlV/XtVbQCuBY7uq/O+qvpiVf0rcBFwcCt/GfA3VfUPVfVd4A+B2sHn/XFV/WtVfR74PPD8Vv7rwO9X1aaqehj4I+Bldo+RJI2QP6+qu6rqPuAM4JWt/N+B06vq4XYu7XcIvYuer6uqb7Xz+T+0db8O/ElV3VpVW4E3Awd790/LjcmftK0P8P2TyC+1908H7quqb/bVu5Md333r90zg5a3L5wNJHqB3d26fvjpf7Vv+NvDEtvx04K7JFVX1beDeHXzeTPt6JvDRvhhuBb4HjO1EWyRJGqS7+pbvpHeeBPh6VX1nhm32B+5syd1UzwTO6js33geEnTvPS0PPK/3Stv4aeGuS/ejdAfwxYAuwV5In9SWAz6B3R3C27gL+sqp2eqwgcDd9s5Ul2Q146hz2MxnHq6vqH+e4vSRJg7Z/3/IzgH9py9vrFXMX8IwkK6ZJAO8CzqiqCxYwRmnoeOdPmqKqvg5MAO8Dbm9dQO4C/gn4kzao/EeAE4GdebbfXwE/l+TIJLv0DU7fbxbbXty2/fEku9Lrqpmd+Ox+7wHOmOzKkuRpbayDJEmj4uQk+7UJy34f+NAstvkMvYupZybZvZ2HX9zWvQc4LclzAZI8JcnLFyVyaYBM/qTpfQD4z+3npFfSGyD+L8BH6Y0p+LvZ7rAlkJMDyr9O7yrj65jFv8OqupneRC0X0jtxbQHuAR6e7ef3OQu4FPjbJN8ErgIOncN+JEkalA8AfwvcBnyZ3mRq21VV3wN+DngW8BV6k7j917buo8BbgAuTPATcBBy1KJFLA5SqHc0ZIWnYJHki8ACwqqpuH3Q8kiQtlSR3AL+6MxdgJfV4508aEUl+LskTkuwO/ClwI3DHYKOSJEnSqDD5kxZQkuOSbJnmdfMC7H4tvS6n/wKsAo4tb91LkiRpluz2KUmSJEkdsMM7f20mpM8k+XySm5P8cSt/f5Lbk1zfXge38iR5e5KNSW5I8sK+fa1L8qX2WtdX/qIkN7Zt3p5krrMYSpIkSZKmMZtunw8DL6mq5wMHA2uSHNbWva6qDm6v61vZUfS6pK0CTgLeDdCm4j2d3qyChwCnJ9mzbfNu4Nf6tlsz75ZJkjQCkuyR5OIk/5zk1iQ/lmSvJBvaxdINk+dLL7BKkuZjhw95b2OKtrS3j22v7fUVXQuc37a7qp3U9gHGgQ1VdR9Akg30EskJ4MlVdVUrPx84Bvj49uLae++9a+XKlTsKf0bf+ta32H333ee8/bBYLu2A5dMW2zFcbMfgXXfddd+oqqcNOo4hdhbwiap6WXuO5xPoPRLmk1V1ZpL1wHrgVB59gfVQehdPD+27wLqa3jn6uiSXVtX9fP8C69XA5fQusHqOXWIek215TLblMdmWx2Rb/cdkZ8+xO0z+AJLsAlxH77ko76yqq5P8d3oPiv5D4JPA+qp6GNiX3vPLJm1qZdsr3zRN+XatXLmSa6+9djbhT2tiYoLx8fE5bz8slks7YPm0xXYMF9sxeEnuHHQMwyrJU4CfAk4AqKrvAt9NspbeRVOA84AJesnfklxg9Ry78Dwm2/KYbMtjsi2Pybb6j8nOnmNnlfy1h2IenGQP4KNJngecBnwV2BU4m95J6Q078+E7K8lJ9LqSMjY2xsTExJz3tWXLlnltPyyWSztg+bTFdgwX26EhdwDwdeB9SZ5P70Lra4Gxqrq71fkqMNaWl+QCqyRpeZpV8jepqh5IciWwpqr+tBU/nOR9wO+295uB/fs226+Vbeb7VzEnyyda+X7T1J/u88+ml2iyevXqms9VgOVyFWG5tAOWT1tsx3CxHRpyK4AXAr/ZetWcRa+L5yOqqpIs+tTcXmBdXB6TbXlMtuUx2ZbHZFvzOSY7TP6SPA34t5b47Qb8DPCWJPtU1d1t4PgxwE1tk0uB1yS5kN54hAdbvSuAN/dN8nIEcFpV3ZfkoTaJzNXA8cA75tQaSZJGyyZgU1Vd3d5fTC/5+1rfeXYf4J623gusI8pjsi2PybY8JtvymGxrPsdkNrN97gNcmeQG4Bp6Ywo+BlyQ5EbgRmBv4E2t/uXAbcBG4C+A3wBo4xDe2PZxDfCGybEJrc572zZfZgdjESRJWg6q6qvAXUme04oOB26hdyF1csbOdcAlbflS4Pg26+dhtAuswBXAEUn2bBdZjwCuaOseSnJYu1h7fN++JEkdM5vZPm8AXjBN+UtmqF/AyTOsOxc4d5rya4Hn7SgWSZKWod+kd0F1V3oXT19F7+LsRUlOBO4EXtHqXg4cTe9i6bdbXVovmskLrLDtBdb3A7vRu7jqBVZJ6qidGvMnSZIWVntO7uppVh0+TV0vsEqS5mw23T4lSZIkSSPO5E+SJEmSOsDkT5IkSZI6wORPkiRJkjrACV9G0Mr1lz2yfMpBWzmhvb/jzJcOKiRJkh5x4+YHHzk3TeW5SpIGxzt/kiRJktQBJn+SJEmS1AEmf5IkSZLUASZ/kiRJktQBJn+SJEmS1AEmf5IkSZLUASZ/kiRJktQBJn+SJEmS1AEmf5IkSZLUASZ/kiRJktQBJn+SJEmS1AEmf5IkSZLUASZ/kiRJktQBJn+SJEmS1AEmf5IkSZLUASZ/kiRJktQBJn+SJEmS1AEmf5IkSZLUASZ/kiRJktQBO0z+kjw+yWeSfD7JzUn+uJUfkOTqJBuTfCjJrq38ce39xrZ+Zd++TmvlX0hyZF/5mla2Mcn6hW+mJEmSJHXbbO78PQy8pKqeDxwMrElyGPAW4G1V9SzgfuDEVv9E4P5W/rZWjyQHAscCzwXWAO9KskuSXYB3AkcBBwKvbHUlSZIkSQtkh8lf9Wxpbx/bXgW8BLi4lZ8HHNOW17b3tPWHJ0krv7CqHq6q24GNwCHttbGqbquq7wIXtrqSJEmSpAUyqzF/7Q7d9cA9wAbgy8ADVbW1VdkE7NuW9wXuAmjrHwSe2l8+ZZuZyiVJkiRJC2TFbCpV1feAg5PsAXwU+OFFjWoGSU4CTgIYGxtjYmJizvvasmXLvLYfpFMO2vrI8thu338/qu2ZNMq/k362Y7jYDkmSpJ5ZJX+TquqBJFcCPwbskWRFu7u3H7C5VdsM7A9sSrICeApwb1/5pP5tZiqf+vlnA2cDrF69usbHx3cm/EeZmJhgPtsP0gnrL3tk+ZSDtvLWG3u/xjuOGx9QRAtjlH8n/WzHcLEdkiRJPbOZ7fNp7Y4fSXYDfga4FbgSeFmrtg64pC1f2t7T1n+qqqqVH9tmAz0AWAV8BrgGWNVmD92V3qQwly5E4yRJGnZJ7khyY5Lrk1zbyvZKsiHJl9rPPVt5kry9zY59Q5IX9u1nXav/pSTr+spf1Pa/sW2bpW+lJGkYzGbM3z7AlUluoJeobaiqjwGnAr+TZCO9MX3ntPrnAE9t5b8DrAeoqpuBi4BbgE8AJ1fV99qdw9cAV9BLKi9qdSVJ6or/VFUHV9Xq9n498MmqWgV8sr2H3szYq9rrJODd0EsWgdOBQ+lNpHb6ZMLY6vxa33ZrFr85kqRhtMNun1V1A/CCacpvo3eCmVr+HeDlM+zrDOCMacovBy6fRbySJHXBWmC8LZ8HTNC76LoWOL/1qLkqyR5J9ml1N1TV/23v/oPsOuv7jr8/kTDxQMAGkq0reSKnUckIVAxojBMymS1ubNl0sDsljKknlomD2mJ3YKo2EWknTvkxNZ0xJKZAqmAVu2MwrhNiF4soqvEOTac25oexLDvEixFjaYzVWv6ByhQi8u0f91n7sj+k1e5q77173q+ZM/ec73nOOc/z7NG996tzznMPAyTZQ++nmSaAl1TVPS1+E73Rub+wbC2RJA2NeY32KUmSTpoC/jzJV9vAZgBjVfV4m/8uMNbmT3Tk7DVtfnpcktRBJzTgiyRJWnK/XFUHk/wMsCfJX/avrKpKUie7Eks5onb/SNTTdXXUWkfsnck+mck+mck+mWkxfWLyJ0nSAFXVwfZ6KMnn6D1S8USSM6rq8XZb56FWfK6Rsw/y/G2iU/GJFl87S/nZ6rFkI2p/9ObbnxuJerpRH5l6oRyxdyb7ZCb7ZCb7ZKbF9Im3fUqSNCBJXpTkp6bmgfOBB/nxkbOnj6h9eRv181zgmXZ76G7g/CSnt4Fezgd2t3XPJjm3jfJ5ed++JEkd45U/SZIGZwz4XPv1hdXAp6vqz5LcB9ya5ErgO8DbWvldwEXAJPB94B0AVXU4yfvpjcoN8L6pwV+AdwGfAk6lN9CLg71IUkeZ/EmSNCBt5OzXzBJ/EjhvlngBV82xr53AzlniXwFevejKSpJGnrd9SpIkSVIHmPxJkiRJUgeY/EmSJElSB5j8SZIkSVIHmPxJkiRJUgeY/EmSJElSB5j8SZIkSVIHmPxJkiRJUgeY/EmSJElSB5j8SZIkSVIHmPxJkiRJUgeY/EmSJElSB5j8SZIkSVIHmPxJkiRJUgeY/EmSJElSB5j8SZIkSVIHmPxJkiRJUgeY/EmSJElSBxw3+UtyZpK7kzyUZF+Sd7f47yU5mOT+Nl3Ut817k0wm+WaSC/rim1tsMsn2vvhZSe5t8c8mOWWpGypJkiRJXTafK39HgW1VtQE4F7gqyYa27iNVdXabdgG0dZcCrwI2Ax9PsirJKuBjwIXABuDtffv5UNvXzwNPAVcuUfskSZIkScwj+auqx6vqa23+e8DDwJpjbHIxcEtV/aCqvg1MAue0abKqHq2qHwK3ABcnCfAm4La2/Y3AJQttkCRJkiRpphN65i/JOuC1wL0tdHWSB5LsTHJ6i60BHuvb7ECLzRV/OfB0VR2dFpckSZIkLZHV8y2Y5MXAHwPvqapnk3wCeD9Q7fU64DdOSi2fr8NWYCvA2NgYExMTC97XkSNHFrX9IG3bePS5+bFTn18e1fZMGeW/ST/bMVxshyRJUs+8kr8kL6CX+N1cVX8CUFVP9K3/I+DzbfEgcGbf5mtbjDniTwKnJVndrv71l/8xVbUD2AGwadOmGh8fn0/1ZzUxMcFith+kK7bf+dz8to1HuW5v78+4/7LxAdVoaYzy36Sf7RgutkOSJKlnPqN9BrgBeLiqPtwXP6Ov2D8CHmzzdwCXJnlhkrOA9cCXgfuA9W1kz1PoDQpzR1UVcDfw1rb9FuD2xTVLkiRJktRvPlf+3gj8OrA3yf0t9jv0Rus8m95tn/uBfwpQVfuS3Ao8RG+k0Kuq6kcASa4GdgOrgJ1Vta/t77eBW5J8APg6vWRTkiRJkrREjpv8VdVfAJll1a5jbPNB4IOzxHfNtl1VPUpvNFBJkiRJ0klwQqN9SpIkSZJGk8mfJEmSJHWAyZ8kSZIkdYDJnyRJA5ZkVZKvJ/l8Wz4ryb1JJpN8to2STRtJ+7Mtfm+SdX37eG+LfzPJBX3xzS02mWT7crdNkjQ8TP4kSRq8dwMP9y1/CPhIVf088BRwZYtfCTzV4h9p5Uiygd5PKL0K2Ax8vCWUq4CPARcCG+iN1L1hGdojSRpCJn+SJA1QkrXAm4FPtuUAbwJua0VuBC5p8xe3Zdr681r5i4FbquoHVfVtYJLeKNrnAJNV9WhV/RC4pZWVJHWQyZ8kSYP1+8BvAX/Tll8OPF1VR9vyAWBNm18DPAbQ1j/Tyj8Xn7bNXHFJUgfN50feJUnSSZDkHwKHquqrScYHXJetwFaAsbExJiYmFryvsVNh28ajs65bzH5H2ZEjRzrb9rnYJzPZJzPZJzMtpk9M/iRJGpw3Am9JchHwk8BLgD8ATkuyul3dWwscbOUPAmcCB5KsBl4KPNkXn9K/zVzxH1NVO4AdAJs2barx8fEFN+qjN9/OdXtn/4qx/7KF73eUTUxMsJg+XYnsk5nsk5nsk5kW0yfe9ilJ0oBU1Xuram1VraM3YMsXq+oy4G7gra3YFuD2Nn9HW6at/2JVVYtf2kYDPQtYD3wZuA9Y30YPPaUd445laJokaQh55U+SpOHz28AtST4AfB24ocVvAP5LkkngML1kjqral+RW4CHgKHBVVf0IIMnVwG5gFbCzqvYta0skSUPD5E+SpCFQVRPARJt/lN5IndPL/D/g1+bY/oPAB2eJ7wJ2LWFVJUkjyts+JUmSJKkDTP4kSZIkqQNM/iRJkiSpA0z+JEmSJKkDTP4kSZIkqQNM/iRJkiSpA0z+JEmSJKkDTP4kSZIkqQNM/iRJkiSpA0z+JEmSJKkDTP4kSZIkqQNM/iRJkiSpA0z+JEmSJKkDjpv8JTkzyd1JHkqyL8m7W/xlSfYkeaS9nt7iSXJ9kskkDyR5Xd++trTyjyTZ0hd/fZK9bZvrk+RkNFaSJEmSumo+V/6OAtuqagNwLnBVkg3AduCuqloP3NWWAS4E1rdpK/AJ6CWLwDXAG4BzgGumEsZW5p19221efNMkSZIkSVOOm/xV1eNV9bU2/z3gYWANcDFwYyt2I3BJm78YuKl67gFOS3IGcAGwp6oOV9VTwB5gc1v3kqq6p6oKuKlvX5IkSZKkJXBCz/wlWQe8FrgXGKuqx9uq7wJjbX4N8FjfZgda7FjxA7PEJUmSJElLZPV8CyZ5MfDHwHuq6tn+x/KqqpLUSajf9DpspXcrKWNjY0xMTCx4X0eOHFnU9oO0bePR5+bHTn1+eVTbM2WU/yb9bMdwsR2SJEk980r+kryAXuJ3c1X9SQs/keSMqnq83bp5qMUPAmf2bb62xQ4C49PiEy2+dpbyM1TVDmAHwKZNm2p8fHy2YvMyMTHBYrYfpCu23/nc/LaNR7lub+/PuP+ypwL04QAAGXFJREFU8QHVaGmM8t+kn+0YLrZDkiSpZz6jfQa4AXi4qj7ct+oOYGrEzi3A7X3xy9uon+cCz7TbQ3cD5yc5vQ30cj6wu617Nsm57ViX9+1LkiRJkrQE5nPl743ArwN7k9zfYr8DXAvcmuRK4DvA29q6XcBFwCTwfeAdAFV1OMn7gftaufdV1eE2/y7gU8CpwBfaJEmSJElaIsdN/qrqL4C5fnfvvFnKF3DVHPvaCeycJf4V4NXHq4skSZIkaWFOaLRPSZIkSdJoMvmTJEmSpA4w+ZMkSZKkDjD5kyRJkqQOMPmTJEmSpA4w+ZMkSZKkDpjP7/xpkdZtv3PW+P5r37zMNZEkSZLUVV75kyRJkqQOMPmTJGlAkvxkki8n+UaSfUn+XYufleTeJJNJPpvklBZ/YVuebOvX9e3rvS3+zSQX9MU3t9hkku3L3UZJ0vAw+ZMkaXB+ALypql4DnA1sTnIu8CHgI1X188BTwJWt/JXAUy3+kVaOJBuAS4FXAZuBjydZlWQV8DHgQmAD8PZWVpLUQSZ/kiQNSPUcaYsvaFMBbwJua/EbgUva/MVtmbb+vCRp8Vuq6gdV9W1gEjinTZNV9WhV/RC4pZWVJHWQyZ8kSQPUrtDdDxwC9gDfAp6uqqOtyAFgTZtfAzwG0NY/A7y8Pz5tm7nikqQOcrRPSZIGqKp+BJyd5DTgc8AvDKIeSbYCWwHGxsaYmJhY8L7GToVtG4/Oum4x+x1lR44c6Wzb52KfzGSfzGSfzLSYPjH5kyRpCFTV00nuBn4ROC3J6nZ1by1wsBU7CJwJHEiyGngp8GRffEr/NnPFpx9/B7ADYNOmTTU+Pr7gtnz05tu5bu/sXzH2X7bw/Y6yiYkJFtOnK5F9MpN9MpN9MtNi+sTbPiVJGpAkP92u+JHkVOBXgYeBu4G3tmJbgNvb/B1tmbb+i1VVLX5pGw30LGA98GXgPmB9Gz30FHqDwtxx8lsmSRpGXvmTJGlwzgBubKNy/gRwa1V9PslDwC1JPgB8Hbihlb8B+C9JJoHD9JI5qmpfkluBh4CjwFXtdlKSXA3sBlYBO6tq3/I1T5I0TEz+JEkakKp6AHjtLPFH6Y3UOT3+/4Bfm2NfHwQ+OEt8F7Br0ZWVJI08b/uUJEmSpA4w+ZMkSZKkDjD5kyRJkqQOMPmTJEmSpA4w+ZMkSZKkDjD5kyRJkqQOMPmTJEmSpA44bvKXZGeSQ0ke7Iv9XpKDSe5v00V9696bZDLJN5Nc0Bff3GKTSbb3xc9Kcm+LfzbJKUvZQEmSJEnS/K78fQrYPEv8I1V1dpt2ASTZAFwKvKpt8/Ekq5KsAj4GXAhsAN7eygJ8qO3r54GngCsX0yBJkiRJ0kzHTf6q6kvA4Xnu72Lglqr6QVV9G5gEzmnTZFU9WlU/BG4BLk4S4E3AbW37G4FLTrANkiRJkqTjWMwzf1cneaDdFnp6i60BHusrc6DF5oq/HHi6qo5Oi0uSJEmSltDqBW73CeD9QLXX64DfWKpKzSXJVmArwNjYGBMTEwve15EjRxa1/YnYtvHorPGFHr9/f2OnPr+8XO05WZbzb3Iy2Y7hYjskSZJ6FpT8VdUTU/NJ/gj4fFs8CJzZV3RtizFH/EngtCSr29W//vKzHXcHsANg06ZNNT4+vpDqA71EaTHbn4grtt85a3z/ZQs7fv/+tm08ynV7Vy9qf8NiOf8mJ5PtGC62Q5IkqWdByV+SM6rq8bb4j4CpkUDvAD6d5MPA3wbWA18GAqxPcha95O5S4J9UVSW5G3grvecAtwC3L7QxkiRpuK2b4z9EAfZf++ZlrIkkdc9xk78knwHGgVckOQBcA4wnOZvebZ/7gX8KUFX7ktwKPAQcBa6qqh+1/VwN7AZWATural87xG8DtyT5APB14IYla50kSZIkCZhH8ldVb58lPGeCVlUfBD44S3wXsGuW+KP0RgOVJEmSJJ0kixntU5IkSZI0Ikz+JEmSJKkDTP4kSZIkqQNM/iRJkiSpA0z+JEmSJKkDTP4kSZIkqQNM/iRJkiSpA0z+JEmSJKkDTP4kSZIkqQNM/iRJkiSpA0z+JEmSJKkDTP4kSZIkqQNM/iRJkiSpA0z+JEmSJKkDTP4kSRqQJGcmuTvJQ0n2JXl3i78syZ4kj7TX01s8Sa5PMpnkgSSv69vXllb+kSRb+uKvT7K3bXN9kix/SyVJw8DkT5KkwTkKbKuqDcC5wFVJNgDbgbuqaj1wV1sGuBBY36atwCeglywC1wBvAM4BrplKGFuZd/Ztt3kZ2iVJGkImf5IkDUhVPV5VX2vz3wMeBtYAFwM3tmI3Ape0+YuBm6rnHuC0JGcAFwB7qupwVT0F7AE2t3Uvqap7qqqAm/r2JUnqGJM/SZKGQJJ1wGuBe4Gxqnq8rfouMNbm1wCP9W12oMWOFT8wS1yS1EGrB10BSZK6LsmLgT8G3lNVz/Y/lldVlaSWoQ5b6d1KytjYGBMTEwve19ipsG3j0RPebjHHHHZHjhxZ0e1bCPtkJvtkJvtkpsX0icmfJEkDlOQF9BK/m6vqT1r4iSRnVNXj7dbNQy1+EDizb/O1LXYQGJ8Wn2jxtbOUn6GqdgA7ADZt2lTj4+OzFZuXj958O9ftPfGvGPsvW/gxh93ExASL6dOVyD6ZyT6ZyT6ZaTF94m2fkiQNSBt58wbg4ar6cN+qO4CpETu3ALf3xS9vo36eCzzTbg/dDZyf5PQ20Mv5wO627tkk57ZjXd63L0lSx3jlT5KkwXkj8OvA3iT3t9jvANcCtya5EvgO8La2bhdwETAJfB94B0BVHU7yfuC+Vu59VXW4zb8L+BRwKvCFNkmSOsjkT5KkAamqvwDm+t2982YpX8BVc+xrJ7BzlvhXgFcvopqSpBXC2z4lSZIkqQNM/iRJkiSpA46b/CXZmeRQkgf7Yi9LsifJI+319BZPkuuTTCZ5IMnr+rbZ0so/kmRLX/z1Sfa2ba5P//jWkiRJkqQlMZ8rf58CNk+LbQfuqqr1wF1tGeBCYH2btgKfgF6yCFwDvAE4B7hmKmFsZd7Zt930Y0mSJEmSFum4yV9VfQk4PC18MXBjm78RuKQvflP13AOc1n6f6AJgT1UdrqqngD3A5rbuJVV1T3uI/aa+fUmSJEmSlshCn/kba78dBPBdYKzNrwEe6yt3oMWOFT8wS1ySJEmStIQW/VMPVVVJaikqczxJttK7nZSxsTEmJiYWvK8jR44savsTsW3j0VnjCz1+//7GTn1+ebnac7Is59/kZLIdw8V2SJIk9Sw0+XsiyRlV9Xi7dfNQix8Ezuwrt7bFDgLj0+ITLb52lvKzqqodwA6ATZs21fj4+FxFj2tiYoLFbD/duu13HmPt7N28/7KFHf+KvmNt23iU6/auXtT+hsVS/00GxXYMF9shSZLUs9DbPu8Apkbs3ALc3he/vI36eS7wTLs9dDdwfpLT20Av5wO727pnk5zbRvm8vG9fkiRJkqQlctwrf0k+Q++q3SuSHKA3aue1wK1JrgS+A7ytFd8FXARMAt8H3gFQVYeTvB+4r5V7X1VNDSLzLnojip4KfKFNkiRJkqQldNzkr6rePseq82YpW8BVc+xnJ7BzlvhXgFcfrx6SJEmSpIVb6G2fkiRJkqQRYvInSZIkSR1g8idJkiRJHWDyJ0mSJEkdYPInSZIkSR1g8idJkiRJHWDyJ0mSJEkdcNzf+euiddvvHHQVJEmSJGlJeeVPkiRJkjrA5E+SJEmSOsDkT5IkSZI6wORPkiRJkjrA5E+SJEmSOsDkT5IkSZI6wORPkiRJkjrA5E+SJEmSOsDkT5IkSZI6YPWgK6DZrdt+56CrIEmSJGkF8cqfJEmSJHWAyZ8kSQOUZGeSQ0ke7Iu9LMmeJI+019NbPEmuTzKZ5IEkr+vbZksr/0iSLX3x1yfZ27a5PkmWt4WSpGFh8idJ0mB9Ctg8LbYduKuq1gN3tWWAC4H1bdoKfAJ6ySJwDfAG4BzgmqmEsZV5Z992048lSeoIkz9Jkgaoqr4EHJ4Wvhi4sc3fCFzSF7+peu4BTktyBnABsKeqDlfVU8AeYHNb95KquqeqCripb1+SpI4x+ZMkafiMVdXjbf67wFibXwM81lfuQIsdK35glrgkqYMc7VOSpCFWVZWkTvZxkmyldyspY2NjTExMLHhfY6fCto1HT3i7xRxz2B05cmRFt28h7JOZ7JOZ7JOZFtMni0r+kuwHvgf8CDhaVZvacwefBdYB+4G3VdVT7QHzPwAuAr4PXFFVX2v72QL827bbD1TVjUiS1F1PJDmjqh5vt24eavGDwJl95da22EFgfFp8osXXzlJ+hqraAewA2LRpU42Pj89WbF4+evPtXLf3xL9i7L9s4cccdhMTEyymT1ci+2Qm+2Qm+2SmxfTJUtz2+fer6uyq2tSWl/IhdUmSuugOYGrEzi3A7X3xy9uon+cCz7TbQ3cD5yc5vX2Gng/sbuueTXJu+0/Yy/v2JUnqmJPxzN+SPKR+EuolSdLQSfIZ4H8Br0xyIMmVwLXAryZ5BPgHbRlgF/AoMAn8EfAugKo6DLwfuK9N72sxWplPtm2+BXxhOdolSRo+i33mr4A/b88i/Kd2y8hSPaQuSdKKV1Vvn2PVebOULeCqOfazE9g5S/wrwKsXU0dJ0sqw2OTvl6vqYJKfAfYk+cv+lUv9kPpSPox+rAclF/KQ+kIcq/7zrUP/Q/Wj/jDsSnmg13YMF9shjY512++cNb7/2jcvc00kaWVaVPJXVQfb66Ekn6P3zN5SPaQ+2/GW7GH0Yz0oecUcHz5L7VgPts+3Dts2Hn3uofpRf1B+pTzQazuGi+2QJEnqWfAzf0lelOSnpubpPVz+IEv0kPpC6yVJkiRJmmkxV/7GgM/1Bg9jNfDpqvqzJPcBt7YH1r8DvK2V30XvZx4m6f3Uwzug95B6kqmH1OHHH1KXJEmSJC2BBSd/VfUo8JpZ4k+yRA+pS5IkSZKWxsn4qQdJkiRJ0pAx+ZMkSZKkDjD5kyRJkqQOMPmTJEmSpA4w+ZMkSZKkDjD5kyRJkqQOWMzv/ElLYt32OwHYtvEoV7T5KfuvffMgqiRJkiStOF75kyRJkqQO6OyVv70Hn5lxlUmSJEmSViqv/EmSJElSB3T2yp8kSRoN645xp47PhkvS/Jn8DdCxPswkSZIkaSl526ckSZIkdYBX/rRsvNIpSZIkDY5X/iRJkiSpA0z+JEmSJKkDTP4kSZIkqQNM/iRJkiSpA0z+JEmSJKkDHO1TkiSNrLlGkvbH3yVpJq/8SZIkSVIHeOVvBTnW7+gt5H9Al3p/kiRJkgbH5K8jvC1GkiRJ6jaTP0mStOJ494okzWTy13HH+nCUJEmStHIMTfKXZDPwB8Aq4JNVde2AqyRJ0orgZ+yP86qgpK4aiuQvySrgY8CvAgeA+5LcUVUPDbZmGrRh/4CerX7bNh5lfAn3B8PRVkmjyc9YSdKUoUj+gHOAyap6FCDJLcDFgB9MQ2qYk5RhSBiHoQ4LNVX3bRuPckVfOxZa72E+V6SO8DP2BCzkcQjfzySNimFJ/tYAj/UtHwDeMKC6aBGW8xnChRxrGD7Ul7qPfG5z4UY5SZdOgJ+xJ9l83oen/4faQvi+JGmxUlWDrgNJ3gpsrqrfbMu/Dryhqq6eVm4rsLUtvhL45iIO+wrg/yxi+2GxUtoBK6cttmO42I7B+9mq+ulBV6Kr/IwdGvbJTPbJTPbJTPbJTP19ckKfscNy5e8gcGbf8toW+zFVtQPYsRQHTPKVqtq0FPsapJXSDlg5bbEdw8V2SH7GDgP7ZCb7ZCb7ZCb7ZKbF9MlPLHVlFug+YH2Ss5KcAlwK3DHgOkmStBL4GStJAobkyl9VHU1yNbCb3jDUO6tq34CrJUnSyPMzVpI0ZSiSP4Cq2gXsWsZDLsmtLUNgpbQDVk5bbMdwsR3qPD9jh4J9MpN9MpN9MpN9MtOC+2QoBnyRJEmSJJ1cw/LMnyRJkiTpJFpRyV+SnUkOJXmwL/ayJHuSPNJeT2/xJLk+yWSSB5K8rm+bLa38I0m2DKAdZya5O8lDSfYlefcotiXJTyb5cpJvtHb8uxY/K8m9rb6fbQMQkOSFbXmyrV/Xt6/3tvg3k1ywnO3oq8OqJF9P8vlRbUeS/Un2Jrk/yVdabKTOq3b805LcluQvkzyc5BdHrR1JXtn+DlPTs0neM2rtULcl2dzezyaTbJ9l/ZzvhyvVPPrkiiT/u+/f/m8Oop7LJbN8N5u2fs73tpVqHn0ynuSZvnPkd5e7jsstc3z3nVamU+fKPPvkxM+VqloxE/ArwOuAB/ti/wHY3ua3Ax9q8xcBXwACnAvc2+IvAx5tr6e3+dOXuR1nAK9r8z8F/BWwYdTa0urz4jb/AuDeVr9bgUtb/A+Bf97m3wX8YZu/FPhsm98AfAN4IXAW8C1g1QDOr38JfBr4fFseuXYA+4FXTIuN1HnV6nAj8Jtt/hTgtFFsR197VgHfBX52lNvh1K2pnbffAn6u/Tv8BrBhWplZ3w9X6jTPPrkC+I+Drusy9smM72bT1s/63raSp3n0yTjtu0ZXJub47tvlc2WefXLC58qKuvJXVV8CDk8LX0zviyLt9ZK++E3Vcw9wWpIzgAuAPVV1uKqeAvYAm09+7Z9XVY9X1dfa/PeAh4E1jFhbWn2OtMUXtKmANwG3zdGOqfbdBpyXJC1+S1X9oKq+DUwC5yxDE56TZC3wZuCTbTmMYDvmMFLnVZKX0vvgvAGgqn5YVU+PWjumOQ/4VlV9h9Fuh7rlHGCyqh6tqh8Ct9A7T/vN9X64Us2nTzplju9m/eZ6b1ux5tEnnXOM7779OnWuzLNPTtiKSv7mMFZVj7f57wJjbX4N8FhfuQMtNld8INotMq+ld9Vs5NqS3q2S9wOH6H0p/RbwdFUdnaVOz9W3rX8GeDlD0A7g94HfAv6mLb+c0WxHAX+e5KtJtrbYqJ1XZwH/G/jP6d2G+8kkL2L02tHvUuAzbX6U26Fumc+5N9f74Uo133+P/7jdtnZbkjOXp2pDy/ew2f1ieo/NfCHJqwZdmeU07btvv86eK8foEzjBc6ULyd9zqnd9dGSGN03yYuCPgfdU1bP960alLVX1o6o6G1hL739Ef2HAVTphSf4hcKiqvjrouiyBX66q1wEXAlcl+ZX+lSNyXq2md7vMJ6rqtcD/pXd75HNGpB0ApPes6FuA/zp93Si1Q9K8/TdgXVX9PXr/KXrjccqre74G/GxVvQb4KPCnA67PsjnWd9+uOk6fnPC50oXk74mpS8Lt9VCLHwT6/7dtbYvNFV9WSV5A7w99c1X9SQuPZFsA2m15dwO/SO8y/dRvTPbX6bn6tvUvBZ5k8O14I/CWJPvp3cLzJuAPGL12UFUH2+sh4HP0EvJRO68OAAeqaup/v26jlwyOWjumXAh8raqeaMuj2g51z3zOvbneD1eq4/ZJVT1ZVT9oi58EXr9MdRtWvodNU1XPTj02U73f6HxBklcMuFon3Rzffft17lw5Xp8s5FzpQvJ3BzA1+t0W4Pa++OVt5KBzgWfarVa7gfOTnJ7eKHvnt9iyac9D3AA8XFUf7ls1Um1J8tNJTmvzpwK/Su9+5buBt87Rjqn2vRX4YrvycQdwaXqjxp0FrAe+vDytgKp6b1Wtrap19G7P+2JVXcaItSPJi5L81NQ8vfPhQUbsvKqq7wKPJXllC50HPDRq7ejzdp6/5RNGtx3qnvuA9emNfHwKvffHO6aVmev9cKU6bp9Me0bpLfQ+F7tsrve2zkryt6aejU1yDr3v6yv5P02O9d23X6fOlfn0yYLOlRqC0WyWaqL3Bepx4K/pXR24kt6zBXcBjwD/HXhZKxvgY/SeQdsLbOrbz2/QG4xjEnjHANrxy/Ru9XoAuL9NF41aW4C/B3y9teNB4Hdb/OfoJT2T9G51e2GL/2Rbnmzrf65vX/+mte+bwIUDPMfGeX60z5FqR6vvN9q0D/g3LT5S51U7/tnAV9q59af0RrkcxXa8iN6b9Ev7YiPXDqfuTu2z6a/aeTn1nvI+4C1tfs73w5U6zaNP/n17D/4Gvf9E/IVB1/kk98ds383+GfDP2vo539tW6jSPPrm67xy5B/ilQdd5Gfpkru++nT1X5tknJ3yupG0oSZIkSVrBunDbpyRJkiR1nsmfJEmSJHWAyZ8kSZIkdYDJnyRJkiR1gMmfJEmSJC2jJDuTHEry4DzLvy3JQ0n2Jfn0go/raJ+SJEmStHyS/ApwBLipql59nLLrgVuBN1XVU0l+pqoOLeS4XvmTJEmSpGVUVV8CDvfHkvydJH+W5KtJ/keSX2ir3gl8rKqeatsuKPEDkz9JkiRJGgY7gH9RVa8H/hXw8Rb/u8DfTfI/k9yTZPNCD7B6CSopSZIkSVqgJC8Gfgn4r0mmwi9sr6uB9cA4sBb4UpKNVfX0iR7H5E+SJEmSBusngKer6uxZ1h0A7q2qvwa+neSv6CWD9y3kIJIkSZKkAamqZ+kldr8GkJ7XtNV/Su+qH0leQe820EcXchyTP0mSJElaRkk+A/wv4JVJDiS5ErgMuDLJN4B9wMWt+G7gySQPAXcD/7qqnlzQcf2pB0mSJEla+bzyJ0mSJEkdYPInSZIkSR1g8idJkiRJHWDyJ0mSJEkdYPInSZIkSR1g8idJkiRJHWDyJ0mSJEkdYPInSZIkSR3w/wF5IlMHBKzEIAAAAABJRU5ErkJggg==\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Multivariate Analysis:"
      ],
      "metadata": {
        "id": "wM-aiMNbTxOl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Categorical Data\n",
        "cat_data = df.select_dtypes(include='object').columns.to_list()\n",
        "\n",
        "for col in cat_data:\n",
        "  sns.catplot(x=col, y='price', kind='bar', dodge=False, height=6, aspect=3, data=df, palette='Set3')\n",
        "  plt.title(\"Rata-Rata 'price' Relatif terhadap - {}\".format(col))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "AEUp7vviTxkV",
        "outputId": "4061fbf2-e582-468e-cd9d-f38e52a794b5"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1296x432 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1296x432 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1296x432 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Numerical Data\n",
        "sns.pairplot(df, diag_kind='kde')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 744
        },
        "id": "32RGGAbXVJ2i",
        "outputId": "72613954-81e0-4964-c761-2854ecf1ec78"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<seaborn.axisgrid.PairGrid at 0x7fd90a5f3e50>"
            ]
          },
          "metadata": {},
          "execution_count": 26
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 720x720 with 20 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Melihat Heat Map untuk melihat korelasi antar data Numerical\n",
        "plt.figure(figsize=(10, 8))\n",
        "correlation_matrix = df.corr().round(2)\n",
        "\n",
        "sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)\n",
        "plt.title(\"Correlation Matrix untuk Fitur Numerik\", size=20)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 522
        },
        "id": "nhA8yNCZVtPB",
        "outputId": "48bab9c6-7564-4006-ae29-c3065f42599b"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Text(0.5, 1.0, 'Correlation Matrix untuk Fitur Numerik')"
            ]
          },
          "metadata": {},
          "execution_count": 27
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 720x576 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Data Preparation"
      ],
      "metadata": {
        "id": "qksUFmKfW4qX"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Untuk data Categorical, diberlakukan sistem One-Hot Encoding untuk mengubah data Categorical menjadi data Numerical\n",
        "df = pd.concat([df, pd.get_dummies(df['mark'], prefix='mark')], axis=1)\n",
        "df = pd.concat([df, pd.get_dummies(df['fuel'], prefix='fuel')], axis=1)\n",
        "df = pd.concat([df, pd.get_dummies(df['province'], prefix='province')], axis=1)\n",
        "df.drop(['mark', 'fuel', 'province'], axis=1, inplace=True)\n",
        "df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 317
        },
        "id": "UTJ7RGLGW43l",
        "outputId": "bd3d0b2d-1d62-44db-d2f7-531f85acd6b7"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   year  mileage  vol_engine  price  mark_alfa-romeo  mark_audi  mark_bmw  \\\n",
              "0  2015   139568        1248  35900                0          0         0   \n",
              "1  2018    31991        1499  78501                0          0         0   \n",
              "5  2017   121203        1598  51900                0          0         0   \n",
              "6  2017   119965        1248  44700                0          0         0   \n",
              "7  2016   201658        1248  29000                0          0         0   \n",
              "\n",
              "   mark_chevrolet  mark_citroen  mark_fiat  ...  province_Mazowieckie  \\\n",
              "0               0             0          0  ...                     1   \n",
              "1               0             0          0  ...                     0   \n",
              "5               0             0          0  ...                     1   \n",
              "6               0             0          0  ...                     0   \n",
              "7               0             0          0  ...                     0   \n",
              "\n",
              "   province_Małopolskie  province_Podkarpackie  province_Pomorskie  \\\n",
              "0                     0                      0                   0   \n",
              "1                     0                      0                   0   \n",
              "5                     0                      0                   0   \n",
              "6                     0                      0                   0   \n",
              "7                     0                      0                   0   \n",
              "\n",
              "   province_Warmińsko-mazurskie  province_Wielkopolskie  \\\n",
              "0                             0                       0   \n",
              "1                             0                       0   \n",
              "5                             0                       0   \n",
              "6                             0                       0   \n",
              "7                             0                       0   \n",
              "\n",
              "   province_Zachodniopomorskie  province_Łódzkie  province_Śląskie  \\\n",
              "0                            0                 0                 0   \n",
              "1                            0                 0                 1   \n",
              "5                            0                 0                 0   \n",
              "6                            0                 0                 0   \n",
              "7                            0                 0                 0   \n",
              "\n",
              "   province_Świętokrzyskie  \n",
              "0                        0  \n",
              "1                        0  \n",
              "5                        0  \n",
              "6                        0  \n",
              "7                        0  \n",
              "\n",
              "[5 rows x 43 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-619b801a-d22b-4281-9070-e92a79dcf6cb\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
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
              "      <th>year</th>\n",
              "      <th>mileage</th>\n",
              "      <th>vol_engine</th>\n",
              "      <th>price</th>\n",
              "      <th>mark_alfa-romeo</th>\n",
              "      <th>mark_audi</th>\n",
              "      <th>mark_bmw</th>\n",
              "      <th>mark_chevrolet</th>\n",
              "      <th>mark_citroen</th>\n",
              "      <th>mark_fiat</th>\n",
              "      <th>...</th>\n",
              "      <th>province_Mazowieckie</th>\n",
              "      <th>province_Małopolskie</th>\n",
              "      <th>province_Podkarpackie</th>\n",
              "      <th>province_Pomorskie</th>\n",
              "      <th>province_Warmińsko-mazurskie</th>\n",
              "      <th>province_Wielkopolskie</th>\n",
              "      <th>province_Zachodniopomorskie</th>\n",
              "      <th>province_Łódzkie</th>\n",
              "      <th>province_Śląskie</th>\n",
              "      <th>province_Świętokrzyskie</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>2015</td>\n",
              "      <td>139568</td>\n",
              "      <td>1248</td>\n",
              "      <td>35900</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>...</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2018</td>\n",
              "      <td>31991</td>\n",
              "      <td>1499</td>\n",
              "      <td>78501</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>2017</td>\n",
              "      <td>121203</td>\n",
              "      <td>1598</td>\n",
              "      <td>51900</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>...</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>2017</td>\n",
              "      <td>119965</td>\n",
              "      <td>1248</td>\n",
              "      <td>44700</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>2016</td>\n",
              "      <td>201658</td>\n",
              "      <td>1248</td>\n",
              "      <td>29000</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>5 rows × 43 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-619b801a-d22b-4281-9070-e92a79dcf6cb')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-619b801a-d22b-4281-9070-e92a79dcf6cb button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-619b801a-d22b-4281-9070-e92a79dcf6cb');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Train-Test Split:"
      ],
      "metadata": {
        "id": "Uf6XIFKfYrpL"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Membagi Dataset menjadi Data Latih dan Data Validasi menggunakan fungsi train_test_split dengan perbandingan 90:10\n",
        "X = df.drop(['price'], axis=1)\n",
        "y = df['price']\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=123)\n",
        "\n",
        "print(f'Total Sample in Whole Dataset: {len(X)}')\n",
        "print(f'Total Sample in Train Dataset: {len(X_train)}')\n",
        "print(f'Total Sample in Test Dataset: {len(X_test)}')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oZBkujgQYWKx",
        "outputId": "d4c6fba7-efd7-46c0-8c47-e6c14c27aa43"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Total Sample in Whole Dataset: 103712\n",
            "Total Sample in Train Dataset: 93340\n",
            "Total Sample in Test Dataset: 10372\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Standarisasi Data:"
      ],
      "metadata": {
        "id": "qZt61NxrYofo"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "numerical_features = ['year', 'mileage', 'vol_engine']\n",
        "scaler = StandardScaler()\n",
        "scaler.fit(X_train[numerical_features])\n",
        "X_train[numerical_features] = scaler.transform(X_train.loc[:, numerical_features])\n",
        "X_train[numerical_features].head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "xHcOs8W4YxwX",
        "outputId": "f7bfea53-f882-4f8d-dca0-b1671522a97e"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "            year   mileage  vol_engine\n",
              "49474  -0.326112  0.123207   -0.406705\n",
              "23048   0.936249 -0.748958    1.851780\n",
              "83167  -1.047461  0.557094    0.253873\n",
              "31406   1.477261 -1.591134    0.255520\n",
              "108212 -1.227799  1.123924    0.253873"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-dea98fde-1143-4dde-89d9-0ca537b018fb\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
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
              "      <th>year</th>\n",
              "      <th>mileage</th>\n",
              "      <th>vol_engine</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>49474</th>\n",
              "      <td>-0.326112</td>\n",
              "      <td>0.123207</td>\n",
              "      <td>-0.406705</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>23048</th>\n",
              "      <td>0.936249</td>\n",
              "      <td>-0.748958</td>\n",
              "      <td>1.851780</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>83167</th>\n",
              "      <td>-1.047461</td>\n",
              "      <td>0.557094</td>\n",
              "      <td>0.253873</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>31406</th>\n",
              "      <td>1.477261</td>\n",
              "      <td>-1.591134</td>\n",
              "      <td>0.255520</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>108212</th>\n",
              "      <td>-1.227799</td>\n",
              "      <td>1.123924</td>\n",
              "      <td>0.253873</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-dea98fde-1143-4dde-89d9-0ca537b018fb')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-dea98fde-1143-4dde-89d9-0ca537b018fb button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-dea98fde-1143-4dde-89d9-0ca537b018fb');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 30
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "X_train[numerical_features].describe().round(4)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 300
        },
        "id": "gk4UJFRDZZCO",
        "outputId": "37afccea-b786-4d3c-c35d-b1d5165712ea"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "             year     mileage  vol_engine\n",
              "count  93340.0000  93340.0000  93340.0000\n",
              "mean      -0.0000      0.0000     -0.0000\n",
              "std        1.0000      1.0000      1.0000\n",
              "min       -8.8020     -1.5912     -1.3902\n",
              "25%       -0.6868     -0.7711     -0.5681\n",
              "50%        0.0346      0.0600     -0.0772\n",
              "75%        0.7559      0.6592      0.2506\n",
              "max        1.6576     29.4388      7.8233"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-5e4df93e-ec25-4b6a-857a-4d42c6b42934\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
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
              "      <th>year</th>\n",
              "      <th>mileage</th>\n",
              "      <th>vol_engine</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>93340.0000</td>\n",
              "      <td>93340.0000</td>\n",
              "      <td>93340.0000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>-0.0000</td>\n",
              "      <td>0.0000</td>\n",
              "      <td>-0.0000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>1.0000</td>\n",
              "      <td>1.0000</td>\n",
              "      <td>1.0000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>-8.8020</td>\n",
              "      <td>-1.5912</td>\n",
              "      <td>-1.3902</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>-0.6868</td>\n",
              "      <td>-0.7711</td>\n",
              "      <td>-0.5681</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>0.0346</td>\n",
              "      <td>0.0600</td>\n",
              "      <td>-0.0772</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>0.7559</td>\n",
              "      <td>0.6592</td>\n",
              "      <td>0.2506</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>1.6576</td>\n",
              "      <td>29.4388</td>\n",
              "      <td>7.8233</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-5e4df93e-ec25-4b6a-857a-4d42c6b42934')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-5e4df93e-ec25-4b6a-857a-4d42c6b42934 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-5e4df93e-ec25-4b6a-857a-4d42c6b42934');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 31
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Model Development:"
      ],
      "metadata": {
        "id": "c9fYB73HZ7mZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Mempersiapkan Dataframe\n",
        "models = pd.DataFrame(index=['train_mse', 'test_mse'], columns=['KNN', 'RandomForest', 'Boosting'])"
      ],
      "metadata": {
        "id": "ylMq1rowOxo5"
      },
      "execution_count": 32,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# K-Nearest Neighbor\n",
        "knn = KNeighborsRegressor(n_neighbors=4)\n",
        "knn.fit(X_train, y_train)\n",
        "\n",
        "models.loc['train_mse', 'KNN'] = mean_squared_error(y_pred=knn.predict(X_train), y_true=y_train)"
      ],
      "metadata": {
        "id": "Td1tsaDjOzUz"
      },
      "execution_count": 33,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Random Forest\n",
        "RF = RandomForestRegressor(n_estimators=50, max_depth=64, random_state=55, n_jobs=-1)\n",
        "RF.fit(X_train, y_train)\n",
        "\n",
        "models.loc['train_mse', 'RandomForest'] = mean_squared_error(y_pred=RF.predict(X_train), y_true=y_train)"
      ],
      "metadata": {
        "id": "KlavGBx-P99J"
      },
      "execution_count": 34,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Boosting Algorithm\n",
        "boosting = AdaBoostRegressor(learning_rate=0.08, random_state=55)\n",
        "boosting.fit(X_train, y_train)\n",
        "\n",
        "models.loc['train_mse', 'Boosting'] = mean_squared_error(y_pred=boosting.predict(X_train), y_true=y_train)"
      ],
      "metadata": {
        "id": "GPfqMj6sP-Kt"
      },
      "execution_count": 35,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Evaluasi Model:"
      ],
      "metadata": {
        "id": "6IPOvBQgP-Rg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Scaling Data Uji\n",
        "X_test.loc[:, numerical_features] = scaler.transform(X_test[numerical_features])"
      ],
      "metadata": {
        "id": "kuC7ZgNkP-WB"
      },
      "execution_count": 36,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Melihat Hasil Prediksi Model\n",
        "mse = pd.DataFrame(columns=['Train', 'Test'], index=['K-Nearest Neighbor', 'Random Forest', 'Boosting'])\n",
        "model_dict = {\"K-Nearest Neighbor\":knn, \"Random Forest\":RF, \"Boosting\":boosting}\n",
        "\n",
        "for name, model in model_dict.items():\n",
        "  mse.loc[name, 'Train'] = mean_squared_error(y_true=y_train, y_pred=model.predict(X_train))/1e3\n",
        "  mse.loc[name, 'Test'] = mean_squared_error(y_true=y_test, y_pred=model.predict(X_test))/1e3\n",
        "\n",
        "mse"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 143
        },
        "id": "rQUzj_n4P-aZ",
        "outputId": "b401db5f-1015-421b-fa6f-76451b8e6225"
      },
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                             Train            Test\n",
              "K-Nearest Neighbor   520014.135924   732296.875684\n",
              "Random Forest        184651.209957   589524.177038\n",
              "Boosting            1838754.256309  1703197.195434"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-39836465-59ae-4a99-b141-8a1ec3dc328d\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
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
              "      <th>Train</th>\n",
              "      <th>Test</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>K-Nearest Neighbor</th>\n",
              "      <td>520014.135924</td>\n",
              "      <td>732296.875684</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Random Forest</th>\n",
              "      <td>184651.209957</td>\n",
              "      <td>589524.177038</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Boosting</th>\n",
              "      <td>1838754.256309</td>\n",
              "      <td>1703197.195434</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-39836465-59ae-4a99-b141-8a1ec3dc328d')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-39836465-59ae-4a99-b141-8a1ec3dc328d button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-39836465-59ae-4a99-b141-8a1ec3dc328d');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 37
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "fig, ax = plt.subplots()\n",
        "mse.sort_values(by='Test', ascending=False).plot(kind='barh', ax=ax, zorder=3)\n",
        "ax.grid(zorder=0)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 278
        },
        "id": "i3JBTZhlP-hm",
        "outputId": "22acb7bb-d7e0-411b-c4ac-fe4b3a8d30ff"
      },
      "execution_count": 38,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Mengetes Algoritma yang Digunakan\n",
        "prediksi = X_test.iloc[:1].copy()\n",
        "pred_dict = {'y_true':y_test[:1]}\n",
        "\n",
        "for name, model in model_dict.items():\n",
        "  pred_dict['Prediksi '+name] = model.predict(prediksi).round(1)\n",
        "\n",
        "pd.DataFrame(pred_dict)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 80
        },
        "id": "GoDycrn_RG4n",
        "outputId": "49175065-f188-4607-9a18-ddfe94d14cf7"
      },
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "       y_true  Prediksi K-Nearest Neighbor  Prediksi Random Forest  \\\n",
              "30695   76000                      51625.0                 52459.8   \n",
              "\n",
              "       Prediksi Boosting  \n",
              "30695            78337.3  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-e540abc7-da93-47b3-880f-bda75f1d9cb4\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
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
              "      <th>y_true</th>\n",
              "      <th>Prediksi K-Nearest Neighbor</th>\n",
              "      <th>Prediksi Random Forest</th>\n",
              "      <th>Prediksi Boosting</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>30695</th>\n",
              "      <td>76000</td>\n",
              "      <td>51625.0</td>\n",
              "      <td>52459.8</td>\n",
              "      <td>78337.3</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-e540abc7-da93-47b3-880f-bda75f1d9cb4')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-e540abc7-da93-47b3-880f-bda75f1d9cb4 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-e540abc7-da93-47b3-880f-bda75f1d9cb4');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 39
        }
      ]
    }
  ]
}