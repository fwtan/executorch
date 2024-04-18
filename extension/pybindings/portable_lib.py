# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

# pyre-strict

# When installed as a pip wheel, we must import `torch` before trying to import
# the pybindings shared library extension. This will load libtorch.so and
# related libs, ensuring that the pybindings lib can resolve those runtime
# dependencies.
import torch as _torch

# Import the actual C++ extension that this file wraps.
from executorch.extension.pybindings import _portable_lib

# Let users import everything from _portable_lib as if this python file defined
# them. Normally we'd exclude names starting with `_`, but _portable_lib
# contains names like `_load_for_executorch` that we need to expose.
__all__ = [name for name in dir(_portable_lib) if not name.startswith("__")]

# The underscores also complicate things because it means we can't use `import
# *` to bring them into our namespace.
for _name in __all__:
    exec(f"from executorch.extension.pybindings._portable_lib import {_name}")

# Clean up so that `dir(portable_lib)` is the same as `dir(_portable_lib)`
# (modulo some __dunder__ names).
del _name
del _portable_lib
del _torch
