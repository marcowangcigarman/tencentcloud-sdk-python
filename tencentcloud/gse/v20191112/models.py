# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tencentcloud.common.abstract_model import AbstractModel


class CreateGameServerSessionRequest(AbstractModel):
    """CreateGameServerSession请求参数结构体

    """

    def __init__(self):
        """
        :param MaximumPlayerSessionCount: 最大玩家数量
        :type MaximumPlayerSessionCount: int
        :param AliasId: 别名ID
        :type AliasId: str
        :param CreatorId: 创建者ID
        :type CreatorId: str
        :param FleetId: 舰队ID
        :type FleetId: str
        :param GameProperties: 游戏属性
        :type GameProperties: list of GameProperty
        :param GameServerSessionData: 游戏服务器会话属性详情
        :type GameServerSessionData: str
        :param GameServerSessionId: 游戏服务器会话自定义ID
        :type GameServerSessionId: str
        :param IdempotencyToken: 幂等token
        :type IdempotencyToken: str
        :param Name: 游戏服务器会话名称
        :type Name: str
        """
        self.MaximumPlayerSessionCount = None
        self.AliasId = None
        self.CreatorId = None
        self.FleetId = None
        self.GameProperties = None
        self.GameServerSessionData = None
        self.GameServerSessionId = None
        self.IdempotencyToken = None
        self.Name = None


    def _deserialize(self, params):
        self.MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        self.AliasId = params.get("AliasId")
        self.CreatorId = params.get("CreatorId")
        self.FleetId = params.get("FleetId")
        if params.get("GameProperties") is not None:
            self.GameProperties = []
            for item in params.get("GameProperties"):
                obj = GameProperty()
                obj._deserialize(item)
                self.GameProperties.append(obj)
        self.GameServerSessionData = params.get("GameServerSessionData")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.IdempotencyToken = params.get("IdempotencyToken")
        self.Name = params.get("Name")


class CreateGameServerSessionResponse(AbstractModel):
    """CreateGameServerSession返回参数结构体

    """

    def __init__(self):
        """
        :param GameServerSession: 游戏服务器会话
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSession: :class:`tencentcloud.gse.v20191112.models.GameServerSession`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GameServerSession = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSession") is not None:
            self.GameServerSession = GameServerSession()
            self.GameServerSession._deserialize(params.get("GameServerSession"))
        self.RequestId = params.get("RequestId")


class DeleteScalingPolicyRequest(AbstractModel):
    """DeleteScalingPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务部署ID
        :type FleetId: str
        :param Name: 名称
        :type Name: str
        """
        self.FleetId = None
        self.Name = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.Name = params.get("Name")


class DeleteScalingPolicyResponse(AbstractModel):
    """DeleteScalingPolicy返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeFleetCapacityRequest(AbstractModel):
    """DescribeFleetCapacity请求参数结构体

    """

    def __init__(self):
        """
        :param FleetIds: 服务部署 Id列表
        :type FleetIds: list of str
        :param Limit: 结果返回最大数量
        :type Limit: int
        :param Offset: 返回结果偏移
        :type Offset: int
        """
        self.FleetIds = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.FleetIds = params.get("FleetIds")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeFleetCapacityResponse(AbstractModel):
    """DescribeFleetCapacity返回参数结构体

    """

    def __init__(self):
        """
        :param FleetCapacity: 服务部署容量配置
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetCapacity: list of FleetCapacity
        :param TotalCount: 结果返回最大数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FleetCapacity = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FleetCapacity") is not None:
            self.FleetCapacity = []
            for item in params.get("FleetCapacity"):
                obj = FleetCapacity()
                obj._deserialize(item)
                self.FleetCapacity.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeGameServerSessionDetailsRequest(AbstractModel):
    """DescribeGameServerSessionDetails请求参数结构体

    """

    def __init__(self):
        """
        :param AliasId: 别名ID
        :type AliasId: str
        :param FleetId: 舰队ID
        :type FleetId: str
        :param GameServerSessionId: 游戏服务器会话ID
        :type GameServerSessionId: str
        :param Limit: 单次查询记录数上限
        :type Limit: int
        :param NextToken: 页偏移，用于查询下一页
        :type NextToken: str
        :param StatusFilter: 游戏服务器会话状态(ACTIVE,ACTIVATING,TERMINATED,TERMINATING,ERROR)
        :type StatusFilter: str
        """
        self.AliasId = None
        self.FleetId = None
        self.GameServerSessionId = None
        self.Limit = None
        self.NextToken = None
        self.StatusFilter = None


    def _deserialize(self, params):
        self.AliasId = params.get("AliasId")
        self.FleetId = params.get("FleetId")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.Limit = params.get("Limit")
        self.NextToken = params.get("NextToken")
        self.StatusFilter = params.get("StatusFilter")


class DescribeGameServerSessionDetailsResponse(AbstractModel):
    """DescribeGameServerSessionDetails返回参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionDetails: 游戏服务器会话详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSessionDetails: list of GameServerSessionDetail
        :param NextToken: 页偏移，用于查询下一页
