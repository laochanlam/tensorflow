from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow.python.platform import test

class LamCustomTest(test.TestCase):

  def testFirstLam(self):
    print("Lam is testing here")

if __name__ == "__main__":
    test.main()