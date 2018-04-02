---
UID: NE:icm.BMFORMAT
title: BMFORMAT
author: windows-driver-content
description: The values of the BMFORMAT enumeration are used by WCS functions to indicate the format that particular bitmaps are in. This data type is extended from BMFORMAT that is available in versions of Windows released before Windows Vista.
old-location: print\bmformat.htm
old-project: print
ms.assetid: 1c29bf1e-e785-48ab-aa2c-3665fd5c0ab0
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: "*PBMFORMAT, BMFORMAT, BMFORMAT enumeration [Print Devices], BM_10b_G3CH, BM_10b_Lab, BM_10b_RGB, BM_10b_XYZ, BM_10b_Yxy, BM_16b_G3CH, BM_16b_GRAY, BM_16b_Lab, BM_16b_RGB, BM_16b_XYZ, BM_16b_Yxy, BM_32b_scARGB, BM_32b_scRGB, BM_565RGB, BM_5CHANNEL, BM_6CHANNEL, BM_7CHANNEL, BM_8CHANNEL, BM_BGRTRIPLETS, BM_CMYKQUADS, BM_G3CHTRIPLETS, BM_GRAY, BM_KYMCQUADS, BM_LabTRIPLETS, BM_NAMED_INDEX, BM_R10G10B10A2, BM_R10G10B10A2_XR, BM_R16G16B16A16_FLOAT, BM_RGBTRIPLETS, BM_S2DOT13FIXED_scARGB, BM_S2DOT13FIXED_scRGB, BM_XYZTRIPLETS, BM_YxyTRIPLETS, BM_x555G3CH, BM_x555Lab, BM_x555RGB, BM_x555XYZ, BM_x555Yxy, BM_xBGRQUADS, BM_xG3CHQUADS, BM_xRGBQUADS, colorfnc_44898765-c0de-41ae-8036-b288ab45b3cb.xml, icm/BMFORMAT, icm/BM_10b_G3CH, icm/BM_10b_Lab, icm/BM_10b_RGB, icm/BM_10b_XYZ, icm/BM_10b_Yxy, icm/BM_16b_G3CH, icm/BM_16b_GRAY, icm/BM_16b_Lab, icm/BM_16b_RGB, icm/BM_16b_XYZ, icm/BM_16b_Yxy, icm/BM_32b_scARGB, icm/BM_32b_scRGB, icm/BM_565RGB, icm/BM_5CHANNEL, icm/BM_6CHANNEL, icm/BM_7CHANNEL, icm/BM_8CHANNEL, icm/BM_BGRTRIPLETS, icm/BM_CMYKQUADS, icm/BM_G3CHTRIPLETS, icm/BM_GRAY, icm/BM_KYMCQUADS, icm/BM_LabTRIPLETS, icm/BM_NAMED_INDEX, icm/BM_R10G10B10A2, icm/BM_R10G10B10A2_XR, icm/BM_R16G16B16A16_FLOAT, icm/BM_RGBTRIPLETS, icm/BM_S2DOT13FIXED_scARGB, icm/BM_S2DOT13FIXED_scRGB, icm/BM_XYZTRIPLETS, icm/BM_YxyTRIPLETS, icm/BM_x555G3CH, icm/BM_x555Lab, icm/BM_x555RGB, icm/BM_x555XYZ, icm/BM_x555Yxy, icm/BM_xBGRQUADS, icm/BM_xG3CHQUADS, icm/BM_xRGBQUADS, print.bmformat"
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
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	icm.h
api_name:
-	BMFORMAT
product:
- Windows
targetos: Windows
req.typenames: BMFORMAT
---

# BMFORMAT Enumeration
The values of the BMFORMAT enumeration are used by WCS functions to indicate the format that particular bitmaps are in. This data type is extended from BMFORMAT that is available in versions of Windows released before Windows Vista.

## Syntax
```
typedef enum BMFORMAT {
  BM_x555RGB              ,
  BM_x555XYZ              ,
  BM_x555Yxy              ,
  BM_x555Lab              ,
  BM_x555G3CH             ,
  BM_RGBTRIPLETS          ,
  BM_BGRTRIPLETS          ,
  BM_XYZTRIPLETS          ,
  BM_YxyTRIPLETS          ,
  BM_LabTRIPLETS          ,
  BM_G3CHTRIPLETS         ,
  BM_5CHANNEL             ,
  BM_6CHANNEL             ,
  BM_7CHANNEL             ,
  BM_8CHANNEL             ,
  BM_GRAY                 ,
  BM_xRGBQUADS            ,
  BM_xBGRQUADS            ,
  BM_xG3CHQUADS           ,
  BM_KYMCQUADS            ,
  BM_CMYKQUADS            ,
  BM_10b_RGB              ,
  BM_10b_XYZ              ,
  BM_10b_Yxy              ,
  BM_10b_Lab              ,
  BM_10b_G3CH             ,
  BM_NAMED_INDEX          ,
  BM_16b_RGB              ,
  BM_16b_XYZ              ,
  BM_16b_Yxy              ,
  BM_16b_Lab              ,
  BM_16b_G3CH             ,
  BM_16b_GRAY             ,
  BM_565RGB               ,
  BM_32b_scRGB            ,
  BM_32b_scARGB           ,
  BM_S2DOT13FIXED_scRGB   ,
  BM_S2DOT13FIXED_scARGB  ,
  BM_R10G10B10A2          ,
  BM_R10G10B10A2_XR       ,
  BM_R16G16B16A16_FLOAT
} ;
```

