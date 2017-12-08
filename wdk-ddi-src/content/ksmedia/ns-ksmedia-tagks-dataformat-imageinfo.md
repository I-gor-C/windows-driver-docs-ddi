---
UID: NS.ksmedia.tagKS_DATAFORMAT_IMAGEINFO
title: tagKS_DATAFORMAT_IMAGEINFO
author: windows-driver-content
description: Specifies an image data format that is used for an independent image pin (or stream).
old-location: stream\ks_dataformat_imageinfo.htm
old-project: stream
ms.assetid: d63289bc-9603-4e79-8a77-d2eb0f2c784c
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: tagKS_DATAFORMAT_IMAGEINFO, KS_DATAFORMAT_IMAGEINFO, *PKS_DATAFORMAT_IMAGEINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KS_DATAFORMAT_IMAGEINFO
req.alt-loc: Ksmedia.h
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

# tagKS_DATAFORMAT_IMAGEINFO structure



## -description
<p>Specifies an image data format that is used for an independent image pin (or stream).</p>


## -syntax

````
typedef struct tagKS_DATAFORMAT_IMAGEINFO {
  KSDATAFORMAT        DataFormat;
  KS_BITMAPINFOHEADER ImageInfoHeader;
} KS_DATAFORMAT_IMAGEINFO, *PKS_DATAFORMAT_IMAGEINFO;
````


## -struct-fields
<dl>

### -field DataFormat

<dd>
<p>A <a href="stream.ksdataformat">KSDATAFORMAT</a> structure that specifies the data format of the image stream.</p>
</dd>

### -field ImageInfoHeader

<dd>
<p>A <a href="stream.ks_bitmapinfoheader">KS_BITMAPINFOHEADER</a> structure that specifies image color and dimension information that the still image capture stream would provide.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
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
<a href="stream.ks_bitmapinfoheader">KS_BITMAPINFOHEADER</a>
</dt>
<dt>
<a href="stream.ksdataformat">KSDATAFORMAT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KS_DATAFORMAT_IMAGEINFO structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
