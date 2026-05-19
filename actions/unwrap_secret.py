from lib import action
import hvac


class VaultUnwrapSecretAction(action.VaultBaseAction):
    def run(self, token, profile_name=None):
        super().run(profile_name=profile_name)
        try:
            resp = self.vault.sys.unwrap(token)
        except hvac.exceptions.InvalidRequest as e:
            return (False, f"{e}")

        return (True, resp)
