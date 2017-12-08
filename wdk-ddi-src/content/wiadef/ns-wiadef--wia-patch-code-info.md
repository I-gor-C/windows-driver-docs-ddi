---
UID: NS.wiadef._WIA_PATCH_CODE_INFO
title: WIA_PATCH_CODE_INFO
author: windows-driver-content
description: The WIA_PATCH_CODE_INFO structure stores information for one decoded patch code.
old-location: image\wia_patch_code_info.htm
old-project: image
ms.assetid: 476C9269-7A88-4D06-80E8-C80E5F29B6CF
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WIA_PATCH_CODE_INFO, WIA_PATCH_CODE_INFO
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
req.alt-api: WIA_PATCH_CODE_INFO
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

# WIA_PATCH_CODE_INFO structure



## -description
<p>The <b>WIA_PATCH_CODE_INFO</b> structure stores information for one decoded patch code.</p>


## -syntax

````
typedef struct _WIA_PATCH_CODE_INFO {
  DWORD Type;
  DWORD Page;
} WIA_PATCH_CODE_INFO;
````


## -struct-fields
<dl>

### -field Type

<dd>
<p>The patch code type. One of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh706269">WIA_IPS_SUPPORTED_PATCH_CODE_TYPES</a> values.</p>
</dd>

### -field Page

<dd>
<p>The page number where the patch code was detected. A zero-based index referring to the current scan job.</p>
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