注意：此字段可能返回 null，表示取不到有效值。
        :type NextToken: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GameServerSessionDetails = None
        self.NextToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessionDetails") is not None:
            self.GameServerSessionDetails = []
            for item in params.get("GameServerSessionDetails"):
                obj = GameServerSessionDetail()
                obj._deserialize(item)
                self.GameServerSessionDetails.append(obj)
        self.NextToken = params.get("NextToken")
        self.RequestId = params.get("RequestId")


class DescribeGameServerSessionPlacementRequest(AbstractModel):
    """DescribeGameServerSessionPlacement请求参数结构体

    """

    def __init__(self):
        """
        :param PlacementId: 游戏服务器会话放置的唯一标识符
        :type PlacementId: str
        """
        self.PlacementId = None


    def _deserialize(self, params):
        self.PlacementId = params.get("PlacementId")


class DescribeGameServerSessionPlacementResponse(AbstractModel):
    """DescribeGameServerSessionPlacement返回参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionPlacement: 游戏服务器会话放置
        :type GameServerSessionPlacement: :class:`tencentcloud.gse.v20191112.models.GameServerSessionPlacement`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GameServerSessionPlacement = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessionPlacement") is not None:
            self.GameServerSessionPlacement = GameServerSessionPlacement()
            self.GameServerSessionPlacement._deserialize(params.get("GameServerSessionPlacement"))
        self.RequestId = params.get("RequestId")


class DescribeGameServerSessionsRequest(AbstractModel):
    """DescribeGameServerSessions请求参数结构体

    """

    def __init__(self):
        """
        :param AliasId: 别名ID
        :type AliasId: str
        :param FleetId: 舰队ID
        :type FleetId: str
        :param GameServerSessionId: 游戏服务器会话ID
        :type GameServerSessionId: str
        :param Limit: 单次查询记录数上限
        :type Limit: int
        :param NextToken: 页偏移，用于查询下一页
        :type NextToken: str
        :param StatusFilter: 游戏服务器会话状态
        :type StatusFilter: str
        """
        self.AliasId = None
        self.FleetId = None
        self.GameServerSessionId = None
        self.Limit = None
        self.NextToken = None
        self.StatusFilter = None


    def _deserialize(self, params):
        self.AliasId = params.get("AliasId")
        self.FleetId = params.get("FleetId")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.Limit = params.get("Limit")
        self.NextToken = params.get("NextToken")
        self.StatusFilter = params.get("StatusFilter")


class DescribeGameServerSessionsResponse(AbstractModel):
    """DescribeGameServerSessions返回参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessions: 游戏服务器会话列表
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSessions: list of GameServerSession
        :param NextToken: 页便宜，用于查询下一页
注意：此字段可能返回 null，表示取不到有效值。
        :type NextToken: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GameServerSessions = None
        self.NextToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessions") is not None:
            self.GameServerSessions = []
            for item in params.get("GameServerSessions"):
                obj = GameServerSession()
                obj._deserialize(item)
                self.GameServerSessions.append(obj)
        self.NextToken = params.get("NextToken")
        self.RequestId = params.get("RequestId")


