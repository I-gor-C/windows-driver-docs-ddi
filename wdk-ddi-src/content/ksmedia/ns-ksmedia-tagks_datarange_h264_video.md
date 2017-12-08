---
UID: NS.KSMEDIA.TAGKS_DATARANGE_H264_VIDEO
title: tagKS_DATARANGE_H264_VIDEO
author: windows-driver-content
description: The KS_DATARANGE_H264_VIDEO structure describes the range of MPEG-2 video formats available for a stream.
old-location: stream\ks_datarange_h264_video.htm
old-project: stream
ms.assetid: E52B252F-0530-4543-A44C-95D4198504CA
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: tagKS_DATARANGE_H264_VIDEO, *PKS_DATARANGE_H264_VIDEO, KS_DATARANGE_H264_VIDEO
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
req.alt-api: KS_DATARANGE_H264_VIDEO
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
---

# tagKS_DATARANGE_H264_VIDEO structure



## -description
The KS_DATARANGE_H264_VIDEO structure describes the range of MPEG-2 video formats available for a stream.


## -syntax

````
typedef struct _KS_DATARANGE_H264_VIDEO {
  KSDATARANGE                 DataRange;
  BOOL                        bFixedSizeSamples;
  BOOL                        bTemporalCompression;
  DWORD                       StreamDescriptionFlags;
  DWORD                       MemoryAllocationFlags;
  KS_VIDEO_STREAM_CONFIG_CAPS ConfigCaps;
  KS_H264VIDEOINFO            VideoInfoHeader;
} KS_DATARANGE_H264_VIDEO, *PKS_DATARANGE_H264_VIDEO;
````


## -struct-fields

### -field DataRange

Specifies the major identifier for the format.

### -field bFixedSizeSamples

Specifies that all the samples are the same size if set to <b>TRUE</b>.

### -field bTemporalCompression

Specifies whether each sample can stand independently on its own, without relying on previous or future samples.

### -field StreamDescriptionFlags

Unused and should be set to zero.

### -field MemoryAllocationFlags

Unused and should be set to zero.

### -field ConfigCaps

Specifies the configuration of the stream, including scaling, cropping, and frame and data rates.

### -field VideoInfoHeader

Specifies the details of the video stream.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 8
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2012
</td>
</tr>
<tr>
<th width="30%">
Header
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
<a href="stream.ksdatarange">KSDATARANGE</a>
</dt>
<dt>
<a href="stream.ks_video_stream_config_caps">KS_VIDEO_STREAM_CONFIG_CAPS</a>
</dt>
<dt>
<a href="stream.ks_h264videoinfo">KS_H264VIDEOINFO</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KS_DATARANGE_H264_VIDEO structure%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
