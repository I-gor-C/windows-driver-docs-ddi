---
UID: NF:portcls.IMiniportAudioEngineNode.GetMixFormat
title: IMiniportAudioEngineNode::GetMixFormat method
author: windows-driver-content
description: Gets the audio data format for the audio engine mixer.
old-location: audio\iminiportaudioenginenode_getmixformat.htm
old-project: audio
ms.assetid: CB0DD6C8-DFB3-42E0-B38F-341677A72E29
ms.author: windowsdriverdev
ms.date: 3/19/2018
ms.keywords: GetMixFormat method [Audio Devices], GetMixFormat method [Audio Devices], IMiniportAudioEngineNode interface, GetMixFormat,IMiniportAudioEngineNode.GetMixFormat, IMiniportAudioEngineNode, IMiniportAudioEngineNode interface [Audio Devices], GetMixFormat method, IMiniportAudioEngineNode::GetMixFormat, audio.iminiportaudioenginenode_getmixformat, portcls/IMiniportAudioEngineNode::GetMixFormat
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
-	IMiniportAudioEngineNode.GetMixFormat
product:
- Windows
targetos: Windows
req.typenames: PC_EXIT_LATENCY, *PPC_EXIT_LATENCY
---


# IMiniportAudioEngineNode::GetMixFormat method
Gets the audio data format for the audio engine mixer.

## Syntax

```
NTSTATUS GetMixFormat(
  ULONG                     ulNodeId,
  KSDATAFORMAT_WAVEFORMATEX *pFormat,
  ULONG                     ulBufferSize
);
```

## Parameters

`ulNodeId`

The ID of the mixer node.

`pFormat`

A structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff537095">KSDATAFORMAT_WAVEFORMATEX</a> that represents the audio data format.

`ulBufferSize`

The data buffer size.


## Return Value

<b>GetMixFormat</b> returns S_OK, if the call was successful. Otherwise, the method returns an appropriate error code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Universal |
| **Header** | portcls.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn302040">IMiniportAudioEngineNode</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff537095">KSDATAFORMAT_WAVEFORMATEX</a>