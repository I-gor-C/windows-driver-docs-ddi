---
UID : NF:portcls.IMiniportAudioEngineNode.GetDeviceChannelVolume
title : IMiniportAudioEngineNode::GetDeviceChannelVolume method
author : windows-driver-content
description : Gets the volume level for a given channel of the audio device.
old-location : audio\iminiportaudioenginenode_getdevicechannelvolume.htm
old-project : audio
ms.assetid : 195AAD37-6993-4F0A-BEF7-848122402742
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : GetDeviceChannelVolume method [Audio Devices], IMiniportAudioEngineNode interface, IMiniportAudioEngineNode interface [Audio Devices], GetDeviceChannelVolume method, audio.iminiportaudioenginenode_getdevicechannelvolume, GetDeviceChannelVolume, GetDeviceChannelVolume method [Audio Devices], IMiniportAudioEngineNode::GetDeviceChannelVolume, portcls/IMiniportAudioEngineNode::GetDeviceChannelVolume, IMiniportAudioEngineNode
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : method
req.header : portcls.h
req.include-header : 
req.target-type : Universal
req.target-min-winverclnt : Windows 8
req.target-min-winversvr : Windows Server 2012
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : portcls.h
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : PC_EXIT_LATENCY, *PPC_EXIT_LATENCY
---


# GetDeviceChannelVolume method
Gets the volume level for a given channel of the audio device.

## Syntax

````
NTSTATUS GetDeviceChannelVolume(
  [in]  ULONG  ulNodeId,
  [in]  UINT32 ulChannel,
  [out] LONG   *plVolume
);
````

## Parameters

`ulNodeId`

The ID for the node that represents the audio device.

`ulChannel`

The audio device channel.

`plVolume`

The current volume level for the audio device channel.


## Return Value

<b>GetDeviceChannelVolume</b> returns S_OK, if the call was successful. Otherwise, the method returns an appropriate error 

code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | portcls.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<a href="..\portcls\nn-portcls-iminiportaudioenginenode.md">IMiniportAudioEngineNode</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IMiniportAudioEngineNode::GetDeviceChannelVolume method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>