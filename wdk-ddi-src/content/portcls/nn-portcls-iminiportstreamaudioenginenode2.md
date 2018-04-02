---
UID: NN:portcls.IMiniportStreamAudioEngineNode2
title: IMiniportStreamAudioEngineNode2
author: windows-driver-content
description: The IMiniportStreamAudioEngineNode2 interface allows an audio miniport driver to extend the capabilities of the IMiniportStreamAudioEngineNode interface.
old-location: audio\iminiportstreamaudioenginenode2.htm
old-project: audio
ms.assetid: 38888C17-31FC-47F4-A49B-A46A9DF962AF
ms.author: windowsdriverdev
ms.date: 3/19/2018
ms.keywords: IMiniportStreamAudioEngineNode2, IMiniportStreamAudioEngineNode2 interface [Audio Devices], IMiniportStreamAudioEngineNode2 interface [Audio Devices], described, audio.iminiportstreamaudioenginenode2, portcls/IMiniportStreamAudioEngineNode2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: portcls.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Portcls.lib
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	Portcls.h
api_name:
-	IMiniportStreamAudioEngineNode2
product:
- Windows
targetos: Windows
req.typenames: PC_EXIT_LATENCY, *PPC_EXIT_LATENCY
---

# IMiniportStreamAudioEngineNode2 interface

The <b>IMiniportStreamAudioEngineNode2</b> interface allows an audio miniport driver to extend the capabilities of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265090">IMiniportStreamAudioEngineNode</a> interface.

## Methods

<p>The <b>IMiniportStreamAudioEngineNode2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IMiniportStreamAudioEngineNode2::SetStreamCurrentWritePositionForLastBuffer](nf-portcls-iminiportstreamaudioenginenode2-setstreamcurrentwritepositionforlastbuffer.md) | Sets the current cursor position in the last audio data stream that was written to the audio buffer. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1 Windows 8.1 |
| **Target Platform** | Windows |
| **Header** | portcls.h |