class DescribePlayerSessionsRequest(AbstractModel):
    """DescribePlayerSessions请求参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionId: 游戏服务器会话ID
        :type GameServerSessionId: str
        :param Limit: 单次查询记录数上限
        :type Limit: int
        :param NextToken: 页偏移，用于查询下一页
        :type NextToken: str
        :param PlayerId: 玩家ID
        :type PlayerId: str
        :param PlayerSessionId: 玩家会话ID
        :type PlayerSessionId: str
        :param PlayerSessionStatusFilter: 玩家会话状态（RESERVED,ACTIVE,COMPLETED,TIMEDOUT）
        :type PlayerSessionStatusFilter: str
        """
        self.GameServerSessionId = None
        self.Limit = None
        self.NextToken = None
        self.PlayerId = None
        self.PlayerSessionId = None
        self.PlayerSessionStatusFilter = None


    def _deserialize(self, params):
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.Limit = params.get("Limit")
        self.NextToken = params.get("NextToken")
        self.PlayerId = params.get("PlayerId")
        self.PlayerSessionId = params.get("PlayerSessionId")
        self.PlayerSessionStatusFilter = params.get("PlayerSessionStatusFilter")


class DescribePlayerSessionsResponse(AbstractModel):
    """DescribePlayerSessions返回参数结构体

    """

    def __init__(self):
        """
        :param PlayerSessions: 玩家会话列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayerSessions: list of PlayerSession
        :param NextToken: 页偏移
注意：此字段可能返回 null，表示取不到有效值。
        :type NextToken: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PlayerSessions = None
        self.NextToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PlayerSessions") is not None:
            self.PlayerSessions = []
            for item in params.get("PlayerSessions"):
                obj = PlayerSession()
                obj._deserialize(item)
                self.PlayerSessions.append(obj)
        self.NextToken = params.get("NextToken")
        self.RequestId = params.get("RequestId")


class DescribeScalingPoliciesRequest(AbstractModel):
    """DescribeScalingPolicies请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务部署ID
        :type FleetId: str
        :param StatusFilter: 状态过滤条件
        :type StatusFilter: str
        :param Offset: 结果返回最大数量
        :type Offset: int
        :param Limit: 返回结果偏移
        :type Limit: int
        """
        self.FleetId = None
        self.StatusFilter = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.StatusFilter = params.get("StatusFilter")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeScalingPoliciesResponse(AbstractModel):
    """DescribeScalingPolicies返回参数结构体

    """

    def __init__(self):
        """
        :param ScalingPolicies: 动态扩缩容配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ScalingPolicies: list of ScalingPolicy
        :param TotalCount: 返回总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ScalingPolicies = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ScalingPolicies") is not None:
            self.ScalingPolicies = []
            for item in params.get("ScalingPolicies"):
                obj = ScalingPolicy()
                obj._deserialize(item)
                self.ScalingPolicies.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DesiredPlayerSession(AbstractModel):
    """玩家游戏会话信息

    """

    def __init__(self):
        """
        :param PlayerId: 与玩家会话关联的唯一玩家标识
        :type PlayerId: str
        :param PlayerData: 开发人员定义的玩家数据
        :type PlayerData: str
        """
        self.PlayerId = None
        self.PlayerData = None


    def _deserialize(self, params):
        self.PlayerId = params.get("PlayerId")
        self.PlayerData = params.get("PlayerData")


class FleetCapacity(AbstractModel):
    """服务部署组容量配置

    """

    def __init__(self):
        """
        :param FleetId: 服务部署 Id
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetId: str
        :param InstanceType: 服务器类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param InstanceCounts: 服务器实例统计数据
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceCounts: :class:`tencentcloud.gse.v20191112.models.InstanceCounts`
        """
        self.FleetId = None
        self.InstanceType = None
        self.InstanceCounts = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.InstanceType = params.get("InstanceType")
        if params.get("InstanceCounts") is not None:
            self.InstanceCounts = InstanceCounts()
            self.InstanceCounts._deserialize(params.get("InstanceCounts"))


class GameProperty(AbstractModel):
    """游戏属性详情

    """

    def __init__(self):
        """
        :param Key: 属性名称
        :type Key: str
        :param Value: 属性值
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class GameServerSession(AbstractModel):
    """游戏会话详情

    """

    def __init__(self):
        """
        :param CreationTime: 游戏服务器会话创建时间
        :type CreationTime: str
        :param CreatorId: 创建者ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorId: str
        :param CurrentPlayerSessionCount: 当前玩家数量
        :type CurrentPlayerSessionCount: int
        :param DnsName: CVM的DNS标识符
注意：此字段可能返回 null，表示取不到有效值。
        :type DnsName: str
        :param FleetId: 舰队ID
        :type FleetId: str
        :param GameProperties: 游戏属性
