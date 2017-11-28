---
UID: NN.dsound.IKsPropertySet~r2
title: IKsPropertySet
author: windows-driver-content
description: The IKsPropertySet interface provides methods that access properties of KS objects that are implemented in a KS minidriver.
old-location: stream\ikspropertyset.htm
old-project: stream
ms.assetid: 9999d6ec-977c-4425-ad38-0c5478272c76
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IKsPropertySet, Set, IKsPropertySet::Set
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: dsound.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IKsPropertySet
req.alt-loc: dsound.h
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
req.iface: IKsPropertySet
---

# IKsPropertySet interface



## -description
<p>The <b>IKsPropertySet</b> interface provides methods that access properties of KS objects that are implemented in a KS minidriver.</p>
<p>The IID for this interface is IID_IKsPropertySet.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IKsPropertySet</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IKsPropertySet</b> also has these types of members:</p>

<p>The <b>IKsPropertySet</b> interface has these methods.</p>

<p>Retrieves a property.</p>

<p>Determines the support of a property.</p>

<p>Sets a property.</p>

<p> </p>

<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IKsPropertySet</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IKsPropertySet</b> also has these types of members:</p>

<p>The <b>IKsPropertySet</b> interface has these methods.</p>

<p>Retrieves a property.</p>

<p>Determines the support of a property.</p>

<p>Sets a property.</p>

<p> </p>

<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IKsPropertySet</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IKsPropertySet</b> also has these types of members:</p>

<p>The <b>IKsPropertySet</b> interface has these methods.</p>

<p>Retrieves a property.</p>

<p>Determines the support of a property.</p>

<p>Sets a property.</p>

<p> </p>

## -members
<p>The <b>IKsPropertySet</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/jj983411">Get</a>
</td>
<td align="left" width="63%">
<p>Retrieves a property.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="stream.ikspropertyset_querysupported">QuerySupported</a>
</td>
<td align="left" width="63%">
<p>Determines the support of a property.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544503">Set</a>
</td>
<td align="left" width="63%">
<p>Sets a property.</p>
</td>
</tr>
</table><p>Retrieves a property.</p>

<p>Determines the support of a property.</p>

<p>Sets a property.</p>

<p> </p>

## -remarks
<p>The <b>IKsPropertySet</b> interface methods translate user-mode property requests into kernel-mode property sets that are used by KS minidrivers. </p>

<p>KS objects include, for example, KS filters, KS pins, and KS clocks. </p>

<p>The <b>IKsPropertySet</b> interface methods translate user-mode property requests into kernel-mode property sets that are used by KS minidrivers. </p>

<p>KS objects include, for example, KS filters, KS pins, and KS clocks. </p>

<p>The <b>IKsPropertySet</b> interface methods translate user-mode property requests into kernel-mode property sets that are used by KS minidrivers. </p>

<p>KS objects include, for example, KS filters, KS pins, and KS clocks. </p>

<p>The <b>IKsPropertySet</b> interface methods translate user-mode property requests into kernel-mode property sets that are used by KS minidrivers. </p>

<p>KS objects include, for example, KS filters, KS pins, and KS clocks. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dsound.h</dt>
</dl>
</td>
</tr>
</table>