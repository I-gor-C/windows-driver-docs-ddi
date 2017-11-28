---
UID: NS.wiadef._WIA_MICR_INFO
title: WIA_MICR_INFO
author: windows-driver-content
description: The WIA_MICR_INFO structure stores information for one decoded MICR code.
old-location: image\wia_micr_info.htm
old-project: image
ms.assetid: E91F5D6F-40F9-4CE2-8C51-4CA7FB27F2C3
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WIA_MICR_INFO, WIA_MICR_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wiadef.h
req.include-header: Wiadef.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WIA_MICR_INFO
req.alt-loc: wiadef.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section.
req.iface: 
req.product: Windows 10 or later.
---

# WIA_MICR_INFO structure



## -description
<p>The <b>WIA_MICR_INFO</b> structure stores information for one decoded MICR code.</p>


## -syntax

````
typedef struct _WIA_MICR_INFO {
  DWORD Size;
  DWORD Page;
  DWORD Length;
  WCHAR Text[1];
} WIA_MICR_INFO;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The total size of this structure, in bytes.</p>
</dd>

### -field <b>Page</b>

<dd>
<p>The page number where the MICR code was detected. A zero-based index referring to the current scan job.</p>
</dd>

### -field <b>Length</b>

<dd>
<p>Length of the MICR text, in characters, excluding the length of the NULL terminator.</p>
</dd>

### -field <b>Text</b>

<dd>
<p>Placeholder for a NULL terminated character string containing the MICR text.</p>
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
<dt>Wiadef.h (include Wiadef.h)</dt>
</dl>
</td>
</tr>
</table>