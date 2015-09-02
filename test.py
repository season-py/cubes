import mock
import unittest
import workspace

class TestCase(unittest.TestCase):

    def setUp(self):
        pass

    @mock.patch.object(workspace.Workspace, 'browser')
    def test_workspace(self, mock_browser):
        mock_browser.return_value = None
        wp = workspace.Workspace()
        print(wp._config)


if __name__ == '__main__':
    unittest.main()
