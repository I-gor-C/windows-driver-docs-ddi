---
UID: NN.portcls.IMiniportWaveRTStream
title: IMiniportWaveRTStream
author: windows-driver-content
description: The IMiniportWaveRTStream interface represents the wave stream that flows through a pin on the KS filter that wraps a WaveRT rendering or capture device.
old-location: audio\iminiportwavertstream.htm
old-project: audio
ms.assetid: be398a37-0329-411b-ba41-a03dbc5f72a1
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
req.alt-api: IMiniportWaveRTStream
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

# IMiniportWaveRTStream interface



## -description
<p>The <code>IMiniportWaveRTStream</code> interface represents the wave stream that flows through a pin on the KS filter that wraps a WaveRT rendering or capture device. The miniport driver implements the <code>IMiniportWaveRTStream</code> interface and exposes it to the port driver. The miniport driver creates a stream object with this interface when the port driver calls the <a href="audio.iminiportwavert_newstream">IMiniportWaveRT::NewStream</a> method. <code>IMiniportWaveRTStream</code> inherits from the <b>IUnknown</b> interface.</p>
<p><code>IMiniportWaveRTStream</code> is supported in Windows Vista and later Windows operating systems.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IMiniportWaveRTStream</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface but does not have additional members.</p>

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