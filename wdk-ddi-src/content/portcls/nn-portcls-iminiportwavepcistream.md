---
UID: NN.portcls.IMiniportWavePciStream
title: IMiniportWavePciStream
author: windows-driver-content
description: The IMiniportWavePciStream interface represents the wave stream that flows through a pin on a WavePci filter.
old-location: audio\iminiportwavepcistream.htm
old-project: audio
ms.assetid: 2341f914-d877-4a87-ac74-fb51e646510e
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PcUnregisterIoTimeout
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
req.alt-api: IMiniportWavePciStream
req.alt-loc: portcls.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# IMiniportWavePciStream interface



## -description
<p>The <code>IMiniportWavePciStream</code> interface represents the wave stream that flows through a pin on a WavePci filter. The filter wraps a WavePci rendering or capture device and is implemented by pairing a WavePci port driver with a WavePci miniport driver. The miniport driver implements the <code>IMiniportWavePciStream</code> interface and exposes it to the port driver. The miniport driver creates a stream object with this interface when the port driver calls the miniport driver's <a href="audio.iminiportwavepci_newstream">IMiniportWavePci::NewStream</a> method. <code>IMiniportWavePciStream</code> inherits from the <b>IUnknown</b> interface.</p>
<p>The <code>IMiniportWavePciStream</code> interface provides methods for managing a single stream of incoming or outgoing audio wave data. This is the interface that exposes most of the miniport driver's functionality.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IMiniportWavePciStream</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface but does not have additional members.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h</dt>
</dl>
</td>
</tr>
</table>