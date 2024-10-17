import matplotlib.pyplot as plt

#from sklearn.datasets import make_regression

#features, target, coeffients = make_regression(n_samples=300,
#                                               n_features=2,
#                                               n_informative=2,
#                                               n_targets=1,
#                                              noise=0.0,
#                                              coef=True,
#                                               random_state=1)
#print(features.shape, target.shape, coeffients)

#plt.scatter(features[:, 0], features[:, 1], s=100)
#plt.show()

#from sklearn.datasets import make_classification

#features, targets = make_classification(n_samples=300,
#                                       n_features=3,
#                                       n_informative=3,
#                                       n_redundant=0,
#                                       n_classes=2,
#                                        weights=[0.25, 0.75],
#                                      random_state=1)
#print(features)
#print(targets)

#from sklearn.datasets import make_blobs
#
#features, targets = make_blobs(n_samples=500,
#                               n_features=2,
#                               centers=4,
#                               cluster_std=1,
#                               shuffle=True,
#                               random_state=1)
#print(targets)
#plt.scatter(features[:, 0], features[:, 1], c=targets, s=100)
#plt.show()

# from sklearn.datasets import make_circles
# features , targets = make_circles(n_samples=500,
#                                    factor=0.2,
#                                   noise=0.1)
# plt.scatter(features[:, 0], features[:, 1], c=targets)
# plt.show()

from sklearn.datasets import make_moons

features, targets = make_moons(n_samples=500,
                               noise=0.1,
                               random_state=1)
plt.scatter(features[:, 0], features[:, 1], c=targets, s=100)
plt.show()




 

