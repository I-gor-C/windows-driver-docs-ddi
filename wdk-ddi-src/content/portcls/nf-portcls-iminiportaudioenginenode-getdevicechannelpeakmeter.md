---
UID: NF:portcls.IMiniportAudioEngineNode.GetDeviceChannelPeakMeter
title: IMiniportAudioEngineNode::GetDeviceChannelPeakMeter method
author: windows-driver-content
description: Gets the PeakMeter value for the audio device channel.
old-location: audio\iminiportaudioenginenode_getdevicechannelpeakmeter.htm
old-project: audio
ms.assetid: 31F291ED-0B04-4CDF-A83B-7CF3717EC234
ms.author: windowsdriverdev
ms.date: 2/8/2018
ms.keywords: IMiniportAudioEngineNode interface [Audio Devices], GetDeviceChannelPeakMeter method, GetDeviceChannelPeakMeter method [Audio Devices], IMiniportAudioEngineNode, audio.iminiportaudioenginenode_getdevicechannelpeakmeter, GetDeviceChannelPeakMeter, IMiniportAudioEngineNode::GetDeviceChannelPeakMeter, GetDeviceChannelPeakMeter method [Audio Devices], IMiniportAudioEngineNode interface, portcls/IMiniportAudioEngineNode::GetDeviceChannelPeakMeter
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
req.lib: portcls.h
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	Portcls.h
apiname:
-	IMiniportAudioEngineNode.GetDeviceChannelPeakMeter
product: Windows
targetos: Windows
req.typenames: "*PPC_EXIT_LATENCY, PC_EXIT_LATENCY"
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
| **Library** | portcls.h |

## See Also

<a href="..\portcls\nn-portcls-iminiportaudioenginenode.md">IMiniportAudioEngineNode</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IMiniportAudioEngineNode::GetDeviceChannelPeakMeter method%20 RELEASE:%20(2/8/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>