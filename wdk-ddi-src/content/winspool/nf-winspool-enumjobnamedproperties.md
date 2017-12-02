---
UID: NF.winspool.EnumJobNamedProperties
title: EnumJobNamedProperties
author: windows-driver-content
description: .
old-location: print\enumjobnamedproperties.htm
old-project: print
ms.assetid: 0C5E2279-79D0-40A2-BA5B-66994A22E963
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: EnumJobNamedProperties
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: winspool.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: EnumJobNamedProperties
req.alt-loc: Winspool.h
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
req.product: Windows 10 or later.
---

# EnumJobNamedProperties function



## -description
<p></p>


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

### -param hPrinter [in]

<dd></dd>

### -param JobId [in]

<dd></dd>

### -param pcProperties [out]

<dd></dd>

### -param ppProperties [out]

<dd></dd>
</dl>

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