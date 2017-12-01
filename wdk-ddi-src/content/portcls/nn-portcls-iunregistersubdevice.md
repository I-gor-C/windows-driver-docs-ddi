---
UID: NN.portcls.IUnregisterSubdevice
title: IUnregisterSubdevice
author: windows-driver-content
description: The IUnregisterSubdevice interface implements a method to remove a registered subdevice.
old-location: audio\iunregistersubdevice.htm
old-project: audio
ms.assetid: 023b0a03-a572-459b-a1eb-b25fcde6ecc5
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
req.alt-api: IUnregisterSubdevice
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

# IUnregisterSubdevice interface



## -description
<p>The <code>IUnregisterSubdevice</code> interface implements a method to remove a registered subdevice. The port driver implements this interface. To determine whether a port driver supports the <code>IUnregisterSubdevice</code> interface, a miniport driver calls the port driver object's <b>QueryInterface</b> method with REFIID <b>IID_IUnregisterSubdevice</b>. The miniport driver is responsible for releasing the <code>IUnregisterSubdevice</code> object after it is no longer needed. The <code>IUnregisterSubdevice</code> interface inherits from <b>IUnknown</b>.</p>
<p>The following port drivers support the <code>IUnregisterSubdevice</code> interface:</p>
<p>WaveCyclic</p>
<p>WavePci</p>
<p>Topology</p>
<p>DMus</p>
<p>MIDI</p>
<p>The single method in this interface unregisters a subdevice that was previously registered by a call to the <a href="..\portcls\nf-portcls-pcregistersubdevice.md">PcRegisterSubdevice</a> routine. PortCls supports <b>PcRegisterSubdevice</b>.</p>
<p>The <code>IUnregisterSubdevice</code> object maintains its own internal reference to the subdevice to ensure that the corresponding device object is not deleted until all references to the <code>IUnregisterSubdevice</code> object are released.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IUnregisterSubdevice</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IUnregisterSubdevice</b> also has these types of members:</p>

<p>The <b>IUnregisterSubdevice</b> interface has these methods.</p>

<p>The <b>UnregisterSubdevice</b> method deletes the registration of a subdevice that was previously registered by a call to <a href="..\portcls\nf-portcls-pcregistersubdevice.md">PcRegisterSubdevice</a>.</p>

<p> </p>

## -members
<p>The <b>IUnregisterSubdevice</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iunregistersubdevice_unregistersubdevice">IUnregisterSubdevice::UnregisterSubdevice</a>
</td>
<td align="left" width="63%">
<p>The <b>UnregisterSubdevice</b> method deletes the registration of a subdevice that was previously registered by a call to <a href="..\portcls\nf-portcls-pcregistersubdevice.md">PcRegisterSubdevice</a>.</p>
</td>
</tr>
</table><p>The <b>UnregisterSubdevice</b> method deletes the registration of a subdevice that was previously registered by a call to <a href="..\portcls\nf-portcls-pcregistersubdevice.md">PcRegisterSubdevice</a>.</p>

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