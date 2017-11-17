---
UID: NS.wiautil._BMP_IMAGE_INFO
title: BMP_IMAGE_INFO
author: windows-driver-content
description: The BMP_IMAGE_INFO structure contains information about a BMP image.
old-location: image\bmp_image_info.htm
ms.assetid: 953e2f00-2275-49a2-b1e5-def7763a8ab7
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: image
req.header: wiautil.h
req.include-header: Wiautil.h, Wiamindr.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BMP_IMAGE_INFO
req.alt-loc: wiautil.h
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
ms.keywords: BMP_IMAGE_INFO, BMP_IMAGE_INFO, *PBMP_IMAGE_INFO
req.iface: 
req.product: Windows 10 or later.
---

# BMP_IMAGE_INFO structure



## -description
<p>The BMP_IMAGE_INFO structure contains information about a BMP image.</p>


## -syntax

````
typedef struct _BMP_IMAGE_INFO {
  INT Width;
  INT Height;
  INT ByteWidth;
  INT Size;
} BMP_IMAGE_INFO, *PBMP_IMAGE_INFO;
````


## -struct-fields
<dl>

### -field <b>Width</b>

<dd>
<p>Specifies the width of the image, in pixels.</p>
</dd>

### -field <b>Height</b>

<dd>
<p>Specifies the height of the image, in lines.</p>
</dd>

### -field <b>ByteWidth</b>

<dd>
<p>Specifies the width of the image, in bytes.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>Specifies the total size of the image, including headers, in bytes.</p>
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
<p>Available in Windows XP and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wiautil.h (include Wiautil.h or Wiamindr.h)</dt>
</dl>
</td>
</tr>
</table>