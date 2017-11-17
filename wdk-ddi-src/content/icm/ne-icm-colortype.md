---
UID: NE.icm.COLORTYPE
title: COLORTYPE
author: windows-driver-content
description: The values of the COLORTYPE enumeration are used by WCS functions to indicate the format of vector content. Most values have equivalent structures that are contained in the ICM COLOR structure (described in the Microsoft Windows SDK documentation).
old-location: print\colortype.htm
ms.assetid: aa7d8d32-7bbe-4091-82a2-32ade463dd9e
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: print
req.header: icm.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Included in Windows Vista and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: COLORTYPE
req.alt-loc: icm.h
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
ms.keywords: HWN_CLIENT_REGISTRATION_PACKET, HWN_CLIENT_REGISTRATION_PACKET, *PHWN_CLIENT_REGISTRATION_PACKET
req.iface: 
---

# COLORTYPE enumeration



## -description
<p>The values of the COLORTYPE enumeration are used by WCS functions to indicate the format of vector content. Most values have equivalent structures that are contained in the ICM COLOR structure (described in the Microsoft Windows SDK documentation).</p>


## -syntax

````
typedef enum  { 
  COLOR_GRAY       = 1,
  COLOR_RGB        = 2,
  COLOR_XYZ        = 3,
  COLOR_Yxy        = 4,
  COLOR_Lab        = 5,
  COLOR_3_CHANNEL  = 6,
  COLOR_CMYK       = 7,
  COLOR_5_CHANNEL  = 8,
  COLOR_6_CHANNEL  = 9,
  COLOR_7_CHANNEL  = 10,
  COLOR_8_CHANNEL  = 11,
  COLOR_NAMED      = 12
} COLORTYPE;
````


## -enum-fields
<dl>

### -field <a id="COLOR_GRAY"></a><a id="color_gray"></a><b>COLOR_GRAY</b>

<dd>
<p>Specifies a 16-bit gray-scale pixel value. Correlates to the ICM GRAYCOLOR.</p>
</dd>

### -field <a id="COLOR_RGB"></a><a id="color_rgb"></a><b>COLOR_RGB</b>

<dd>
<p>Specifies a 48-bit RGB pixel value. Correlates to the ICM RGBCOLOR structure.</p>
</dd>

### -field <a id="COLOR_XYZ"></a><a id="color_xyz"></a><b>COLOR_XYZ</b>

<dd>
<p>Specifies a 48-bit CIEXYZ pixel value. Correlates to the ICM XYZCOLOR structure.</p>
</dd>

### -field <a id="COLOR_Yxy"></a><a id="color_yxy"></a><a id="COLOR_YXY"></a><b>COLOR_Yxy</b>

<dd>
<p>Specifies a 48-bit CIE Yxy pixel value. Correlates to the ICM YxyCOLOR structure.</p>
</dd>

### -field <a id="COLOR_Lab"></a><a id="color_lab"></a><a id="COLOR_LAB"></a><b>COLOR_Lab</b>

<dd>
<p>Specifies a 48-bit CIELAB pixel value. Correlates to the ICM LabCOLOR structure.</p>
</dd>

### -field <a id="COLOR_3_CHANNEL"></a><a id="color_3_channel"></a><b>COLOR_3_CHANNEL</b>

<dd>
<p>Specifies a 48-bit generic three-channel pixel value. Correlates to the ICM GENERIC3CHANNEL structure.</p>
</dd>

### -field <a id="COLOR_CMYK"></a><a id="color_cmyk"></a><b>COLOR_CMYK</b>

<dd>
<p>Specifies a 48-bit CMYK pixel value. Correlates to the ICM CMYKCOLOR structure.</p>
</dd>

### -field <a id="COLOR_5_CHANNEL"></a><a id="color_5_channel"></a><b>COLOR_5_CHANNEL</b>

<dd>
<p>Specifies a 64-bit generic five-channel pixel value.</p>
</dd>

### -field <a id="COLOR_6_CHANNEL"></a><a id="color_6_channel"></a><b>COLOR_6_CHANNEL</b>

<dd>
<p>Specifies a 64-bit generic six-channel pixel value.</p>
</dd>

### -field <a id="COLOR_7_CHANNEL"></a><a id="color_7_channel"></a><b>COLOR_7_CHANNEL</b>

<dd>
<p>Specifies a 64-bit generic seven-channel pixel value.</p>
</dd>

### -field <a id="COLOR_8_CHANNEL"></a><a id="color_8_channel"></a><b>COLOR_8_CHANNEL</b>

<dd>
<p>Specifies a 64-bit generic eight-channel pixel value.</p>
</dd>

### -field <a id="COLOR_NAMED"></a><a id="color_named"></a><b>COLOR_NAMED</b>

<dd>
<p>Specifies a 32-bit named color-indexed pixel value. Correlates to the ICM NAMEDCOLOR structure.</p>
</dd>
</dl>

## -remarks
<p>In addition to managing the common two, three, and four channel color spaces, ICM 2.0 and WCS are able to perform color management with device profiles that contain five through eight color channels. ICM 2.0 and WCS are also able to use named color spaces. When five, six, seven, or eight color channels are used, the provider of the device profile is free to determine what the color channels represent. The same is true of named color spaces. ICM 2.0 and WCS are able to manage these color spaces as long as there is a mapping in the device profile that maps the channels or the name space to the Profile Connection Space (PCS). The device profile must also contain a mapping from the PCS into the five, six, seven, or eight channel spaces, or into the named color space.</p>

<p>The PCOLORTYPE and LPCOLORTYPE data types are defined as pointers to this enumeration:</p>

<p>In addition to managing the common two, three, and four channel color spaces, ICM 2.0 and WCS are able to perform color management with device profiles that contain five through eight color channels. ICM 2.0 and WCS are also able to use named color spaces. When five, six, seven, or eight color channels are used, the provider of the device profile is free to determine what the color channels represent. The same is true of named color spaces. ICM 2.0 and WCS are able to manage these color spaces as long as there is a mapping in the device profile that maps the channels or the name space to the Profile Connection Space (PCS). The device profile must also contain a mapping from the PCS into the five, six, seven, or eight channel spaces, or into the named color space.</p>

<p>The PCOLORTYPE and LPCOLORTYPE data types are defined as pointers to this enumeration:</p>

<p>In addition to managing the common two, three, and four channel color spaces, ICM 2.0 and WCS are able to perform color management with device profiles that contain five through eight color channels. ICM 2.0 and WCS are also able to use named color spaces. When five, six, seven, or eight color channels are used, the provider of the device profile is free to determine what the color channels represent. The same is true of named color spaces. ICM 2.0 and WCS are able to manage these color spaces as long as there is a mapping in the device profile that maps the channels or the name space to the Profile Connection Space (PCS). The device profile must also contain a mapping from the PCS into the five, six, seven, or eight channel spaces, or into the named color space.</p>

<p>The PCOLORTYPE and LPCOLORTYPE data types are defined as pointers to this enumeration:</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Included in Windows Vista and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Icm.h</dt>
</dl>
</td>
</tr>
</table>