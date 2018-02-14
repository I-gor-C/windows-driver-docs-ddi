---
UID: NN:portcls.IMiniportAudioSignalProcessing
title: IMiniportAudioSignalProcessing
author: windows-driver-content
description: The IMiniportAudioSignalProcessing interface is implemented by the WaveRT miniport component of any audio driver, if any of its pins support audio signal processing modes.
old-location: audio\iminiportaudiosignalprocessing.htm
old-project: audio
ms.assetid: 6C520509-347F-4E01-95C4-0D3306031E51
ms.author: windowsdriverdev
ms.date: 2/8/2018
ms.keywords: audio.iminiportaudiosignalprocessing, IMiniportAudioSignalProcessing interface [Audio Devices], IMiniportAudioSignalProcessing interface [Audio Devices], described, IMiniportAudioSignalProcessing, portcls/IMiniportAudioSignalProcessing
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	Portcls.h
apiname:
-	IMiniportAudioSignalProcessing
product: Windows
targetos: Windows
req.typenames: "*PPC_EXIT_LATENCY, PC_EXIT_LATENCY"
---

# IMiniportAudioSignalProcessing interface

The IMiniportAudioSignalProcessing interface is implemented by the WaveRT miniport component of any audio driver, if any of its pins support audio signal processing modes.

## Methods

<p>The <b>IMiniportAudioSignalProcessing</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [portcls.IMiniportAudioSignalProcessing.GetModes](nf-portcls-iminiportaudiosignalprocessing-getmodes.md) | The GetModes method, Gets the audio signal processing modes supported by an audio pin. |

## Remarks

Any of the Portcls miniport drivers can also implement the <b>GetModes</b> method.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1 Windows 8.1 |
| **Target Platform** | Windows |
| **Header** | portcls.h |