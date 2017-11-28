---
UID: NS.ksmedia.tagKS_MPEGVIDEOINFO2
title: tagKS_MPEGVIDEOINFO2
author: windows-driver-content
description: The KS_MPEGVIDEOINFO2 structure describes an MPEG-2 video stream, including bob or weave settings.
old-location: stream\ks_mpegvideoinfo2.htm
old-project: stream
ms.assetid: 735bff90-7406-4fe8-87d5-de3aa48fbcd0
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: tagKS_MPEGVIDEOINFO2, KS_MPEGVIDEOINFO2, *PKS_MPEGVIDEOINFO2
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
req.alt-api: KS_MPEGVIDEOINFO2
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

# tagKS_MPEGVIDEOINFO2 structure



## -description
<p>The KS_MPEGVIDEOINFO2 structure describes an MPEG-2 video stream, including bob or weave settings.</p>


## -syntax

````
typedef struct tagKS_MPEGVIDEOINFO2 {
  KS_VIDEOINFOHEADER2 hdr;
  DWORD               dwStartTimeCode;
  DWORD               cbSequenceHeader;
  DWORD               dwProfile;
  DWORD               dwLevel;
  DWORD               dwFlags;
  DWORD               bSequenceHeader[1];
} KS_MPEGVIDEOINFO2, *PKS_MPEGVIDEOINFO2;
````


## -struct-fields
<dl>

### -field <b>hdr</b>

<dd>
<p>Specifies a <a href="https://msdn.microsoft.com/library/windows/hardware/ff567702">KS_VIDEOINFOHEADER2</a> structure that describes the details of the video stream.</p>
</dd>

### -field <b>dwStartTimeCode</b>

<dd>
<p>A 25-bit "group-of-pictures" time code at the start of data (not used for DVD).</p>
</dd>

### -field <b>cbSequenceHeader</b>

<dd>
<p>The length of the <b>bSequenceHeader</b> member, in bytes (zero for DVD).</p>
</dd>

### -field <b>dwProfile</b>

<dd>
<p>Specifies the MPEG-2 profile. This member must be one of the values from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567662">KS_MPEG2Profile</a> enumeration.</p>
</dd>

### -field <b>dwLevel</b>

<dd>
<p>Specifies the MPEG-2 level. This member must be one of the values from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567660">KS_MPEG2Level</a> enumeration.</p>
</dd>

### -field <b>dwFlags</b>

<dd>
<p>Specifies the flags that indicate preferences. This member can be set to one or more (logical OR) values that are defined in <i>ksmedia.h</i>.</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p><b>KS_MPEG2_DoPanScan</b></p>
</td>
<td>
<p>If set, the MPEG-2 video decoder should crop the output image based on pan-scan vectors in the picture display extension and change the picture aspect ratio accordingly.</p>
</td>
</tr>
<tr>
<td>
<p><b>KS_MPEG2_DVDLine21Field1</b></p>
</td>
<td>
<p>If set, the MPEG-2 decoder must be able to produce an output pin for DVD-style closed caption data found in the GOP layer of Field 1.</p>
</td>
</tr>
<tr>
<td>
<p><b>KS_MPEG2_DVDLine21Field2</b></p>
</td>
<td>
<p>If set, the MPEG-2 decoder must be able to produce an output pin for DVD-style closed caption data found in the GOP layer of Field 2.</p>
</td>
</tr>
<tr>
<td>
<p><b>KS_MPEG2_SourceIsLetterboxed</b></p>
</td>
<td>
<p>If set, indicates that black bars have been encoded in the top and bottom of the video.</p>
</td>
</tr>
<tr>
<td>
<p><b>KS_MPEG2_FilmCameraMode</b></p>
</td>
<td>
<p>If set, indicates "film mode" used for 625/50 content. If cleared, indicates that "camera mode" was used.</p>
</td>
</tr>
<tr>
<td>
<p><b>KS_MPEG2_LetterboxAnalogOut</b></p>
</td>
<td>
<p>If set, and the stream is sent to an analog output, then the stream should be letterboxed. Streams sent to VGA should be letterboxed only by renderers.</p>
</td>
</tr>
<tr>
<td>
<p><b>KS_MPEG2_DSS_UserData</b></p>
</td>
<td>
<p>If set, the MPEG-2 decoder must process DSS-style user data.</p>
</td>
</tr>
<tr>
<td>
<p><b>KS_MPEG2_DVB_UserData</b></p>
</td>
<td>
<p>If set, the MPEG-2 decoder must process DVB-style user data.</p>
</td>
</tr>
<tr>
<td>
<p><b>KS_MPEG2_27MHzTimebase</b></p>
</td>
<td>
<p>If set, the PTS and DTS timestamps advance at 27 MHz rather than 90 kHz.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>bSequenceHeader</b>

<dd>
<p>The length of the <b>bSequenceHeader</b> member, in bytes (zero for DVD).</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567702">KS_VIDEOINFOHEADER2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KS_MPEGVIDEOINFO2 structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
