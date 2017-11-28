---
UID: NS.wiamicro._SCANINFO
title: SCANINFO
author: windows-driver-content
description: The SCANINFO structure is used to store and communicate information about a scan acquisition.
old-location: image\scaninfo.htm
old-project: image
ms.assetid: 58a0cc96-7180-4823-a4af-bf2d5fa49474
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: SCANINFO, SCANINFO, *PSCANINFO
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
req.alt-api: SCANINFO
req.alt-loc: wiamicro.h
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
req.iface: 
req.product: Windows 10 or later.
---

# SCANINFO structure



## -description
<p>The SCANINFO structure is used to store and communicate information about a scan acquisition. The WIA Flatbed Driver reads values from the SCANINFO structure, but never writes values. It is the microdriver's responsibility to set values for the SCANINFO members.</p>


## -syntax

````
typedef struct _SCANINFO {
  LONG       ADF;
  LONG       TPA;
  LONG       Endorser;
  LONG       OpticalXResolution;
  LONG       OpticalYResolution;
  LONG       BedWidth;
  LONG       BedHeight;
  RANGEVALUE IntensityRange;
  RANGEVALUE ContrastRange;
  LONG       SupportedCompressionType;
  LONG       SupportedDataTypes;
  LONG       WidthPixels;
  LONG       WidthBytes;
  LONG       Lines;
  LONG       DataType;
  LONG       PixelBits;
  LONG       Intensity;
  LONG       Contrast;
  LONG       Xresolution;
  LONG       Yresolution;
  SCANWINDOW Window;
  LONG       DitherPattern;
  LONG       Negative;
  LONG       Mirror;
  LONG       AutoBack;
  LONG       ColorDitherPattern;
  LONG       ToneMap;
  LONG       Compression;
  LONG       RawDataFormat;
  LONG       RawPixelOrder;
  LONG       bNeedDataAlignment;
  LONG       DelayBetweenRead;
  LONG       MaxBufferSize;
  HANDLE     DeviceIOHandles[MAX_IO_HANDLES];
  LONG       lReserved[MAX_RESERVED];
  VOID       *pMicroDriverContext;
} SCANINFO, *PSCANINFO;
````


## -struct-fields
<dl>

### -field <b>ADF</b>

<dd>
<p>Indicates whether the scanner supports an automatic document feeder (ADF). This member can be one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>0</p>
</td>
<td>
<p>The scanner does not support an ADF.</p>
</td>
</tr>
<tr>
<td>
<p>1</p>
</td>
<td>
<p>The scanner supports an ADF.</p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p>The scanner supports an ADF with duplex capability.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>TPA</b>

<dd>
<p>Indicates whether the scanner supports TPA (TransParency Adapter). The value can be:</p>
<p>0 - not supported</p>
<p>1 - supported</p>
</dd>

### -field <b>Endorser</b>

<dd>
<p>Indicates whether the scanner has endorser capabilities. The value can be:</p>
<p>0 - not supported</p>
<p>1 - supported</p>
</dd>

### -field <b>OpticalXResolution</b>

<dd>
<p>Specifies the horizontal dpi setting of the scanner optics.</p>
</dd>

### -field <b>OpticalYResolution</b>

<dd>
<p>Specifies the vertical dpi setting of the scanner optics.</p>
</dd>

### -field <b>BedWidth</b>

<dd>
<p>Specifies the bed width of the scanner in thousandths of an inch.</p>
</dd>

### -field <b>BedHeight</b>

<dd>
<p>Specifies the bed height of the scanner in thousandths of an inch.</p>
</dd>

### -field <b>IntensityRange</b>

<dd>
<p>Specifies the intensity/brightness range values of the scanner.</p>
</dd>

### -field <b>ContrastRange</b>

<dd>
<p>Specifies the contrast range values of the scanner.</p>
</dd>

### -field <b>SupportedCompressionType</b>

<dd>
<p>Specifies a mask value of supported compression types. A value of zero indicates that no compression types are supported.</p>
</dd>

### -field <b>SupportedDataTypes</b>

<dd>
<p>Specifies a mask value of supported data types. A value of zero indicates that no data types are supported. This member can be the bitwise OR of the following.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>SUPPORT_BW</p>
</td>
<td>
<p>The image is 1 bit-per-pixel black and white.</p>
</td>
</tr>
<tr>
<td>
<p>SUPPORT_COLOR</p>
</td>
<td>
<p>The image is 24 bits-per-pixel color.</p>
</td>
</tr>
<tr>
<td>
<p>SUPPORT_GRAYSCALE</p>
</td>
<td>
<p>The image is 8 bits-per-pixel grayscale.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>WidthPixels</b>

<dd>
<p>Specifies the width of the current image in pixels.</p>
</dd>

### -field <b>WidthBytes</b>

<dd>
<p>Specifies the width of the current image in bytes.</p>
</dd>

### -field <b>Lines</b>

<dd>
<p>Specifies the height of the current image in pixels.</p>
</dd>

### -field <b>DataType</b>

