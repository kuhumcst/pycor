import os

basename = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    DanNet_PATH = 'N:/HUM-NORS-cst-projekter/COR/data_modeller/DanNet'
    # word2vec_PATH = 'N:/HUM-NORS-cst-projekter/COR/data_modeller/word2vec/dsl_skipgram_2020_m5_f500_epoch2_w5.model.txtvectors'
    word2vec_PATH = 'C:/Users/nmp828/Documents/pycor/data/dsl_skipgram_2020_m5_f500_epoch2_w5.model.txtvectors'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    ENV = 'development'
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ClusteringConfig(object):
    def __init__(self, model_name):
        self.model_name = model_name

        if model_name == 'bert':
            self.bh = 0.8  # binary threshold
            self.h0 = 0.42  # lower threshold
            self.h1 = 0.75  # upper threshold
            self.h_mean1 = 0.7  # cluster upper threshold
            self.hm_mean = 0.632  # cluster median threshold
            self.h_mean0 = 0.3  # cluster median lower threshold
            self.bias = 0.95
            self.absmin = 0.2 #0.344 # about 1_Q1
            self.absmax = 0.7 #0.455 # HIGHER THAN 0_Q3



        elif model_name == 'word2vec':
            self.bh = 0.31 #0.348  # binary threshold #a bit higher than 1_Q2
            self.h0 = 0.298 #0.32 #0.19  # lower threshold #smaller than 0_Q1
            self.h1 = 0.4 #0.428 #0.458  # upper threshold #larger than 1_Q3
            self.h_mean1 = 0.375 #0.45  # cluster upper threshold #about 0_Q2
            self.hm_mean = 0.151 # cluster median threshold #check data
            self.h_mean0 = 0.308 #0.325  # cluster median lower threshold #about 1_Q2
            self.bias = 0.7
            self.absmin = 0.23 #0.344 # about 1_Q1
            self.absmax = 0.46 #0.455 # HIGHER THAN 0_Q3

        elif model_name == 'base':
            self.bh = 0.5  # binary threshold
            self.h0 = 0  # lower threshold
            self.h1 = 1  # upper threshold
            self.h_mean1 = 1  # cluster upper threshold
            self.hm_mean = 0.5  # cluster median threshold
            self.h_mean0 = 0  # cluster median lower threshold
            self.bias = 1
            self.absmin = 0
            self.absmax = 1