注意：此字段可能返回 null，表示取不到有效值。
        :type GameProperties: list of GameProperty
        :param GameServerSessionData: 游戏服务器会话属性详情
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSessionData: str
        :param GameServerSessionId: 游戏服务器会话ID
        :type GameServerSessionId: str
        :param IpAddress: CVM IP地址
        :type IpAddress: str
        :param MatchmakerData: 对战进程详情
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchmakerData: str
        :param MaximumPlayerSessionCount: 最大玩家数量
        :type MaximumPlayerSessionCount: int
        :param Name: 游戏服务器会话名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param PlayerSessionCreationPolicy: 玩家会话创建策略
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayerSessionCreationPolicy: str
        :param Port: 端口号
        :type Port: int
        :param Status: 游戏服务器会话状态
        :type Status: str
        :param StatusReason: 游戏服务器会话状态附加信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusReason: str
        :param TerminationTime: 终止的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TerminationTime: str
        :param InstanceType: 实例类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        """
        self.CreationTime = None
        self.CreatorId = None
        self.CurrentPlayerSessionCount = None
        self.DnsName = None
        self.FleetId = None
        self.GameProperties = None
        self.GameServerSessionData = None
        self.GameServerSessionId = None
        self.IpAddress = None
        self.MatchmakerData = None
        self.MaximumPlayerSessionCount = None
        self.Name = None
        self.PlayerSessionCreationPolicy = None
        self.Port = None
        self.Status = None
        self.StatusReason = None
        self.TerminationTime = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.CreationTime = params.get("CreationTime")
        self.CreatorId = params.get("CreatorId")
        self.CurrentPlayerSessionCount = params.get("CurrentPlayerSessionCount")
        self.DnsName = params.get("DnsName")
        self.FleetId = params.get("FleetId")
        if params.get("GameProperties") is not None:
            self.GameProperties = []
            for item in params.get("GameProperties"):
                obj = GameProperty()
                obj._deserialize(item)
                self.GameProperties.append(obj)
        self.GameServerSessionData = params.get("GameServerSessionData")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.IpAddress = params.get("IpAddress")
        self.MatchmakerData = params.get("MatchmakerData")
        self.MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        self.Name = params.get("Name")
        self.PlayerSessionCreationPolicy = params.get("PlayerSessionCreationPolicy")
        self.Port = params.get("Port")
        self.Status = params.get("Status")
        self.StatusReason = params.get("StatusReason")
        self.TerminationTime = params.get("TerminationTime")
        self.InstanceType = params.get("InstanceType")


class GameServerSessionDetail(AbstractModel):
    """游戏服务器会话详情（GameServerSessionDetail）

    """

    def __init__(self):
        """
        :param GameServerSession: 游戏服务器会话
        :type GameServerSession: :class:`tencentcloud.gse.v20191112.models.GameServerSession`
        :param ProtectionPolicy: 保护策略，可选（NoProtection,FullProtection）
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtectionPolicy: str
        """
        self.GameServerSession = None
        self.ProtectionPolicy = None


    def _deserialize(self, params):
        if params.get("GameServerSession") is not None:
            self.GameServerSession = GameServerSession()
            self.GameServerSession._deserialize(params.get("GameServerSession"))
        self.ProtectionPolicy = params.get("ProtectionPolicy")


class GameServerSessionPlacement(AbstractModel):
    """游戏会话部署对象

    """

    def __init__(self):
        """
        :param PlacementId: 部署Id
        :type PlacementId: str
        :param GameServerSessionQueueName: 服务部署组名称
        :type GameServerSessionQueueName: str
        :param PlayerLatencies: 玩家延迟
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayerLatencies: list of PlayerLatency
        :param Status: 服务部署状态
        :type Status: str
        :param DnsName: 分配给正在运行游戏会话的实例的DNS标识符
注意：此字段可能返回 null，表示取不到有效值。
        :type DnsName: str
        :param GameServerSessionId: 游戏会话Id
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSessionId: str
        :param GameServerSessionName: 游戏会话名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSessionName: str
        :param GameServerSessionRegion: 服务部署区域
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSessionRegion: str
        :param GameProperties: 游戏属性
注意：此字段可能返回 null，表示取不到有效值。
        :type GameProperties: list of GameProperty
        :param MaximumPlayerSessionCount: 最大玩家数量
        :type MaximumPlayerSessionCount: int
        :param GameServerSessionData: 游戏会话数据
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSessionData: str
        :param IpAddress: 运行游戏会话的实例的IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :type IpAddress: str
        :param Port: 运行游戏会话的实例的端口号
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param MatchmakerData: 游戏匹配数据
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchmakerData: str
        :param PlacedPlayerSessions: 部署的玩家游戏数据
