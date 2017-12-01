---
UID: NN.ksproxy.IKsObject
title: IKsObject
author: windows-driver-content
description: The IKsObject interface provides a method to retrieve the file handle of a KS object.
old-location: stream\iksobject.htm
old-project: stream
ms.assetid: c4422564-3fc0-4087-b628-056488c723e6
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
req.alt-api: IKsObject
req.alt-loc: ksproxy.h,ksproxy.h.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ksproxy.h
req.dll: 
req.irql: 
req.iface: 
---

# IKsObject interface



## -description
<p>The <b>IKsObject</b> interface provides a method to retrieve the file handle of a KS object. </p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IKsObject</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IKsObject</b> also has these types of members:</p>

<p>The <b>IKsObject</b> interface has these methods.</p>

<p>Retrieves the file handle of a KS object.</p>

<p> </p>

<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IKsObject</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IKsObject</b> also has these types of members:</p>

<p>The <b>IKsObject</b> interface has these methods.</p>

<p>Retrieves the file handle of a KS object.</p>

<p> </p>

<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IKsObject</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IKsObject</b> also has these types of members:</p>

<p>The <b>IKsObject</b> interface has these methods.</p>

<p>Retrieves the file handle of a KS object.</p>

<p> </p>

## -members
<p>The <b>IKsObject</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="stream.iksobject_ksgetobjecthandle">KsGetObjectHandle</a>
</td>
<td align="left" width="63%">
<p>Retrieves the file handle of a KS object.</p>
</td>
</tr>
</table><p>Retrieves the file handle of a KS object.</p>

<p> </p>

## -remarks
<p>The IID for this interface is IID_IKsObject.</p>

<p><b>IKsObject</b> is defined in <i>Ksproxy.h</i> within the #ifdef __STREAMS__ section.</p>

<p>__STREAMS__ is defined in <i>Stream.h</i>, a header from the DirectX SDK.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ksproxy.h</dt>
</dl>
</td>
</tr>
</table>