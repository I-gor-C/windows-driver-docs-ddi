---
UID: NE.icm.BMFORMAT
title: BMFORMAT
author: windows-driver-content
description: The values of the BMFORMAT enumeration are used by WCS functions to indicate the format that particular bitmaps are in. This data type is extended from BMFORMAT that is available in versions of Windows released before Windows Vista.
old-location: print\bmformat.htm
ms.assetid: 1c29bf1e-e785-48ab-aa2c-3665fd5c0ab0
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
ms.keywords: HWN_CLIENT_REGISTRATION_PACKET, HWN_CLIENT_REGISTRATION_PACKET, *PHWN_CLIENT_REGISTRATION_PACKET
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

### -field <a id="BM_x555RGB"></a><a id="bm_x555rgb"></a><a id="BM_X555RGB"></a><b>BM_x555RGB</b>

<dd>
<p>16 bits per pixel. RGB color space. 5 bits per channel. The most significant bit is ignored.</p>
</dd>

### -field <a id="BM_x555XYZ"></a><a id="bm_x555xyz"></a><a id="BM_X555XYZ"></a><b>BM_x555XYZ</b>

<dd>
<p>16 bits per pixel. Yxy color space. 5 bits per channel. The most significant bit is ignored.</p>
</dd>

### -field <a id="BM_x555Yxy"></a><a id="bm_x555yxy"></a><a id="BM_X555YXY"></a><b>BM_x555Yxy</b>

<dd>
<p>16 bits per pixel. Yxy color space. 5 bits per channel. The most significant bit is ignored.</p>
</dd>

### -field <a id="BM_x555Lab"></a><a id="bm_x555lab"></a><a id="BM_X555LAB"></a><b>BM_x555Lab</b>

<dd>
<p>BM_x555G3CH</p>
</dd>

### -field <a id="BM_x555G3CH"></a><a id="bm_x555g3ch"></a><a id="BM_X555G3CH"></a><b>BM_x555G3CH</b>

<dd>
<p>16 bits per pixel. G3CH color space. 5 bits per channel. The most significant bit is ignored.</p>
</dd>

### -field <a id="BM_RGBTRIPLETS"></a><a id="bm_rgbtriplets"></a><b>BM_RGBTRIPLETS</b>

<dd>
<p>24 bits per pixel maximum. For three channel colors, such as red, green, and blue, the total size is 24 bits per pixel. For single channel colors, such as gray, the total size is 8 bits per pixel.</p>
</dd>

### -field <a id="BM_BGRTRIPLETS"></a><a id="bm_bgrtriplets"></a><b>BM_BGRTRIPLETS</b>

<dd>
<p>24 bits per pixel maximum. For three channel colors, such as red, green, and blue, the total size is 24 bits per pixel. For single channel colors, such as gray, the total size is 8 bits per pixel.</p>
</dd>

### -field <a id="BM_XYZTRIPLETS"></a><a id="bm_xyztriplets"></a><b>BM_XYZTRIPLETS</b>

<dd>
<p>24 bits per pixel maximum. For three channel colors, such as red, green, and blue, the total size is 24 bits per pixel. For single channel colors, such as gray, the total size is 8 bits per pixel.</p>
</dd>

### -field <a id="BM_YxyTRIPLETS"></a><a id="bm_yxytriplets"></a><a id="BM_YXYTRIPLETS"></a><b>BM_YxyTRIPLETS</b>

<dd>
<p>24 bits per pixel maximum. For three channel, Y, x, and y values, the total size is 24 bits per pixel. For single channel gray scale, the total size is 8 bits per pixel.</p>
</dd>

### -field <a id="BM_LabTRIPLETS"></a><a id="bm_labtriplets"></a><a id="BM_LABTRIPLETS"></a><b>BM_LabTRIPLETS</b>

<dd>
<p>24 bits per pixel maximum. For three channel, L, a, and b values, the total size is 24 bits per pixel. For single channel gray scale, the total size is 8 bits per pixel.</p>
</dd>

### -field <a id="BM_G3CHTRIPLETS"></a><a id="bm_g3chtriplets"></a><b>BM_G3CHTRIPLETS</b>

<dd>
<p>24 bits per pixel maximum. For three channel values, the total size is 24 bits per pixel. For single channel gray scale, the total size is 8 bits per pixel.</p>
</dd>

### -field <a id="BM_5CHANNEL"></a><a id="bm_5channel"></a><b>BM_5CHANNEL</b>

