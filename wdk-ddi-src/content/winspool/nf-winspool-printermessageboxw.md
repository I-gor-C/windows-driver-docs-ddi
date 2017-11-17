---
UID: NF.winspool.PrinterMessageBoxW
title: PrinterMessageBoxW
author: windows-driver-content
description: TBD.
old-location: print\printermessageboxw.htm
ms.assetid: F5E7FB7C-A38F-4DBA-9C98-9554FA80CC07
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: winspool.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PrinterMessageBoxW
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
ms.keywords: PrinterMessageBoxW
req.iface: 
req.product: Windows 10 or later.
---

# PrinterMessageBoxW function



## -description
<p>TBD</p>


## -syntax

````
DWORD WINAPI PrinterMessageBoxW(
  _In_ HANDLE     hPrinter,
       DWORD      Error,
  _In_ HWND       hWnd,
  _In_ LPWSTR     pText,
  _In_ LPWSTR     pCaption,
       DWORD      dwType
);
````


## -parameters
<dl>

### -param <i>hPrinter</i> [in]

<dd>
<p>TBD</p>
</dd>

### -param <i>Error</i> 

<dd>
<p>TBD</p>
</dd>

### -param <i>hWnd</i> [in]

<dd>
<p>TBD</p>
</dd>

### -param <i>pText</i> [in]

<dd>
<p>TBD</p>
</dd>

### -param <i>pCaption</i> [in]

<dd>
<p>TBD</p>
</dd>

### -param <i>dwType</i> 

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
<dt>Winspool.h</dt>
</dl>
</td>
</tr>
</table>