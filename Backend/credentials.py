# Credentials file

# MongoDB credentials
# Return:
# Parameters
# dblink - database link
# database_name - name of the database
# collection_name - name of the collection
def mongodb_parameters():

    params = {
        'dblink': 'mongodb://test:test123@ds237363.mlab.com:37363/meher',
        'database_name': 'meher'
    }

    return params