注意：此字段可能返回 null，表示取不到有效值。
        :type PlacedPlayerSessions: list of PlacedPlayerSession
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        """
        self.PlacementId = None
        self.GameServerSessionQueueName = None
        self.PlayerLatencies = None
        self.Status = None
        self.DnsName = None
        self.GameServerSessionId = None
        self.GameServerSessionName = None
        self.GameServerSessionRegion = None
        self.GameProperties = None
        self.MaximumPlayerSessionCount = None
        self.GameServerSessionData = None
        self.IpAddress = None
        self.Port = None
        self.MatchmakerData = None
        self.PlacedPlayerSessions = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.PlacementId = params.get("PlacementId")
        self.GameServerSessionQueueName = params.get("GameServerSessionQueueName")
        if params.get("PlayerLatencies") is not None:
            self.PlayerLatencies = []
            for item in params.get("PlayerLatencies"):
                obj = PlayerLatency()
                obj._deserialize(item)
                self.PlayerLatencies.append(obj)
        self.Status = params.get("Status")
        self.DnsName = params.get("DnsName")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.GameServerSessionName = params.get("GameServerSessionName")
        self.GameServerSessionRegion = params.get("GameServerSessionRegion")
        if params.get("GameProperties") is not None:
            self.GameProperties = []
            for item in params.get("GameProperties"):
                obj = GameProperty()
                obj._deserialize(item)
                self.GameProperties.append(obj)
        self.MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        self.GameServerSessionData = params.get("GameServerSessionData")
        self.IpAddress = params.get("IpAddress")
        self.Port = params.get("Port")
        self.MatchmakerData = params.get("MatchmakerData")
        if params.get("PlacedPlayerSessions") is not None:
            self.PlacedPlayerSessions = []
            for item in params.get("PlacedPlayerSessions"):
                obj = PlacedPlayerSession()
                obj._deserialize(item)
                self.PlacedPlayerSessions.append(obj)
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class GetGameServerSessionLogUrlRequest(AbstractModel):
    """GetGameServerSessionLogUrl请求参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionId: 游戏服务器会话ID
        :type GameServerSessionId: str
        """
        self.GameServerSessionId = None


    def _deserialize(self, params):
        self.GameServerSessionId = params.get("GameServerSessionId")


class GetGameServerSessionLogUrlResponse(AbstractModel):
    """GetGameServerSessionLogUrl返回参数结构体

    """

    def __init__(self):
        """
        :param PreSignedUrl: 日志下载URL
注意：此字段可能返回 null，表示取不到有效值。
        :type PreSignedUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PreSignedUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PreSignedUrl = params.get("PreSignedUrl")
        self.RequestId = params.get("RequestId")


class InstanceCounts(AbstractModel):
    """服务器实例统计数据

    """

    def __init__(self):
        """
        :param Active: 活跃的服务器实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type Active: int
        :param Desired: 期望的服务器实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type Desired: int
        :param Idle: 空闲的服务器实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type Idle: int
        :param MaxiNum: 服务器实例数最大限制
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxiNum: int
        :param MiniNum: 服务器实例数最小限制
注意：此字段可能返回 null，表示取不到有效值。
        :type MiniNum: int
        :param Pending: 已开始创建，但未激活的服务器实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type Pending: int
        :param Terminating: 结束中的服务器实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type Terminating: int
        """
        self.Active = None
        self.Desired = None
        self.Idle = None
        self.MaxiNum = None
        self.MiniNum = None
        self.Pending = None
        self.Terminating = None


    def _deserialize(self, params):
        self.Active = params.get("Active")
        self.Desired = params.get("Desired")
        self.Idle = params.get("Idle")
        self.MaxiNum = params.get("MaxiNum")
        self.MiniNum = params.get("MiniNum")
        self.Pending = params.get("Pending")
        self.Terminating = params.get("Terminating")


class JoinGameServerSessionRequest(AbstractModel):
    """JoinGameServerSession请求参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionId: 游戏服务器会话ID
        :type GameServerSessionId: str
        :param PlayerId: 玩家ID
        :type PlayerId: str
        :param PlayerData: 玩家自定义信息
        :type PlayerData: str
        """
        self.GameServerSessionId = None
        self.PlayerId = None
        self.PlayerData = None


    def _deserialize(self, params):
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.PlayerId = params.get("PlayerId")
        self.PlayerData = params.get("PlayerData")


