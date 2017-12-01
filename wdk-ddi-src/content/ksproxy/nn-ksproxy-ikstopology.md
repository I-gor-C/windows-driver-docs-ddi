---
UID: NN.ksproxy.IKsTopology
title: IKsTopology
author: windows-driver-content
description: The IKsTopology interface provides a method that opens topology node objects contained within a filter.
old-location: stream\ikstopology.htm
old-project: stream
ms.assetid: 418a415c-b4db-41a1-825e-66704c45e134
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsSynchronousDeviceControl
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: ksproxy.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IKsTopology
req.alt-loc: ksproxy.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# IKsTopology interface



## -description
<p>The <b>IKsTopology</b> interface provides a method that opens topology node objects contained within a filter.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IKsTopology</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IKsTopology</b> also has these types of members:</p>

<p>The <b>IKsTopology</b> interface has these methods.</p>

<p>Requests a KS filter object to open a topology node object.</p>

<p> </p>

<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IKsTopology</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IKsTopology</b> also has these types of members:</p>

<p>The <b>IKsTopology</b> interface has these methods.</p>

<p>Requests a KS filter object to open a topology node object.</p>

<p> </p>

## -members
<p>The <b>IKsTopology</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="stream.ikstopology_createnodeinstance">CreateNodeInstance</a>
</td>
<td align="left" width="63%">
<p>Requests a KS filter object to open a topology node object.</p>
</td>
</tr>
</table><p>Requests a KS filter object to open a topology node object.</p>

<p> </p>

## -remarks
<p>The IID for this interface is IID_IKsTopology.</p>

<p>The <b>IKsTopology</b> interface is supported by filters. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksproxy.h</dt>
</dl>
</td>
</tr>
</table>