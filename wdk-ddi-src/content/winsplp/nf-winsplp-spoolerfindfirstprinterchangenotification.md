---
UID: NF.winsplp.SpoolerFindFirstPrinterChangeNotification
title: SpoolerFindFirstPrinterChangeNotification
author: windows-driver-content
description: .
old-location: print\spoolerfindfirstprinterchangenotification.htm
old-project: print
ms.assetid: 429A5DF5-46A6-4A41-A77B-4D5743C841DC
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: SpoolerFindFirstPrinterChangeNotification
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
req.alt-api: SpoolerFindFirstPrinterChangeNotification
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

# SpoolerFindFirstPrinterChangeNotification function



## -description
<p></p>


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

### -param hPrinter [in]

<dd></dd>

### -param fdwFilterFlags 

<dd></dd>

### -param fdwOptions 

<dd></dd>

### -param pPrinterNotifyOptions [in]

<dd></dd>

### -param pvReserved [in, optional]

<dd></dd>

### -param pNotificationConfig [in]

<dd></dd>

### -param phNotify [out, optional]

<dd></dd>

### -param phEvent [out, optional]

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