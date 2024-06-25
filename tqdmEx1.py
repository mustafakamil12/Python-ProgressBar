import time
from tqdm.notebook import tqdm

dogs = ['dog1', 'dog2', 'dog3','dog4', 'dog5', 'dog6','dog7', 'dog8', 'dog9']

pbar = tqdm(total=9)
for dog in tqdm(dogs, desc='dog counter', unit='barks'):
    time.sleep(0.5)
    pbar.set_description(f'Processing {dog}')
print('done')