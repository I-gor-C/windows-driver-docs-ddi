---
UID: NS.ksmedia._KS_DVD_YCrCb
title: KS_DVD_YCrCb
author: windows-driver-content
description: The KS_DVD_YCrCb structure is used to describe a color in the YCrCb colorspace.
old-location: stream\ks_dvd_ycrcb.htm
ms.assetid: 78010e49-ad09-4eb3-bb48-17040737a0a0
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KS_DVD_YCrCb
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
ms.keywords: KS_DVD_YCrCb, KS_DVD_YCrCb, *PKS_DVD_YCrCb
req.iface: 
---

# KS_DVD_YCrCb structure



## -description
<p>The KS_DVD_YCrCb structure is used to describe a color in the YCrCb colorspace.</p>


## -syntax

````
typedef struct _KS_DVD_YCrCb {
  UCHAR Reserved;
  UCHAR Y;
  UCHAR Cr;
  UCHAR Cb;
} KS_DVD_YCrCb, *PKS_DVD_YCrCb;
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

### -field <b>Cr</b>

<dd>
<p>Indicates the color-red (chrominance) component of the color.</p>
</dd>

### -field <b>Cb</b>

<dd>
<p>Indicates the color-blue (chrominance) component of the color.</p>
</dd>
</dl>

## -remarks
<p>The KS_DVD_YCrCb structure is used </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567642">KS_DVD_YUV</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KS_DVD_YCrCb structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
