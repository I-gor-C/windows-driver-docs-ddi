---
UID: NN.portcls.IPortWavePciStream
title: IPortWavePciStream
author: windows-driver-content
description: The IPortWavePciStream interface is the stream-associated callback interface that provides mapping services to WavePci miniport stream objects.
old-location: audio\iportwavepcistream.htm
old-project: audio
ms.assetid: c59ea7d7-17f1-4751-a948-387d7568b832
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
req.alt-api: IPortWavePciStream
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

# IPortWavePciStream interface



## -description
<p>The <code>IPortWavePciStream</code> interface is the stream-associated callback interface that provides mapping services to WavePci miniport stream objects. The WavePci port driver implements this interface and exposes it to the miniport driver. The port driver provides a reference to an <code>IPortWavePciStream</code> object to each miniport stream object that it creates. <code>IPortWavePciStream</code> inherits from the <b>IUnknown</b> interface.</p>
<p>The stream is associated with a pin on the WavePci filter, which the adapter driver forms by binding the port and miniport drivers. The port driver calls the <a href="audio.iminiportwavepci_newstream">IMiniportWavePci::NewStream</a> method to create the miniport stream object; the port driver passes an <code>IPortWavePciStream</code> reference as one of the call parameters.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPortWavePciStream</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface but does not have additional members.</p>

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