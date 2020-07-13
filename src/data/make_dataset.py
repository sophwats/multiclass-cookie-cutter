# -*- coding: utf-8 -*-
import logging
import pandas as pd
import os



def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    logger.info('import data, extract parts we want in a list')
    
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk('input_filepath/20_newsgroups'):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
        
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
    
    logger.info('storing data in parquet file')
    df.to_parquet(output_filepath)
    

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()
