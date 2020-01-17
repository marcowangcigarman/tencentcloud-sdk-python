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


class CreateAsrVocabRequest(AbstractModel):
    """CreateAsrVocab请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 热词表名称，长度在1-255之间
        :type Name: str
        :param Description: 热词表描述，长度在0-1000之间
        :type Description: str
        :param WordWeights: 词权重数组，包含全部的热词和对应的权重。每个热词的长度不大于10，权重为[1,10]之间整数，数组长度不大于128
        :type WordWeights: list of HotWord
        :param WordWeightStr: 词权重文件（纯文本文件）的二进制base64编码，以行分隔，每行的格式为word|weight，即以英文符号|为分割，左边为词，右边为权重，如：你好|5。
当用户传此参数（参数长度大于0），即以此参数解析词权重，WordWeights会被忽略
        :type WordWeightStr: str
        """
        self.Name = None
        self.Description = None
        self.WordWeights = None
        self.WordWeightStr = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("WordWeights") is not None:
            self.WordWeights = []
            for item in params.get("WordWeights"):
                obj = HotWord()
                obj._deserialize(item)
                self.WordWeights.append(obj)
        self.WordWeightStr = params.get("WordWeightStr")


class CreateAsrVocabResponse(AbstractModel):
    """CreateAsrVocab返回参数结构体

    """

    def __init__(self):
        """
        :param VocabId: 词表ID，可用于获取词表信息
        :type VocabId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VocabId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VocabId = params.get("VocabId")
        self.RequestId = params.get("RequestId")


class CreateRecTaskRequest(AbstractModel):
    """CreateRecTask请求参数结构体

    """

    def __init__(self):
        """
        :param EngineModelType: 引擎模型类型。
8k_zh：电话 8k 中文普通话通用，可用于双声道音频的识别；
8k_zh_s：电话 8k 中文普通话话者分离，仅用于单声道；
16k_zh：16k 中文普通话通用；
16k_en：16k 英语；
16k_ca：16k 粤语。
        :type EngineModelType: str
        :param ChannelNum: 语音声道数。1：单声道；2：双声道（仅在电话 8k 通用模型下支持）。
        :type ChannelNum: int
        :param ResTextFormat: 识别结果文本编码方式。0：UTF-8。
        :type ResTextFormat: int
        :param SourceType: 语音数据来源。0：语音 URL；1：语音数据（post body）。
        :type SourceType: int
        :param CallbackUrl: 回调 URL，用户自行搭建的用于接收识别结果的服务器地址， 长度小于2048字节。如果用户使用回调方式获取识别结果，需提交该参数；如果用户使用轮询方式获取识别结果，则无需提交该参数。
        :type CallbackUrl: str
        :param Url: 语音的URL地址，需要公网可下载。长度小于2048字节，当 SourceType 值为 0 时须填写该字段，为 1 时不需要填写。注意：请确保录音文件时长在一个小时之内，否则可能识别失败。请保证文件的下载速度，否则可能下载失败。
        :type Url: str
        :param Data: 语音数据，当SourceType 值为1时必须填写，为0可不写。要base64编码(采用python语言时注意读取文件应该为string而不是byte，以byte格式读取后要decode()。编码后的数据不可带有回车换行符)。音频数据要小于5MB。
        :type Data: str
        :param DataLen: 数据长度，当 SourceType 值为1时必须填写，为0可不写（此数据长度为数据未进行base64编码时的数据长度）。
        :type DataLen: int
        :param HotwordId: 热词id。用于调用对应的热词表，如果在调用语音识别服务时，不进行单独的热词id设置，自动生效默认热词；如果进行了单独的热词id设置，那么将生效单独设置的热词id。
        :type HotwordId: str
        """
        self.EngineModelType = None
        self.ChannelNum = None
        self.ResTextFormat = None
        self.SourceType = None
        self.CallbackUrl = None
        self.Url = None
        self.Data = None
        self.DataLen = None
        self.HotwordId = None


    def _deserialize(self, params):
        self.EngineModelType = params.get("EngineModelType")
        self.ChannelNum = params.get("ChannelNum")
        self.ResTextFormat = params.get("ResTextFormat")
        self.SourceType = params.get("SourceType")
        self.CallbackUrl = params.get("CallbackUrl")
        self.Url = params.get("Url")
        self.Data = params.get("Data")
        self.DataLen = params.get("DataLen")
        self.HotwordId = params.get("HotwordId")


class CreateRecTaskResponse(AbstractModel):
    """CreateRecTask返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 录音文件识别的请求返回结果，包含结果查询需要的TaskId
        :type Data: :class:`tencentcloud.asr.v20190614.models.Task`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = Task()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DeleteAsrVocabRequest(AbstractModel):
    """DeleteAsrVocab请求参数结构体

    """

    def __init__(self):
        """
        :param VocabId: 热词表Id
        :type VocabId: str
        """
        self.VocabId = None


    def _deserialize(self, params):
        self.VocabId = params.get("VocabId")


