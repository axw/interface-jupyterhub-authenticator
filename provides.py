import json

from charmhelpers.core import hookenv
from charms.reactive import hook
from charms.reactive import RelationBase
from charms.reactive import scopes


class JupyterHubAuthenticatorProvides(RelationBase):
    scope = scopes.GLOBAL

    @hook('{provides:jupyterhub-authenticator}-relation-{joined,changed}')
    def changed(self):
        if self.get_remote('authenticator-class'):
            self.set_state('{relation_name}.available')

    @hook('{provides:jupyterhub-authenticator}-relation-{broken,departed}')
    def broken(self):
        self.remove_state('{relation_name}.available')

    def config(self):
        authenticator_class = self.get_remote('authenticator-class')
        authenticator_config = self.get_remote('authenticator-config')
        if authenticator_config:
            authenticator_config = json.loads(authenticator_config)
        else:
            authenticator_config = {}
        return authenticator_class, authenticator_config

