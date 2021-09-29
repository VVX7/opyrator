"""
    Author: Roger Johnston, Twitter: @VV_X_7
    License: Apache License 2.0
"""

from typing import List, Optional, Union, IO, Dict, Any
from opyrator.abstract import AbstractOperator


class Account(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.email: str = ""
        self.tag: str = ""
        self.license: str = ""
        self.badges: List[str] = []
        self.token: str = ""


class Adversary(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.id: str = ""
        self.name: str = ""
        self.goals: List[Goal] = []
        self.ttps: List[str] = []


class AdversaryUpdate(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add: List[str] = []
        self.remove: List[str] = []


class Agent(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name: str = ""
        self.label: str = ""
        self.history: List[str] = []
        self.queue: List[str] = []
        self.links: List[Link] = []
        self.facts: Dict[str, List[Fact]] = {}
        self.locked: bool
        self.location: str = ""
        self.target: str = ""
        self.hostname: str = ""
        self.state: int
        self.key: str = ""
        self.busy: bool
        self.handler: AgentHandler
        self.interval: int
        self.platform: str = ""
        self.executors: List[str] = []
        self.agentRange: str = ""
        self.sleep: int
        self.automaticFacts: List[Fact] = []


class AgentHandler(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name: str = ""
        self.labActive: bool


class Attack(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.id: str = ""
        self.name: str = ""
        self.description: str = ""
        self.tactic: str = ""
        self.technique: Technique
        self.platforms: Platform
        self.metadata: AttackMetadata
        self.modified: bool


class AttackVersion(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.version: int
        self.checksum: str = ""
        self.license: str = ""
        self.releaseDate: str = ""


class AttackMetadata(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.version: int
        self.license: str = ""
        self.tags: List[str] = []
        self.authors: List[str] = []
        self.enabled: bool
        self.checksum: str = ""
        self.releaseDate: str = ""
        self.latest: AttackVersion


class Challenge(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.id: str = ""
        self.key: str = ""
        self.attempts: int
        self.completed: int
        self.difficulty: int
        self.flag: Flag


class CommandVariant(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.command: str = ""
        self.payload: str = ""


class Command(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.command: str = ""
        self.payload: str = ""
        self.variants: List[CommandVariant] = []


class Course(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.id: str = ""
        self.name: str = ""
        self.description: str = ""
        self.variants: List[Challenge] = []


class Executor(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.psh: Command
        self.exec: Command
        self.cmd: Command
        self.sh: Command
        self.keyword: Command


class Fact(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.host: str = ""
        self.key: str = ""
        self.value: str = ""
        self.linkID: str = ""
        self.ttp: str = ""


class FlagTemplate(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name: str = ""
        self.data: List[str] = []


class Flag(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.id: str = ""
        self.flagTemplate: FlagTemplate
        self.name: str = ""
        self.challenge: str = ""
        self.context: str = ""
        self.resources: FlagResources
        self.answer: str = ""
        self.hints: List[str] = []
        self.blocks: Dict[str, str] = {}


class FlagResources(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.links: List[str] = []


class Goal(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.key: str = ""
        self.value: str = ""
        self.criteria: str = ""


class InternalSettings(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.local: Workspace
        self.identity: str = ""
        self.account: Account
        self.version: str = ""


class Instruction(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.id: str = ""
        self.operation: str = ""
        self.ttp: str = ""
        self.facts: Dict[str, str] = {}
        self.executor: str = ""


class Link(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.unique: str = ""
        self.tag: str = ""
        self.host: str = ""
        self.platform: str = ""
        self.timestamp: int
        self.ttp: str = ""
        self.executor: str = ""
        self.request: str = ""
        self.response: str = ""
        self.status: int
        self.pid: int
        self.tactic: str = ""
        self.technique: str = ""
        self.operation: str = ""


class OperatorClient(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.API: RestAPI


class OperationAudit(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.status: int
        self.links: List[str] = []


class Operation(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.id: str = ""
        self.adversary: Adversary
        self.agentRange: str = ""
        self.audit: Dict[str, OperationAudit]
        self.opStart: str = ""
        self.opEnd: str = ""


class Preferences(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.notices: List[str] = []


class Program(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.id: str = ""
        self.name: str = ""
        self.description: str = ""
        self.license: str = ""
        self.id: List[Course] = []


class Plugin(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name: str = ""
        self.description: str = ""
        self.custom: Dict[str, str] = {}


class Platform(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.windows: Executor
        self.linux: Executor
        self.darwin: Executor
        # TODO: fix global shadow
        # self.global: Executor


class Redirector(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name: str = ""


class RestAPI(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.token: str = ""
        self.port: str = ""
        self.url: str = ""
        self.endpoints: Dict[str, RequestStatus]


class RequestStatus(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.processing: bool


class Schedule(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.agentRange: str = ""
        self.adversary: str = ""
        self.dayOfWeek: str = ""
        self.hour: str = ""
        self.minute: str = ""
        self.timeout: int


class Technique(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.id: str = ""
        self.name: str = ""


class Tactic(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.tactic: str = ""
        self.techniques: Dict[str, Technique]


class WorkspaceKeys(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.agent: List[str] = []
        self.data: List[str] = []


class WorkspacePublisher(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.local: bool
        self.prelude: bool


class Workspace(AbstractOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.workspace: str = ""
        self.data: WorkspaceKeys
        self.server: str = ""
        self.tcpPort: int
        self.udpPort: int
        self.httpPort: int
        self.grpcPort: int
        self.shellPort: int
        self.publishers: WorkspacePublisher
        self.redirectors: Redirector
        self.sources: List[str] = []
        self.protect: int
        self.preferences: Preferences
        self.gatekeepers: List[str] = []
