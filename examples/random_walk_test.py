# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
"""Unit tests for //compiler_gym/bin:random_walk."""
import gym
from absl.flags import FLAGS
from random_walk import run_random_walk


def test_run_random_walk_smoke_test():
    FLAGS.unparse_flags()
    FLAGS(["argv0"])
    with gym.make("llvm-autophase-ic-v0") as env:
        env.benchmark = "cbench-v1/crc32"
        run_random_walk(env=env, step_count=5)
