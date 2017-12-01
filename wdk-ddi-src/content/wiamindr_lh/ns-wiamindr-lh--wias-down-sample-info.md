---
UID: NS.wiamindr_lh._WIAS_DOWN_SAMPLE_INFO
title: WIAS_DOWN_SAMPLE_INFO
author: windows-driver-content
description: The WIAS_DOWN_SAMPLE_INFO structure stores information used by the downsampling helper function, wiasDownSampleBuffer.
old-location: image\wias_down_sample_info.htm
old-project: image
ms.assetid: af9d35d8-9e3c-4be0-8ba4-a0b548b1d7ac
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WIAS_DOWN_SAMPLE_INFO, WIAS_DOWN_SAMPLE_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wiamindr_lh.h
req.include-header: Wiamindr.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Me and in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WIAS_DOWN_SAMPLE_INFO
req.alt-loc: wiamindr_lh.h
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
req.iface: IWiaMiniDrvTransferCallback
req.product: Windows 10 or later.
---

# WIAS_DOWN_SAMPLE_INFO structure



## -description
<p>The WIAS_DOWN_SAMPLE_INFO structure stores information used by the downsampling helper function, <a href="..\wiamdef\nf-wiamdef-wiasdownsamplebuffer.md">wiasDownSampleBuffer</a>.</p>


## -syntax

````
typedef struct _WIAS_DOWN_SAMPLE_INFO {
  ULONG ulOriginalWidth;
  ULONG ulOriginalHeight;
  ULONG ulBitsPerPixel;
  ULONG ulXRes;
  ULONG ulYRes;
  ULONG ulDownSampledWidth;
  ULONG ulDownSampledHeight;
  ULONG ulActualSize;
  ULONG ulDestBufSize;
  ULONG ulSrcBufSize;
  BYTE  *pSrcBuffer;
  BYTE  *pDestBuffer;
} WIAS_DOWN_SAMPLE_INFO, *PWIAS_DOWN_SAMPLE_INFO;
````


## -struct-fields
<dl>

### -field <b>ulOriginalWidth</b>

<dd>
<p>Specifies the width, in pixels, of the input data.</p>
</dd>

### -field <b>ulOriginalHeight</b>

<dd>
<p>Specifies the height, in pixels, of the input data.</p>
</dd>

### -field <b>ulBitsPerPixel</b>

<dd>
<p>Specifies the number of bits per pixel of the input data.</p>
</dd>

### -field <b>ulXRes</b>

<dd>
<p>Specifies the horizontal resolution of the input data.</p>
</dd>

### -field <b>ulYRes</b>

<dd>
<p>Specifies the vertical resolution of the input data.</p>
</dd>

### -field <b>ulDownSampledWidth</b>

<dd>
<p>Specifies the width, in pixels, of the output data.</p>
</dd>

### -field <b>ulDownSampledHeight</b>

<dd>
<p>Specifies the width, in pixels, of the output data.</p>
</dd>

### -field <b>ulActualSize</b>

<dd>
<p>Specifies the number of bytes placed in the destination buffer.</p>
</dd>

### -field <b>ulDestBufSize</b>

<dd>
<p>Specifies the size, in bytes, of the destination buffer.</p>
</dd>

### -field <b>ulSrcBufSize</b>

<dd>
<p>Specifies the size, in bytes, of the source buffer.</p>
</dd>

### -field <b>pSrcBuffer</b>

<dd>
<p>Points to the source buffer.</p>
</dd>

### -field <b>pDestBuffer</b>

<dd>
<p>Points to the destination buffer.</p>
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
<p>Available in Windows Me and in Windows XP and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wiamindr_lh.h (include Wiamindr.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wiamdef\nf-wiamdef-wiasdownsamplebuffer.md">wiasDownSampleBuffer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20WIAS_DOWN_SAMPLE_INFO structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
