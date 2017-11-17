---
UID: NF.smclib.SmartcardSetDebugLevel
title: SmartcardSetDebugLevel
author: windows-driver-content
description: The SmartcardSetDebugLevel routine sets the debug level.
old-location: smartcrd\smartcardsetdebuglevel.htm
ms.assetid: 8b11f35c-71dc-4cc0-a8b0-415f31734263
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: smartcrd
req.header: smclib.h
req.include-header: Smclib.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SmartcardSetDebugLevel
req.alt-loc: Smclib.lib,Smclib.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Smclib.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: SmartcardSetDebugLevel
req.iface: 
req.product: Windows 10 or later.
---

# SmartcardSetDebugLevel function



## -description
<p>The <b>SmartcardSetDebugLevel</b> routine sets the debug level.</p>


## -syntax

````
void SmartcardSetDebugLevel(
   ULONG DebugLevel
);
````


## -parameters
<dl>

### -param <i>DebugLevel</i> 

<dd>
<p>The level of debug information that will be generated after this routine is called. </p>
</dd>
</dl>

## -returns
<p>None </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows XP and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Smclib.h (include Smclib.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Smclib.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>