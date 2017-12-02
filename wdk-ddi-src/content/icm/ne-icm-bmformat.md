---
UID: NE.icm.BMFORMAT
title: BMFORMAT
author: windows-driver-content
description: The values of the BMFORMAT enumeration are used by WCS functions to indicate the format that particular bitmaps are in. This data type is extended from BMFORMAT that is available in versions of Windows released before Windows Vista.
old-location: print\bmformat.htm
old-project: print
ms.assetid: 1c29bf1e-e785-48ab-aa2c-3665fd5c0ab0
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: HWN_CLIENT_REGISTRATION_PACKET, HWN_CLIENT_REGISTRATION_PACKET, *PHWN_CLIENT_REGISTRATION_PACKET
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: icm.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Included in Windows Vista and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BMFORMAT
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
req.iface: 
---

# BMFORMAT enumeration



## -description
<p>The values of the BMFORMAT enumeration are used by WCS functions to indicate the format that particular bitmaps are in. This data type is extended from BMFORMAT that is available in versions of Windows released before Windows Vista.</p>


## -syntax

````
typedef enum  { 
  BM_x555RGB              = 0x0000,
  BM_x555XYZ              = 0x0101,
  BM_x555Yxy              = 0x102,
  BM_x555Lab              = 0x103,
  BM_x555G3CH             = 0x104,
  BM_RGBTRIPLETS          = 0x0002,
  BM_BGRTRIPLETS          = 0x0004,
  BM_XYZTRIPLETS          = 0x0201,
  BM_YxyTRIPLETS          = 0x202,
  BM_LabTRIPLETS          = 0x203,
  BM_G3CHTRIPLETS         = 0x204,
  BM_5CHANNEL             = 0x205,
  BM_6CHANNEL             = 0x206,
  BM_7CHANNEL             = 0x207,
  BM_8CHANNEL             = 0x208,
  BM_GRAY                 = 0x209,
  BM_xRGBQUADS            = 0x0008,
  BM_xBGRQUADS            = 0x0010,
  BM_xG3CHQUADS           = 0x0304,
  BM_KYMCQUADS            = 0x305,
  BM_CMYKQUADS            = 0x0020,
  BM_10b_RGB              = 0x0009,
  BM_10b_XYZ              = 0x0401,
  BM_10b_Yxy              = 0x402,
  BM_10b_Lab              = 0x403,
  BM_10b_G3CH             = 0x404,
  BM_NAMED_INDEX          = 0x405,
  BM_16b_RGB              = 0x000A,
  BM_16b_XYZ              = 0x0501,
  BM_16b_Yxy              = 0x502,
  BM_16b_Lab              = 0x503,
  BM_16b_G3CH             = 0x504,
  BM_16b_GRAY             = 0x505,
  BM_565RGB               = 0x0001,
  BM_32b_scRGB            = 0x0601,
  BM_32b_scARGB           = 0x0602,
  BM_S2DOT13FIXED_scRGB   = 0x0603,
  BM_S2DOT13FIXED_scARGB  = 0x0604,
  BM_R10G10B10A2          = 0x0701,
  BM_R10G10B10A2_XR       = 0x0702,
  BM_R16G16B16A16_FLOAT   = 0x0703 
} BMFORMAT;
````


## -enum-fields
<dl>

### -field BM_x555RGB

<dd>
<p>16 bits per pixel. RGB color space. 5 bits per channel. The most significant bit is ignored.</p>
</dd>

### -field BM_x555XYZ

<dd>
<p>16 bits per pixel. Yxy color space. 5 bits per channel. The most significant bit is ignored.</p>
</dd>

### -field BM_x555Yxy

<dd>
<p>16 bits per pixel. Yxy color space. 5 bits per channel. The most significant bit is ignored.</p>
</dd>

### -field BM_x555Lab

<dd>
<p>BM_x555G3CH</p>
</dd>

### -field BM_x555G3CH

<dd>
<p>16 bits per pixel. G3CH color space. 5 bits per channel. The most significant bit is ignored.</p>
</dd>

### -field BM_RGBTRIPLETS

<dd>
<p>24 bits per pixel maximum. For three channel colors, such as red, green, and blue, the total size is 24 bits per pixel. For single channel colors, such as gray, the total size is 8 bits per pixel.</p>
</dd>

### -field BM_BGRTRIPLETS

<dd>
<p>24 bits per pixel maximum. For three channel colors, such as red, green, and blue, the total size is 24 bits per pixel. For single channel colors, such as gray, the total size is 8 bits per pixel.</p>
</dd>

### -field BM_XYZTRIPLETS

<dd>
<p>24 bits per pixel maximum. For three channel colors, such as red, green, and blue, the total size is 24 bits per pixel. For single channel colors, such as gray, the total size is 8 bits per pixel.</p>
</dd>

### -field BM_YxyTRIPLETS

<dd>
<p>24 bits per pixel maximum. For three channel, Y, x, and y values, the total size is 24 bits per pixel. For single channel gray scale, the total size is 8 bits per pixel.</p>
</dd>

### -field BM_LabTRIPLETS

<dd>
<p>24 bits per pixel maximum. For three channel, L, a, and b values, the total size is 24 bits per pixel. For single channel gray scale, the total size is 8 bits per pixel.</p>
</dd>

### -field BM_G3CHTRIPLETS

