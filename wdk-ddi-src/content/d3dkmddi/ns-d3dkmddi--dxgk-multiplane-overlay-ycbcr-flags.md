---
UID: NS.d3dkmddi._DXGK_MULTIPLANE_OVERLAY_YCbCr_FLAGS
title: DXGK_MULTIPLANE_OVERLAY_YCbCr_FLAGS
author: windows-driver-content
description: Identifies YUV range and conversion info that describes a multiplane overlay.
old-location: display\dxgk_multiplane_overlay_ycbcr_flags.htm
old-project: display
ms.assetid: c3a463b1-fc6f-4834-87e5-1d694f2823f9
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MULTIPLANE_OVERLAY_YCbCr_FLAGS, DXGK_MULTIPLANE_OVERLAY_YCbCr_FLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_MULTIPLANE_OVERLAY_YCbCr_FLAGS
req.alt-loc: D3dkmddi.h
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

# DXGK_MULTIPLANE_OVERLAY_YCbCr_FLAGS structure



## -description
<p>Identifies YUV range and conversion info that describes a multiplane overlay.</p>


## -syntax

````
typedef struct _DXGK_MULTIPLANE_OVERLAY_YCbCr_FLAGS {
  union {
    struct {
      UINT NominalRange  :1;
      UINT Bt709  :1;
      UINT xvYCC  :1;
      UINT Reserved  :29;
    };
    UINT   Value;
  };
} DXGK_MULTIPLANE_OVERLAY_YCbCr_FLAGS;
````


## -struct-fields
<dl>

### -field <b>NominalRange</b>

<dd>
<p>If set, YUV values range from 16 to 235, inclusive, instead of the default range of 0 to 255, inclusive.</p>
<p>Setting this member is equivalent to setting the first bit of the 32-bit <b>Value</b> member (0x00000001).</p>
</dd>

### -field <b>Bt709</b>

<dd>
<p>If set, YUV values should be converted using the BT.709 standard, instead of the default BT.601 conversion.</p>
<p>Setting this member is equivalent to setting the second bit of the 32-bit <b>Value</b> member (0x00000002).</p>
</dd>

### -field <b>xvYCC</b>

<dd>
<p>If set, YUV values contain xvYCC data, instead of conventional YCbCr data.</p>
<p>Setting this member is equivalent to setting the third bit of the 32-bit <b>Value</b> member (0x00000004).</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
<p>Setting this member to zero is equivalent to setting the remaining 29 bits (0xFFFFFFF8) of the 32-bit <b>Value</b> member to zeros.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>A 32-bit value that identifies the type of blend operation to perform.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
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