class DeleteAsrVocabResponse(AbstractModel):
    """DeleteAsrVocab返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 从CreateRecTask接口获取的TaskId，用于获取任务状态与结果。
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class DescribeTaskStatusResponse(AbstractModel):
    """DescribeTaskStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 录音文件识别的请求返回结果。
        :type Data: :class:`tencentcloud.asr.v20190614.models.TaskStatus`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = TaskStatus()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class GetAsrVocabRequest(AbstractModel):
    """GetAsrVocab请求参数结构体

    """

    def __init__(self):
        """
        :param VocabId: 热词表ID
        :type VocabId: str
        """
        self.VocabId = None


    def _deserialize(self, params):
        self.VocabId = params.get("VocabId")


class GetAsrVocabResponse(AbstractModel):
    """GetAsrVocab返回参数结构体

    """

    def __init__(self):
        """
        :param Name: 热词表名称
        :type Name: str
        :param Description: 热词表描述
        :type Description: str
        :param VocabId: 热词表ID
        :type VocabId: str
        :param WordWeights: 词权重列表
        :type WordWeights: list of HotWord
        :param CreateTime: 词表创建时间
        :type CreateTime: str
        :param UpdateTime: 词表更新时间
        :type UpdateTime: str
        :param State: 热词表状态，1为默认状态即在识别时默认加载该热词表进行识别，0为初始状态
        :type State: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.Description = None
        self.VocabId = None
        self.WordWeights = None
        self.CreateTime = None
        self.UpdateTime = None
        self.State = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.VocabId = params.get("VocabId")
        if params.get("WordWeights") is not None:
            self.WordWeights = []
            for item in params.get("WordWeights"):
                obj = HotWord()
                obj._deserialize(item)
                self.WordWeights.append(obj)
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.State = params.get("State")
        self.RequestId = params.get("RequestId")


class HotWord(AbstractModel):
    """热词的词和权重

    """

    def __init__(self):
        """
        :param Word: 热词
        :type Word: str
        :param Weight: 权重
        :type Weight: int
        """
        self.Word = None
        self.Weight = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        self.Weight = params.get("Weight")


class SentenceRecognitionRequest(AbstractModel):
    """SentenceRecognition请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 腾讯云项目 ID，可填 0，总长度不超过 1024 字节。
        :type ProjectId: int
        :param SubServiceType: 子服务类型。2： 一句话识别。
        :type SubServiceType: int
        :param EngSerViceType: 引擎模型类型。
