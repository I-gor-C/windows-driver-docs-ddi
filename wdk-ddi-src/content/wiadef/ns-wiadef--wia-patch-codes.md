---
UID: NS.wiadef._WIA_PATCH_CODES
title: WIA_PATCH_CODES
author: windows-driver-content
description: The WIA_PATCH_CODES structure stores header information for the patch code metadata report of one scan job (one call to IWiaMiniDrv::drvAcquireItemData).
old-location: image\wia_patch_codes.htm
old-project: image
ms.assetid: CFD2403B-DDD4-4318-9084-1B3E3462FBDC
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WIA_PATCH_CODES, WIA_PATCH_CODES
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
req.alt-api: WIA_PATCH_CODES
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

# WIA_PATCH_CODES structure



## -description
<p>The <b>WIA_PATCH_CODES</b> structure stores header information for the patch code metadata report of one scan job (one call to <a href="image.iwiaminidrv_drvacquireitemdata">IWiaMiniDrv::drvAcquireItemData</a>).</p>


## -syntax

````
typedef struct _WIA_PATCH_CODES {
  DWORD                Tag;
  DWORD                Version;
  DWORD                Size;
  DWORD                Count;
  WIA_PATCH_CODES_INFO PatchCodes[1];
} WIA_PATCH_CODES;
````


## -struct-fields
<dl>

### -field Tag

<dd>
<p>Must be the literal 'WBAT', 4 single byte ASCII characters. </p>
</dd>

### -field Version

<dd>
<p>Must be the value 0x00010000 (Version 1.0).</p>
</dd>

### -field Size

<dd>
<p>The complete size of this <b>WIA_PATCH_CODES</b> header structure, in bytes, including the complete size of the <a href="..\wiadef\ns-wiadef--wia-patch-code-info.md">WIA_PATCH_CODES_INFO</a> list.</p>
</dd>

### -field Count

<dd>
<p>Specifies the number of <a href="..\wiadef\ns-wiadef--wia-patch-code-info.md">WIA_PATCH_CODES_INFO</a> elements in the PatchCodes sequence.</p>
</dd>

### -field PatchCodes

<dd>
<p>Placeholder for a sequence of <b>Count</b> contiguous <a href="..\wiadef\ns-wiadef--wia-patch-code-info.md">WIA_PATCH_CODES_INFO</a> structures.</p>
</dd>
</dl>

## -remarks
<p>The header must be followed by a sequence of patch code information structures, one for each detected patch code, in the order the patch codes were found and decoded.</p>

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