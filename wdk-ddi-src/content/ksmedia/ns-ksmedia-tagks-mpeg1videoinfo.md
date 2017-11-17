---
UID: NS.ksmedia.tagKS_MPEG1VIDEOINFO
title: tagKS_MPEG1VIDEOINFO
author: windows-driver-content
description: The KS_MPEG1VIDEOINFO structure describes an MPEG-1 video stream.
old-location: stream\ks_mpeg1videoinfo.htm
ms.assetid: 301b954a-4e50-4a04-a575-17d7d54fa691
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
req.alt-api: KS_MPEG1VIDEOINFO
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
ms.keywords: tagKS_MPEG1VIDEOINFO, KS_MPEG1VIDEOINFO, *PKS_MPEG1VIDEOINFO
req.iface: 
---

# tagKS_MPEG1VIDEOINFO structure



## -description
<p>The KS_MPEG1VIDEOINFO structure describes an MPEG-1 video stream.</p>


## -syntax

````
typedef struct tagKS_MPEG1VIDEOINFO {
  KS_VIDEOINFOHEADER hdr;
  DWORD              dwStartTimeCode;
  DWORD              cbSequenceHeader;
  BYTE               bSequenceHeader[1];
} KS_MPEG1VIDEOINFO, *PKS_MPEG1VIDEOINFO;
````


## -struct-fields
<dl>

### -field <b>hdr</b>

<dd>
<p>Specifies a <a href="https://msdn.microsoft.com/library/windows/hardware/ff567700">KS_VIDEOINFOHEADER</a> structure that describes the details of the video stream.</p>
</dd>

### -field <b>dwStartTimeCode</b>

<dd>
<p>A 25-bit "group-of-pictures" time code at the start of data.</p>
</dd>

### -field <b>cbSequenceHeader</b>

<dd>
<p>The length of the <b>bSequenceHeader</b> member, in bytes.</p>
</dd>

### -field <b>bSequenceHeader</b>

<dd>
<p>The length of the <b>bSequenceHeader</b> member, in bytes.</p>
</dd>
</dl>

## -remarks


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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567700">KS_VIDEOINFOHEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KS_MPEG1VIDEOINFO structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
