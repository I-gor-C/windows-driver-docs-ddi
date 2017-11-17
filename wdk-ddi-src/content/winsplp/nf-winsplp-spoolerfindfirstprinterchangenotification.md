---
UID: NF.winsplp.SpoolerFindFirstPrinterChangeNotification
title: SpoolerFindFirstPrinterChangeNotification
author: windows-driver-content
description: TBD.
old-location: print\spoolerfindfirstprinterchangenotification.htm
ms.assetid: 429A5DF5-46A6-4A41-A77B-4D5743C841DC
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
req.alt-api: SpoolerFindFirstPrinterChangeNotification
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
ms.keywords: SpoolerFindFirstPrinterChangeNotification
req.iface: 
req.product: Windows 10 or later.
---

# SpoolerFindFirstPrinterChangeNotification function



## -description
<p>TBD</p>


## -syntax

````
BOOL WINAPI SpoolerFindFirstPrinterChangeNotification(
  _In_      HANDLE                   hPrinter,
            DWORD                    fdwFilterFlags,
            DWORD                    fdwOptions,
  _In_      PVOID                    pPrinterNotifyOptions,
  _In_opt_  PVOID                    pvReserved,
  _In_      PVOID                    pNotificationConfig,
  _Out_opt_ PHANDLE                  phNotify,
  _Out_opt_ PHANDLE                  phEvent
);
````


## -parameters
<dl>

### -param <i>hPrinter</i> [in]

<dd>
<p>TBD</p>
</dd>

### -param <i>fdwFilterFlags</i> 

<dd>
<p>TBD</p>
</dd>

### -param <i>fdwOptions</i> 

<dd>
<p>TBD</p>
</dd>

### -param <i>pPrinterNotifyOptions</i> [in]

<dd>
<p>TBD</p>
</dd>

### -param <i>pvReserved</i> [in, optional]

<dd>
<p>TBD</p>
</dd>

### -param <i>pNotificationConfig</i> [in]

<dd>
<p>TBD</p>
</dd>

### -param <i>phNotify</i> [out, optional]

<dd>
<p>TBD</p>
</dd>

### -param <i>phEvent</i> [out, optional]

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