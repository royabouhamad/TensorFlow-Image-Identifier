import os, sys

import tensorflow as tf
def label(filePath):
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

    # change this as you see fit
    image_path = filePath

    # Read in the image_data
    image_data = tf.gfile.FastGFile(image_path, 'rb').read()

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line
                       in tf.gfile.GFile("tensor/retrained_labels.txt")]

    # Unpersists graph from file
    with tf.gfile.FastGFile("tensor/retrained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

        predictions = sess.run(softmax_tensor, \
                 {'DecodeJpeg/contents:0': image_data})

        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

        human_string = label_lines[top_k[0]]
        score = predictions[0][top_k[0]]
        score *= 100
        return (human_string, score)
