---
UID: NF:portcls.IMiniportAudioEngineNode.SetDeviceChannelVolume
title: IMiniportAudioEngineNode::SetDeviceChannelVolume method
author: windows-driver-content
description: Sets the volume level for a given channel of the audio device.
old-location: audio\iminiportaudioenginenode_setdevicechannelvolume.htm
old-project: audio
ms.assetid: 05DA619B-B36A-4E14-9F63-E12E90E0BDCD
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: IMiniportAudioEngineNode, IMiniportAudioEngineNode interface [Audio Devices], SetDeviceChannelVolume method, IMiniportAudioEngineNode::SetDeviceChannelVolume, SetDeviceChannelVolume method [Audio Devices], SetDeviceChannelVolume method [Audio Devices], IMiniportAudioEngineNode interface, SetDeviceChannelVolume,IMiniportAudioEngineNode.SetDeviceChannelVolume, audio.iminiportaudioenginenode_setdevicechannelvolume, portcls/IMiniportAudioEngineNode::SetDeviceChannelVolume
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
-	IMiniportAudioEngineNode.SetDeviceChannelVolume
product: Windows
targetos: Windows
req.typenames: PC_EXIT_LATENCY, *PPC_EXIT_LATENCY
---


# SetDeviceChannelVolume method
Sets the volume level for a given channel of the audio device.

## Syntax

````
NTSTATUS SetDeviceChannelVolume(
  [in] ULONG  ulNodeId,
  [in] UINT32 ulChannel,
  [in] LONG   lVolume
);
````

## Parameters

`ulNodeId`

The ID for the node that represents the audio device.

`ulChannel`

The audio device channel.

`lVolume`

The volume level to which the channel will be set.


## Return Value

<b>SetDeviceChannelVolume</b> returns S_OK, if the call was successful. Otherwise, the method returns an appropriate error code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Universal |
| **Header** | portcls.h |

## See Also

<a href="..\portcls\nn-portcls-iminiportaudioenginenode.md">IMiniportAudioEngineNode</a>