<dd>
<p>Specifies the current data type set of the current image. This member can be set to one of the following.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>WIA_DATA_COLOR</p>
</td>
<td>
<p>The driver supports 24 bit-per-pixel color.</p>
</td>
</tr>
<tr>
<td>
<p>WIA_DATA_COLOR_DITHER</p>
</td>
<td>
<p>This value is not supported in the WIA Flatbed driver.</p>
</td>
</tr>
<tr>
<td>
<p>WIA_DATA_COLOR_THRESHOLD</p>
</td>
<td>
<p>This value is not supported in the WIA Flatbed driver.</p>
</td>
</tr>
<tr>
<td>
<p>WIA_DATA_DITHER</p>
</td>
<td>
<p>This value is not supported in the WIA Flatbed driver.</p>
</td>
</tr>
<tr>
<td>
<p>WIA_DATA_GRAYSCALE</p>
</td>
<td>
<p>The driver supports 8 bit-per-pixel grayscale.</p>
</td>
</tr>
<tr>
<td>
<p>WIA_DATA_THRESHOLD</p>
</td>
<td>
<p>The driver supports 1 bit-per-pixel black and white.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>PixelBits</b>

<dd>
<p>Specifies the current bit depth setting of the current image.</p>
</dd>

### -field <b>Intensity</b>

<dd>
<p>Specifies the current intensity/brightness setting of the scanner.</p>
</dd>

### -field <b>Contrast</b>

<dd>
<p>Specifies the current contrast setting of the scanner.</p>
</dd>

### -field <b>Xresolution</b>

<dd>
<p>Specifies the horizontal dpi setting of the scanner optics.</p>
</dd>

### -field <b>Yresolution</b>

<dd>
<p>Specifies the vertical dpi setting of the scanner optics.</p>
</dd>

### -field <b>Window</b>

<dd>
<p>Specifies the current scanner window settings.</p>
</dd>

### -field <b>DitherPattern</b>

<dd>
<p>Specifies the dither pattern of the scanner.</p>
</dd>

### -field <b>Negative</b>

<dd>
<p>Specifies whether negative is on or off. The value can be:</p>
<p>0 - off</p>
<p>1 - on</p>
</dd>

### -field <b>Mirror</b>

<dd>
<p>Specifies whether mirror is on or off. The value can be:</p>
<p>0 - off</p>
<p>1 - on</p>
</dd>

### -field <b>AutoBack</b>

<dd>
<p>Specifies whether AutoBack is on or off. The value can be:</p>
<p>0 - off</p>
<p>1 - on</p>
</dd>

### -field <b>ColorDitherPattern</b>

<dd>
<p>Reserved. Set to zero.</p>
</dd>

### -field <b>ToneMap</b>

<dd>
<p>Reserved. Set to zero.</p>
</dd>

### -field <b>Compression</b>

<dd>
<p>Specifies whether compression is on or off for the scanner. The value can be:</p>
<p>0 - off</p>
<p>1 - on</p>
</dd>

### -field <b>RawDataFormat</b>

<dd>
<p>Specifies the raw data format for the scanner. The value can be:</p>
<p>0 - packed data</p>
<p>1 - planar data</p>
</dd>

### -field <b>RawPixelOrder</b>

<dd>
<p>Specifies the pixel order for the scanner. The value can be:</p>
<p>0 - RGB</p>
<p>1 - BGR</p>
</dd>

### -field <b>bNeedDataAlignment</b>

<dd>
<p>Specifies whether data alignment is needed for the scanner. The value can be:</p>
<p>0 - false</p>
<p>1 - true</p>
</dd>

### -field <b>DelayBetweenRead</b>

<dd>
<p>Specifies the time delay in milliseconds between <a href="https://msdn.microsoft.com/library/windows/hardware/dn915807">Scan</a> function calls that the scanner can support.</p>
</dd>

### -field <b>MaxBufferSize</b>

<dd>
<p>Specifies the maximum buffer size in the scanner.</p>
</dd>

### -field <b>DeviceIOHandles</b>

<dd>
<p>Specifies an array of device I/O handles needed for device communication.</p>
</dd>

### -field <b>lReserved</b>

<dd>
<p>Specifies an array of reserved bits.</p>
</dd>

### -field <b>pMicroDriverContext</b>

<dd>
<p>Points to the microdriver's context. <i>This member is defined only for Microsoft Windows XP and later</i>. The microdriver allocates the buffer pointed to by this member. The buffer should be allocated in CMD_INITIALIZE, and freed in CMD_UNINITIALIZE. (See <a href="https://msdn.microsoft.com/library/windows/hardware/ff547067">Required Commands</a>.) The WIA Flatbed driver knows nothing of this pointer, and hence will not alter the memory pointed to by this member.</p>
</dd>
</dl>

## -remarks
<p>This structure is used as a parameter in the microdriver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff548129">SetPixelWindow</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/dn915807">Scan</a> functions.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Me and in Windows XP and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wiamicro.h (include Wiamicro.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548129">SetPixelWindow</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn915807">Scan</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20SCANINFO structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
