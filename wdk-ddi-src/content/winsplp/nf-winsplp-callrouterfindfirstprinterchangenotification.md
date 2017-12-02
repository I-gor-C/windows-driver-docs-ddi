---
UID: NF.winsplp.CallRouterFindFirstPrinterChangeNotification
title: CallRouterFindFirstPrinterChangeNotification
author: windows-driver-content
description: .
old-location: print\callrouterfindfirstprinterchangenotification.htm
old-project: print
ms.assetid: 7B974255-2FCB-4EFE-B33F-9856E0A09FC4
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: CallRouterFindFirstPrinterChangeNotification
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
req.alt-api: CallRouterFindFirstPrinterChangeNotification
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

# CallRouterFindFirstPrinterChangeNotification function



## -description
<p></p>


## -syntax

````
DWORD WINAPI CallRouterFindFirstPrinterChangeNotification(
  _In_ HANDLE                  hPrinterRPC,
       DWORD                   fdwFilterFlags,
       DWORD                   fdwOptions,
  _In_ HANDLE                  hNotify,
  _In_ PPRINTER_NOTIFY_OPTIONS pPrinterNotifyOptions
);
````


## -parameters
<dl>

### -param hPrinterRPC [in]

<dd></dd>

### -param fdwFilterFlags 

<dd></dd>

### -param fdwOptions 

<dd></dd>

### -param hNotify [in]

<dd></dd>

### -param pPrinterNotifyOptions [in]

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