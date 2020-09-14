# Text-classification-using-the-semi-supervised-learning-methods 
Abstract:<br>
The work is devoted to the issue of semi-supervised learning for
the tasks of text classification. One of the aims is to test the semi-supervised
learning algorithm called FixMatch in the NLP domain.
This method is considered to be state-of-the-art for problems of image
classification with a few training labeled examples. In order to test
FixMatch for text classification, it is necessary to create realistic
augmentations, which will be proposed in the following work. In
order to evaluate the FixMatch properly, two other popular SSL
methods (VAT, Pseudo-Label) and supervised model, will be trained
as comparative baselines. Another goal of this work is to check how
the result on the test set are affected by training process and selection
of hyperparameters using different ratio of the training and validation
set sizes. The last goal will be to examine the quality of the chosen
hyperparameters on small validation sets, also by checking the results
of the SLL methods which were trained on more labelled and unlabeled
data.

Results of the conducted experiments for the FixMatch algorithm
indicate, that with chosen experimental settings it was not possible
to transfer state-of-the-art scores from the computer vision domain
into the NLP domain. It can be hypothesized that the number of
validation data samples and/or the duration of training was too low.
After observing some of the experiments results with different SSL
methods, a conclusion appears, that the number of examples in the
validation set should be slightly less or equal to the number of examples
in the training set. For tested SSL methods, the error on the test set
is decreasing with training on an additional number of labeled data,
while in the case of unlabeled data, there is no such relation.
