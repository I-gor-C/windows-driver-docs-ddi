---
UID: NF.winsplp.SpoolerFindNextPrinterChangeNotification
title: SpoolerFindNextPrinterChangeNotification
author: windows-driver-content
description: .
old-location: print\spoolerfindnextprinterchangenotification.htm
old-project: print
ms.assetid: FE69BD53-F463-480A-820B-4259D6F48BD0
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: SpoolerFindNextPrinterChangeNotification
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
req.alt-api: SpoolerFindNextPrinterChangeNotification
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

# SpoolerFindNextPrinterChangeNotification function



## -description
<p></p>


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

<dd></dd>

### -param <i>pfdwChange</i> [out]

<dd></dd>

### -param <i>pPrinterNotifyOptions</i> [in, optional]

<dd></dd>

### -param <i>ppPrinterNotifyInfo</i> [in, out, optional]

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