class JoinGameServerSessionResponse(AbstractModel):
    """JoinGameServerSession返回参数结构体

    """

    def __init__(self):
        """
        :param PlayerSession: 玩家会话
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayerSession: :class:`tencentcloud.gse.v20191112.models.PlayerSession`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PlayerSession = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PlayerSession") is not None:
            self.PlayerSession = PlayerSession()
            self.PlayerSession._deserialize(params.get("PlayerSession"))
        self.RequestId = params.get("RequestId")


class PlacedPlayerSession(AbstractModel):
    """部署的玩家游戏会话

    """

    def __init__(self):
        """
        :param PlayerId: 玩家Id
        :type PlayerId: str
        :param PlayerSessionId: 玩家会话Id
        :type PlayerSessionId: str
        """
        self.PlayerId = None
        self.PlayerSessionId = None


    def _deserialize(self, params):
        self.PlayerId = params.get("PlayerId")
        self.PlayerSessionId = params.get("PlayerSessionId")


class PlayerLatency(AbstractModel):
    """玩家延迟信息

    """

    def __init__(self):
        """
        :param PlayerId: 玩家Id
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayerId: str
        :param RegionIdentifier: 延迟对应的区域名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionIdentifier: str
        :param LatencyInMilliseconds: 毫秒级延迟
        :type LatencyInMilliseconds: int
        """
        self.PlayerId = None
        self.RegionIdentifier = None
        self.LatencyInMilliseconds = None


    def _deserialize(self, params):
        self.PlayerId = params.get("PlayerId")
        self.RegionIdentifier = params.get("RegionIdentifier")
        self.LatencyInMilliseconds = params.get("LatencyInMilliseconds")


class PlayerSession(AbstractModel):
    """玩家会话详情

    """

    def __init__(self):
        """
        :param CreationTime: 玩家会话创建时间
        :type CreationTime: str
        :param DnsName: 游戏服务器会话运行的DNS标识
注意：此字段可能返回 null，表示取不到有效值。
        :type DnsName: str
        :param FleetId: 舰队ID
        :type FleetId: str
        :param GameServerSessionId: 游戏服务器会话ID
        :type GameServerSessionId: str
        :param IpAddress: 游戏服务器会话运行的CVM地址
        :type IpAddress: str
        :param PlayerData: 玩家相关信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayerData: str
        :param PlayerId: 玩家ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayerId: str
        :param PlayerSessionId: 玩家会话ID
        :type PlayerSessionId: str
        :param Port: 端口号
        :type Port: int
        :param Status: 玩家会话的状态
        :type Status: str
        :param TerminationTime: 玩家会话终止时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TerminationTime: str
        """
        self.CreationTime = None
        self.DnsName = None
        self.FleetId = None
        self.GameServerSessionId = None
        self.IpAddress = None
        self.PlayerData = None
        self.PlayerId = None
        self.PlayerSessionId = None
        self.Port = None
        self.Status = None
        self.TerminationTime = None


    def _deserialize(self, params):
        self.CreationTime = params.get("CreationTime")
        self.DnsName = params.get("DnsName")
        self.FleetId = params.get("FleetId")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.IpAddress = params.get("IpAddress")
        self.PlayerData = params.get("PlayerData")
        self.PlayerId = params.get("PlayerId")
        self.PlayerSessionId = params.get("PlayerSessionId")
        self.Port = params.get("Port")
        self.Status = params.get("Status")
        self.TerminationTime = params.get("TerminationTime")


class PutScalingPolicyRequest(AbstractModel):
    """PutScalingPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务部署ID
        :type FleetId: str
        :param TargetConfiguration: 基于规则的扩缩容配置
        :type TargetConfiguration: :class:`tencentcloud.gse.v20191112.models.TargetConfiguration`
        """
        self.FleetId = None
        self.TargetConfiguration = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        if params.get("TargetConfiguration") is not None:
            self.TargetConfiguration = TargetConfiguration()
            self.TargetConfiguration._deserialize(params.get("TargetConfiguration"))


class PutScalingPolicyResponse(AbstractModel):
    """PutScalingPolicy返回参数结构体

    """

    def __init__(self):
        """
        :param Name: 规则名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.RequestId = params.get("RequestId")


