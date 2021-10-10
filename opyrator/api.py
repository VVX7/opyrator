"""
    Author: Roger Johnston, Twitter: @VV_X_7
    License: Apache License 2.0

    References: PyMISP - MISP Project, https://github.com/MISP/PyMISP
"""
import json
import sys
import requests
from urllib.parse import urljoin
from . import __version__
from opyrator.objects import *
from typing import List, Optional, Union, IO, Dict, Any, Iterable, Mapping, Tuple


class API:

    def __init__(self, url: str, key: str, ssl: bool, cert: Tuple[str, tuple] = None,
                 timeout: Optional[Union[float, Tuple[float, float]]] = None):
        self.url: str = url
        self.key: str = key
        self.ssl: bool = ssl
        self.cert: Optional[Tuple[str, tuple]] = cert
        self.timeout: Optional[Union[float, Tuple[float, float]]] = timeout
        self.__session = requests.Session()

    def _request(self, method: str, url: str, data: Union[Iterable, Mapping, bytes] = {},
                 params: Mapping = {}, output_type: str = 'json',
                 content_type: str = 'json') -> requests.Response:
        """
        From PyMISP _prepare_request:
          https://github.com/MISP/PyMISP/blob/d44847b63a724a4b6f58e4e5074612068e32609d/pymisp/api.py#L3505
        """
        url = urljoin(self.url, url)

        if data == {} or isinstance(data, bytes):
            d = data
        elif data:
            if isinstance(data, dict):
                data = {k: v for k, v in data.items() if v is not None}
            d = data

        req = requests.Request(method, url, data=d, params=params)

        user_agent = f'Opyrator {__version__} - Python {".".join(str(x) for x in sys.version_info[:2])}'

        prepped = self.__session.prepare_request(req)
        prepped.headers.update(
            {'Authorization': self.key,
             'Accept': f'application/{output_type}',
             'content-type': f'application/{content_type}',
             'User-Agent': user_agent})
        settings = self.__session.merge_environment_settings(req.url, proxies={}, stream=None,
                                                             verify=self.ssl, cert=self.cert)
        return self.__session.send(prepped, timeout=self.timeout, **settings)

    # Adversary
    def get_adversaries(self) -> List[Adversary]:
        """
        Returns a list of Adversary objects.
        """
        response = self._request("GET", "/adversary")
        result = []
        for k, v in response.json().items():
            adv = Adversary()
            adv.from_dict(**v)
            result.append(adv)
        return result

    def get_adversary(self, adversary_id: str) -> Adversary:
        """
        Retrieves an Adversary by "id".
        :param adversary_id:
        :return:
        """
        response = self._request("GET", f"/adversary/{adversary_id}")
        result = Adversary()
        result.from_dict(**response.json())
        return result

    def create_adversary(self, adversary: Adversary) -> str:
        """
        Creates a new adversary given an Adversary object.
        :param adversary:
        :return:
        """
        response = self._request("POST", "/adversary", data=adversary.to_json())
        return response.json()

    def update_adversary(self, adversary_id: str, adversary: AdversaryUpdate) -> str:
        """
        Modifies the TTPs of an Adversary.
        :param adversary_id:
        :param adversary:
        :return:
        """
        response = self._request("PATCH", f"/adversary/{adversary_id}", data=adversary.to_json())
        return response.json()

    def delete_adversary(self, adversary_id: str) -> str:
        """
        Deletes the Adversary by id.
        :param adversary_id:
        :return:
        """
        response = self._request("DELETE", f"/adversary/{adversary_id}")
        return response.json()

    # Agent
    def get_agents(self, facts: bool = True, links: bool = True) -> List[Agent]:
        """
        Returns a sequence of Agents.
        :param facts:
        :param links:
        :return:
        """
        result = []
        response = self._request("GET", f"/agent?facts={int(facts)}&links={int(links)}")
        for k, v in response.json().items():
            agent = Agent()
            agent.from_dict(**v)
            result.append(agent)
        return result

    def get_agent(self, agent_id: str, facts: bool = True, links: bool = True) -> Agent:
        """
        Returns an Agent object by name.
        :param agent_id:
        :param facts:
        :param links:
        :return:
        """
        response = self._request("GET", f"/agent/{agent_id}?facts={int(facts)}&links={int(links)}")
        result = Agent()
        result.from_dict(**response.json())
        return result

    def task_agent(self,  agent_id: str, task: Instruction) -> str:
        """
        Tasks an Agent with an Instruction.
        TODO: FIX ME
        :param agent_id:
        :param task:
        :return:
        """
        d = {"instruction": task.to_json()}
        response = self._request("POST", f"/agent/{agent_id}", data=d)
        return response.json()

    # Attack
    def get_attacks(self) -> List[Attack]:
        """
        Returns a sequence of Attack objects.
        :return:
        """
        result = []
        response = self._request("GET", "/attack/")
        for k, v in response.json().items():
            attack = Attack()
            attack.from_dict(**v)
            result.append(attack)
        return result

    def get_attack(self, attack_id: str) -> Attack:
        """
        Retrieves an Attack by `attack_id`.
        :param attack_id:
        :return:
        """
        response = self._request("GET", f"/attack/{attack_id}")
        result = Attack()
        result.from_dict(**response.json())
        return result

    def create_attack(self, attack: Attack) -> str:
        """
        Creates a new Attack given an Attack object.
        :param attack:
        :return:
        """
        response = self._request("POST", "/attack", data=attack.to_json())
        result = response.json()
        return result

    def update_attack(self, attack_id: str, attack: Attack) -> str:
        """
        Updates an Attack by "id".
        :param attack_id:
        :param attack:
        :return:
        """
        response = self._request("PUT", f"/attack/{attack_id}", data=attack.to_json())
        result = response.json()
        return result

    def delete_attack(self,  attack_id: str) -> str:
        """
        Deletes an Attack by "id".
        :param attack_id:
        :return:
        """
        response = self._request("DELETE", f"/attack/{attack_id}")
        result = response.json()
        return result

    def import_attack_file(self, path: str) -> str:
        """
        Imports an Attack file.
        :param path:
        :return:
        """
        d = {"path": path}
        response = self._request("POST", "/attack/import/file", data=d)
        result = response.json()
        return result

    def import_attack_file_dir(self, path: str) -> str:
        """
        Imports a directory of Attack files.
        :param path:
        :return:
        """
        d = {"path": path}
        response = self._request("POST", "/attack/import/directory", data=d)
        result = response.json()
        return result

    def import_attack_repo(self, path: str) -> str:
        """
        Imports a git repo of Attack files.
        :param path:
        :return:
        """
        d = {"path": path}
        response = self._request("POST", "/attack/import/repo", data=d)
        result = response.json()
        return result

    # Internal
    def get_internal_settings(self) -> InternalSettings:
        """
        Returns internal configuration data.
        :return:
        """
        response = self._request("GET", "/internal/config/settings")
        result = InternalSettings()
        result.from_dict(**response.json())
        return result

    def update_internal_settings(self, settings: InternalSettings) -> str:
        """
        Updates the internal configuration data.
        :param settings:
        :return:
        """
        response = self._request("POST", "/internal/config/settings", data=settings.to_json())
        return response.json()

    def get_internal_global_redirectors(self) -> Redirector:
        """
        Returns internal global redirectors.
        :return:
        """
        response = self._request("GET", "/internal/global/redirectors")
        result = Redirector()
        result.from_dict(**response.json())
        return result

    def get_internal_global_facts(self) -> List[List[Fact]]:
        """
        Returns internal global facts.
        :return:
        """
        result = []
        response = self._request("GET", "/internal/global/facts")
        for i in response.json():
            l = []
            for n in i:
                fact = Fact()
                l.append(fact)
            result.append(l)
        return result

    # Operation
    def get_operation(self) -> Operation:
        """
        Returns a sequence of Operation objects.
        :return:
        """
        response = self._request("GET", "/operation")
        result = Operation()
        result.from_dict(**response.json())
        return result

    def get_operation_links(self) -> Dict[str, Operation]:
        """
        Returns a map of Operation IDs by Link ID.
        :return:
        """
        response = self._request("GET", "/operation/links")
        result = {}
        for k, v in response.json().items():
            operation = Operation()
            operation.from_dict(**v)
            result[k] = operation
        return result

    # Plugin
    def get_plugin(self, name: str) -> Plugin:
        """
        Returns the plugin configuration data specified by name.
        :param name:
        :return:
        """
        response = self._request("GET", f"/plugin/{name}")
        result = Plugin()
        result.from_dict(**response.json())
        return result

    def update_plugin(self, name: str, plugin: Plugin) -> str:
        """
        Updates the plugin configuration data specified by name.
        :param plugin:
        :return:
        """
        response = self._request("POST", f"/plugin/{name}", data=plugin.to_json())
        result = response.json()
        return result

    # Program
    def get_programs(self) -> Dict[str, Program]:
        """
        Returns training programs.
        :return:
        """
        response = self._request("GET", "/program")
        result = {}
        for k, v in response.json().items():
            operation = Program()
            operation.from_dict(**v)
            result[k] = operation
        return result

    # Schedules
    def get_schedules(self) -> List[Schedule]:
        """
        Returns a sequence of Schedule objects.
        :return:
        """
        response = self._request("GET", "/schedule")
        result = []
        for i in response.json():
            schedule = Schedule()
            schedule.from_dict(**i)
            result.append(schedule)
        return result

    def create_schedules(self, schedule: Schedule) -> str:
        """
        Creates a new schedule given an adversary ID and range.
        :param schedule:
        :return:
        """
        response = self._request("POST", "/schedule", data=schedule.to_json())
        return response.json()

    def delete_schedule(self, adversary_id: str) -> str:
        """

        :param adversary_id:
        :return:
        """
        response = self._request("DELETE", f"/schedule/{adversary_id}")
        return response.json()

    # Tactics
    def get_tactics(self) -> List[Tactic]:
        """
        Returns the internal state machine describing the order of the planner.
        :return:
        """
        response = self._request("GET", "/tactics")
        result = []
        for i in response.json():
            tactic = Tactic()
            tactic.from_dict(**i)
            result.append(tactic)
        return result

    def update_tactics(self, state: List[str]) -> str:
        """
        Updates the internal state machine.
        :param state:
        :return:
        """
        response = self._request("POST", "/schedule", data=state)
        return response.json()

    #


















