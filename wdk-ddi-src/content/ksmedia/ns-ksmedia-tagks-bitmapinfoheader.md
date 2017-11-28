---
UID: NS.ksmedia.tagKS_BITMAPINFOHEADER
title: tagKS_BITMAPINFOHEADER
author: windows-driver-content
description: The KS_BITMAPINFOHEADER structure describes details about the video stream, such as image dimensions and pixel depth.
old-location: stream\ks_bitmapinfoheader.htm
old-project: stream
ms.assetid: 77101494-97bb-4049-8c6c-cdb4ee82f312
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: tagKS_BITMAPINFOHEADER, KS_BITMAPINFOHEADER, *PKS_BITMAPINFOHEADER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KS_BITMAPINFOHEADER
req.alt-loc: ksmedia.h
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
---

# tagKS_BITMAPINFOHEADER structure



## -description
<p>The KS_BITMAPINFOHEADER structure describes details about the video stream, such as image dimensions and pixel depth. </p>


## -syntax

````
typedef struct tagKS_BITMAPINFOHEADER {
  DWORD biSize;
  LONG  biWidth;
  LONG  biHeight;
  WORD  biPlanes;
  WORD  biBitCount;
  DWORD biCompression;
  DWORD biSizeImage;
  LONG  biXPelsPerMeter;
  LONG  biYPelsPerMeter;
  DWORD biClrUsed;
  DWORD biClrImportant;
} KS_BITMAPINFOHEADER, *PKS_BITMAPINFOHEADER;
````


## -struct-fields
<dl>

### -field <b>biSize</b>

<dd>
<p>Specifies the size of the structure in bytes.</p>
</dd>

### -field <b>biWidth</b>

<dd>
<p>Specifies the width of the bitmap in pixels.</p>
</dd>

### -field <b>biHeight</b>

<dd>
<p>Specifies the height of the bitmap in pixels.</p>
</dd>

### -field <b>biPlanes</b>

<dd>
<p>Specifies the number of planes. This is always set to 1.</p>
</dd>

### -field <b>biBitCount</b>

<dd>
<p>Specifies the color bits per pixel. For example, 1, 4, 8, or 24.</p>
</dd>

### -field <b>biCompression</b>

<dd>
<p>Specifies the compression scheme.</p>
</dd>

### -field <b>biSizeImage</b>

<dd>
<p>Specifies the size of bitmap bits in bytes. (Only required if using compression.)</p>
</dd>

### -field <b>biXPelsPerMeter</b>

<dd>
<p>Specifies the horizontal resolution in pixels per meter.</p>
</dd>

### -field <b>biYPelsPerMeter</b>

<dd>
<p>Specifies the vertical resolution in pixels per meter.</p>
</dd>

### -field <b>biClrUsed</b>

<dd>
<p>Specifies the number of colors used in the image.</p>
</dd>

### -field <b>biClrImportant</b>

<dd>
<p>Specifies the number of important colors in the image.</p>
</dd>
</dl>

## -remarks
<p>This is the same structure as the user-mode GDI bitmap header (BITMAPINFOHEADER) structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h (include Ksmedia.h)</dt>
</dl>
</td>
</tr>
</table>