class ScalingPolicy(AbstractModel):
    """动态扩缩容配置

    """

    def __init__(self):
        """
        :param FleetId: 服务部署ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetId: str
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param ScalingAdjustment: 保留参数
注意：此字段可能返回 null，表示取不到有效值。
        :type ScalingAdjustment: str
        :param ScalingAdjustmentType: 保留参数
注意：此字段可能返回 null，表示取不到有效值。
        :type ScalingAdjustmentType: str
        :param ComparisonOperator: 保留参数
注意：此字段可能返回 null，表示取不到有效值。
        :type ComparisonOperator: str
        :param Threshold: 保留参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Threshold: str
        :param EvaluationPeriods: 保留参数
注意：此字段可能返回 null，表示取不到有效值。
        :type EvaluationPeriods: str
        :param MetricName: 保留参数
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricName: str
        :param PolicyType: 策略类型
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyType: str
        :param TargetConfiguration: 基于规则的配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetConfiguration: :class:`tencentcloud.gse.v20191112.models.TargetConfiguration`
        """
        self.FleetId = None
        self.Name = None
        self.Status = None
        self.ScalingAdjustment = None
        self.ScalingAdjustmentType = None
        self.ComparisonOperator = None
        self.Threshold = None
        self.EvaluationPeriods = None
        self.MetricName = None
        self.PolicyType = None
        self.TargetConfiguration = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.ScalingAdjustment = params.get("ScalingAdjustment")
        self.ScalingAdjustmentType = params.get("ScalingAdjustmentType")
        self.ComparisonOperator = params.get("ComparisonOperator")
        self.Threshold = params.get("Threshold")
        self.EvaluationPeriods = params.get("EvaluationPeriods")
        self.MetricName = params.get("MetricName")
        self.PolicyType = params.get("PolicyType")
        if params.get("TargetConfiguration") is not None:
            self.TargetConfiguration = TargetConfiguration()
            self.TargetConfiguration._deserialize(params.get("TargetConfiguration"))


class StartGameServerSessionPlacementRequest(AbstractModel):
    """StartGameServerSessionPlacement请求参数结构体

    """

    def __init__(self):
        """
        :param PlacementId: 开始部署游戏服务器会话的唯一标识符
        :type PlacementId: str
        :param GameServerSessionQueueName: 游戏服务器会话队列名称
        :type GameServerSessionQueueName: str
        :param MaximumPlayerSessionCount: 游戏服务器允许同时连接到游戏会话的最大玩家数量
        :type MaximumPlayerSessionCount: int
        :param DesiredPlayerSessions: 玩家游戏会话信息
        :type DesiredPlayerSessions: list of DesiredPlayerSession
        :param GameProperties: 玩家游戏会话属性
        :type GameProperties: list of GameProperty
        :param GameServerSessionData: 游戏服务器会话数据
        :type GameServerSessionData: str
        :param GameServerSessionName: 游戏服务器会话名称
        :type GameServerSessionName: str
        :param PlayerLatencies: 玩家延迟
        :type PlayerLatencies: list of PlayerLatency
        """
        self.PlacementId = None
        self.GameServerSessionQueueName = None
        self.MaximumPlayerSessionCount = None
        self.DesiredPlayerSessions = None
        self.GameProperties = None
        self.GameServerSessionData = None
        self.GameServerSessionName = None
        self.PlayerLatencies = None


    def _deserialize(self, params):
        self.PlacementId = params.get("PlacementId")
        self.GameServerSessionQueueName = params.get("GameServerSessionQueueName")
        self.MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        if params.get("DesiredPlayerSessions") is not None:
            self.DesiredPlayerSessions = []
            for item in params.get("DesiredPlayerSessions"):
                obj = DesiredPlayerSession()
                obj._deserialize(item)
                self.DesiredPlayerSessions.append(obj)
        if params.get("GameProperties") is not None:
            self.GameProperties = []
            for item in params.get("GameProperties"):
                obj = GameProperty()
                obj._deserialize(item)
                self.GameProperties.append(obj)
        self.GameServerSessionData = params.get("GameServerSessionData")
        self.GameServerSessionName = params.get("GameServerSessionName")
        if params.get("PlayerLatencies") is not None:
            self.PlayerLatencies = []
            for item in params.get("PlayerLatencies"):
                obj = PlayerLatency()
                obj._deserialize(item)
                self.PlayerLatencies.append(obj)


