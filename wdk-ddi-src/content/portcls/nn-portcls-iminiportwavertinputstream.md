---
UID: NN.portcls.IMiniportWaveRTInputStream
title: IMiniportWaveRTInputStream
author: windows-driver-content
description: The IMiniportWaveRTInputStream interface represents the input wave stream that flows through a pin on the KS filter that wraps a WaveRT rendering or capture device. IMiniportWaveRTInputStream inherits from the IUnknown interface.
old-location: audio\iminiportwavertinputstream.htm
old-project: audio
ms.assetid: BF490F9C-C1CD-4AEE-A970-161C5BB3A523
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
req.alt-api: IMiniportWaveRTInputStream
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

# IMiniportWaveRTInputStream interface



## -description
<p>The <code>IMiniportWaveRTInputStream</code> interface represents the input wave stream that flows through a pin on the KS filter that wraps a WaveRT rendering or capture device. <code>IMiniportWaveRTInputStream</code> inherits from the <b>IUnknown</b> interface.</p>
<p>A driver can implement this interface for better coordination of audio dataflow from the driver to OS. If this interface is available on a capture stream, the OS uses methods on this interface to access data in the WaveRt buffer. 
     <code>IMiniportWaveRTInputStream</code> is supported in Windows 10 and later.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IMiniportWaveRTInputStream</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface but does not have additional members.</p>

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