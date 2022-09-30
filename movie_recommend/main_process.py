"""
영화 추천 모델
====================

100 라인까지 허용
"""
import os
import pandas as pd




class RecommendMovie():
    
    def __init__(self, env):
        
        if env == 'google':  
            self.data_dir = 'drive/MyDrive/jupyterlab/RecoSys/Data'
        else :
            pass
            

    def load_data(self):
        # user data
        user_path = os.path.join(self.data_dir, 'u.user')
        user_colsL = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
        user_df = pd.read_csv(user_path, sep ='|', names = user_colsL, encoding = 'latin-1')
        user_df = user_df.set_index('user_id')
        
        # item data
        item_path = os.path.join(self.data_dir, 'u.item')
        item_colsL = ['movie_id','title','release date','video release date','IMDB URL',
                      'unknown','Action','Adventure','Animat ion', 'Children\'s','Comedy',
                      'Crime','Documentary ','Drama','Fantasy','Film- Noir','Horror',
                      'Musical','Mystery','Romance ','Sci-Fi','Thriller','War','Western']
        item_df = pd.read_csv(item_path, sep ='|',names = item_colsL, encoding = 'latin-1')
        item_df = item_df.set_index('movie_id')
        
        # rate data
        rate_path = os.path.join(self.data_dir,  'u.data')
        rate_colsL = ['user_id', 'movie_id', 'rating', 'timestamp']
        rate_df = pd.read_csv(rate_path, sep = '\t', names = rate_colsL, encoding = 'latin-1')
        

        return user_df, item_df, rate_df


# ------------------------------------------------------------------------------------------------ # 