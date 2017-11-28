---
UID: NF.winsplp.ProvidorFindFirstPrinterChangeNotification
title: ProvidorFindFirstPrinterChangeNotification
author: windows-driver-content
description: .
old-location: print\providorfindfirstprinterchangenotification.htm
old-project: print
ms.assetid: AFDA244D-D692-44C1-8BA3-5E1F013558D6
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: ProvidorFindFirstPrinterChangeNotification
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
req.alt-api: ProvidorFindFirstPrinterChangeNotification
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

# ProvidorFindFirstPrinterChangeNotification function



## -description
<p></p>


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

<dd></dd>

### -param <i>fdwFlags</i> 

<dd></dd>

### -param <i>fdwOptions</i> 

<dd></dd>

### -param <i>hNotify</i> [in]

<dd></dd>

### -param <i>pPrinterNotifyOptions</i> [in, optional]

<dd></dd>

### -param <i>pvReserved1</i> [out, optional]

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