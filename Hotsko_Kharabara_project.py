import numpy as np
from matplotlib import pyplot as plt
import os
import cv2 
import tensorflow as tf
import joblib

def normalize_data(data):
    mean_of_each_image = data.mean(axis=0)
    data_normalized = data - mean_of_each_image
    # data_normalized /= np.std(data, axis=0)
    return data_normalized

def transform_data(data, principal_components):
    data_normalized = normalize_data(data)
    return data_normalized.dot(principal_components)


def run(img_pathes):
    images_np = np.zeros((len(img_pathes), 100, 100), dtype=np.uint8)
    for i in range(len(img_pathes)):
        img = cv2.imread(img_pathes[i], cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (100, 100))
        images_np[i] = img
    
    principal_components = np.load('model_data/principal_components.npy')

    images_np = images_np.reshape(images_np.shape[0], -1)

    img_transformed = transform_data(images_np, principal_components)
    # Load the model
    Random_Forest_model = joblib.load('model_data/Random_Forest.pkl')
    Decision_Tree_model = joblib.load('model_data/decission_tree.pkl')
    KNN_model = joblib.load('model_data/KNeighbors.pkl')
    SVC_model = joblib.load('model_data/svc.pkl')

    # Predict the result
    Decision_Tree_model_result = Decision_Tree_model.predict(img_transformed)
    Random_Forest_model_result = Random_Forest_model.predict(img_transformed)
    KNN_model_result = KNN_model.predict(img_transformed)
    SVC_model_result = SVC_model.predict(img_transformed)
    return Decision_Tree_model_result, Random_Forest_model_result, KNN_model_result, SVC_model_result
    
if __name__ == "__main__":
    print(run(["static/2.jpg"]))