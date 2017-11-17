---
UID: NF.winsplp.SpoolerRefreshPrinterChangeNotification
title: SpoolerRefreshPrinterChangeNotification
author: windows-driver-content
description: TBD.
old-location: print\spoolerrefreshprinterchangenotification.htm
ms.assetid: 86D8D605-3620-4F43-B4A5-6AF568265E92
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
req.alt-api: SpoolerRefreshPrinterChangeNotification
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
ms.keywords: SpoolerRefreshPrinterChangeNotification
req.iface: 
req.product: Windows 10 or later.
---

# SpoolerRefreshPrinterChangeNotification function



## -description
<p>TBD</p>


## -syntax

````
BOOL WINAPI SpoolerRefreshPrinterChangeNotification(
  _In_        HANDLE                    hPrinter,
  _In_        DWORD                     dwColor,
  _In_        PPRINTER_NOTIFY_OPTIONS   pOptions,
  _Inout_opt_ PPRINTER_NOTIFY_INFO      ppInfo
);
````


## -parameters
<dl>

### -param <i>hPrinter</i> [in]

<dd>
<p>TBD</p>
</dd>

### -param <i>dwColor</i> [in]

<dd>
<p>TBD</p>
</dd>

### -param <i>pOptions</i> [in]

<dd>
<p>TBD</p>
</dd>

### -param <i>ppInfo</i> [in, out, optional]

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