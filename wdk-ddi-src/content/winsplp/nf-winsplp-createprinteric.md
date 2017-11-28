---
UID: NF.winsplp.CreatePrinterIC
title: CreatePrinterIC
author: windows-driver-content
description: .
old-location: print\createprinteric.htm
old-project: print
ms.assetid: 87C99B3A-EF77-4D87-9953-BBE9628D2A3D
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: CreatePrinterIC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: winsplp.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CreatePrinterIC
req.alt-loc: Winsplp.h
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

# CreatePrinterIC function



## -description
<p></p>


## -syntax

````
HANDLE WINAPI CreatePrinterIC(
  _In_     HANDLE     hPrinter,
  _In_opt_ LPDEVMODEW pDevMode
);
````


## -parameters
<dl>

### -param <i>hPrinter</i> [in]

<dd></dd>

### -param <i>pDevMode</i> [in, optional]

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
<dt>Winsplp.h</dt>
</dl>
</td>
</tr>
</table>