---
UID: NS.winddiui._DEVQUERYPRINT_INFO
title: DEVQUERYPRINT_INFO
author: windows-driver-content
description: The DEVQUERYPRINT_INFO structure is used as an input parameter to a printer interface DLL's DevQueryPrintEx function.
old-location: print\devqueryprint_info.htm
old-project: print
ms.assetid: c46193f2-4c69-4aed-a063-2225faba9ee1
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: DEVQUERYPRINT_INFO, DEVQUERYPRINT_INFO, *PDEVQUERYPRINT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: winddiui.h
req.include-header: Winddiui.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEVQUERYPRINT_INFO
req.alt-loc: winddiui.h
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

# DEVQUERYPRINT_INFO structure



## -description
<p>The DEVQUERYPRINT_INFO structure is used as an input parameter to a printer interface DLL's <a href="https://msdn.microsoft.com/library/windows/hardware/ff547576">DevQueryPrintEx</a> function.</p>


## -syntax

````
typedef struct _DEVQUERYPRINT_INFO {
  WORD    cbSize;
  WORD    Level;
  HANDLE  hPrinter;
  DEVMODE *pDevMode;
  LPWSTR  pszErrorStr;
  DWORD   cchErrorStr;
  DWORD   cchNeeded;
} DEVQUERYPRINT_INFO, *PDEVQUERYPRINT_INFO;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd>
<p>Spooler-supplied size, in bytes, of the DEVQUERYPRINT_INFO structure.</p>
</dd>

### -field <b>Level</b>

<dd>
<p>Spooler-supplied level of the DEVQUERYPRINT_INFO structure. Currently, this member is always set to 1.</p>
</dd>

### -field <b>hPrinter</b>

<dd>
<p>Spooler-supplied printer handle.</p>
</dd>

### -field <b>pDevMode</b>

<dd>
<p>Spooler-supplied pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure describing printer characteristics required by the print job.</p>
</dd>

### -field <b>pszErrorStr</b>

<dd>
<p>Spooler-supplied pointer to a buffer to receive a NULL-terminated error text string, if the print job cannot be printed.</p>
</dd>

### -field <b>cchErrorStr</b>

<dd>
<p>Spooler-supplied size, in bytes, of the string buffer pointed to by <b>pszErrorStr</b>.</p>
</dd>

### -field <b>cchNeeded</b>

<dd>
<p>Driver-supplied length, in bytes, of the error string supplied in the buffer pointed to by <b>pszErrorStr</b>. If the string is too large to fit in the buffer, the string should be truncated, but the untruncated length should be specified here.</p>
</dd>
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
<dt>Winddiui.h (include Winddiui.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547576">DevQueryPrintEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20DEVQUERYPRINT_INFO structure%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
