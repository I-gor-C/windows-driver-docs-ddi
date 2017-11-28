---
UID: NN.portcls.IPortClsRuntimePower
title: IPortClsRuntimePower
author: windows-driver-content
description: IPortClsRuntimePower is the interface that the port class driver (PortCls) uses for accessing the runtime power management capabilities of the audio adapter.
old-location: audio\iportclsruntimepower.htm
old-project: audio
ms.assetid: 8D03B2A0-6C8C-4EBE-86F4-70C8DE179947
ms.author: windowsdriverdev
ms.date: 11/21/2017
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
req.alt-api: IPortClsRuntimePower
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

# IPortClsRuntimePower interface



## -description
<p>IPortClsRuntimePower is the interface that the port class driver (PortCls)  uses for accessing the runtime power management capabilities of the audio adapter.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPortClsRuntimePower</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IPortClsRuntimePower</b> also has these types of members:</p>

<p>The <b>IPortClsRuntimePower</b> interface has these methods.</p>

<p>The port class driver (PortCls) uses the <code>RegisterPowerControlCallback</code>  method to register a power control callback.</p>

<p>The port class driver (PortCls) uses the <code>SendPowerControl</code>  method to send power control codes to the audio adapter.</p>

<p>The port class driver (PortCls) uses the <code>UnregisterPowerControlCallback</code>  method to unregister a power control callback.</p>

<p> </p>

## -members
<p>The <b>IPortClsRuntimePower</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265126">RegisterPowerControlCallback</a>
</td>
<td align="left" width="63%">
<p>The port class driver (PortCls) uses the <code>RegisterPowerControlCallback</code>  method to register a power control callback.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265127">SendPowerControl</a>
</td>
<td align="left" width="63%">
<p>The port class driver (PortCls) uses the <code>SendPowerControl</code>  method to send power control codes to the audio adapter.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265128">UnregisterPowerControlCallback</a>
</td>
<td align="left" width="63%">
<p>The port class driver (PortCls) uses the <code>UnregisterPowerControlCallback</code>  method to unregister a power control callback.</p>
</td>
</tr>
</table><p>The port class driver (PortCls) uses the <code>RegisterPowerControlCallback</code>  method to register a power control callback.</p>

<p>The port class driver (PortCls) uses the <code>SendPowerControl</code>  method to send power control codes to the audio adapter.</p>

<p>The port class driver (PortCls) uses the <code>UnregisterPowerControlCallback</code>  method to unregister a power control callback.</p>

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