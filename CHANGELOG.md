# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [ 0.0.9 ] 2018-01-08

### Removed
* auto removing reference keys from sorts, overly protective and not necessary

## [ 0.0.8 ] 2017-12-05

## Added
* `collection.get_total_count` method

## [ 0.0.7 ] 2017-10-25

## Changed
* `target.get()` calls on `Model` and `Collection` changed to
  `target.collapse()`
* `Collection.set_target` wraps targets set with `$in` operator in `NestedDict`
  to block collapsing when `target.collapse()` is called

## [ 0.0.6 ] 2017-10-24

### Added
* case to record `$push` operation to handle nested dicts and wrap them
  correctly so they are not flattened to delimited notation in
  `flatten_updates` call
* test for `$push` case added

## [ 0.0.5 ] 2017-10-12

### Added
* `Collection.total_count` attribute. This gets populated after `find` method
  is called
* test case for `Collection.total_count` changes
* test case for `DelimitedDict._collapse_delimited_notation` changes

## [ 0.0.4 ] 2017-10-05

### Changed

* fixed issue with `DelimitedDict._collapse_delimited_notation` that was
  causing empty dicts as values to be dropped during conversion

## [ 0.0.2 ] 2017-10-04

### Changed
* fixed issue with collection.set_target overwriting collection.default_target

## [ 0.0.1 ] 2017-10-01

### Added
* initial release
