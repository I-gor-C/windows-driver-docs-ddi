---
UID: NN.dmusicks.IMiniportDMus
title: IMiniportDMus
author: windows-driver-content
description: The IMiniportDMus interface is the primary interface for a DMus miniport driver for a DirectMusic synthesizer device.
old-location: audio\iminiportdmus.htm
old-project: audio
ms.assetid: 12cd3533-1830-46cd-a1eb-350f7461a61d
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ISynthSinkDMus, SyncToMaster, ISynthSinkDMus::SyncToMaster
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: dmusicks.h
req.include-header: Dmusicks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IMiniportDMus
req.alt-loc: dmusicks.h
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
req.iface: ISynthSinkDMus
---

# IMiniportDMus interface



## -description
<p>The <code>IMiniportDMus</code> interface is the primary interface for a DMus miniport driver for a DirectMusic synthesizer device. The DMus port driver communicates with the miniport driver through this interface. The adapter driver creates the DMus miniport object and passes the object's <code>IMiniportDMus</code> interface pointer to the port driver's <a href="audio.iport_init">IPort::Init</a> method (see the code example in <a href="NULL">Subdevice Creation</a>). <code>IMiniportDMus</code> inherits from the <a href="..\portcls\nn-portcls-iminiport.md">IMiniport</a> interface.</p>
<p>An adapter driver forms a miniport/port driver pair by binding an <code>IMiniportDMus</code> object to an <a href="..\dmusicks\nn-dmusicks-iportdmus.md">IPortDMus</a> object. The PortCls system driver registers this pair with the system as a DirectMusic filter (see <a href="NULL">MIDI and DirectMusic Filters</a>).</p>
<p>The <code>IMiniportDMus</code> interface provides methods for initializing the miniport driver, for creating a new DirectMusic stream, and for notifying the miniport driver of an interrupt service request.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IMiniportDMus</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IMiniportDMus</b> also has these types of members:</p>

<p>The <b>IMiniportDMus</b> interface has these methods.</p>

<p>The <code>Init</code> method initializes the DMus miniport object.</p>

<p>The <code>NewStream</code> method creates a new instance of a logical stream associated with a specified physical channel.</p>

<p>
   This method does not currently need to be implemented in the miniport driver. The<code> Service</code> method is currently unused.</p>

<p> </p>

## -members
<p>The <b>IMiniportDMus</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iminiportdmus_init">IMiniportDMus::Init</a>
</td>
<td align="left" width="63%">
<p>The <code>Init</code> method initializes the DMus miniport object.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iminiportdmus_newstream">IMiniportDMus::NewStream</a>
</td>
<td align="left" width="63%">
<p>The <code>NewStream</code> method creates a new instance of a logical stream associated with a specified physical channel.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iminiportdmus_service">IMiniportDMus::Service</a>
</td>
<td align="left" width="63%">
<p>
   This method does not currently need to be implemented in the miniport driver. The<code> Service</code> method is currently unused.</p>
</td>
</tr>
</table><p>The <code>Init</code> method initializes the DMus miniport object.</p>

<p>The <code>NewStream</code> method creates a new instance of a logical stream associated with a specified physical channel.</p>

<p>
   This method does not currently need to be implemented in the miniport driver. The<code> Service</code> method is currently unused.</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dmusicks.h (include Dmusicks.h)</dt>
</dl>
</td>
</tr>
</table>