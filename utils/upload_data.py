import data.db_connector
def upload_data():
    button = input("Do you want to upload data? (y/n)")
    if button == 'y':
        data.db_connector.store_question()
    else:
        print('Operation canceled')
