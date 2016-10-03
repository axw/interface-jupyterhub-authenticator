import json

from charms.reactive import hook
from charms.reactive import RelationBase
from charms.reactive import scopes


class JupyterHubAuthenticatorRequires(RelationBase):
    scope = scopes.GLOBAL

    @hook('{requires:jupyterhub-authenticator}-relation-{joined,changed}')
    def changed(self):
        self.set_state('{relation_name}.available')

    @hook('{requires:jupyterhub-authenticator}-relation-{departed,broken}')
    def broken(self):
        self.remove_state('{relation_name}.available')

    def set_authenticator(self, authenticator_class, config=None):
        self.set_remote('authenticator-class', authenticator_class)
        if config:
            self.set_remote('authenticator-config', json.dumps(config))
