---
UID: NN.portcls.IPowerNotify
title: IPowerNotify
author: windows-driver-content
description: The IPowerNotify interface is an optional interface that miniport drivers can expose if they require advance notification of impending power-state changes.
old-location: audio\ipowernotify.htm
old-project: audio
ms.assetid: f4856f40-b462-4e69-9324-a2cc837b2893
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
req.alt-api: IPowerNotify
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

# IPowerNotify interface



## -description
<p>The <code>IPowerNotify</code> interface is an optional interface that miniport drivers can expose if they require advance notification of impending power-state changes. To determine whether the miniport driver supports the <code>IPowerNotify</code> interface, the port driver calls the miniport driver object's <b>QueryInterface</b> method with REFIID <b>IID_IPowerNotify</b>. The following miniport driver types can support <code>IPowerNotify</code>:</p>
<p>
<a href="..\portcls\nn-portcls-iminiportwavepci.md">IMiniportWavePci</a>
</p>
<p>
<a href="..\portcls\nn-portcls-iminiportwavecyclic.md">IMiniportWaveCyclic</a>
</p>
<p>
<a href="..\portcls\nn-portcls-iminiportmidi.md">IMiniportMidi</a>
</p>
<p>
<a href="..\dmusicks\nn-dmusicks-iminiportdmus.md">IMiniportDMus</a>
</p>
<p>
<a href="..\portcls\nn-portcls-iminiporttopology.md">IMiniportTopology</a>
</p>
<p><code>IPowerNotify</code> inherits from the <b>IUnknown</b> interface.</p>
<p>The <code>IPowerNotify</code> interface provides a single method that the port driver calls to notify the miniport driver when a change in power state occurs.</p>
<p>For example, when the operating system tells a wave audio device to go to a sleep state, the port driver pauses any active streams and then calls the power-notification callback to inform the miniport driver of the impending power down. The miniport driver then has an opportunity to save any necessary context before the adapter's <b>PowerChangeState</b> method is called.</p>
<p>The process is reversed when the device is powering up. PortCls first calls the adapter's <b>PowerChangeState</b> method to power up the adapter. The port driver then calls the miniport driver's callback to allow the miniport driver to restore its context. Finally, the port driver unpauses any previously paused active audio streams.</p>
<p>For more information, see <a href="NULL">Implementing IPowerNotify</a>.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPowerNotify</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IPowerNotify</b> also has these types of members:</p>

<p>The <b>IPowerNotify</b> interface has these methods.</p>

<p>The <code>PowerChangeNotify</code> method notifies the miniport driver of changes in the power state.</p>

<p> </p>

## -members
<p>The <b>IPowerNotify</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.ipowernotify_powerchangenotify">IPowerNotify::PowerChangeNotify</a>
</td>
<td align="left" width="63%">
<p>The <code>PowerChangeNotify</code> method notifies the miniport driver of changes in the power state.</p>
</td>
</tr>
</table><p>The <code>PowerChangeNotify</code> method notifies the miniport driver of changes in the power state.</p>

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
<dt>Portcls.h</dt>
</dl>
</td>
</tr>
</table>