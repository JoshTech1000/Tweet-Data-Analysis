import orjson
import os
from zipfile import ZipFile
from shapely.geometry import shape

def dir_list(path_of_dir):  # get the names of files in folder
    return os.listdir(path_of_dir)


def question_1(element):
    return (element.get('id'), element.get('created_at'), element.get('timestamp_ms')) if element.get('id') else None

def question_2(element):
    return (element.get('id'), element.get('user').get('id')) if element.get('id') else None

def question_3(element):
    if element.get('id') and element.get('coordinates'):
        long, lat = element.get('coordinates').get('coordinates')
        return lat, long

def question_3_3(element):
    if element.get('id') and (place:=element.get('place')):
        return element.get('id'), shape(place.get('bounding_box'))
    
def question_3_4(element):
    if element.get('id') and element.get('coordinates'):
        # long, lat = element.get('coordinates').get('coordinates')
        return element.get('id'), shape(element.get('coordinates'))
    
def question_4_1(element):
    if element.get('id') and element.get('timestamp_ms'):
        return element.get('id'), element.get('timestamp_ms'), 
    
def zip_tweet_operator(zip_f, dir_path="TwitterJune2022", orjson_get=question_1):
    # zip_f name of zip file
    # TODO: change the function to suit your needs

    #zip_folder is just zipfile but seen in the lens of a folder that contains files as zipfile contains atleast a file
    with ZipFile(f'{dir_path}/{zip_f}', 'r') as zip_folder:
        with zip_folder.open(zip_folder.namelist()[0], ) as orjson_file_obj:
            return tuple(map(orjson_get, map(orjson.loads, orjson_file_obj)))

""" codes below run the zip_tweet_operator based on the question functions above.
    And the functions below is used in the tweet_op ipynb file.
    x -> zipfile name

"""
def ques_op3(x):
    return zip_tweet_operator(x, orjson_get=question_3)

def ques_op2(x):
    return zip_tweet_operator(x, orjson_get=question_2)

def ques_op3_3(x):
    return zip_tweet_operator(x, orjson_get=question_3_3)


def ques_op3_4(x):
    return zip_tweet_operator(x, orjson_get=question_3_4)

def ques_op4_1(x):
    return zip_tweet_operator(x, orjson_get=question_4_1)