8k_zh：电话 8k 中文普通话通用；
16k_zh：16k 中文普通话通用；
16k_en：16k 英语；
16k_ca：16k 粤语。
        :type EngSerViceType: str
        :param SourceType: 语音数据来源。0：语音 URL；1：语音数据（post body）。
        :type SourceType: int
        :param VoiceFormat: 识别音频的音频格式。mp3、wav。
        :type VoiceFormat: str
        :param UsrAudioKey: 用户端对此任务的唯一标识，用户自助生成，用于用户查找识别结果。
        :type UsrAudioKey: str
        :param Url: 语音 URL，公网可下载。当 SourceType 值为 0（语音 URL上传） 时须填写该字段，为 1 时不填；URL 的长度大于 0，小于 2048，需进行urlencode编码。音频时间长度要小于60s。
        :type Url: str
        :param Data: 语音数据，当SourceType 值为1（本地语音数据上传）时必须填写，当SourceType 值为0（语音 URL上传）可不写。要使用base64编码(采用python语言时注意读取文件应该为string而不是byte，以byte格式读取后要decode()。编码后的数据不可带有回车换行符)。音频数据要小于600KB。
        :type Data: str
        :param DataLen: 数据长度，单位为字节。当 SourceType 值为1（本地语音数据上传）时必须填写，当 SourceType 值为0（语音 URL上传）可不写（此数据长度为数据未进行base64编码时的数据长度）。
        :type DataLen: int
        :param HotwordId: 热词id。用于调用对应的热词表，如果在调用语音识别服务时，不进行单独的热词id设置，自动生效默认热词；如果进行了单独的热词id设置，那么将生效单独设置的热词id。
        :type HotwordId: str
        """
        self.ProjectId = None
        self.SubServiceType = None
        self.EngSerViceType = None
        self.SourceType = None
        self.VoiceFormat = None
        self.UsrAudioKey = None
        self.Url = None
        self.Data = None
        self.DataLen = None
        self.HotwordId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.SubServiceType = params.get("SubServiceType")
        self.EngSerViceType = params.get("EngSerViceType")
        self.SourceType = params.get("SourceType")
        self.VoiceFormat = params.get("VoiceFormat")
        self.UsrAudioKey = params.get("UsrAudioKey")
        self.Url = params.get("Url")
        self.Data = params.get("Data")
        self.DataLen = params.get("DataLen")
        self.HotwordId = params.get("HotwordId")


class SentenceRecognitionResponse(AbstractModel):
    """SentenceRecognition返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 识别结果。
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class Task(AbstractModel):
    """录音文件识别请求的返回数据

    """

    def __init__(self):
        """
        :param TaskId: 任务ID，可通过此ID在轮询接口获取识别状态与结果
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class TaskStatus(AbstractModel):
    """获取录音识别结果结果的返回参数

    """

    def __init__(self):
        """
        :param TaskId: 任务标识。
        :type TaskId: int
        :param Status: 任务状态码，0：任务等待，1：任务执行中，2：任务成功，3：任务失败。
        :type Status: int
        :param StatusStr: 任务状态，waiting：任务等待，doing：任务执行中，success：任务成功，failed：任务失败。
        :type StatusStr: str
        :param Result: 识别结果。
        :type Result: str
        :param ErrorMsg: 失败原因说明。
        :type ErrorMsg: str
        """
        self.TaskId = None
        self.Status = None
        self.StatusStr = None
        self.Result = None
        self.ErrorMsg = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.StatusStr = params.get("StatusStr")
        self.Result = params.get("Result")
        self.ErrorMsg = params.get("ErrorMsg")


class UpdateAsrVocabRequest(AbstractModel):
    """UpdateAsrVocab请求参数结构体

    """

    def __init__(self):
        """
        :param VocabId: 热词表ID
        :type VocabId: str
        :param Name: 热词表名称
        :type Name: str
        :param WordWeights: 词权重数组，包含全部的热词和对应的权重。每个热词的长度不大于10，权重为[1,10]之间整数，数组长度不大于128
        :type WordWeights: list of HotWord
        :param WordWeightStr: 词权重文件（纯文本文件）的二进制base64编码，以行分隔，每行的格式为word|weight，即以英文符号|为分割，左边为词，右边为权重，如：你好|5。
当用户传此参数（参数长度大于0），即以此参数解析词权重，WordWeights会被忽略
        :type WordWeightStr: str
        :param Description: 热词表描述
        :type Description: str
        """
        self.VocabId = None
        self.Name = None
        self.WordWeights = None
        self.WordWeightStr = None
        self.Description = None


    def _deserialize(self, params):
        self.VocabId = params.get("VocabId")
        self.Name = params.get("Name")
        if params.get("WordWeights") is not None:
            self.WordWeights = []
            for item in params.get("WordWeights"):
                obj = HotWord()
                obj._deserialize(item)
                self.WordWeights.append(obj)
        self.WordWeightStr = params.get("WordWeightStr")
        self.Description = params.get("Description")


class UpdateAsrVocabResponse(AbstractModel):
    """UpdateAsrVocab返回参数结构体

    """

    def __init__(self):
        """
        :param VocabId: 热词表ID
        :type VocabId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VocabId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VocabId = params.get("VocabId")
        self.RequestId = params.get("RequestId")