class StartGameServerSessionPlacementResponse(AbstractModel):
    """StartGameServerSessionPlacement返回参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionPlacement: 游戏服务器会话放置
        :type GameServerSessionPlacement: :class:`tencentcloud.gse.v20191112.models.GameServerSessionPlacement`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GameServerSessionPlacement = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessionPlacement") is not None:
            self.GameServerSessionPlacement = GameServerSessionPlacement()
            self.GameServerSessionPlacement._deserialize(params.get("GameServerSessionPlacement"))
        self.RequestId = params.get("RequestId")


class StopGameServerSessionPlacementRequest(AbstractModel):
    """StopGameServerSessionPlacement请求参数结构体

    """

    def __init__(self):
        """
        :param PlacementId: 游戏服务器会话放置的唯一标识符
        :type PlacementId: str
        """
        self.PlacementId = None


    def _deserialize(self, params):
        self.PlacementId = params.get("PlacementId")


class StopGameServerSessionPlacementResponse(AbstractModel):
    """StopGameServerSessionPlacement返回参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionPlacement: 游戏服务器会话放置
        :type GameServerSessionPlacement: :class:`tencentcloud.gse.v20191112.models.GameServerSessionPlacement`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GameServerSessionPlacement = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessionPlacement") is not None:
            self.GameServerSessionPlacement = GameServerSessionPlacement()
            self.GameServerSessionPlacement._deserialize(params.get("GameServerSessionPlacement"))
        self.RequestId = params.get("RequestId")


class TargetConfiguration(AbstractModel):
    """基于规则的动态扩缩容配置项

    """

    def __init__(self):
        """
        :param TargetValue: 预留存率
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetValue: int
        """
        self.TargetValue = None


    def _deserialize(self, params):
        self.TargetValue = params.get("TargetValue")


class UpdateFleetCapacityRequest(AbstractModel):
    """UpdateFleetCapacity请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务部署ID
        :type FleetId: str
        :param DesiredInstances: 期望的服务器实例数
        :type DesiredInstances: int
        :param MinSize: 服务器实例数最小限制
        :type MinSize: int
        :param MaxSize: 服务器实例数最大限制
        :type MaxSize: int
        """
        self.FleetId = None
        self.DesiredInstances = None
        self.MinSize = None
        self.MaxSize = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.DesiredInstances = params.get("DesiredInstances")
        self.MinSize = params.get("MinSize")
        self.MaxSize = params.get("MaxSize")


class UpdateFleetCapacityResponse(AbstractModel):
    """UpdateFleetCapacity返回参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务部署ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FleetId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.RequestId = params.get("RequestId")


class UpdateGameServerSessionRequest(AbstractModel):
    """UpdateGameServerSession请求参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionId: 游戏服务器会话ID
        :type GameServerSessionId: str
        :param MaximumPlayerSessionCount: 最大玩家数量
        :type MaximumPlayerSessionCount: int
        :param Name: 游戏服务器会话名称
        :type Name: str
        :param PlayerSessionCreationPolicy: 玩家会话创建策略（ACCEPT_ALL,DENY_ALL）
        :type PlayerSessionCreationPolicy: str
        :param ProtectionPolicy: 保护策略(NoProtection,TimeLimitProtection,FullProtection)
        :type ProtectionPolicy: str
        """
        self.GameServerSessionId = None
        self.MaximumPlayerSessionCount = None
        self.Name = None
        self.PlayerSessionCreationPolicy = None
        self.ProtectionPolicy = None


    def _deserialize(self, params):
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        self.Name = params.get("Name")
        self.PlayerSessionCreationPolicy = params.get("PlayerSessionCreationPolicy")
        self.ProtectionPolicy = params.get("ProtectionPolicy")


class UpdateGameServerSessionResponse(AbstractModel):
    """UpdateGameServerSession返回参数结构体

    """

    def __init__(self):
        """
        :param GameServerSession: 更新后的游戏会话
        :type GameServerSession: :class:`tencentcloud.gse.v20191112.models.GameServerSession`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GameServerSession = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSession") is not None:
            self.GameServerSession = GameServerSession()
            self.GameServerSession._deserialize(params.get("GameServerSession"))
        self.RequestId = params.get("RequestId")