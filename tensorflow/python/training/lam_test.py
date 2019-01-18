from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow.python.platform import test
from tensorflow.python.training.server_lib import ClusterSpec
from tensorflow.python.training.server_lib import Server
class LamCustomTest(test.TestCase):

  def testFirstLam(self):
    print("Lam is testing here")

    ps_input = "localhost:2222".split(',')
    worker_input = "localhost:2223".split(',')

    local_job_name = "ps"
    local_task_index = 0

    cluster = ClusterSpec({"ps": ps_input, "worker": worker_input})
    server = Server(cluster, job_name=local_job_name, task_index=local_task_index)

if __name__ == "__main__":
    test.main()