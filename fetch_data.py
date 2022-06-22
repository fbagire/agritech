import numpy as np
import pylas

pylas.read('C:/Windows/System32/ept-data/3-0-1-3.laz')
    # as fh:
    # print('Points from Header:', fh.header.point_count)
    # las = fh.read()
    # print(las)
    # print('Points from data:', len(las.points))
    # ground_pts = las.classification == 2
    # bins, counts = np.unique(las.return_number[ground_pts], return_counts=True)
    # print('Ground Point Return Number distribution:')
    # for r, c in zip(bins, counts):
    #     print('    {}:{}'.format(r, c))
