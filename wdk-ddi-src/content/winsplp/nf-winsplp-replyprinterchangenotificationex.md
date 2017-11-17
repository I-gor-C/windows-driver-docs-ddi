---
UID: NF.winsplp.ReplyPrinterChangeNotificationEx
title: ReplyPrinterChangeNotificationEx
author: windows-driver-content
description: TBD.
old-location: print\replyprinterchangenotificationex.htm
ms.assetid: A3A906C0-FA96-4008-B904-1DA333B59833
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
req.alt-api: ReplyPrinterChangeNotificationEx
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
ms.keywords: ReplyPrinterChangeNotificationEx
req.iface: 
req.product: Windows 10 or later.
---

# ReplyPrinterChangeNotificationEx function



## -description
<p>TBD</p>


## -syntax

````
 WINAPI ReplyPrinterChangeNotificationEx(
  _In_  HANDLE    hNotify,
        DWORD     dwColor,
        DWORD     fdwFlags,
  _Out_ PDWORD    pdwResult,
  _In_  PVOID     pPrinterNotifyInfo
);
````


## -parameters
<dl>

### -param <i>hNotify</i> [in]

<dd>
<p>TBD</p>
</dd>

### -param <i>dwColor</i> 

<dd>
<p>TBD</p>
</dd>

### -param <i>fdwFlags</i> 

<dd>
<p>TBD</p>
</dd>

### -param <i>pdwResult</i> [out]

<dd>
<p>TBD</p>
</dd>

### -param <i>pPrinterNotifyInfo</i> [in]

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