<dd>
<p>24 bits per pixel maximum. For three channel values, the total size is 24 bits per pixel. For single channel gray scale, the total size is 8 bits per pixel.</p>
</dd>

### -field BM_5CHANNEL

<dd>
<p>40 bits per pixel. 8 bits apiece are used for each channel.</p>
</dd>

### -field BM_6CHANNEL

<dd></dd>

### -field BM_7CHANNEL

<dd>
<p>56 bits per pixel. 8 bits apiece are used for each channel.</p>
</dd>

### -field BM_8CHANNEL

<dd>
<p>64 bits per pixel. 8 bits apiece are used for each channel.</p>
</dd>

### -field BM_GRAY

<dd>
<p>32 bits per pixel. Only the 8 bit gray-scale value is used.</p>
</dd>

### -field BM_xRGBQUADS

<dd>
<p>32 bits per pixel. 8 bits are used for each color channel. The most significant byte is ignored.</p>
</dd>

### -field BM_xBGRQUADS

<dd>
<p>32 bits per pixel. 8 bits are used for each color channel. The most significant byte is ignored.</p>
</dd>

### -field BM_xG3CHQUADS

<dd>
<p>32 bits per pixel. 8 bits are used for each color channel. The most significant byte is ignored.</p>
</dd>

### -field BM_KYMCQUADS

<dd>
<p>32 bits per pixel. 8 bits are used for each color channel.</p>
</dd>

### -field BM_CMYKQUADS

<dd>
<p>32 bits per pixel. 8 bits are used for each color channel.</p>
</dd>

### -field BM_10b_RGB

<dd>
<p>32 bits per pixel. 10 bits are used for each color channel. The 2 most significant bits are ignored. </p>
</dd>

### -field BM_10b_XYZ

<dd>
<p>32 bits per pixel. 10 bits are used for each color channel. The 2 most significant bits are ignored.</p>
</dd>

### -field BM_10b_Yxy

<dd>
<p>32 bits per pixel. 10 bits are used for each color channel. The 2 most significant bits are ignored.</p>
</dd>

### -field BM_10b_Lab

<dd>
<p>32 bits per pixel. 10 bits are used for each color channel. The 2 most significant bits are ignored.</p>
</dd>

### -field BM_10b_G3CH

<dd>
<p>32 bits per pixel. 10 bits are used for each color channel. The 2 most significant bits are ignored.</p>
</dd>

### -field BM_NAMED_INDEX

<dd>
<p>32 bits per pixel. Named color indices. Index numbering begins at one. </p>
</dd>

### -field BM_16b_RGB

<dd>
<p>64 bits per pixel. 16 bits are used for the gray-scale value. Each of the three color channels uses 16 bits.</p>
</dd>

### -field BM_16b_XYZ

<dd>
<p>64 bits per pixel. 16 bits are used for the gray-scale value. Each of the three color channels uses 16 bits.</p>
</dd>

### -field BM_16b_Yxy

<dd>
<p>64 bits per pixel. 16 bits are used for the gray-scale value. Each of the three color channels uses 16 bits.</p>
</dd>

### -field BM_16b_Lab

<dd>
<p>64 bits per pixel. 16 bits are used for the gray-scale value. Each of the three color channels uses 16 bits.</p>
</dd>

### -field BM_16b_G3CH

<dd>
<p>64 bits per pixel. 16 bits are used for the gray-scale value. Each of the three color channels uses 16 bits.</p>
</dd>

### -field BM_16b_GRAY

<dd>
<p>64 bits per pixel. 16 bits are used for the gray-scale value. All other bits are ignored.</p>
</dd>

### -field BM_565RGB

<dd>
<p>16 bits per pixel. 5 bits are used for red, 6 for green, and 5 for blue.</p>
</dd>

### -field BM_32b_scRGB

<dd>
<p>96 bits per pixel. 32 bits are used for each color channel, as defined by the IEEE 32-bit floating point standard.</p>
</dd>

### -field BM_32b_scARGB

<dd>
<p>128 bits per pixel. 32 bits are used for each color channel, as defined by the IEEE 32-bit floating point standard.</p>
</dd>

### -field BM_S2DOT13FIXED_scRGB

<dd>
<p>48 bits per pixel. Color data is stored as one 16-bit word per channel, with a fixed range of -4 to +4, inclusive. A signed format is used, with 1 bit for the sign, 2 bits for the integer portion, and 13 bits for the fractional portion.</p>
</dd>

### -field BM_S2DOT13FIXED_scARGB

<dd>
<p>64 bits per pixel. Color data is stored as one 16-bit word per channel, with a fixed range of -4 to +4, inclusive. A signed format is used, with 1 bit for the sign, 2 bits for the integer portion, and 13 bits for the fractional portion.</p>
</dd>

### -field BM_R10G10B10A2

<dd></dd>

### -field BM_R10G10B10A2_XR

<dd></dd>

### -field BM_R16G16B16A16_FLOAT

<dd>
<p>#endif // NTDDI_VERSION &gt;= NTDDI_WIN7</p>
</dd>
</dl>

## -remarks
<p>The last four values were added to the BMFORMAT enumeration beginning with Windows Vista.</p>

<p>The PBMFORMAT and LPBMFORMAT data types are defined as pointers to this enumeration:</p>

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