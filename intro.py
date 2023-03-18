from intra import IntraAPIClient
from config import campus_id

# from intra import ic
import pandas as pd

if __name__ == "__main__":
    ic = IntraAPIClient()

    campus_payload = {
        "filter[name]":"Seoul",
    }

    campus_response = ic.get("campus", params = campus_payload)
    if campus_response.status_code != 200: # Make sure response status is OK
        print('campus_response', campus_response)
        exit()
    campus_data = campus_response.json()
    #print('\ncampus_data', campus_data, type(campus_data))
    # campus_df = pd.read_json(campus_data)
    # campus_df.info()

    blocs_payload = {
        "filter[campus_id]":campus_id,
    }

    blocs_response = ic.get("blocs", params = blocs_payload)
    if blocs_response.status_code != 200: # Make sure response status is OK
        print('blocs_response', blocs_response)
        exit()
    blocs_data = blocs_response.json()
    blocs_df = pd.DataFrame.from_records(blocs_data)
    # blocs_df['squad_size'] = blocs_df['squad_size'].str.split(',')
    # blocs_df['created_at'] = blocs_df['created_at'].str.split(',')
    # blocs_df['updated_at'] = blocs_df['updated_at'].str.split(',')
    # blocs_df['coalitions'] = blocs_df['coalitions'].str.split(',')
    blocs_df.info()
    print(f'blocs_df.shape={blocs_df.shape}')
    print(blocs_df.head())

    coalitions = blocs_df.at[0, "coalitions"]
    #print(coalitions)
    #print(f'type(coalitions)= {type(coalitions)}')

    #print('\nblocs_data', blocs_data, type(blocs_data), len(blocs_data))
    #coalitions = blocs_data[0]["coalitions"]
    #print('\ncoalitions', coalitions, type(coalitions), len(coalitions))
    #coalitions_df = pd.read_json(coalitions)
    coalitions_df = pd.DataFrame.from_records(coalitions)
    coalitions_df.info()
    print(f'coalitions_df.shape={coalitions_df.shape}')
    print(coalitions_df.head())

    #coalition_names_df = coalitions_df.loc[:, ["id", "name"]]
    #print(f'coalition_names_df.shape={coalition_names_df.shape}')
    #coalition_names_df.info()
    #coalition_names_df = coalition_names_df.astype({'name':'string'})
    #coalition_names_df.loc[:,'name2'] = coalition_names_df['name'].str.split(',')
    #print(coalition_names_df.head())


    # payload = {
    #     "filter[primary_campus_id]":campus_id
    # }

    # # Let's see the progress
    # ic.progress_bar=True

    # # GET all users with specified primary campus
    # # Note that .pages_threaded returns json
    # data = ic.pages_threaded("users", params=payload)

    # for i, user in enumerate(data):
    #     print(f'i={i}, user={user}')



    # Filter by campus in specified range of updated_at
    payload = {
        "filter[campus_id]":campus_id,
        #"range[updated_at]":"2019-01-01T00:00:00.000Z,2021-01-01T00:00:00.000Z"
    }

    # # GET campus_users of specified campus in range
    # response = ic.get("campus_users", params=payload)
    # if response.status_code == 200: # Is the status OK?
    #     data = response.json()

    # for i, user in enumerate(data):
    #     print(f'\ni={i}, user={user}')



    response = ic.get("users/seongcho/locations_stats", params=payload)
    response = ic.get("users/seongcho", params=payload)

    if response.status_code == 200: # Is the status OK?
        data = response.json()

    for i, key in enumerate(data):
        print(f'\ni={i}, {key}:{data[key]}')


    exit()

    payload = {
        "filter[name]":"Seoul",
        #"filter[primary_campus]":29,
        #"filter[cursus]":1,
        #"range[final_mark]":"100,125",
        #"sort":"-final_mark,name"
    }

    #response = ic.get("campus", params = payload)
    response = ic.get("teams", params = payload)
    # response = ic.get("https://api.intra.42.fr/v2/teams")

    print('response', response)


    if response.status_code == 200: # Make sure response status is OK
        data = response.json()
        print('data', data, type(data))
        #df = pd.read_json(data)
        # df.info()



