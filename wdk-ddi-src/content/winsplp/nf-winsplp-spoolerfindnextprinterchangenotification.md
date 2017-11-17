---
UID: NF.winsplp.SpoolerFindNextPrinterChangeNotification
title: SpoolerFindNextPrinterChangeNotification
author: windows-driver-content
description: TBD.
old-location: print\spoolerfindnextprinterchangenotification.htm
ms.assetid: FE69BD53-F463-480A-820B-4259D6F48BD0
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
req.alt-api: SpoolerFindNextPrinterChangeNotification
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
ms.keywords: SpoolerFindNextPrinterChangeNotification
req.iface: 
req.product: Windows 10 or later.
---

# SpoolerFindNextPrinterChangeNotification function



## -description
<p>TBD</p>


## -syntax

````
BOOL WINAPI SpoolerFindNextPrinterChangeNotification(
  _In_        HANDLE     hPrinter,
  _Out_       LPDWORD    pfdwChange,
  _In_opt_    LPVOID     pPrinterNotifyOptions,
  _Inout_opt_ LPVOID     *ppPrinterNotifyInfo
);
````


## -parameters
<dl>

### -param <i>hPrinter</i> [in]

<dd>
<p>TBD</p>
</dd>

### -param <i>pfdwChange</i> [out]

<dd>
<p>TBD</p>
</dd>

### -param <i>pPrinterNotifyOptions</i> [in, optional]

<dd>
<p>TBD</p>
</dd>

### -param <i>ppPrinterNotifyInfo</i> [in, out, optional]

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