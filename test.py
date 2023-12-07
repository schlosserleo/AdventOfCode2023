from tqdm import tqdm, trange
import time

with tqdm(total=100) as pbar:
    for i in range(10):
        time.sleep(0.2)
        pbar.update(10)

print('done')