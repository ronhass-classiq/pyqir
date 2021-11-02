# Copyright(c) Microsoft Corporation.
# Licensed under the MIT License.

from typing import Any
from .pyqir_jit import *

class QirJit(object):
    """
    The QirJit object loads bitcode/QIR for evaluation and processing

    """

    def __init__(self):
        self.pyqirjit = PyQirJit()

    def eval(self, file_path: str, pyobj: Any):
        """
        JIT compiles the circuit delegating quantum operations to the supplied object

        :param file_path: file path of existing QIR in a ll or bc file
        :type file_path: str

        :param pyobj: python GateSet object defining the quantum operations
        :type pyobj: str
        """
        self.pyqirjit.eval(file_path, pyobj)
