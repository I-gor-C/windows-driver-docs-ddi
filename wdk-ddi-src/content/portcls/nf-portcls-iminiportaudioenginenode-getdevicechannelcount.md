---
UID: NF:portcls.IMiniportAudioEngineNode.GetDeviceChannelCount
title: IMiniportAudioEngineNode::GetDeviceChannelCount method
author: windows-driver-content
description: Gets a count of the number of channels supported by the audio device.
old-location: audio\iminiportaudioenginenode_getdevicechannelcount.htm
old-project: audio
ms.assetid: 978193AE-55CD-4255-8722-A1E008E98F08
ms.author: windowsdriverdev
ms.date: 3/19/2018
ms.keywords: GetDeviceChannelCount method [Audio Devices], GetDeviceChannelCount method [Audio Devices], IMiniportAudioEngineNode interface, GetDeviceChannelCount,IMiniportAudioEngineNode.GetDeviceChannelCount, IMiniportAudioEngineNode, IMiniportAudioEngineNode interface [Audio Devices], GetDeviceChannelCount method, IMiniportAudioEngineNode::GetDeviceChannelCount, audio.iminiportaudioenginenode_getdevicechannelcount, portcls/IMiniportAudioEngineNode::GetDeviceChannelCount
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: portcls.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	Portcls.h
api_name:
-	IMiniportAudioEngineNode.GetDeviceChannelCount
product: Windows
targetos: Windows
req.typenames: PC_EXIT_LATENCY, *PPC_EXIT_LATENCY
---


# IMiniportAudioEngineNode::GetDeviceChannelCount method
Gets a count of the number of channels supported by the audio device.

## Syntax

```
NTSTATUS GetDeviceChannelCount(
  ULONG              ulNodeId,
  eChannelTargetType targetType,
  UINT32             *pulChannelCount
);
```

## Parameters

`ulNodeId`

The ID of the node that represents the audio device.

`targetType`

An <a href="https://msdn.microsoft.com/library/windows/hardware/dn302034">eChannelTargetType</a> enumerated value that specifies the types of target nodes in the channels. For example, there could be Volume, Mute or PeakMeter nodes.

`pulChannelCount`

The number of channels supported by the audio device.


## Return Value

<b>GetDeviceChannelCount</b> returns S_OK, if the call was successful. Otherwise, the method 

returns an appropriate error code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Universal |
| **Header** | portcls.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn302040">IMiniportAudioEngineNode</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn302034">eChannelTargetType</a>