---
UID: NF.winsplp.CallRouterFindFirstPrinterChangeNotification
title: CallRouterFindFirstPrinterChangeNotification
author: windows-driver-content
description: TBD.
old-location: print\callrouterfindfirstprinterchangenotification.htm
ms.assetid: 7B974255-2FCB-4EFE-B33F-9856E0A09FC4
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
req.alt-api: CallRouterFindFirstPrinterChangeNotification
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
ms.keywords: CallRouterFindFirstPrinterChangeNotification
req.iface: 
req.product: Windows 10 or later.
---

# CallRouterFindFirstPrinterChangeNotification function



## -description
<p>TBD</p>


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

### -param <i>hPrinterRPC</i> [in]

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

### -param <i>hNotify</i> [in]

<dd>
<p>TBD</p>
</dd>

### -param <i>pPrinterNotifyOptions</i> [in]

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