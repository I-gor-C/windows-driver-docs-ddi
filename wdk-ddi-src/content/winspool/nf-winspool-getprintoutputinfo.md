---
UID: NF.winspool.GetPrintOutputInfo
title: GetPrintOutputInfo
author: windows-driver-content
description: TBD.
old-location: print\getprintoutputinfo.htm
ms.assetid: 0EC09215-48B1-4B71-9B4C-99A25C35269F
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
req.alt-api: GetPrintOutputInfo
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
ms.keywords: GetPrintOutputInfo
req.iface: 
req.product: Windows 10 or later.
---

# GetPrintOutputInfo function



## -description
<p>TBD</p>


## -syntax

````
HRESULT WINAPI GetPrintOutputInfo(
  _In_  HWND    hWnd,
  _In_  PCWSTR  pszPrinter,
  _Out_ HANDLE  *phFile,
  _Out_ PWSTR   *ppszOutputFile
);
````


## -parameters
<dl>

### -param <i>hWnd</i> [in]

<dd>
<p>TBD</p>
</dd>

### -param <i>pszPrinter</i> [in]

<dd>
<p>TBD</p>
</dd>

### -param <i>phFile</i> [out]

<dd>
<p>TBD</p>
</dd>

### -param <i>ppszOutputFile</i> [out]

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