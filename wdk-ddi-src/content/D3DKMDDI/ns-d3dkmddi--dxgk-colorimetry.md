---
UID: NS.d3dkmddi._DXGK_COLORIMETRY
title: DXGK_COLORIMETRY
author: windows-driver-content
description: Describes colorimetry and closely related fields used to describe overrides from the descriptor retrieved from the display device.
old-location: display\dxgk_colorimetry.htm
ms.assetid: F3F9B6EC-B978-4C87-8AE0-8F6BC73099D2
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_COLORIMETRY
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
ms.keywords: DXGK_COLORIMETRY, DXGK_COLORIMETRY, *PDXGK_COLORIMETRY
req.iface: 
---

# DXGK_COLORIMETRY structure



## -description
<p>Describes colorimetry and closely related fields used to describe overrides from the descriptor retrieved from the display device.</p>


## -syntax

````
typedef struct _DXGK_COLORIMETRY {
  D3DKMDT_2DOFFSET                   RedPoint;
  D3DKMDT_2DOFFSET                   GreenPoint;
  D3DKMDT_2DOFFSET                   BluePoint;
  D3DKMDT_2DOFFSET                   WhitePoint;
  ULONG                              MinLuminance;
  ULONG                              MaxLuminance;
  ULONG                              MaxFullFrameLuminance;
  D3DKMDT_WIRE_FORMAT_AND_PREFERENCE FormatBitDepths;
  DXGK_STANDARD_COLORIMETRY_FLAGS    StandardColorimetryFlags;
} DXGK_COLORIMETRY, *PDXGK_COLORIMETRY;
````


## -struct-fields
<dl>

### -field <b>RedPoint</b>

<dd>
<p>Override for display red point.  Note, each dimension is a 10-bit value stored in the least significant bits.
Zero indicates no override.</p>
</dd>

### -field <b>GreenPoint</b>

<dd>
<p>Override for display green point. Note, each dimension is a 10-bit value stored in the least significant bits.</p>
</dd>

### -field <b>BluePoint</b>

<dd>
<p>Override for display blue point. Note, each dimension is a 10-bit value stored in the least significant bits.</p>
</dd>

### -field <b>WhitePoint</b>

<dd>
<p>Override for display white point. Note, each dimension is a 10-bit value stored in the least significant bits.</p>
</dd>

### -field <b>MinLuminance</b>

<dd>
<p>Override for the minimum luminance value supported by the display measured in one ten thousandth of a nit.  Only valid if MaxLuminance is non-zero.  Zero is a valid value.</p>
</dd>

### -field <b>MaxLuminance</b>

<dd>
<p>Override for the maximum luminance value supported by the display measured in one ten thousandth of a nit.  This luminance level is expected to be supported for only a relatively small area in any given frame.  
Zero indicates no override of MaxLuminance, MaxFullFrameLuminance or MinLuminance.
</p>
</dd>

### -field <b>MaxFullFrameLuminance</b>

<dd>
<p>Override for the max full frame luminance value supported by the display measured in one ten thousandth of a nit.  This luminance level must be supported across every pixel in the frame simultaneously in order to provide an estimate of the average luminance value which can be supported by the display across a frame.
Only valid if MaxLuminance is non-zero.  Zero is not a valid override.
</p>
</dd>

### -field <b>FormatBitDepths</b>

<dd>
<p>Overrides the supported bits per color channel in each of the five color encodings specified for wire-formats.  At least one bit must be set, excluding the Preference field which is reserved and must be zero.</p>
</dd>

### -field <b>StandardColorimetryFlags</b>

<dd>
<p>Indicates support for specific colorimetry and EOTF capabilities using bit-fields.</p>
</dd>
</dl>

## -remarks
<p>This struct is used both for querying overrides from the driver, and for the OS reporting the final set of values it has selected.  Overrides are supported for integrated displays using this structure which is embedded within the DXGK_QUERYINTEGRATEDDISPLAYOUT struct and for external displays where this stuct is used as the output buffer is for an adapter query type DXGKQAITYPE_QUERYCOLORIMETRYOVERRIDES.  The selected and adjusted overrides are reported back to the driver using DxgkDdiSetTargetAdjustedColorimetry.

</p>

<p>When querying overrides, the OS requires that either all fields are filled by the driver or the buffer is left zeroed to avoid the complexity of attempting to merge these inter-related attributes from different sources. If the struct is not completely zeroed, the OS validates that fields which must not be zero as noted above, are not zero.  

</p>

<p>The color points are further validated beyond a simple sanity check (each value must be between 1 and 1023) to ensure reasonable values by comparing the coordinates of each point to the standard points and ensuring that none is too far away from the standard.

</p>

<p>When the OS calls DxgkDdiSetTargetAdjustedColorimetry, the FormatBitDepths and StandardColorimetryFlags are zeroed as these are capability fields so only valid in queries.
</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h</dt>
</dl>
</td>
</tr>
</table>