---
UID: NS.ksmedia.tagKS_DATAFORMAT_H264VIDEOINFO
title: tagKS_DATAFORMAT_H264VIDEOINFO
author: windows-driver-content
description: The KS_DATAFORMAT_H264VIDEOINFO structure describes the data formats range available for a stream.
old-location: stream\ks_dataformat_h264videoinfo.htm
old-project: stream
ms.assetid: 6D2C0245-542E-4749-B8F3-531BFA3800E3
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: tagKS_DATAFORMAT_H264VIDEOINFO, KS_DATAFORMAT_H264VIDEOINFO, *PKS_DATAFORMAT_H264VIDEOINFO
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
req.alt-api: KS_DATAFORMAT_H264VIDEOINFO
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

# tagKS_DATAFORMAT_H264VIDEOINFO structure



## -description
<p>The KS_DATAFORMAT_H264VIDEOINFO structure describes the data formats range available for a stream.</p>


## -syntax

````
typedef struct _KS_DATAFORMAT_H264VIDEOINFO {
  KSDATAFORMAT                     DataFormat;
     KS_H264VIDEOINFO              H264VideoInfoHeader;
} KS_DATAFORMAT_H264VIDEOINFO, *PKS_DATAFORMAT_H264VIDEOINFO;
````


## -struct-fields
<dl>

### -field <b>DataFormat</b>

<dd>
<p>Specifies the major identifier for the format. </p>
</dd>

### -field <b>H264VideoInfoHeader</b>

<dd>
<p>Specifies the details of the video stream.</p>
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
<a href="stream.ksdataformat">KSDATAFORMAT</a>
</dt>
<dt>
<a href="stream.ks_h264videoinfo">KS_H264VIDEOINFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KS_DATAFORMAT_H264VIDEOINFO structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
