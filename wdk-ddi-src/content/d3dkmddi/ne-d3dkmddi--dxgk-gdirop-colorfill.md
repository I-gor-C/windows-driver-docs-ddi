---
UID: NE.d3dkmddi._DXGK_GDIROP_COLORFILL
title: DXGK_GDIROP_COLORFILL
author: windows-driver-content
description: The DXGK_GDIROP_COLORFILL enumeration indicates the type of GDI raster operation (ROP) to implement in a GDI hardware-accelerated color fill operation.
old-location: display\dxgk_gdirop_colorfill.htm
old-project: display
ms.assetid: 1ef99bb0-855a-46d1-9702-5fc3eba5e68e
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_GDIROP_COLORFILL
req.alt-loc: d3dkmddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# DXGK_GDIROP_COLORFILL enumeration



## -description
<p>The DXGK_GDIROP_COLORFILL enumeration indicates the type of GDI raster operation (ROP) to implement in a GDI hardware-accelerated color fill operation.</p>


## -syntax

````
typedef enum _DXGK_GDIROP_COLORFILL { 
  DXGK_GDIROPCF_INVALID    = 0,
  DXGK_GDIROPCF_PATCOPY    = 1,
  DXGK_GDIROPCF_PATINVERT  = 2,
  DXGK_GDIROPCF_PDXN       = 3,
  DXGK_GDIROPCF_DSTINVERT  = 4,
  DXGK_GDIROPCF_PATAND     = 5,
  DXGK_GDIROPCF_PATOR      = 6,
  DXGK_GDIROPCF_ROP3       = 7
} DXGK_GDIROP_COLORFILL;
````


## -enum-fields
<dl>

### -field <a id="DXGK_GDIROPCF_INVALID"></a><a id="dxgk_gdiropcf_invalid"></a><b>DXGK_GDIROPCF_INVALID</b>

<dd>
<p>Indicates that the GDI raster operation is invalid.</p>
</dd>

### -field <a id="DXGK_GDIROPCF_PATCOPY"></a><a id="dxgk_gdiropcf_patcopy"></a><b>DXGK_GDIROPCF_PATCOPY</b>

<dd>
<p>Indicates that the specified color is copied into all pixels of the destination rectangle.</p>
</dd>

### -field <a id="DXGK_GDIROPCF_PATINVERT"></a><a id="dxgk_gdiropcf_patinvert"></a><b>DXGK_GDIROPCF_PATINVERT</b>

<dd>
<p>Indicates that the specified color is combined with the colors of the destination rectangle by using the Boolean <b>XOR</b> operator.</p>
</dd>

### -field <a id="DXGK_GDIROPCF_PDXN"></a><a id="dxgk_gdiropcf_pdxn"></a><b>DXGK_GDIROPCF_PDXN</b>

<dd>
<p>Indicates that the specified color is combined with the colors of the destination rectangle by using the Boolean <b>NOT(XOR)</b> operator.</p>
</dd>

### -field <a id="DXGK_GDIROPCF_DSTINVERT"></a><a id="dxgk_gdiropcf_dstinvert"></a><b>DXGK_GDIROPCF_DSTINVERT</b>

<dd>
<p>Indicates that the destination rectangle is inverted.</p>
</dd>

### -field <a id="DXGK_GDIROPCF_PATAND"></a><a id="dxgk_gdiropcf_patand"></a><b>DXGK_GDIROPCF_PATAND</b>

<dd>
<p>Indicates that the specified color is combined with the colors of the destination rectangle by using the Boolean <b>AND</b> operator.</p>
</dd>

### -field <a id="DXGK_GDIROPCF_PATOR"></a><a id="dxgk_gdiropcf_pator"></a><b>DXGK_GDIROPCF_PATOR</b>

<dd>
<p>Indicates that the colors of the specified pattern are combined with the colors of the destination rectangle by using the Boolean <b>OR</b> operator.</p>
</dd>

### -field <a id="DXGK_GDIROPCF_ROP3"></a><a id="dxgk_gdiropcf_rop3"></a><b>DXGK_GDIROPCF_ROP3</b>

<dd>
<p>Indicates that a ternary GDI raster operation (ROP3) will be applied.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>