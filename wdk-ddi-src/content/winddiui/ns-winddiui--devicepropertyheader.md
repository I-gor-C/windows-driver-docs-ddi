---
UID: NS.winddiui._DEVICEPROPERTYHEADER
title: DEVICEPROPERTYHEADER
author: windows-driver-content
description: The DEVICEPROPERTYHEADER structure is used as an input parameter to a printer interface DLL's DrvDevicePropertySheets function.
old-location: print\devicepropertyheader.htm
old-project: print
ms.assetid: f1b9cd2f-fa5b-4f34-a237-06d00badf1d1
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: DEVICEPROPERTYHEADER, DEVICEPROPERTYHEADER, *PDEVICEPROPERTYHEADER
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
req.alt-api: DEVICEPROPERTYHEADER
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

# DEVICEPROPERTYHEADER structure



## -description
<p>The DEVICEPROPERTYHEADER structure is used as an input parameter to a printer interface DLL's <a href="https://msdn.microsoft.com/library/windows/hardware/ff548542">DrvDevicePropertySheets</a> function.</p>


## -syntax

````
typedef struct _DEVICEPROPERTYHEADER {
  WORD   cbSize;
  WORD   Flags;
  HANDLE hPrinter;
  LPTSTR pszPrinterName;
} DEVICEPROPERTYHEADER, *PDEVICEPROPERTYHEADER;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd>
<p>Size, in bytes, of the DEVICEPROPERTYHEADER structure.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Is a set of flags that can be set to the following value: </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>DPS_NOPERMISSION</p>
</td>
<td>
<p>If set, the user is not permitted to update device settings.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>hPrinter</b>

<dd>
<p>Printer handle.</p>
</dd>

### -field <b>pszPrinterName</b>

<dd>
<p>Pointer to a NULL-terminated string representing a printer name.</p>
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