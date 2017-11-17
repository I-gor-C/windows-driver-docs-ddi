---
UID: NF.winspool.PrinterMessageBoxA
title: PrinterMessageBoxA
author: windows-driver-content
description: TBD.
old-location: print\printermessageboxa.htm
ms.assetid: 6C238FF8-1EBC-4E3B-9184-D82F5A39DA2F
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
req.alt-api: PrinterMessageBoxA
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
ms.keywords: PrinterMessageBoxA
req.iface: 
req.product: Windows 10 or later.
---

# PrinterMessageBoxA function



## -description
<p>TBD</p>


## -syntax

````
DWORD WINAPI PrinterMessageBoxA(
  _In_ HANDLE         hPrinter,
       DWORD          Error,
  _In_ HWND           hWnd,
  _In_ LPSTR          pText,
  _In_ LPSTR          pCaption,
       DWORD          dwType
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