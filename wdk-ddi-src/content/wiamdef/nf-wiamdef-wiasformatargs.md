---
UID: NF.wiamdef.wiasFormatArgs
title: wiasFormatArgs
author: windows-driver-content
description: The wiasFormatArgs function formats an argument list into a packaged string for logging.
old-location: image\wiasformatargs.htm
old-project: image
ms.assetid: 409c4ff6-3a0e-408a-879d-2875ac245fb8
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: wiasFormatArgs
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wiamdef.h
req.include-header: Wiamdef.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows Me and in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: wiasFormatArgs
req.alt-loc: Wiaservc.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wiaservc.lib
req.dll: Wiaservc.dll
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# wiasFormatArgs function



## -description
<p>The <b>wiasFormatArgs</b> function formats an argument list into a packaged string for logging.</p>


## -syntax

````
BSTR __cdecl wiasFormatArgs(
   LPCSTR   lpszFormat, ...
);
````


## -parameters
<dl>

### -param <i>lpszFormat, ...</i> 

<dd>
<p>Specifies a variable argument list, which starts with an ANSI format string containing the message and any format specifiers. The ellipsis (...) specifies a variable number of arguments that follow the format string.</p>
</dd>
</dl>

## -returns
<p>This function returns a BSTR containing the format string, the arguments following the format string, and a format signature.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Microsoft Windows Me and in Windows XP and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wiamdef.h (include Wiamdef.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wiaservc.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Wiaservc.dll</dt>
</dl>
</td>
</tr>
</table>