import pandas as pd
import requests
import os
import tqdm

def download_image(url,filename,N):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    # filename = os.path.basename(url) #takes the last part of the url
    with open(f'./images-{N}/{filename}', 'wb') as f:
        f.write(response.content) 
        


# open dataset
# SOURCE: https://mushroomobserver.org/articles/20
df = pd.read_csv('./mushroom_image_dataset.csv')

# open swiss_fungi.xlsx 
# SOURCE: https://swissfungi.wsl.ch/en/distribution-data.html
df_swiss_fungi = pd.read_excel('./swiss_fungi_dataset.xlsx')

# extract pilzname from df_swiss_fungi in a list
list_swiss_fungi = df_swiss_fungi['PILZNAME'].unique()
len(list_swiss_fungi)

# create new df_filtered that only contains swiss fungi
df_filtered = df[df['name'].isin(list_swiss_fungi)]


# download images for selected mushrooms
mushroom_list = ['Morchella','Gyromitra esculenta','Cantharellus','Amanita muscaria',
                 'Omphalotus olearius', 'Boletus edulis', 'Boletus radicans', 'Lepiota',
                 'Macrolepiota procera', 'Laccaria amethystina', 'Cortinarius vernus',
                 'Coprinus comatus', 'Coprinopsis atramentaria', 'Agaricus campestris', 'Agaricus xanthodermus']  # Add your list of mushrooms here


N = 20
for mushroom in tqdm.tqdm(mushroom_list, desc='Downloading images'):
    df_res = df_filtered[df_filtered['name'].str.contains(mushroom)]

    # create folder for each mushroom
    if not os.path.exists(f'./images-{N}/{mushroom}'):
        os.makedirs(f'./images-{N}/{mushroom}')

    for i in tqdm.tqdm(range(min(N, len(df_res))), desc=f'{mushroom} images', leave=False):
        download_image(df_res.iloc[i]['image'],f'{mushroom}/{mushroom}_{i}.jpg',N)

