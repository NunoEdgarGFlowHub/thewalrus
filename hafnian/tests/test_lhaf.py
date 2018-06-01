# Copyright 2018 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

import numpy as np
from scipy.special import factorial as fac
from hafnian.lhaf import hafnian


class TestLhaf(unittest.TestCase):

    def setUp(self):
        self.n = 6

    def test_2x2(self):
        A = np.complex128(np.random.random([2, 2])) + 1j*np.random.random([2, 2])
        A = A + A.T
        haf = hafnian(A)
        self.assertEqual(haf, A[0, 1])

    def test_4x4(self):
        A = np.complex128(np.random.random([4, 4]))
        A += 1j*np.random.random([4, 4])
        A += A.T
        haf = hafnian(A)
        expected = A[0, 1]*A[2, 3] + \
            A[0, 2]*A[1, 3] + A[0, 3]*A[1, 2]
        self.assertEqual(haf, expected)

    def test_identity(self):
        A = np.identity(self.n)
        haf = hafnian(A)
        self.assertEqual(haf, 0)

    def test_ones(self):
        A = np.complex128(np.ones([2*self.n, 2*self.n]))
        haf = hafnian(A)
        expected = fac(2*self.n)/(fac(self.n)*(2**self.n))
        self.assertTrue(np.allclose(haf, expected))

    def test_block_ones(self):
        O = np.zeros([self.n, self.n])
        B = np.ones([self.n, self.n])
        A = np.vstack([np.hstack([O, B]),
                       np.hstack([B, O])])
        A = np.complex128(A)
        haf = hafnian(A)
        expected = float(fac(self.n))
        self.assertTrue(haf, expected)


if __name__ == '__main__':
    unittest.main()
