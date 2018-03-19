---
UID: NF:portcls.IMiniportAudioEngineNode.GetDeviceChannelPeakMeter
title: IMiniportAudioEngineNode::GetDeviceChannelPeakMeter method
author: windows-driver-content
description: Gets the PeakMeter value for the audio device channel.
old-location: audio\iminiportaudioenginenode_getdevicechannelpeakmeter.htm
old-project: audio
ms.assetid: 31F291ED-0B04-4CDF-A83B-7CF3717EC234
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: GetDeviceChannelPeakMeter method [Audio Devices], GetDeviceChannelPeakMeter method [Audio Devices], IMiniportAudioEngineNode interface, GetDeviceChannelPeakMeter,IMiniportAudioEngineNode.GetDeviceChannelPeakMeter, IMiniportAudioEngineNode, IMiniportAudioEngineNode interface [Audio Devices], GetDeviceChannelPeakMeter method, IMiniportAudioEngineNode::GetDeviceChannelPeakMeter, audio.iminiportaudioenginenode_getdevicechannelpeakmeter, portcls/IMiniportAudioEngineNode::GetDeviceChannelPeakMeter
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
-	IMiniportAudioEngineNode.GetDeviceChannelPeakMeter
product: Windows
targetos: Windows
req.typenames: PC_EXIT_LATENCY, *PPC_EXIT_LATENCY
---


# GetDeviceChannelPeakMeter method
Gets the PeakMeter value  for the audio device channel.

## Syntax

````
NTSTATUS GetDeviceChannelPeakMeter(
  [in]  ULONG  ulNodeId,
  [in]  UINT32 ulChannel,
  [out] LONG   *plPeakMeter
);
````

## Parameters

`ulNodeId`

The ID for the node that represents the audio device.

`ulChannel`

The audio device channel.

`plPeakMeter`

The PeakMeter value for the audio device channel.


## Return Value

<b>GetDeviceChannelPeakMeter</b> returns S_OK, if the call was successful. Otherwise, the method returns an appropriate error 

code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Universal |
| **Header** | portcls.h |

## See Also

<a href="..\portcls\nn-portcls-iminiportaudioenginenode.md">IMiniportAudioEngineNode</a>