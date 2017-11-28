---
UID: NF.winspool.SetJobNamedProperty
title: SetJobNamedProperty
author: windows-driver-content
description: .
old-location: print\setjobnamedproperty.htm
old-project: print
ms.assetid: 6A03B009-21D4-4CD2-9BB5-36F402118270
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: SetJobNamedProperty
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
req.alt-api: SetJobNamedProperty
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

# SetJobNamedProperty function



## -description
<p></p>


## -syntax

````
DWORD WINAPI SetJobNamedProperty(
  _In_       HANDLE                    hPrinter,
  _In_       DWORD                     JobId,
  _In_ const PrintNamedProperty        *pProperty
);
````


## -parameters
<dl>

### -param <i>hPrinter</i> [in]

<dd></dd>

### -param <i>JobId</i> [in]

<dd>
<p>TD</p>
</dd>

### -param <i>pProperty</i> [in]

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