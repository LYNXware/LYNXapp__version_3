from resource_path import resource_path
import pickle

with open(resource_path(f'user/layouts/major/halmak_adjusted.pickle'), 'rb') as f:
    main_left = pickle.load(f)
    main_right = pickle.load(f)
    sub_left = pickle.load(f)
    sub_right = pickle.load(f)
    app_version = pickle.load(f)  # 'appVersion'


print(main_left)
print(main_left['LI1'])
print(main_left['LI1'].ascii_set)