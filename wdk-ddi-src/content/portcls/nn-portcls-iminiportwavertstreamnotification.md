---
UID: NN.portcls.IMiniportWaveRTStreamNotification
title: IMiniportWaveRTStreamNotification
author: windows-driver-content
description: The IMiniportWaveRTStreamNotification interface is supported in Windows Vista and later Windows operating systems, and it augments the IMiniportWaveRTStream interface, providing additional methods to facilitate DMA driver event notifications.
old-location: audio\iminiportwavertstreamnotification.htm
old-project: audio
ms.assetid: e009c459-77f7-43ee-9e95-8408324b0a9b
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
req.alt-api: IMiniportWaveRTStreamNotification
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

# IMiniportWaveRTStreamNotification interface



## -description
<p>The <code>IMiniportWaveRTStreamNotification</code> interface is supported in Windows Vista and later Windows operating systems, and it augments the <a href="..\portcls\nn-portcls-iminiportwavertstream.md">IMiniportWaveRTStream</a> interface, providing additional methods to facilitate DMA driver event notifications. </p>
<p>To access the <code>IMiniportWaveRTStreamNotification</code> interface, the <a href="NULL">WaveRT port driver</a> calls the <a href="audio.iminiportwavert_newstream">IMiniportWaveRT::NewStream</a> method and receives an <a href="..\portcls\nn-portcls-iminiportwavertstream.md">IMiniportWaveRTStream</a> interface. The WaveRT port driver then queries the <b>IMiniportWaveRTStream</b> interface, uisng QueryInterface, and receives the <code>IMiniportWaveRTStreamNotification</code> interface. </p>
<p><code>IMiniportWaveRTStreamNotification</code> inherits from the <b>IUnknown</b> interface.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IMiniportWaveRTStreamNotification</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface but does not have additional members.</p>

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