## Constants

<table>
            
                <tr>
                    <td>BM_x555RGB</td>
                    <td>16 bits per pixel. RGB color space. 5 bits per channel. The most significant bit is ignored.</td>
                </tr>
            
                <tr>
                    <td>BM_x555XYZ</td>
                    <td>16 bits per pixel. Yxy color space. 5 bits per channel. The most significant bit is ignored.</td>
                </tr>
            
                <tr>
                    <td>BM_x555Yxy</td>
                    <td>16 bits per pixel. Yxy color space. 5 bits per channel. The most significant bit is ignored.</td>
                </tr>
            
                <tr>
                    <td>BM_x555Lab</td>
                    <td>BM_x555G3CH</td>
                </tr>
            
                <tr>
                    <td>BM_x555G3CH</td>
                    <td>16 bits per pixel. G3CH color space. 5 bits per channel. The most significant bit is ignored.</td>
                </tr>
            
                <tr>
                    <td>BM_RGBTRIPLETS</td>
                    <td>24 bits per pixel maximum. For three channel colors, such as red, green, and blue, the total size is 24 bits per pixel. For single channel colors, such as gray, the total size is 8 bits per pixel.</td>
                </tr>
            
                <tr>
                    <td>BM_BGRTRIPLETS</td>
                    <td>24 bits per pixel maximum. For three channel colors, such as red, green, and blue, the total size is 24 bits per pixel. For single channel colors, such as gray, the total size is 8 bits per pixel.</td>
                </tr>
            
                <tr>
                    <td>BM_XYZTRIPLETS</td>
                    <td>24 bits per pixel maximum. For three channel colors, such as red, green, and blue, the total size is 24 bits per pixel. For single channel colors, such as gray, the total size is 8 bits per pixel.</td>
                </tr>
            
                <tr>
                    <td>BM_YxyTRIPLETS</td>
                    <td>24 bits per pixel maximum. For three channel, Y, x, and y values, the total size is 24 bits per pixel. For single channel gray scale, the total size is 8 bits per pixel.</td>
                </tr>
            
                <tr>
                    <td>BM_LabTRIPLETS</td>
                    <td>24 bits per pixel maximum. For three channel, L, a, and b values, the total size is 24 bits per pixel. For single channel gray scale, the total size is 8 bits per pixel.</td>
                </tr>
            
                <tr>
                    <td>BM_G3CHTRIPLETS</td>
                    <td>24 bits per pixel maximum. For three channel values, the total size is 24 bits per pixel. For single channel gray scale, the total size is 8 bits per pixel.</td>
                </tr>
            
                <tr>
                    <td>BM_5CHANNEL</td>
                    <td>40 bits per pixel. 8 bits apiece are used for each channel.</td>
                </tr>
            
                <tr>
                    <td>BM_6CHANNEL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>BM_7CHANNEL</td>
                    <td>56 bits per pixel. 8 bits apiece are used for each channel.</td>
                </tr>
            
                <tr>
                    <td>BM_8CHANNEL</td>
                    <td>64 bits per pixel. 8 bits apiece are used for each channel.</td>
                </tr>
            
                <tr>
                    <td>BM_GRAY</td>
                    <td>32 bits per pixel. Only the 8 bit gray-scale value is used.</td>
                </tr>
            
                <tr>
                    <td>BM_xRGBQUADS</td>
                    <td>32 bits per pixel. 8 bits are used for each color channel. The most significant byte is ignored.</td>
                </tr>
            
                <tr>
                    <td>BM_xBGRQUADS</td>
                    <td>32 bits per pixel. 8 bits are used for each color channel. The most significant byte is ignored.</td>
                </tr>
            
                <tr>
                    <td>BM_xG3CHQUADS</td>
                    <td>32 bits per pixel. 8 bits are used for each color channel. The most significant byte is ignored.</td>
                </tr>
            
                <tr>
                    <td>BM_KYMCQUADS</td>
                    <td>32 bits per pixel. 8 bits are used for each color channel.</td>
                </tr>
            
                <tr>
                    <td>BM_CMYKQUADS</td>
                    <td>32 bits per pixel. 8 bits are used for each color channel.</td>
                </tr>
            
                <tr>
                    <td>BM_10b_RGB</td>
                    <td>32 bits per pixel. 10 bits are used for each color channel. The 2 most significant bits are ignored.</td>
                </tr>
            
                <tr>
                    <td>BM_10b_XYZ</td>
                    <td>32 bits per pixel. 10 bits are used for each color channel. The 2 most significant bits are ignored.</td>
                </tr>
            
                <tr>
                    <td>BM_10b_Yxy</td>
                    <td>32 bits per pixel. 10 bits are used for each color channel. The 2 most significant bits are ignored.</td>
                </tr>
            
                <tr>
                    <td>BM_10b_Lab</td>
                    <td>32 bits per pixel. 10 bits are used for each color channel. The 2 most significant bits are ignored.</td>
                </tr>
            
                <tr>
                    <td>BM_10b_G3CH</td>
                    <td>32 bits per pixel. 10 bits are used for each color channel. The 2 most significant bits are ignored.</td>
                </tr>
            
                <tr>
                    <td>BM_NAMED_INDEX</td>
                    <td>32 bits per pixel. Named color indices. Index numbering begins at one.</td>
                </tr>
            
                <tr>
                    <td>BM_16b_RGB</td>
                    <td>64 bits per pixel. 16 bits are used for the gray-scale value. Each of the three color channels uses 16 bits.</td>
                </tr>
            
                <tr>
                    <td>BM_16b_XYZ</td>
                    <td>64 bits per pixel. 16 bits are used for the gray-scale value. Each of the three color channels uses 16 bits.</td>
                </tr>
            
                <tr>
                    <td>BM_16b_Yxy</td>
                    <td>64 bits per pixel. 16 bits are used for the gray-scale value. Each of the three color channels uses 16 bits.</td>
                </tr>
            
                <tr>
                    <td>BM_16b_Lab</td>
                    <td>64 bits per pixel. 16 bits are used for the gray-scale value. Each of the three color channels uses 16 bits.</td>
                </tr>
            
                <tr>
                    <td>BM_16b_G3CH</td>
                    <td>64 bits per pixel. 16 bits are used for the gray-scale value. Each of the three color channels uses 16 bits.</td>
                </tr>
            
                <tr>
                    <td>BM_16b_GRAY</td>
                    <td>64 bits per pixel. 16 bits are used for the gray-scale value. All other bits are ignored.</td>
                </tr>
            
                <tr>
                    <td>BM_565RGB</td>
                    <td>16 bits per pixel. 5 bits are used for red, 6 for green, and 5 for blue.</td>
                </tr>
            
                <tr>
                    <td>BM_32b_scRGB</td>
                    <td>96 bits per pixel. 32 bits are used for each color channel, as defined by the IEEE 32-bit floating point standard.</td>
                </tr>
            
                <tr>
                    <td>BM_32b_scARGB</td>
                    <td>128 bits per pixel. 32 bits are used for each color channel, as defined by the IEEE 32-bit floating point standard.</td>
                </tr>
            
                <tr>
                    <td>BM_S2DOT13FIXED_scRGB</td>
                    <td>48 bits per pixel. Color data is stored as one 16-bit word per channel, with a fixed range of -4 to +4, inclusive. A signed format is used, with 1 bit for the sign, 2 bits for the integer portion, and 13 bits for the fractional portion.</td>
                </tr>
            
                <tr>
                    <td>BM_S2DOT13FIXED_scARGB</td>
                    <td>64 bits per pixel. Color data is stored as one 16-bit word per channel, with a fixed range of -4 to +4, inclusive. A signed format is used, with 1 bit for the sign, 2 bits for the integer portion, and 13 bits for the fractional portion.</td>
                </tr>
            
                <tr>
                    <td>BM_R10G10B10A2</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>BM_R10G10B10A2_XR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>BM_R16G16B16A16_FLOAT</td>
                    <td>#endif // NTDDI_VERSION &gt;= NTDDI_WIN7</td>
                </tr>
</table>

## Remarks

The last four values were added to the BMFORMAT enumeration beginning with Windows Vista.

The PBMFORMAT and LPBMFORMAT data types are defined as pointers to this enumeration:

<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef BMFORMAT *PBMFORMAT, *LPBMFORMAT;</pre>
</td>
</tr>
</table></span></div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Included in Windows Vista and later. Included in Windows Vista and later. |
| **Header** | icm.h |