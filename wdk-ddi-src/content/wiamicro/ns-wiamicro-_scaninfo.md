---
UID: NS:wiamicro._SCANINFO
title: "_SCANINFO"
author: windows-driver-content
description: The SCANINFO structure is used to store and communicate information about a scan acquisition.
old-location: image\scaninfo.htm
old-project: image
ms.assetid: 58a0cc96-7180-4823-a4af-bf2d5fa49474
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: "*PSCANINFO, MicroDrv_42f31c58-206a-468e-98ff-794c69b82457.xml, PSCANINFO, PSCANINFO structure pointer [Imaging Devices], SCANINFO, SCANINFO structure [Imaging Devices], _SCANINFO, image.scaninfo, wiamicro/PSCANINFO, wiamicro/SCANINFO"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wiamicro.h
req.include-header: Wiamicro.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Me and in Windows XP and later versions of the Windows operating systems.
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
-	wiamicro.h
api_name:
-	SCANINFO
product: Windows
targetos: Windows
req.typenames: SCANINFO, *PSCANINFO
req.product: Windows 10 or later.
---

# _SCANINFO structure
The SCANINFO structure is used to store and communicate information about a scan acquisition. The WIA Flatbed Driver reads values from the SCANINFO structure, but never writes values. It is the microdriver's responsibility to set values for the SCANINFO members.

## Syntax
```
typedef struct _SCANINFO {
  LONG       ADF;
  LONG       TPA;
  LONG       Endorser;
  LONG       OpticalXResolution;
  LONG       OpticalYResolution;
  LONG       BedWidth;
  LONG       BedHeight;
  RANGEVALUE IntensityRange;
  RANGEVALUE ContrastRange;
  LONG       SupportedCompressionType;
  LONG       SupportedDataTypes;
  LONG       WidthPixels;
  LONG       WidthBytes;
  LONG       Lines;
  LONG       DataType;
  LONG       PixelBits;
  LONG       Intensity;
  LONG       Contrast;
  LONG       Xresolution;
  LONG       Yresolution;
  SCANWINDOW Window;
  LONG       DitherPattern;
  LONG       Negative;
  LONG       Mirror;
  LONG       AutoBack;
  LONG       ColorDitherPattern;
  LONG       ToneMap;
  LONG       Compression;
  LONG       RawDataFormat;
  LONG       RawPixelOrder;
  LONG       bNeedDataAlignment;
  LONG       DelayBetweenRead;
  LONG       MaxBufferSize;
  HANDLE     DeviceIOHandles[MAX_IO_HANDLES];
  LONG       lReserved[MAX_RESERVED];
  VOID       *pMicroDriverContext;
} *PSCANINFO, SCANINFO;
```

## Members


`ADF`

Indicates whether the scanner supports an automatic document feeder (ADF). This member can be one of the following values:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
0

</td>
<td>
The scanner does not support an ADF.

</td>
</tr>
<tr>
<td>
1

</td>
<td>
The scanner supports an ADF.

</td>
</tr>
<tr>
<td>
2

</td>
<td>
The scanner supports an ADF with duplex capability.

</td>
</tr>
</table>

`TPA`

Indicates whether the scanner supports TPA (TransParency Adapter). The value can be:

0 - not supported

1 - supported

`Endorser`

Indicates whether the scanner has endorser capabilities. The value can be:

0 - not supported

1 - supported

`OpticalXResolution`

Specifies the horizontal dpi setting of the scanner optics.

`OpticalYResolution`

Specifies the vertical dpi setting of the scanner optics.

`BedWidth`

Specifies the bed width of the scanner in thousandths of an inch.

`BedHeight`

Specifies the bed height of the scanner in thousandths of an inch.

`IntensityRange`

Specifies the intensity/brightness range values of the scanner.

`ContrastRange`

Specifies the contrast range values of the scanner.

`SupportedCompressionType`

Specifies a mask value of supported compression types. A value of zero indicates that no compression types are supported.

`SupportedDataTypes`

Specifies a mask value of supported data types. A value of zero indicates that no data types are supported. This member can be the bitwise OR of the following.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
SUPPORT_BW

