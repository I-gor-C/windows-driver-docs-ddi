---
UID: NF.winspool.EnumJobNamedProperties
title: EnumJobNamedProperties
author: windows-driver-content
description: TBD.
old-location: print\enumjobnamedproperties.htm
ms.assetid: 0C5E2279-79D0-40A2-BA5B-66994A22E963
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: winspool.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: EnumJobNamedProperties
req.alt-loc: 
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
ms.keywords: EnumJobNamedProperties
req.iface: 
req.product: Windows 10 or later.
---

# EnumJobNamedProperties function



## -description
<p>TBD</p>


## -syntax

````
DWORD WINAPI EnumJobNamedProperties(
  _In_  HANDLE              hPrinter,
  _In_  DWORD               JobId,
  _Out_ DWORD               *pcProperties,
  _Out_ PrintNamedProperty  **ppProperties
);
````


## -parameters
<dl>

### -param <i>hPrinter</i> [in]

<dd>
<p>TBD</p>
</dd>

### -param <i>JobId</i> [in]

<dd>
<p>TBD</p>
</dd>

### -param <i>pcProperties</i> [out]

<dd>
<p>TBD</p>
</dd>

### -param <i>ppProperties</i> [out]

<dd>
<p>TBD</p>
</dd>
</dl>

## -returns
<p>TBD</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Winspool.h</dt>
</dl>
</td>
</tr>
</table>