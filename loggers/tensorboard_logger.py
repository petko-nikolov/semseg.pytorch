from tensorboardX import SummaryWriter
import numpy as np
from utils import flatten_dict, ColorPalette256


class TensorboardLogger:
    def __init__(self, log_directory):
        self.log_directory = log_directory
        self.summary_writer = SummaryWriter(self.log_directory)
        self.color_palette = ColorPalette256(256)

    def log_metrics(self, iteration, metrics, prefix):
        for key, value in flatten_dict(metrics).items():
            self.summary_writer.add_scalar(
                "{}/{}".format(prefix, key), value, iteration)

    def log_prediction_images(self, iteration, image, gt, prediction, name, prefix):
        gt = self.color_palette.encode_color(gt).transpose([0, 3, 1, 2])
        prediction = self.color_palette.encode_color(prediction).transpose([0, 3, 1, 2])
        combined_images = np.concatenate((image, gt, prediction), axis=-1)
        for i in range(image.shape[0]):
            self.summary_writer.add_image(
                "{}/{}/{}".format(prefix, name, i), combined_images[i], iteration)
