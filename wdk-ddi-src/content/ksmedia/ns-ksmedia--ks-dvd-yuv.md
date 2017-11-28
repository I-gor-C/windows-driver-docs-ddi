---
UID: NS.ksmedia._KS_DVD_YUV
title: KS_DVD_YUV
author: windows-driver-content
description: The KS_DVD_YUV structure is used to describe a color in the YUV colorspace.
old-location: stream\ks_dvd_yuv.htm
old-project: stream
ms.assetid: 9b155d09-6fb2-4c6c-bde6-7eadeb09bc40
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KS_DVD_YUV, KS_DVD_YUV, *PKS_DVD_YUV
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
req.alt-api: KS_DVD_YUV
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

# KS_DVD_YUV structure



## -description
<p>The KS_DVD_YUV structure is used to describe a color in the YUV colorspace.</p>


## -syntax

````
typedef struct _KS_DVD_YUV {
  UCHAR Reserved;
  UCHAR Y;
  UCHAR V;
  UCHAR U;
} KS_DVD_YUV, *PKS_DVD_YUV;
````


## -struct-fields
<dl>

### -field <b>Reserved</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field <b>Y</b>

<dd>
<p>Indicates the luminance (brightness) component of the color.</p>
</dd>

### -field <b>V</b>

<dd>
<p>Indicates the color-red (chrominance) component of the color.</p>
</dd>

### -field <b>U</b>

<dd>
<p>Indicates the color-blue (chrominance) component of the color.</p>
</dd>
</dl>

## -remarks
<p>The KS_DVD_YUV structure is used </p>

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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567641">KS_DVD_YCrCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KS_DVD_YUV structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
