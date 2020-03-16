from ftw.upgrade import UpgradeStep


class Installiframefix(UpgradeStep):
    """Install ftw.iframefix.
    """

    def __call__(self):
        self.setup_install_profile('profile-ftw.iframefix:default')
        self.install_upgrade_profile()
