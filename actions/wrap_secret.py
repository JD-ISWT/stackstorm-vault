from lib import action


class VaultWrapSecretAction(action.VaultBaseAction):
    def run(self, secret, ttl, profile_name=None):
        super().run(profile_name=profile_name)
        resp = self.vault.sys.wrap(payload=secret, ttl=ttl)
        return (True, resp)
