import numpy as np
import torch
import torch.nn.functional as F
import torch.utils.data as data

from neuralnets.util.io import read_volume
from neuralnets.util.tools import sample_unlabeled_input, sample_labeled_input


class StandardDataset(data.Dataset):

    def __init__(self, data_path, scaling=None, type='tif3d'):
        self.data_path = data_path
        self.scaling = scaling

        # load the data
        self.data = read_volume(data_path, type=type)

        # rescale the dataset if necessary
        if scaling is not None:
            target_size = np.asarray(np.multiply(self.data.shape, scaling), dtype=int)
            self.data = \
                F.interpolate(torch.Tensor(self.data[np.newaxis, np.newaxis, ...]), size=tuple(target_size),
                              mode='area')[0, 0, ...].numpy()

    def __getitem__(self, i):
        pass

    def __len__(self):
        return self.data.shape[0]

    def get_stats(self):
        mu = np.mean(self.data)
        std = np.std(self.data)

        return mu, std


class StronglyLabeledStandardDataset(StandardDataset):

    def __init__(self, data_path, label_path, scaling=None, type='tif3d'):
        super().__init__(data_path, scaling=scaling, type=type)

        self.label_path = label_path

        # load labels
        self.labels = read_volume(label_path, type=type)

        # rescale the dataset if necessary
        if scaling is not None:
            target_size = np.asarray(np.multiply(self.labels.shape, scaling), dtype=int)
            self.labels = \
                F.interpolate(torch.Tensor(self.labels[np.newaxis, np.newaxis, ...]), size=tuple(target_size),
                              mode='area')[0, 0, ...].numpy()

        self.mu, self.std = self.get_stats()

    def __getitem__(self, i):

        # get random sample
        input = self.data[i]
        target = self.labels[i]

        if input.shape[0] > 1:
            # add channel axis if the data is 3D
            input, target = input[np.newaxis, ...], target[np.newaxis, ...]

        if target.min() == 255:  # make sure we have at least one labeled pixel in the sample, otherwise processing is useless
            return self.__getitem__(i)
        else:
            return input, target


class UnlabeledStandardDataset(StandardDataset):

    def __init__(self, data_path, scaling=None, type='tif3d'):
        super().__init__(data_path, scaling=scaling, type=type)

        self.mu, self.std = self.get_stats()

    def __getitem__(self, i):

        # get random sample
        input = self.data[i]

        if input.shape[0] > 1:
            # add channel axis if the data is 3D
            return input[np.newaxis, ...]
        else:
            return input


class VolumeDataset(data.Dataset):

    def __init__(self, data_path, input_shape, scaling=None, len_epoch=1000, type='tif3d'):
        self.data_path = data_path
        self.input_shape = input_shape
        self.scaling = scaling
        self.len_epoch = len_epoch

        # load the data
        self.data = read_volume(data_path, type=type)

        # rescale the dataset if necessary
        if scaling is not None:
            target_size = np.asarray(np.multiply(self.data.shape, scaling), dtype=int)
            self.data = \
                F.interpolate(torch.Tensor(self.data[np.newaxis, np.newaxis, ...]), size=tuple(target_size),
                              mode='area')[0, 0, ...].numpy()

    def __getitem__(self, i):
        pass

    def __len__(self):
        return self.len_epoch

    def get_stats(self):
        mu = np.mean(self.data)
        std = np.std(self.data)

        return mu, std


class StronglyLabeledVolumeDataset(VolumeDataset):

    def __init__(self, data_path, label_path, input_shape=None, scaling=None, len_epoch=1000, type='tif3d'):
        super().__init__(data_path, input_shape, scaling=scaling, len_epoch=len_epoch, type=type)

        self.label_path = label_path

        # load labels
        self.labels = read_volume(label_path, type=type)

        # rescale the dataset if necessary
        if scaling is not None:
            target_size = np.asarray(np.multiply(self.labels.shape, scaling), dtype=int)
            self.labels = \
                F.interpolate(torch.Tensor(self.labels[np.newaxis, np.newaxis, ...]), size=tuple(target_size),
                              mode='area')[0, 0, ...].numpy()

        self.mu, self.std = self.get_stats()

    def __getitem__(self, i):

        # get random sample
        input, target = sample_labeled_input(self.data, self.labels, self.input_shape)

        if input.shape[0] > 1:
            # add channel axis if the data is 3D
            input, target = input[np.newaxis, ...], target[np.newaxis, ...]

        if target.min() == 255:  # make sure we have at least one labeled pixel in the sample, otherwise processing is useless
            return self.__getitem__(i)
        else:
            return input, target


