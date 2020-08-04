# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
import pandas as pd
from dotenv import find_dotenv, load_dotenv
import os


@click.command()	
@click.argument('input_filepath', type=click.Path(exists=True))	
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    logger.info('import data, extract parts we want in a list')
    print("Testing")
    print(os.getcwd())
    print(os.path.join(os.getcwd(), input_filepath, '20_newsgroups'))
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk('input_filepath/20_newsgroups'):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    print("here")
    print(listOfFiles)
    print(len(listOfFiles))
    print("new_paths")
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(os.path.join(os.getcwd(), input_filepath, '20_newsgroups')):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    print("here")
    print(listOfFiles)
    print(len(listOfFiles))
    
    data=[]
    passed=[]
    for file in listOfFiles:
    
        f = open(file, 'r') 
        try:
            lines = f.read()
            data.append([lines.split('\n\n', 1)[1], lines.split('\nSubject: ', 1)[1].split('\n', 1)[0], file.split('/')[2]])
        except:
            passed.append(file.split('/')[2:])
            pass
        f.close()
    
    logger.info('transform data to pandas dataframe')
    
    df = pd.DataFrame(data, columns = ['Message', 'Subject', 'Category'])
    #print(df.shape())
    
    logger.info('storing data in parquet file')
    df.to_parquet(output_filepath)
    

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
