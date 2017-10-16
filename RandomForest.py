import numpy as np



import sys
import tensorflow
from tensorflow.contrib.tensor_forest.client\
    import random_forest
from tensorflow.contrib.tensor_forest.python\
    import tensor_forest
from tensorflow.contrib.tensor_forest.python\
    import tensor_forest_v5

FLAGS = None

## Random Forest Classifier
def build_estimator(model_dir):
    """Build an estimator"""
    hparams = tensor_forest.ForestHParams(
        num_classes=10, num_features=784,
        num_trees=FLAGS.num_trees, max_nodes=FLAGS.max_nodes)
    graph_builder_class = tensor_forest.RandomForestGraphs
    if FLAGS.use_training_loss:
        graph_builder_class = tensor_forest_v5.TrainingLossForest
        