<dd>
<p>40 bits per pixel. 8 bits apiece are used for each channel.</p>
</dd>

### -field <a id="BM_6CHANNEL"></a><a id="bm_6channel"></a><b>BM_6CHANNEL</b>

<dd></dd>

### -field <a id="BM_7CHANNEL"></a><a id="bm_7channel"></a><b>BM_7CHANNEL</b>

<dd>
<p>56 bits per pixel. 8 bits apiece are used for each channel.</p>
</dd>

### -field <a id="BM_8CHANNEL"></a><a id="bm_8channel"></a><b>BM_8CHANNEL</b>

<dd>
<p>64 bits per pixel. 8 bits apiece are used for each channel.</p>
</dd>

### -field <a id="BM_GRAY"></a><a id="bm_gray"></a><b>BM_GRAY</b>

<dd>
<p>32 bits per pixel. Only the 8 bit gray-scale value is used.</p>
</dd>

### -field <a id="BM_xRGBQUADS"></a><a id="bm_xrgbquads"></a><a id="BM_XRGBQUADS"></a><b>BM_xRGBQUADS</b>

<dd>
<p>32 bits per pixel. 8 bits are used for each color channel. The most significant byte is ignored.</p>
</dd>

### -field <a id="BM_xBGRQUADS"></a><a id="bm_xbgrquads"></a><a id="BM_XBGRQUADS"></a><b>BM_xBGRQUADS</b>

<dd>
<p>32 bits per pixel. 8 bits are used for each color channel. The most significant byte is ignored.</p>
</dd>

### -field <a id="BM_xG3CHQUADS"></a><a id="bm_xg3chquads"></a><a id="BM_XG3CHQUADS"></a><b>BM_xG3CHQUADS</b>

<dd>
<p>32 bits per pixel. 8 bits are used for each color channel. The most significant byte is ignored.</p>
</dd>

### -field <a id="BM_KYMCQUADS"></a><a id="bm_kymcquads"></a><b>BM_KYMCQUADS</b>

<dd>
<p>32 bits per pixel. 8 bits are used for each color channel.</p>
</dd>

### -field <a id="BM_CMYKQUADS"></a><a id="bm_cmykquads"></a><b>BM_CMYKQUADS</b>

<dd>
<p>32 bits per pixel. 8 bits are used for each color channel.</p>
</dd>

### -field <a id="BM_10b_RGB"></a><a id="bm_10b_rgb"></a><a id="BM_10B_RGB"></a><b>BM_10b_RGB</b>

<dd>
<p>32 bits per pixel. 10 bits are used for each color channel. The 2 most significant bits are ignored. </p>
</dd>

### -field <a id="BM_10b_XYZ"></a><a id="bm_10b_xyz"></a><a id="BM_10B_XYZ"></a><b>BM_10b_XYZ</b>

<dd>
<p>32 bits per pixel. 10 bits are used for each color channel. The 2 most significant bits are ignored.</p>
</dd>

### -field <a id="BM_10b_Yxy"></a><a id="bm_10b_yxy"></a><a id="BM_10B_YXY"></a><b>BM_10b_Yxy</b>

<dd>
<p>32 bits per pixel. 10 bits are used for each color channel. The 2 most significant bits are ignored.</p>
</dd>

### -field <a id="BM_10b_Lab"></a><a id="bm_10b_lab"></a><a id="BM_10B_LAB"></a><b>BM_10b_Lab</b>

<dd>
<p>32 bits per pixel. 10 bits are used for each color channel. The 2 most significant bits are ignored.</p>
</dd>

### -field <a id="BM_10b_G3CH"></a><a id="bm_10b_g3ch"></a><a id="BM_10B_G3CH"></a><b>BM_10b_G3CH</b>

<dd>
<p>32 bits per pixel. 10 bits are used for each color channel. The 2 most significant bits are ignored.</p>
</dd>

### -field <a id="BM_NAMED_INDEX"></a><a id="bm_named_index"></a><b>BM_NAMED_INDEX</b>

<dd>
<p>32 bits per pixel. Named color indices. Index numbering begins at one. </p>
</dd>

### -field <a id="BM_16b_RGB"></a><a id="bm_16b_rgb"></a><a id="BM_16B_RGB"></a><b>BM_16b_RGB</b>

<dd>
<p>64 bits per pixel. 16 bits are used for the gray-scale value. Each of the three color channels uses 16 bits.</p>
</dd>

### -field <a id="BM_16b_XYZ"></a><a id="bm_16b_xyz"></a><a id="BM_16B_XYZ"></a><b>BM_16b_XYZ</b>

