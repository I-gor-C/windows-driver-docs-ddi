---
UID: NF.winsplp.ProvidorFindFirstPrinterChangeNotification
title: ProvidorFindFirstPrinterChangeNotification
author: windows-driver-content
description: TBD.
old-location: print\providorfindfirstprinterchangenotification.htm
ms.assetid: AFDA244D-D692-44C1-8BA3-5E1F013558D6
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
req.alt-api: ProvidorFindFirstPrinterChangeNotification
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
ms.keywords: ProvidorFindFirstPrinterChangeNotification
req.iface: 
req.product: Windows 10 or later.
---

# ProvidorFindFirstPrinterChangeNotification function



## -description
<p>TBD</p>


## -syntax

````
BOOL WINAPI ProvidorFindFirstPrinterChangeNotification(
  _In_      HANDLE                   hPrinter,
            DWORD                    fdwFlags,
            DWORD                    fdwOptions,
  _In_      HANDLE                   hNotify,
  _In_opt_  PVOID                    pPrinterNotifyOptions,
  _Out_opt_ PVOID                    pvReserved1
);
````


## -parameters
<dl>

### -param <i>hPrinter</i> [in]

<dd>
<p>TBD</p>
</dd>

### -param <i>fdwFlags</i> 

<dd>
<p>TBD</p>
</dd>

### -param <i>fdwOptions</i> 

<dd>
<p>TBD</p>
</dd>

### -param <i>hNotify</i> [in]

<dd>
<p>TBD</p>
</dd>

### -param <i>pPrinterNotifyOptions</i> [in, optional]

<dd>
<p>TBD</p>
</dd>

### -param <i>pvReserved1</i> [out, optional]

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