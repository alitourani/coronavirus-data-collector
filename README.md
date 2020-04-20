# Coronavirus Data Collector
Collect the COVID-19 related data for research and analysis

## Prerequisites
You need to have Python 3.1+ installed in your computer (I use [Anaconda](https://www.anaconda.com/distribution/ "Anaconda") platform for development):
1. Create a new environment using `conda create -n coronaVirus` command and select it to be activated using `conda activate coronaVirus`.
2. Install essential libraries using the below command:
`conda install pandas matplotlib wordcloud`
3. You may need to use pip to install [OpenBlender](https://www.openblender.io/ "OpenBlender") package using `pip install OpenBlender`

## Datasets
The application uses **Center for System Science and Engineering (CSSE)** COVID-19 daily reports provided by Johns Hopkins University ([link to dataset](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports "link to dataset")) as coronavirus recent statistics. Sign up through [this](https://www.openblender.io/ "this") link (it is free) to be able to pull the dataset. However, I have included a dataset for April 20, 2020 in this repository, but if you want to access the real-time data, you should pull it from the OpenBlender website.
You can also use the **API token** provided for you after registration and pull the dataset into a **Pandas dataframe**. A sample script to do this is provided in the repository.

## References
1. Towards data science article (see [link](https://towardsdatascience.com/gather-all-the-coronavirus-data-with-python-19aa22167dea "link"))
