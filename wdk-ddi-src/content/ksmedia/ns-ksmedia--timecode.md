---
UID: NS.ksmedia._timecode
title: timecode
author: windows-driver-content
description: The TIMECODE union describes a timecode from an external device. This structure is no longer used.
old-location: stream\timecode.htm
ms.assetid: 3387e014-3a62-4d76-ac6d-6446e4fa39d0
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
req.alt-api: TIMECODE
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
ms.keywords: timecode, TIMECODE
req.iface: 
---

# timecode structure



## -description
<p>The TIMECODE union describes a timecode from an external device. This structure is no longer used.</p>


## -syntax

````
typedef union _timecode {
  struct {
    WORD  wFrameRate;
    WORD  wFrameFract;
    DWORD dwFrames;
  };
  DWORDLONG qw;
} TIMECODE, *PTIMECODE;
````


## -struct-fields
<dl>

### -field <b>wFrameRate</b>

<dd>
<p>Specifies the frame rate.</p>
</dd>

### -field <b>wFrameFract</b>

<dd>
<p>Specifies the fractional frame. The full-scale frame is 0x1000.</p>
</dd>

### -field <b>dwFrames</b>

<dd>
<p>Specifies a timecode value as a binary frame count.</p>
</dd>

### -field <b>qw</b>

<dd>
<p>Specifies the timecode as a quad-word.</p>
</dd>
</dl>

## -remarks
<p>This structure is defined for the purpose of searching to a timecode based on an absolute track number (ATN) and/or relative time counter (RTC). However, not all devices support searching to a timecode using this structure.</p>

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
<a href="https://msdn.microsoft.com/f3ff3815-0f4f-4fcb-89bd-e77d8002813c">KSPROPERTY_EXTXPORT_RAW_AVC_CMD</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20TIMECODE union%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
