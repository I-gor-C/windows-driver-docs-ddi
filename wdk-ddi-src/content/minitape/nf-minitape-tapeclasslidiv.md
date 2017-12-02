---
UID: NF.minitape.TapeClassLiDiv
title: TapeClassLiDiv
author: windows-driver-content
description: The TapeClassLiDiv routine performs a division of the two indicated integers.
old-location: storage\tapeclasslidiv.htm
old-project: storage
ms.assetid: 13c449c6-6e2b-434e-8948-62c8af237173
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: TapeClassLiDiv
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: minitape.h
req.include-header: Minitape.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TapeClassLiDiv
req.alt-loc: Tape.lib,Tape.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Tape.lib
req.dll: 
req.irql: 
req.iface: 
---

# TapeClassLiDiv function



## -description
<p>The <b>TapeClassLiDiv</b> routine performs a division of the two indicated integers. </p>


## -syntax

````
LARGE_INTEGER TapeClassLiDiv(
  _In_ LARGE_INTEGER Dividend,
  _In_ LARGE_INTEGER Divisor
);
````


## -parameters
<dl>

### -param Dividend [in]

<dd>
<p>Contains the dividend.</p>
</dd>

### -param Divisor [in]

<dd>
<p>Contains the divisor.</p>
</dd>
</dl>

## -returns
<p><b>TapeClassLiDiv</b> returns the result of the division. </p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Minitape.h (include Minitape.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Tape.lib</dt>
</dl>
</td>
</tr>
</table>