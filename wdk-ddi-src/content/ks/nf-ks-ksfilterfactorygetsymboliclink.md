---
UID: NF.ks.KsFilterFactoryGetSymbolicLink
title: KsFilterFactoryGetSymbolicLink
author: windows-driver-content
description: The KsFilterFactoryGetSymbolicLink function returns the symbolic link associated with a given filter factory.
old-location: stream\ksfilterfactorygetsymboliclink.htm
old-project: stream
ms.assetid: db657820-75b7-49fe-904d-05f8bc45b8c5
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsFilterFactoryGetSymbolicLink
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsFilterFactoryGetSymbolicLink
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# KsFilterFactoryGetSymbolicLink function



## -description
<p>The<b> KsFilterFactoryGetSymbolicLink</b> function returns the symbolic link associated with a given filter factory.</p>


## -syntax

````
PUNICODE_STRING KsFilterFactoryGetSymbolicLink(
  _In_ PKSFILTERFACTORY FilterFactory
);
````


## -parameters
<dl>

### -param FilterFactory [in]

<dd>
<p>A pointer to a <a href="..\ks\ns-ks--ksfilterfactory.md">KSFILTERFACTORY</a> structure for which to acquire the symbolic link.</p>
</dd>
</dl>

## -returns
<p><b>KsFilterFactoryGetSymbolicLink</b> returns a pointer to a Unicode string containing the <a href="wdkgloss.s#wdkgloss.symbolic_link#wdkgloss.symbolic_link"><i>symbolic link</i></a> for the filter factory if the call is successful, and <b>NULL</b> if unsuccessful. <b>NULL</b> indicates that no device interfaces have been registered for <i>FilterFactory</i>.</p>

## -remarks
<p>If <i>FilterFactory</i> has no registered device interfaces, <b>KsFilterFactoryGetSymbolicLink</b> returns <b>NULL</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>