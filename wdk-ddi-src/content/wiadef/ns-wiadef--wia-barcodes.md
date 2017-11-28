---
UID: NS.wiadef._WIA_BARCODES
title: WIA_BARCODES
author: windows-driver-content
description: The WIA_BARCODES structure stores header information for the barcode metadata report of one scan job (one call to IWiaMiniDrv::drvAcquireItemData).
old-location: image\wia_barcodes.htm
old-project: image
ms.assetid: 2B89FF49-4376-49A7-B7CC-1C67D89C7E7A
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WIA_BARCODES, WIA_BARCODES
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
req.alt-api: WIA_BARCODES
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

# WIA_BARCODES structure



## -description
<p>The <b>WIA_BARCODES</b> structure stores header information for the barcode metadata report of one scan job (one call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff543956">IWiaMiniDrv::drvAcquireItemData</a>).</p>


## -syntax

````
typedef struct _WIA_BARCODES {
  DWORD            Tag;
  DWORD            Version;
  DWORD            Size;
  DWORD            Count;
  WIA_BARCODE_INFO Barcodes[1];
} WIA_BARCODES;
````


## -struct-fields
<dl>

### -field <b>Tag</b>

<dd>
<p>Must be the literal 'WBAR', 4 single byte ASCII characters. </p>
</dd>

### -field <b>Version</b>

<dd>
<p>Must be the value 0x00010000 (Version 1.0).</p>
</dd>

### -field <b>Size</b>

<dd>
<p>The complete size of this <b>WIA_BARCODES</b> header structure, in bytes, including the complete size of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh706205">WIA_BARCODE_INFO</a> list.</p>
</dd>

### -field <b>Count</b>

<dd>
<p>Specifies the number of <a href="https://msdn.microsoft.com/library/windows/hardware/hh706205">WIA_BARCODE_INFO</a> elements in the Barcodes sequence.</p>
</dd>

### -field <b>Barcodes</b>

<dd>
<p>Placeholder for  a sequence of <b>Count</b> contiguous <a href="https://msdn.microsoft.com/library/windows/hardware/hh706205">WIA_BARCODE_INFO</a> structures.</p>
</dd>
</dl>

## -remarks
<p>The header must be followed by a sequence of barcode information structures, one for each decoded barcode, in the order the barcodes were found and decoded.</p>

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