---
UID: NN.portcls.IPortTopology
title: IPortTopology
author: windows-driver-content
description: The IPortTopology interface provides generic port driver support to a topology miniport driver.
old-location: audio\iporttopology.htm
old-project: audio
ms.assetid: 820b00e8-a917-4bef-ac36-e8103f59d998
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
req.alt-api: IPortTopology
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

# IPortTopology interface



## -description
<p>The <code>IPortTopology</code> interface provides generic port driver support to a topology miniport driver. The PortCls system driver implements this interface and exposes it to the adapter driver that implements the <a href="..\portcls\nn-portcls-iminiporttopology.md">IMiniportTopology</a> object. An adapter driver creates an <code>IPortTopology</code> object by calling <a href="..\portcls\nf-portcls-pcnewport.md">PcNewPort</a> and specifying REFIID <b>IID_IPortTopology</b>. <code>IPortTopology</code> inherits from the <a href="..\portcls\nn-portcls-iport.md">IPort</a> interface.</p>
<p>An adapter driver forms a miniport/port driver pair by binding an <b>IMiniportTopology</b> object to an <code>IPortTopology</code> object. The PortCls system driver registers this pair with the system as a <a href="https://msdn.microsoft.com/1b3d35e9-5858-407c-9cd0-06307d82ce58">topology filter</a>.</p>
<p>The <code>IPortTopology</code> interface supports only the methods that it inherits from the <b>IPort</b> interface.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPortTopology</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface but does not have additional members.</p>

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