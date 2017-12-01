---
UID: NN.portcls.IMiniport
title: IMiniport
author: windows-driver-content
description: The IMiniport interface is the generic miniport interface that all miniport objects support. IMiniport inherits from the IUnknown interface.
old-location: audio\iminiport.htm
old-project: audio
ms.assetid: 981a3560-473a-40b2-a1dc-4ab9dc618e67
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
req.alt-api: IMiniport
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

# IMiniport interface



## -description
<p>The <code>IMiniport</code> interface is the generic miniport interface that all miniport objects support. <code>IMiniport</code> inherits from the <b>IUnknown</b> interface.</p>
<p><code>IMiniport</code> is the base interface for the following miniport interfaces:</p>
<p>
<a href="..\dmusicks\nn-dmusicks-iminiportdmus.md">IMiniportDMus</a>
</p>
<p>
<a href="..\portcls\nn-portcls-iminiportmidi.md">IMiniportMidi</a>
</p>
<p>
<a href="..\portcls\nn-portcls-iminiporttopology.md">IMiniportTopology</a>
</p>
<p>
<a href="..\portcls\nn-portcls-iminiportwavecyclic.md">IMiniportWaveCyclic</a>
</p>
<p>
<a href="..\portcls\nn-portcls-iminiportwavepci.md">IMiniportWavePci</a>
</p>
<p>
<a href="..\portcls\nn-portcls-iminiportwavert.md">IMiniportWaveRT</a>
</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IMiniport</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface but does not have additional members.</p>

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