---
UID: NF.winspool.PrinterMessageBoxW
title: PrinterMessageBoxW
author: windows-driver-content
description: .
old-location: print\printermessageboxw.htm
old-project: print
ms.assetid: F5E7FB7C-A38F-4DBA-9C98-9554FA80CC07
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: PrinterMessageBoxW
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
req.alt-api: PrinterMessageBoxW
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

# PrinterMessageBoxW function



## -description
<p></p>


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

### -param hPrinter [in]

<dd></dd>

### -param Error 

<dd></dd>

### -param hWnd [in]

<dd></dd>

### -param pText [in]

<dd></dd>

### -param pCaption [in]

<dd></dd>

### -param dwType 

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