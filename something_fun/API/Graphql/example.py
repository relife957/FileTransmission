import requests
from prettyprinter import pprint

def get_date(query,variables):
    url = 'https://graphql.anilist.co'

    # Make the HTTP Api request
    response = requests.post(url, json={'query': query, 'variables': variables})
    if response.status_code == 200 :
        return response.json()
    return "错误: "+ str(response.status_code)

def main():
    query = '''
    query ($id: Int) { # Define which variables will be used in the query (id)
      Character (id: $id) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
        id
        name{
            first
            last
            native
            alternative
        }
        image{
            large
            medium
        }
        description
        siteUrl
      }
    }
    '''
    # Define our query variables and values that will be used in the query request
    variables = {
        'id': 34564
    }
    res = get_date(query,variables)
    pprint(res)


if __name__ == '__main__':
    main()