class UnlabeledVolumeDataset(VolumeDataset):

    def __init__(self, data_path, input_shape=None, scaling=None, len_epoch=1000, type='tif3d'):
        super().__init__(data_path, input_shape, scaling=scaling, len_epoch=len_epoch, type=type)

        self.mu, self.std = self.get_stats()

    def __getitem__(self, i):

        # get random sample
        input = sample_unlabeled_input(self.data, self.input_shape)

        if input.shape[0] > 1:
            # add channel axis if the data is 3D
            return input[np.newaxis, ...]
        else:
            return input


class MultiVolumeDataset(data.Dataset):

    def __init__(self, data_path, input_shape, scaling=None, len_epoch=1000, types=['tif3d'], sampling_mode='uniform'):
        self.data_path = data_path
        self.input_shape = input_shape
        self.scaling = scaling
        self.len_epoch = len_epoch
        self.sampling_mode = sampling_mode

        # load the data
        self.data = []
        self.data_sizes = []
        for k, path in enumerate(data_path):
            data = read_volume(path, type=types[k])

            # rescale the dataset if necessary
            if scaling is not None:
                target_size = np.asarray(np.multiply(data.shape, scaling[k]), dtype=int)
                data = \
                    F.interpolate(torch.Tensor(data[np.newaxis, np.newaxis, ...]), size=tuple(target_size),
                                  mode='area')[0, 0, ...].numpy()

            self.data.append(data)
            self.data_sizes.append(data.size)
        self.data_sizes = np.array(self.data_sizes)
        self.data_sizes /= np.sum(self.data_sizes)

    def __getitem__(self, i):
        pass

    def __len__(self):
        return self.len_epoch

    def get_stats(self):
        mu = []
        std = []

        for data in self.data:
            mu.append(np.mean(data))
            std.append(np.std(data))

        return mu, std


class StronglyLabeledMultiVolumeDataset(MultiVolumeDataset):

    def __init__(self, data_path, label_path, input_shape=None, scaling=None, len_epoch=1000, types=['tif3d'],
                 sampling_mode='uniform'):
        super().__init__(data_path, input_shape, scaling=scaling, len_epoch=len_epoch, types=types,
                         sampling_mode=sampling_mode)

        self.label_path = label_path

        # load the data
        self.labels = []
        for k, path in enumerate(label_path):
            labels = read_volume(path, type=types[k])

            # rescale the dataset if necessary
            if scaling is not None:
                target_size = np.asarray(np.multiply(labels.shape, scaling[k]), dtype=int)
                labels = \
                    F.interpolate(torch.Tensor(labels[np.newaxis, np.newaxis, ...]), size=tuple(target_size),
                                  mode='area')[0, 0, ...].numpy()

            self.labels.append(labels)

        self.mu, self.std = self.get_stats()

    def __getitem__(self, i):

        # select dataset
        if self.sampling_mode is 'uniform':
            k = np.random.randint(0, len(self.data))
        else:
            k = np.random.choice(len(self.data), p=self.data_sizes)

        # get random sample
        input, target = sample_labeled_input(self.data[k], self.labels[k], self.input_shape)

        if input.shape[0] > 1:
            # add channel axis if the data is 3D
            input, target = input[np.newaxis, ...], target[np.newaxis, ...]

        if target.min() == 255:  # make sure we have at least one labeled pixel in the sample, otherwise processing is useless
            return self.__getitem__(i)
        else:
            return input, target


class UnlabeledMultiVolumeDataset(MultiVolumeDataset):

    def __init__(self, data_path, input_shape=None, scaling=None, len_epoch=1000, types='tif3d',
                 sampling_mode='uniform'):
        super().__init__(data_path, input_shape, scaling=scaling, len_epoch=len_epoch, types=types,
                         sampling_mode=sampling_mode)

        self.mu, self.std = self.get_stats()

    def __getitem__(self, i):

        # select dataset
        if self.sampling_mode is 'uniform':
            k = np.random.randint(0, len(self.data))
        else:
            k = np.random.choice(len(self.data), p=self.data_sizes)

        # get random sample
        input = sample_unlabeled_input(self.data[k], self.input_shape)

        if input.shape[0] > 1:
            # add channel axis if the data is 3D
            return input[np.newaxis, ...]
        else:
            return input
