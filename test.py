import helloworld as hello
import unittests

class TestHello(unittest.TestCase):
  def test_hello_world(self):
    self.assertEqual("Hello, World!", hello.hello_world())
