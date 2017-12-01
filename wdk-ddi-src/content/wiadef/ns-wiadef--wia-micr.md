---
UID: NS.wiadef._WIA_MICR
title: WIA_MICR
author: windows-driver-content
description: The WIA_MICR structure stores header information for the MICR metadata report of one scan job (one call to IWiaMiniDrv::drvAcquireItemData).
old-location: image\wia_micr.htm
old-project: image
ms.assetid: CAD08405-698C-4C3A-A03F-827837199CC8
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WIA_MICR, WIA_MICR
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
req.alt-api: WIA_MICR
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

# WIA_MICR structure



## -description
<p>The <b>WIA_MICR</b> structure stores header information for the MICR metadata report of one scan job (one call to <a href="image.iwiaminidrv_drvacquireitemdata">IWiaMiniDrv::drvAcquireItemData</a>).</p>


## -syntax

````
typedef struct _WIA_MICR {
  DWORD         Tag;
  DWORD         Version;
  DWORD         Size;
  WCHAR         Placeholder;
  DWORD         Count;
  WIA_MICR_INFO Micr[1];
} WIA_MICR;
````


## -struct-fields
<dl>

### -field <b>Tag</b>

<dd>
<p>Must be the literal 'WMIC', 4 single byte ASCII characters. </p>
</dd>

### -field <b>Version</b>

<dd>
<p>Must be the value 0x00010000 (Version 1.0).</p>
</dd>

### -field <b>Size</b>

<dd>
<p>The complete size of this <b>WIA_MICR</b> header structure, in bytes, including the complete size of the <a href="..\wiadef\ns-wiadef--wia-micr-info.md">WIA_MICR_INFO</a> list.</p>
</dd>

### -field <b>Placeholder</b>

<dd>
<p>Placeholder for unrecognized characters.</p>
</dd>

### -field <b>Count</b>

<dd>
<p>Specifies the number of <a href="..\wiadef\ns-wiadef--wia-micr-info.md">WIA_MICR_INFO</a> elements in the <b>Micr</b> sequence.</p>
</dd>

### -field <b>Micr</b>

<dd>
<p>Placeholder for a sequence of <b>Count</b> contiguous <a href="..\wiadef\ns-wiadef--wia-micr-info.md">WIA_MICR_INFO</a> structures.</p>
</dd>
</dl>

## -remarks
<p>The header must be followed by a sequence of MICR information structures, one for each decoded MICR code, in the order the MICR codes were found and decoded.</p>

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