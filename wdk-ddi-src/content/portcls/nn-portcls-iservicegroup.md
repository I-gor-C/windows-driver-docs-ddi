---
UID: NN.portcls.IServiceGroup
title: IServiceGroup
author: windows-driver-content
description: The IServiceGroup interface encapsulates a group of objects that all require notification of the same service request.
old-location: audio\iservicegroup.htm
old-project: audio
ms.assetid: eef2741e-e1a3-471b-a756-d89990929738
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
req.alt-api: IServiceGroup
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

# IServiceGroup interface



## -description
<p>The <code>IServiceGroup</code> interface encapsulates a group of objects that all require notification of the same service request. When the service group object receives notification of the request, it forwards the notification to each of the objects in the group. The PortCls system driver implements the <code>IServiceGroup</code> interface and exposes it to miniport drivers. A miniport driver creates an <code>IServiceGroup</code> object by calling <a href="..\portcls\nf-portcls-pcnewservicegroup.md">PcNewServiceGroup</a>. <code>IServiceGroup</code> inherits from the <a href="..\portcls\nn-portcls-iservicesink.md">IServiceSink</a> interface.</p>
<p>Port drivers typically use service group objects to demultiplex requests for interrupt service, although the functionality of a service group is general enough to make it potentially useful for other purposes as well. For more information, see <a href="NULL">Service Sink and Service Group Objects</a>.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IServiceGroup</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IServiceGroup</b> also has these types of members:</p>

<p>The <b>IServiceGroup</b> interface has these methods.</p>

<p>The <code>AddMember</code> method adds a member to the service group.</p>

<p>The <code>CancelDelayedService</code> method cancels the previously requested delayed service.</p>

<p>The <code>RemoveMember</code> method removes the specified member from the service group.</p>

<p>The <code>RequestDelayedService</code> method requests service after the specified delay.</p>

<p>The <code>SupportDelayedService</code> method indicates that the service group should prepare to support delayed service.</p>

<p> </p>

## -members
<p>The <b>IServiceGroup</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iservicegroup_addmember">IServiceGroup::AddMember</a>
</td>
<td align="left" width="63%">
<p>The <code>AddMember</code> method adds a member to the service group.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iservicegroup_canceldelayedservice">IServiceGroup::CancelDelayedService</a>
</td>
<td align="left" width="63%">
<p>The <code>CancelDelayedService</code> method cancels the previously requested delayed service.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iservicegroup_removemember">IServiceGroup::RemoveMember</a>
</td>
<td align="left" width="63%">
<p>The <code>RemoveMember</code> method removes the specified member from the service group.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iservicegroup_requestdelayedservice">IServiceGroup::RequestDelayedService</a>
</td>
<td align="left" width="63%">
<p>The <code>RequestDelayedService</code> method requests service after the specified delay.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iservicegroup_supportdelayedservice">IServiceGroup::SupportDelayedService</a>
</td>
<td align="left" width="63%">
<p>The <code>SupportDelayedService</code> method indicates that the service group should prepare to support delayed service.</p>
</td>
</tr>
</table><p>The <code>AddMember</code> method adds a member to the service group.</p>

<p>The <code>CancelDelayedService</code> method cancels the previously requested delayed service.</p>

<p>The <code>RemoveMember</code> method removes the specified member from the service group.</p>

<p>The <code>RequestDelayedService</code> method requests service after the specified delay.</p>

<p>The <code>SupportDelayedService</code> method indicates that the service group should prepare to support delayed service.</p>

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