import tensorflow as tf
import time

flags = tf.app.flags
flags.DEFINE_string('mode', 'train', 'train or test')

# Training logs
flags.DEFINE_integer('max_step', 250000, '# of step for training')
flags.DEFINE_integer('SAVE_FREQ', 1000, 'Number of steps to save model')
flags.DEFINE_integer('SUMMARY_FREQ', 100, 'Number of step to save summary')
flags.DEFINE_integer('VAL_FREQ', 1000, 'Number of step to evaluate the network on Validation data')
flags.DEFINE_float('init_lr', 1e-3, 'learning rate')

# Hyper-parameters
flags.DEFINE_string('loss_type', 'dice', 'cross-entropy or dice')
flags.DEFINE_float('lmbda', 1e-3, 'L2 regularization coefficient')
flags.DEFINE_integer('batch_size', 5, 'training batch size')

# data
flags.DEFINE_string('data_dir', '../h5_data_SA/', 'Data directory')
flags.DEFINE_integer('height', 32, 'height size')   # should be equal to patch_size
flags.DEFINE_integer('width', 32, 'width size')     # should be equal to patch_size
flags.DEFINE_integer('depth', 32, 'depth size')     # should be equal to patch_size
flags.DEFINE_integer('channel', 1, 'channel size')

# Directories
flags.DEFINE_string('logdir', './log_dir', 'Logs directory')
flags.DEFINE_string('modeldir', './model_dir', 'Model directory')
flags.DEFINE_string('savedir', './result', 'Result saving directory')

flags.DEFINE_string('model_name', 'model', 'Model file name')
flags.DEFINE_integer('reload_step', 0, 'Reload step to continue training')

# network architecture
flags.DEFINE_integer('num_cls', 2, 'Number of output classes')
flags.DEFINE_integer('start_channel_num', 16, 'start number of outputs for the first conv layer')
flags.DEFINE_integer('filter_size', 3, 'Filter size for the conv and deconv layers')
flags.DEFINE_integer('pool_filter_size', 2, 'Filter size for pooling layers')

args = tf.app.flags.FLAGS
