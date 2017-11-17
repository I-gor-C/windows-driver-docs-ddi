---
UID: NF.winsplp.DevQueryPrint
title: DevQueryPrint
author: windows-driver-content
description: TBD.
old-location: print\devqueryprint.htm
ms.assetid: B3135A43-A328-4103-AB75-A37F02322F70
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: winsplp.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DevQueryPrint
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
ms.keywords: DevQueryPrint
req.iface: 
req.product: Windows 10 or later.
---

# DevQueryPrint function



## -description
<p>TBD</p>


## -syntax

````
BOOL WINAPI DevQueryPrint(
  _In_  HANDLE    hPrinter,
  _In_  LPDEVMODE pDevMode,
  _Out_ DWORD     *pResID
);
````


## -parameters
<dl>

### -param <i>hPrinter</i> [in]

<dd>
<p>TBD</p>
</dd>

### -param <i>pDevMode</i> [in]

<dd>
<p>TBD</p>
</dd>

### -param <i>pResID</i> [out]

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
<dt>Winsplp.h</dt>
</dl>
</td>
</tr>
</table>