</td>
<td>
The image is 1 bit-per-pixel black and white.

</td>
</tr>
<tr>
<td>
SUPPORT_COLOR

</td>
<td>
The image is 24 bits-per-pixel color.

</td>
</tr>
<tr>
<td>
SUPPORT_GRAYSCALE

</td>
<td>
The image is 8 bits-per-pixel grayscale.

</td>
</tr>
</table>

`WidthPixels`

Specifies the width of the current image in pixels.

`WidthBytes`

Specifies the width of the current image in bytes.

`Lines`

Specifies the height of the current image in pixels.

`DataType`

Specifies the current data type set of the current image. This member can be set to one of the following.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
WIA_DATA_COLOR

</td>
<td>
The driver supports 24 bit-per-pixel color.

</td>
</tr>
<tr>
<td>
WIA_DATA_COLOR_DITHER

</td>
<td>
This value is not supported in the WIA Flatbed driver.

</td>
</tr>
<tr>
<td>
WIA_DATA_COLOR_THRESHOLD

</td>
<td>
This value is not supported in the WIA Flatbed driver.

</td>
</tr>
<tr>
<td>
WIA_DATA_DITHER

</td>
<td>
This value is not supported in the WIA Flatbed driver.

</td>
</tr>
<tr>
<td>
WIA_DATA_GRAYSCALE

</td>
<td>
The driver supports 8 bit-per-pixel grayscale.

</td>
</tr>
<tr>
<td>
WIA_DATA_THRESHOLD

</td>
<td>
The driver supports 1 bit-per-pixel black and white.

</td>
</tr>
</table>

`PixelBits`

Specifies the current bit depth setting of the current image.

`Intensity`

Specifies the current intensity/brightness setting of the scanner.

`Contrast`

Specifies the current contrast setting of the scanner.

`Xresolution`

Specifies the horizontal dpi setting of the scanner optics.

`Yresolution`

Specifies the vertical dpi setting of the scanner optics.

`Window`

Specifies the current scanner window settings.

`DitherPattern`

Specifies the dither pattern of the scanner.

`Negative`

Specifies whether negative is on or off. The value can be:

0 - off

1 - on

`Mirror`

Specifies whether mirror is on or off. The value can be:

0 - off

1 - on

`AutoBack`

Specifies whether AutoBack is on or off. The value can be:

0 - off

1 - on

`ColorDitherPattern`

Reserved. Set to zero.

`ToneMap`

Reserved. Set to zero.

`Compression`

Specifies whether compression is on or off for the scanner. The value can be:

0 - off

1 - on

`RawDataFormat`

Specifies the raw data format for the scanner. The value can be:

0 - packed data

1 - planar data

`RawPixelOrder`

Specifies the pixel order for the scanner. The value can be:

0 - RGB

1 - BGR

`bNeedDataAlignment`

Specifies whether data alignment is needed for the scanner. The value can be:

0 - false

1 - true

`DelayBetweenRead`

Specifies the time delay in milliseconds between <a href="https://msdn.microsoft.com/library/windows/hardware/dn915807">Scan</a> function calls that the scanner can support.

`MaxBufferSize`

Specifies the maximum buffer size in the scanner.

`DeviceIOHandles`

Specifies an array of device I/O handles needed for device communication.

`lReserved`

Specifies an array of reserved bits.

`pMicroDriverContext`

Points to the microdriver's context. <i>This member is defined only for Microsoft Windows XP and later</i>. The microdriver allocates the buffer pointed to by this member. The buffer should be allocated in CMD_INITIALIZE, and freed in CMD_UNINITIALIZE. (See <a href="https://msdn.microsoft.com/library/windows/hardware/ff547067">Required Commands</a>.) The WIA Flatbed driver knows nothing of this pointer, and hence will not alter the memory pointed to by this member.

## Remarks
This structure is used as a parameter in the microdriver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff548129">SetPixelWindow</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/dn915807">Scan</a> functions.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Me and in Windows XP and later versions of the Windows operating systems. Available in Windows Me and in Windows XP and later versions of the Windows operating systems. |
| **Header** | wiamicro.h (include Wiamicro.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn915807">Scan</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548129">SetPixelWindow</a>