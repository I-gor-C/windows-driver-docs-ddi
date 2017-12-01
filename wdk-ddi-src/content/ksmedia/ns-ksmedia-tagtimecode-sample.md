---
UID: NS.ksmedia.tagTIMECODE_SAMPLE
title: tagTIMECODE_SAMPLE
author: windows-driver-content
description: The TIMECODE_SAMPLE structure describes a complete timecode.
old-location: stream\timecode_sample.htm
old-project: stream
ms.assetid: 01654107-29a1-4f34-bb9a-a17fe36a84fe
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: tagTIMECODE_SAMPLE, TIMECODE_SAMPLE
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
req.alt-api: TIMECODE_SAMPLE
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

# tagTIMECODE_SAMPLE structure



## -description
<p>The TIMECODE_SAMPLE structure describes a complete timecode.</p>


## -syntax

````
typedef struct tagTIMECODE_SAMPLE {
  LONGLONG qwTick;
  TIMECODE timecode;
  DWORD    dwUser;
  DWORD    dwFlags;
} TIMECODE_SAMPLE;
````


## -struct-fields
<dl>

### -field <b>qwTick</b>

<dd>
<p>Specifies a reference time, in 100-nanosecond units.</p>
</dd>

### -field <b>timecode</b>

<dd>
<p>Specifies the <a href="..\ksmedia\ns-ksmedia--timecode.md">TIMECODE</a> structure.</p>
</dd>

### -field <b>dwUser</b>

<dd>
<p>Specifies packed SMPTE user-bits.</p>
</dd>

### -field <b>dwFlags</b>

<dd>
<p>Specifies any optional timecode flag masks.</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>AM_TIMECODE_FLAG_FCM</p>
</td>
<td>
<p>Frame-code mode; 0 = nondrop; 1 = drop.</p>
</td>
</tr>
<tr>
<td>
<p>AM_TIMECODE_FLAG_CF</p>
</td>
<td>
<p>Color-frame flag.</p>
</td>
</tr>
<tr>
<td>
<p>AM_TIMECODE_FLAG_FIELD</p>
</td>
<td>
<p>Field flag.</p>
</td>
</tr>
<tr>
<td>
<p>AM_TIMECODE_FLAG_DF</p>
</td>
<td>
<p>Drop-frame flag (from flags in actual timecode on external media).</p>
</td>
</tr>
<tr>
<td>
<p>AM_TIMECODE_COLORFRAME</p>
</td>
<td>
<p>Specifies frame, in color sequence.</p>
</td>
</tr>
<tr>
<td>
<p>AM_TIMECODE_COLORSEQUENCE</p>
</td>
<td>
<p>Duration, in frames, of complete sequence.</p>
</td>
</tr>
<tr>
<td>
<p>AM_TIMECODE_FILMSEQUENCE_TYPE</p>
</td>
<td>
<p>One of the FILM_SEQUENCE_<i>XXX</i> tokens.</p>
</td>
</tr>
<tr>
<td>
<p>ED_DEVCAP_TIMECODE_READ</p>
</td>
<td>
<p>Read SMPTE timecode; applies to DV camcorders.</p>
</td>
</tr>
<tr>
<td>
<p>ED_DEVCAP_ATN_READ</p>
</td>
<td>
<p>Read the absolute track number (ATN); applies to DV camcorders.</p>
</td>
</tr>
<tr>
<td>
<p>ED_DEVCAP_RTC_READ</p>
</td>
<td>
<p>Read the relative time counter (RTC); applies to MPEG camcorders.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks
<p>Any ED_Xxx tokens are defined in <i>xprtdefs.h</i> in the DirectX SDK.</p>

<p>The upper 16 bits in <b>dwFlags</b> are reserved for future use and must be set to zero.</p>

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
<a href="..\ksmedia\ns-ksmedia--timecode.md">TIMECODE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20TIMECODE_SAMPLE structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
