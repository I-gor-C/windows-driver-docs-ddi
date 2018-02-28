---
UID: NN:portcls.IMiniportWaveRTOutputStream
title: IMiniportWaveRTOutputStream
author: windows-driver-content
description: The IMiniportWaveRTOutputStream interface represents the output wave stream. IMiniportWaveRTOutputStream inherits from the IUnknown interface.
old-location: audio\iminiportwavertoutputstream.htm
old-project: audio
ms.assetid: 40210313-1216-4E1A-B696-B23D2ACED605
ms.author: windowsdriverdev
ms.date: 2/22/2018
ms.keywords: IMiniportWaveRTOutputStream, IMiniportWaveRTOutputStream interface [Audio Devices], IMiniportWaveRTOutputStream interface [Audio Devices], described, audio.iminiportwavertoutputstream, portcls/IMiniportWaveRTOutputStream
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: portcls.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
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
-	portcls.h
api_name:
-	IMiniportWaveRTOutputStream
product: Windows
targetos: Windows
req.typenames: PC_EXIT_LATENCY, *PPC_EXIT_LATENCY
---

# IMiniportWaveRTOutputStream interface

The <code>IMiniportWaveRTOutputStream</code> interface represents the output wave stream. <code>IMiniportWaveRTOutputStream</code> inherits from the <b>IUnknown</b> interface.

<code>IMiniportWaveRTOutputStream</code> is supported in Windows 10 and later.

## Methods

<p>The <b>IMiniportWaveRTOutputStream</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IMiniportWaveRTOutputStream::GetOutputStreamPresentationPosition](nf-portcls-iminiportwavertoutputstream-getoutputstreampresentationposition.md) | Returns stream presentation information. |
| [IMiniportWaveRTOutputStream::GetPacketCount](nf-portcls-iminiportwavertoutputstream-getpacketcount.md) | GetPacketCount returns the (1-based) count of packets completely transferred from the WaveRT buffer into hardware. |
| [IMiniportWaveRTOutputStream::SetWritePacket](nf-portcls-iminiportwavertoutputstream-setwritepacket.md) | SetWritePacket informs the driver that the OS has written valid data to the WaveRT buffer. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | portcls.h |