# Credentials file

# MongoDB credentials
# Return:
# Parameters
# dblink - database link
# database_name - name of the database
# collection_name - name of the collection
def mongodb_parameters():

    params = {
        'dblink': 'mongodb://test:test123@ds213896.mlab.com:13896/e-learning-on-cloud',
        'database_name': 'e-learning-on-cloud',
        'collection_name': 'User'
    }

    return params
