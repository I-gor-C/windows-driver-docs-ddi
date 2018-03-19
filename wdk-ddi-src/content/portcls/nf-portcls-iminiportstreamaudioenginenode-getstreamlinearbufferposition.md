---
UID: NF:portcls.IMiniportStreamAudioEngineNode.GetStreamLinearBufferPosition
title: IMiniportStreamAudioEngineNode::GetStreamLinearBufferPosition method
author: windows-driver-content
description: Gets the number of bytes that the DMA has fetched from the audio buffer since the beginning of the stream.
old-location: audio\iminiportstreamaudioenginenode_getstreamlinearbufferposition.htm
old-project: audio
ms.assetid: C1C91ECE-7AFF-468B-84AE-9D289EECE1E1
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: GetStreamLinearBufferPosition method [Audio Devices], GetStreamLinearBufferPosition method [Audio Devices], IMiniportStreamAudioEngineNode interface, GetStreamLinearBufferPosition,IMiniportStreamAudioEngineNode.GetStreamLinearBufferPosition, IMiniportStreamAudioEngineNode, IMiniportStreamAudioEngineNode interface [Audio Devices], GetStreamLinearBufferPosition method, IMiniportStreamAudioEngineNode::GetStreamLinearBufferPosition, audio.iminiportstreamaudioenginenode_getstreamlinearbufferposition, portcls/IMiniportStreamAudioEngineNode::GetStreamLinearBufferPosition
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
-	IMiniportStreamAudioEngineNode.GetStreamLinearBufferPosition
product: Windows
targetos: Windows
req.typenames: PC_EXIT_LATENCY, *PPC_EXIT_LATENCY
---


# GetStreamLinearBufferPosition method
Gets the number of bytes that the DMA has fetched from the audio buffer since the beginning of the stream.

## Syntax

````
NTSTATUS GetStreamLinearBufferPosition(
  [out] ULONGLONG *pullLinearBufferPosition
);
````

## Parameters

`pullLinearBufferPosition`

The number of bytes that the DMA has fetched.


## Return Value

<b>GetStreamLinearBufferPosition</b> returns S_OK, if the call was successful. Otherwise, the method returns an appropriate error code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Universal |
| **Header** | portcls.h |

## See Also

<a href="..\portcls\nn-portcls-iminiportstreamaudioenginenode.md">IMiniportStreamAudioEngineNode</a>