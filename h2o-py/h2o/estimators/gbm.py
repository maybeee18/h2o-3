#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# This file is auto-generated by h2o-3/h2o-bindings/bin/gen_python.py
# Copyright 2016 H2O.ai;  Apache License Version 2.0 (see LICENSE for details)
#
from __future__ import absolute_import, division, print_function, unicode_literals

from h2o.estimators.estimator_base import H2OEstimator
from h2o.exceptions import H2OValueError
from h2o.frame import H2OFrame
from h2o.utils.typechecks import assert_is_type, Enum, numeric


class H2OGradientBoostingEstimator(H2OEstimator):
    """
    Gradient Boosting Machine

    Builds gradient boosted trees on a parsed data set, for regression or classification.
    The default distribution function will guess the model type based on the response column type.
    Otherwise, the response column must be an enum for "bernoulli" or "multinomial", and numeric
    for all other distributions.
    """

    algo = "gbm"

    def __init__(self, **kwargs):
        super(H2OGradientBoostingEstimator, self).__init__()
        self._parms = {}
        names_list = {"model_id", "training_frame", "validation_frame", "nfolds", "keep_cross_validation_predictions",
                      "keep_cross_validation_fold_assignment", "score_each_iteration", "score_tree_interval",
                      "fold_assignment", "fold_column", "response_column", "ignored_columns", "ignore_const_cols",
                      "offset_column", "weights_column", "balance_classes", "class_sampling_factors",
                      "max_after_balance_size", "max_confusion_matrix_size", "max_hit_ratio_k", "ntrees", "max_depth",
                      "min_rows", "nbins", "nbins_top_level", "nbins_cats", "r2_stopping", "stopping_rounds",
                      "stopping_metric", "stopping_tolerance", "max_runtime_secs", "seed", "build_tree_one_node",
                      "learn_rate", "learn_rate_annealing", "distribution", "quantile_alpha", "tweedie_power",
                      "huber_alpha", "checkpoint", "sample_rate", "sample_rate_per_class", "col_sample_rate",
                      "col_sample_rate_change_per_level", "col_sample_rate_per_tree", "min_split_improvement",
                      "histogram_type", "max_abs_leafnode_pred", "pred_noise_bandwidth", "categorical_encoding"}
        if "Lambda" in kwargs: kwargs["lambda_"] = kwargs.pop("Lambda")
        for pname, pvalue in kwargs.items():
            if pname == 'model_id':
                self._id = pvalue
                self._parms["model_id"] = pvalue
            elif pname in names_list:
                # Using setattr(...) will invoke type-checking of the arguments
                setattr(self, pname, pvalue)
            else:
                raise H2OValueError("Unknown parameter %s = %r" % (pname, pvalue))

    @property
    def training_frame(self):
        """str: Id of the training data frame (Not required, to allow initial validation of model parameters)."""
        return self._parms.get("training_frame")

    @training_frame.setter
    def training_frame(self, training_frame):
        assert_is_type(training_frame, None, H2OFrame)
        self._parms["training_frame"] = training_frame


    @property
    def validation_frame(self):
        """str: Id of the validation data frame."""
        return self._parms.get("validation_frame")

    @validation_frame.setter
    def validation_frame(self, validation_frame):
        assert_is_type(validation_frame, None, H2OFrame)
        self._parms["validation_frame"] = validation_frame


    @property
    def nfolds(self):
        """int: Number of folds for N-fold cross-validation (0 to disable or >= 2). (Default: 0)"""
        return self._parms.get("nfolds")

    @nfolds.setter
    def nfolds(self, nfolds):
        assert_is_type(nfolds, None, int)
        self._parms["nfolds"] = nfolds


    @property
    def keep_cross_validation_predictions(self):
        """bool: Whether to keep the predictions of the cross-validation models. (Default: False)"""
        return self._parms.get("keep_cross_validation_predictions")

    @keep_cross_validation_predictions.setter
    def keep_cross_validation_predictions(self, keep_cross_validation_predictions):
        assert_is_type(keep_cross_validation_predictions, None, bool)
        self._parms["keep_cross_validation_predictions"] = keep_cross_validation_predictions


    @property
    def keep_cross_validation_fold_assignment(self):
        """bool: Whether to keep the cross-validation fold assignment. (Default: False)"""
        return self._parms.get("keep_cross_validation_fold_assignment")

    @keep_cross_validation_fold_assignment.setter
    def keep_cross_validation_fold_assignment(self, keep_cross_validation_fold_assignment):
        assert_is_type(keep_cross_validation_fold_assignment, None, bool)
        self._parms["keep_cross_validation_fold_assignment"] = keep_cross_validation_fold_assignment


    @property
    def score_each_iteration(self):
        """bool: Whether to score during each iteration of model training. (Default: False)"""
        return self._parms.get("score_each_iteration")

    @score_each_iteration.setter
    def score_each_iteration(self, score_each_iteration):
        assert_is_type(score_each_iteration, None, bool)
        self._parms["score_each_iteration"] = score_each_iteration


    @property
    def score_tree_interval(self):
        """int: Score the model after every so many trees. Disabled if set to 0. (Default: 0)"""
        return self._parms.get("score_tree_interval")

    @score_tree_interval.setter
    def score_tree_interval(self, score_tree_interval):
        assert_is_type(score_tree_interval, None, int)
        self._parms["score_tree_interval"] = score_tree_interval


    @property
    def fold_assignment(self):
        """
        Enum["auto", "random", "modulo", "stratified"]: Cross-validation fold assignment scheme, if fold_column is not
        specified. The 'Stratified' option will stratify the folds based on the response variable, for classification
        problems. (Default: "auto")
        """
        return self._parms.get("fold_assignment")

    @fold_assignment.setter
    def fold_assignment(self, fold_assignment):
        assert_is_type(fold_assignment, None, Enum("auto", "random", "modulo", "stratified"))
        self._parms["fold_assignment"] = fold_assignment


    @property
    def fold_column(self):
        """str: Column with cross-validation fold index assignment per observation."""
        return self._parms.get("fold_column")

    @fold_column.setter
    def fold_column(self, fold_column):
        assert_is_type(fold_column, None, str)
        self._parms["fold_column"] = fold_column


    @property
    def response_column(self):
        """str: Response variable column."""
        return self._parms.get("response_column")

    @response_column.setter
    def response_column(self, response_column):
        assert_is_type(response_column, None, str)
        self._parms["response_column"] = response_column


    @property
    def ignored_columns(self):
        """List[str]: Names of columns to ignore for training."""
        return self._parms.get("ignored_columns")

    @ignored_columns.setter
    def ignored_columns(self, ignored_columns):
        assert_is_type(ignored_columns, None, [str])
        self._parms["ignored_columns"] = ignored_columns


    @property
    def ignore_const_cols(self):
        """bool: Ignore constant columns. (Default: True)"""
        return self._parms.get("ignore_const_cols")

    @ignore_const_cols.setter
    def ignore_const_cols(self, ignore_const_cols):
        assert_is_type(ignore_const_cols, None, bool)
        self._parms["ignore_const_cols"] = ignore_const_cols


    @property
    def offset_column(self):
        """
        str: Offset column. This will be added to the combination of columns before applying the link function.
        """
        return self._parms.get("offset_column")

    @offset_column.setter
    def offset_column(self, offset_column):
        assert_is_type(offset_column, None, str)
        self._parms["offset_column"] = offset_column


    @property
    def weights_column(self):
        """
        str: Column with observation weights. Giving some observation a weight of zero is equivalent to excluding it
        from the dataset; giving an observation a relative weight of 2 is equivalent to repeating that row twice.
        Negative weights are not allowed.
        """
        return self._parms.get("weights_column")

    @weights_column.setter
    def weights_column(self, weights_column):
        assert_is_type(weights_column, None, str)
        self._parms["weights_column"] = weights_column


    @property
    def balance_classes(self):
        """
        bool: Balance training data class counts via over/under-sampling (for imbalanced data). (Default: False)
        """
        return self._parms.get("balance_classes")

    @balance_classes.setter
    def balance_classes(self, balance_classes):
        assert_is_type(balance_classes, None, bool)
        self._parms["balance_classes"] = balance_classes


    @property
    def class_sampling_factors(self):
        """
        List[float]: Desired over/under-sampling ratios per class (in lexicographic order). If not specified, sampling
        factors will be automatically computed to obtain class balance during training. Requires balance_classes.
        """
        return self._parms.get("class_sampling_factors")

    @class_sampling_factors.setter
    def class_sampling_factors(self, class_sampling_factors):
        assert_is_type(class_sampling_factors, None, [float])
        self._parms["class_sampling_factors"] = class_sampling_factors


    @property
    def max_after_balance_size(self):
        """
        float: Maximum relative size of the training data after balancing class counts (can be less than 1.0). Requires
        balance_classes. (Default: 5.0)
        """
        return self._parms.get("max_after_balance_size")

    @max_after_balance_size.setter
    def max_after_balance_size(self, max_after_balance_size):
        assert_is_type(max_after_balance_size, None, float)
        self._parms["max_after_balance_size"] = max_after_balance_size


    @property
    def max_confusion_matrix_size(self):
        """int: Maximum size (# classes) for confusion matrices to be printed in the Logs (Default: 20)"""
        return self._parms.get("max_confusion_matrix_size")

    @max_confusion_matrix_size.setter
    def max_confusion_matrix_size(self, max_confusion_matrix_size):
        assert_is_type(max_confusion_matrix_size, None, int)
        self._parms["max_confusion_matrix_size"] = max_confusion_matrix_size


    @property
    def max_hit_ratio_k(self):
        """
        int: Max. number (top K) of predictions to use for hit ratio computation (for multi-class only, 0 to disable)
        (Default: 0)
        """
        return self._parms.get("max_hit_ratio_k")

    @max_hit_ratio_k.setter
    def max_hit_ratio_k(self, max_hit_ratio_k):
        assert_is_type(max_hit_ratio_k, None, int)
        self._parms["max_hit_ratio_k"] = max_hit_ratio_k


    @property
    def ntrees(self):
        """int: Number of trees. (Default: 50)"""
        return self._parms.get("ntrees")

    @ntrees.setter
    def ntrees(self, ntrees):
        assert_is_type(ntrees, None, int)
        self._parms["ntrees"] = ntrees


    @property
    def max_depth(self):
        """int: Maximum tree depth. (Default: 5)"""
        return self._parms.get("max_depth")

    @max_depth.setter
    def max_depth(self, max_depth):
        assert_is_type(max_depth, None, int)
        self._parms["max_depth"] = max_depth


    @property
    def min_rows(self):
        """float: Fewest allowed (weighted) observations in a leaf. (Default: 10.0)"""
        return self._parms.get("min_rows")

    @min_rows.setter
    def min_rows(self, min_rows):
        assert_is_type(min_rows, None, numeric)
        self._parms["min_rows"] = min_rows


    @property
    def nbins(self):
        """
        int: For numerical columns (real/int), build a histogram of (at least) this many bins, then split at the best
        point (Default: 20)
        """
        return self._parms.get("nbins")

    @nbins.setter
    def nbins(self, nbins):
        assert_is_type(nbins, None, int)
        self._parms["nbins"] = nbins


    @property
    def nbins_top_level(self):
        """
        int: For numerical columns (real/int), build a histogram of (at most) this many bins at the root level, then
        decrease by factor of two per level (Default: 1024)
        """
        return self._parms.get("nbins_top_level")

    @nbins_top_level.setter
    def nbins_top_level(self, nbins_top_level):
        assert_is_type(nbins_top_level, None, int)
        self._parms["nbins_top_level"] = nbins_top_level


    @property
    def nbins_cats(self):
        """
        int: For categorical columns (factors), build a histogram of this many bins, then split at the best point.
        Higher values can lead to more overfitting. (Default: 1024)
        """
        return self._parms.get("nbins_cats")

    @nbins_cats.setter
    def nbins_cats(self, nbins_cats):
        assert_is_type(nbins_cats, None, int)
        self._parms["nbins_cats"] = nbins_cats


    @property
    def r2_stopping(self):
        """
        float: r2_stopping is no longer supported and will be ignored if set - please use stopping_rounds,
        stopping_metric and stopping_tolerance instead. Previous version of H2O would stop making trees when the R^2
        metric equals or exceeds this (Default: 1.79769313486e+308)
        """
        return self._parms.get("r2_stopping")

    @r2_stopping.setter
    def r2_stopping(self, r2_stopping):
        assert_is_type(r2_stopping, None, numeric)
        self._parms["r2_stopping"] = r2_stopping


    @property
    def stopping_rounds(self):
        """
        int: Early stopping based on convergence of stopping_metric. Stop if simple moving average of length k of the
        stopping_metric does not improve for k:=stopping_rounds scoring events (0 to disable) (Default: 0)
        """
        return self._parms.get("stopping_rounds")

    @stopping_rounds.setter
    def stopping_rounds(self, stopping_rounds):
        assert_is_type(stopping_rounds, None, int)
        self._parms["stopping_rounds"] = stopping_rounds


    @property
    def stopping_metric(self):
        """
        Enum["auto", "deviance", "logloss", "mse", "auc", "lift_top_group", "r2", "misclassification",
        "mean_per_class_error"]: Metric to use for early stopping (AUTO: logloss for classification, deviance for
        regression) (Default: "auto")
        """
        return self._parms.get("stopping_metric")

    @stopping_metric.setter
    def stopping_metric(self, stopping_metric):
        assert_is_type(stopping_metric, None, Enum("auto", "deviance", "logloss", "mse", "auc", "lift_top_group", "r2", "misclassification", "mean_per_class_error"))
        self._parms["stopping_metric"] = stopping_metric


    @property
    def stopping_tolerance(self):
        """
        float: Relative tolerance for metric-based stopping criterion (stop if relative improvement is not at least this
        much) (Default: 0.001)
        """
        return self._parms.get("stopping_tolerance")

    @stopping_tolerance.setter
    def stopping_tolerance(self, stopping_tolerance):
        assert_is_type(stopping_tolerance, None, numeric)
        self._parms["stopping_tolerance"] = stopping_tolerance


    @property
    def max_runtime_secs(self):
        """float: Maximum allowed runtime in seconds for model training. Use 0 to disable. (Default: 0.0)"""
        return self._parms.get("max_runtime_secs")

    @max_runtime_secs.setter
    def max_runtime_secs(self, max_runtime_secs):
        assert_is_type(max_runtime_secs, None, numeric)
        self._parms["max_runtime_secs"] = max_runtime_secs


    @property
    def seed(self):
        """int: Seed for pseudo random number generator (if applicable) (Default: -1)"""
        return self._parms.get("seed")

    @seed.setter
    def seed(self, seed):
        assert_is_type(seed, None, int)
        self._parms["seed"] = seed


    @property
    def build_tree_one_node(self):
        """
        bool: Run on one node only; no network overhead but fewer cpus used.  Suitable for small datasets. (Default:
        False)
        """
        return self._parms.get("build_tree_one_node")

    @build_tree_one_node.setter
    def build_tree_one_node(self, build_tree_one_node):
        assert_is_type(build_tree_one_node, None, bool)
        self._parms["build_tree_one_node"] = build_tree_one_node


    @property
    def learn_rate(self):
        """float: Learning rate (from 0.0 to 1.0) (Default: 0.1)"""
        return self._parms.get("learn_rate")

    @learn_rate.setter
    def learn_rate(self, learn_rate):
        assert_is_type(learn_rate, None, numeric)
        self._parms["learn_rate"] = learn_rate


    @property
    def learn_rate_annealing(self):
        """float: Scale the learning rate by this factor after each tree (e.g., 0.99 or 0.999)  (Default: 1.0)"""
        return self._parms.get("learn_rate_annealing")

    @learn_rate_annealing.setter
    def learn_rate_annealing(self, learn_rate_annealing):
        assert_is_type(learn_rate_annealing, None, numeric)
        self._parms["learn_rate_annealing"] = learn_rate_annealing


    @property
    def distribution(self):
        """
        Enum["auto", "bernoulli", "multinomial", "gaussian", "poisson", "gamma", "tweedie", "laplace", "quantile",
        "huber"]: Distribution function (Default: "auto")
        """
        return self._parms.get("distribution")

    @distribution.setter
    def distribution(self, distribution):
        assert_is_type(distribution, None, Enum("auto", "bernoulli", "multinomial", "gaussian", "poisson", "gamma", "tweedie", "laplace", "quantile", "huber"))
        self._parms["distribution"] = distribution


    @property
    def quantile_alpha(self):
        """float: Desired quantile for Quantile regression, must be between 0 and 1. (Default: 0.5)"""
        return self._parms.get("quantile_alpha")

    @quantile_alpha.setter
    def quantile_alpha(self, quantile_alpha):
        assert_is_type(quantile_alpha, None, numeric)
        self._parms["quantile_alpha"] = quantile_alpha


    @property
    def tweedie_power(self):
        """float: Tweedie power for Tweedie regression, must be between 1 and 2. (Default: 1.5)"""
        return self._parms.get("tweedie_power")

    @tweedie_power.setter
    def tweedie_power(self, tweedie_power):
        assert_is_type(tweedie_power, None, numeric)
        self._parms["tweedie_power"] = tweedie_power


    @property
    def huber_alpha(self):
        """
        float: Desired quantile for Huber/M-regression (threshold between quadratic and linear loss, must be between 0
        and 1). (Default: 0.9)
        """
        return self._parms.get("huber_alpha")

    @huber_alpha.setter
    def huber_alpha(self, huber_alpha):
        assert_is_type(huber_alpha, None, numeric)
        self._parms["huber_alpha"] = huber_alpha


    @property
    def checkpoint(self):
        """str: Model checkpoint to resume training with."""
        return self._parms.get("checkpoint")

    @checkpoint.setter
    def checkpoint(self, checkpoint):
        assert_is_type(checkpoint, None, str, H2OEstimator)
        self._parms["checkpoint"] = checkpoint


    @property
    def sample_rate(self):
        """float: Row sample rate per tree (from 0.0 to 1.0) (Default: 1.0)"""
        return self._parms.get("sample_rate")

    @sample_rate.setter
    def sample_rate(self, sample_rate):
        assert_is_type(sample_rate, None, numeric)
        self._parms["sample_rate"] = sample_rate


    @property
    def sample_rate_per_class(self):
        """List[float]: Row sample rate per tree per class (from 0.0 to 1.0)"""
        return self._parms.get("sample_rate_per_class")

    @sample_rate_per_class.setter
    def sample_rate_per_class(self, sample_rate_per_class):
        assert_is_type(sample_rate_per_class, None, [numeric])
        self._parms["sample_rate_per_class"] = sample_rate_per_class


    @property
    def col_sample_rate(self):
        """float: Column sample rate (from 0.0 to 1.0) (Default: 1.0)"""
        return self._parms.get("col_sample_rate")

    @col_sample_rate.setter
    def col_sample_rate(self, col_sample_rate):
        assert_is_type(col_sample_rate, None, numeric)
        self._parms["col_sample_rate"] = col_sample_rate


    @property
    def col_sample_rate_change_per_level(self):
        """float: Relative change of the column sampling rate for every level (from 0.0 to 2.0) (Default: 1.0)"""
        return self._parms.get("col_sample_rate_change_per_level")

    @col_sample_rate_change_per_level.setter
    def col_sample_rate_change_per_level(self, col_sample_rate_change_per_level):
        assert_is_type(col_sample_rate_change_per_level, None, numeric)
        self._parms["col_sample_rate_change_per_level"] = col_sample_rate_change_per_level


    @property
    def col_sample_rate_per_tree(self):
        """float: Column sample rate per tree (from 0.0 to 1.0) (Default: 1.0)"""
        return self._parms.get("col_sample_rate_per_tree")

    @col_sample_rate_per_tree.setter
    def col_sample_rate_per_tree(self, col_sample_rate_per_tree):
        assert_is_type(col_sample_rate_per_tree, None, numeric)
        self._parms["col_sample_rate_per_tree"] = col_sample_rate_per_tree


    @property
    def min_split_improvement(self):
        """
        float: Minimum relative improvement in squared error reduction for a split to happen (Default: 1e-05)
        """
        return self._parms.get("min_split_improvement")

    @min_split_improvement.setter
    def min_split_improvement(self, min_split_improvement):
        assert_is_type(min_split_improvement, None, numeric)
        self._parms["min_split_improvement"] = min_split_improvement


    @property
    def histogram_type(self):
        """
        Enum["auto", "uniform_adaptive", "random", "quantiles_global", "round_robin"]: What type of histogram to use for
        finding optimal split points (Default: "auto")
        """
        return self._parms.get("histogram_type")

    @histogram_type.setter
    def histogram_type(self, histogram_type):
        assert_is_type(histogram_type, None, Enum("auto", "uniform_adaptive", "random", "quantiles_global", "round_robin"))
        self._parms["histogram_type"] = histogram_type


    @property
    def max_abs_leafnode_pred(self):
        """float: Maximum absolute value of a leaf node prediction (Default: 1.79769313486e+308)"""
        return self._parms.get("max_abs_leafnode_pred")

    @max_abs_leafnode_pred.setter
    def max_abs_leafnode_pred(self, max_abs_leafnode_pred):
        assert_is_type(max_abs_leafnode_pred, None, numeric)
        self._parms["max_abs_leafnode_pred"] = max_abs_leafnode_pred


    @property
    def pred_noise_bandwidth(self):
        """
        float: Bandwidth (sigma) of Gaussian multiplicative noise ~N(1,sigma) for tree node predictions (Default: 0.0)
        """
        return self._parms.get("pred_noise_bandwidth")

    @pred_noise_bandwidth.setter
    def pred_noise_bandwidth(self, pred_noise_bandwidth):
        assert_is_type(pred_noise_bandwidth, None, numeric)
        self._parms["pred_noise_bandwidth"] = pred_noise_bandwidth


    @property
    def categorical_encoding(self):
        """
        Enum["auto", "enum", "one_hot_internal", "one_hot_explicit", "binary", "eigen"]: Encoding scheme for categorical
        features (Default: "auto")
        """
        return self._parms.get("categorical_encoding")

    @categorical_encoding.setter
    def categorical_encoding(self, categorical_encoding):
        assert_is_type(categorical_encoding, None, Enum("auto", "enum", "one_hot_internal", "one_hot_explicit", "binary", "eigen"))
        self._parms["categorical_encoding"] = categorical_encoding


