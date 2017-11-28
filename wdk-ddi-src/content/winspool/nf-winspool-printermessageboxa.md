---
UID: NF.winspool.PrinterMessageBoxA
title: PrinterMessageBoxA
author: windows-driver-content
description: .
old-location: print\printermessageboxa.htm
old-project: print
ms.assetid: 6C238FF8-1EBC-4E3B-9184-D82F5A39DA2F
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: PrinterMessageBoxA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: winspool.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PrinterMessageBoxA
req.alt-loc: Winspool.h
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

# PrinterMessageBoxA function



## -description
<p></p>


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

<dd></dd>

### -param <i>Error</i> 

<dd></dd>

### -param <i>hWnd</i> [in]

<dd></dd>

### -param <i>pText</i> [in]

<dd></dd>

### -param <i>pCaption</i> [in]

<dd></dd>

### -param <i>dwType</i> 

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
<dt>Winspool.h</dt>
</dl>
</td>
</tr>
</table>