<dd>
<p>64 bits per pixel. 16 bits are used for the gray-scale value. Each of the three color channels uses 16 bits.</p>
</dd>

### -field <a id="BM_16b_Yxy"></a><a id="bm_16b_yxy"></a><a id="BM_16B_YXY"></a><b>BM_16b_Yxy</b>

<dd>
<p>64 bits per pixel. 16 bits are used for the gray-scale value. Each of the three color channels uses 16 bits.</p>
</dd>

### -field <a id="BM_16b_Lab"></a><a id="bm_16b_lab"></a><a id="BM_16B_LAB"></a><b>BM_16b_Lab</b>

<dd>
<p>64 bits per pixel. 16 bits are used for the gray-scale value. Each of the three color channels uses 16 bits.</p>
</dd>

### -field <a id="BM_16b_G3CH"></a><a id="bm_16b_g3ch"></a><a id="BM_16B_G3CH"></a><b>BM_16b_G3CH</b>

<dd>
<p>64 bits per pixel. 16 bits are used for the gray-scale value. Each of the three color channels uses 16 bits.</p>
</dd>

### -field <a id="BM_16b_GRAY"></a><a id="bm_16b_gray"></a><a id="BM_16B_GRAY"></a><b>BM_16b_GRAY</b>

<dd>
<p>64 bits per pixel. 16 bits are used for the gray-scale value. All other bits are ignored.</p>
</dd>

### -field <a id="BM_565RGB"></a><a id="bm_565rgb"></a><b>BM_565RGB</b>

<dd>
<p>16 bits per pixel. 5 bits are used for red, 6 for green, and 5 for blue.</p>
</dd>

### -field <a id="BM_32b_scRGB"></a><a id="bm_32b_scrgb"></a><a id="BM_32B_SCRGB"></a><b>BM_32b_scRGB</b>

<dd>
<p>96 bits per pixel. 32 bits are used for each color channel, as defined by the IEEE 32-bit floating point standard.</p>
</dd>

### -field <a id="BM_32b_scARGB"></a><a id="bm_32b_scargb"></a><a id="BM_32B_SCARGB"></a><b>BM_32b_scARGB</b>

<dd>
<p>128 bits per pixel. 32 bits are used for each color channel, as defined by the IEEE 32-bit floating point standard.</p>
</dd>

### -field <a id="BM_S2DOT13FIXED_scRGB"></a><a id="bm_s2dot13fixed_scrgb"></a><a id="BM_S2DOT13FIXED_SCRGB"></a><b>BM_S2DOT13FIXED_scRGB</b>

<dd>
<p>48 bits per pixel. Color data is stored as one 16-bit word per channel, with a fixed range of -4 to +4, inclusive. A signed format is used, with 1 bit for the sign, 2 bits for the integer portion, and 13 bits for the fractional portion.</p>
</dd>

### -field <a id="BM_S2DOT13FIXED_scARGB"></a><a id="bm_s2dot13fixed_scargb"></a><a id="BM_S2DOT13FIXED_SCARGB"></a><b>BM_S2DOT13FIXED_scARGB</b>

<dd>
<p>64 bits per pixel. Color data is stored as one 16-bit word per channel, with a fixed range of -4 to +4, inclusive. A signed format is used, with 1 bit for the sign, 2 bits for the integer portion, and 13 bits for the fractional portion.</p>
</dd>

### -field <a id="BM_R10G10B10A2"></a><a id="bm_r10g10b10a2"></a><b>BM_R10G10B10A2</b>

<dd></dd>

### -field <a id="BM_R10G10B10A2_XR"></a><a id="bm_r10g10b10a2_xr"></a><b>BM_R10G10B10A2_XR</b>

<dd></dd>

### -field <a id="BM_R16G16B16A16_FLOAT"></a><a id="bm_r16g16b16a16_float"></a><b>BM_R16G16B16A16_FLOAT</b>

<dd>
<p>#endif // NTDDI_VERSION &gt;= NTDDI_WIN7</p>
</dd>
</dl>

## -remarks
<p>The last four values were added to the BMFORMAT enumeration beginning with Windows Vista.</p>

<p>The PBMFORMAT and LPBMFORMAT data types are defined as pointers to this enumeration:</p>

<p>The last four values were added to the BMFORMAT enumeration beginning with Windows Vista.</p>

<p>The PBMFORMAT and LPBMFORMAT data types are defined as pointers to this enumeration:</p>

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