---
UID: NF.winsplp.PlayGdiScriptOnPrinterIC
title: PlayGdiScriptOnPrinterIC
author: windows-driver-content
description: .
old-location: print\playgdiscriptonprinteric.htm
old-project: print
ms.assetid: DB5FCF40-77C2-4741-9E6B-77A9CD98E29A
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: PlayGdiScriptOnPrinterIC
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
req.alt-api: PlayGdiScriptOnPrinterIC
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

# PlayGdiScriptOnPrinterIC function



## -description
<p></p>


## -syntax

````
BOOL WINAPI PlayGdiScriptOnPrinterIC(
  _In_  HANDLE   hPrinterIC,
  _In_  LPBYTE   pIn,
  _In_  DWORD    cIn,
  _Out_ LPBYTE   pOut,
  _In_  DWORD    cOut,
  _In_  DWORD    ul
);
````


## -parameters
<dl>

### -param <i>hPrinterIC</i> [in]

<dd></dd>

### -param <i>pIn</i> [in]

<dd></dd>

### -param <i>cIn</i> [in]

<dd></dd>

### -param <i>pOut</i> [out]

<dd></dd>

### -param <i>cOut</i> [in]

<dd></dd>

### -param <i>ul</i> [in]

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