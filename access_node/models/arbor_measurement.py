# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from access_node.models.base_model_ import Model
from access_node import util


class ArborMeasurement(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, simulation_times: List[float]=None, gids: List[int]=None, values: List[float]=None):  # noqa: E501
        """ArborMeasurement - a model defined in Swagger

        :param simulation_times: The simulation_times of this ArborMeasurement.  # noqa: E501
        :type simulation_times: List[float]
        :param gids: The gids of this ArborMeasurement.  # noqa: E501
        :type gids: List[int]
        :param values: The values of this ArborMeasurement.  # noqa: E501
        :type values: List[float]
        """
        self.swagger_types = {
            'simulation_times': List[float],
            'gids': List[int],
            'values': List[float]
        }

        self.attribute_map = {
            'simulation_times': 'simulation_times',
            'gids': 'gids',
            'values': 'values'
        }

        self._simulation_times = simulation_times
        self._gids = gids
        self._values = values

    @classmethod
    def from_dict(cls, dikt) -> 'ArborMeasurement':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ArborMeasurement of this ArborMeasurement.  # noqa: E501
        :rtype: ArborMeasurement
        """
        return util.deserialize_model(dikt, cls)

    @property
    def simulation_times(self) -> List[float]:
        """Gets the simulation_times of this ArborMeasurement.

        This array is always sorted.  # noqa: E501

        :return: The simulation_times of this ArborMeasurement.
        :rtype: List[float]
        """
        return self._simulation_times

    @simulation_times.setter
    def simulation_times(self, simulation_times: List[float]):
        """Sets the simulation_times of this ArborMeasurement.

        This array is always sorted.  # noqa: E501

        :param simulation_times: The simulation_times of this ArborMeasurement.
        :type simulation_times: List[float]
        """

        self._simulation_times = simulation_times

    @property
    def gids(self) -> List[int]:
        """Gets the gids of this ArborMeasurement.


        :return: The gids of this ArborMeasurement.
        :rtype: List[int]
        """
        return self._gids

    @gids.setter
    def gids(self, gids: List[int]):
        """Sets the gids of this ArborMeasurement.


        :param gids: The gids of this ArborMeasurement.
        :type gids: List[int]
        """

        self._gids = gids

    @property
    def values(self) -> List[float]:
        """Gets the values of this ArborMeasurement.

        This array contains the measured values for each gid and time to get the value for gid n at time t you have to use the index n * length(simulation_times) + t  # noqa: E501

        :return: The values of this ArborMeasurement.
        :rtype: List[float]
        """
        return self._values

    @values.setter
    def values(self, values: List[float]):
        """Sets the values of this ArborMeasurement.

        This array contains the measured values for each gid and time to get the value for gid n at time t you have to use the index n * length(simulation_times) + t  # noqa: E501

        :param values: The values of this ArborMeasurement.
        :type values: List[float]
        """

        self._values = values
