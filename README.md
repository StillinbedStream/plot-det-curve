# plot-det-curve
This repository proposes examples of DET (Detection error tradeoff) curve plot. For the moment, only one example in file *example1.py* is available.

> A detection error tradeoff (DET) graph is a graphical plot of error rates for binary classification systems, plotting the false rejection rate vs. false acceptance rate.
> - [wikipedia definition](https://en.wikipedia.org/wiki/Detection_error_tradeoff)

## Install requirements
To use this code, you only need to install python and then install the requirements using the following command:
```
pip install -r requirements.txt
```

## Binary classification
### What is binary classification

> Binary or binomial classification is the task of classifying the elements of a given set into two groups (predicting which group each one belongs to)
> - [wikipedia definition](https://en.wikipedia.org/wiki/Binary_classification)

### Score system
Most of the time, to do a binary classification we ask to the system for a given input to generate a score between 0 and 1. Then, we guess at which class belong the input using a threshold. If the value is less than the threshold, the class 0, otherwise, the class is 1.

### Target and Non Target
- Targets are elements to associate with the class 1.
- Non target are elements associated to the class 2.

You may encounter the variables ```__tar__``` and ```__non__```. They respectively correspond to the score gave by the system for each target elements and the non target elements.

### Others needed information
Here, all you need about det curve:
- [Detection error tradeoff](https://en.wikipedia.org/wiki/Detection_error_tradeoff)
- [False acceptance (rate)](https://www.webopedia.com/TERM/F/false_acceptance.html)
- [False rejection (rate)](https://www.webopedia.com/TERM/F/false_rejection.html)

## Sidekit documentation
Here some interesting links:
- [documentation](https://projets-lium.univ-lemans.fr/sidekit/api/bosaris/detplot.html)
- [sources](https://projets-lium.univ-lemans.fr/sidekit/_modules/sidekit/bosaris/detplot.html)
