---
UID: NS.ksmedia.PKSAUDIO_POSITIONEX
title: PKSAUDIO_POSITIONEX
author: windows-driver-content
description: The KSAUDIO_POSITIONEX structure specifies the stream position and the associated timestamp information for a kernel streaming (KS)-based audio driver.
old-location: audio\ksaudio_positionex.htm
old-project: audio
ms.assetid: 63cd938c-1ccd-4f67-a4eb-2898002ae762
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSAUDIO_POSITIONEX, KSAUDIO_POSITIONEX, *PKSAUDIO_POSITIONEX
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSAUDIO_POSITIONEX
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

# PKSAUDIO_POSITIONEX structure



## -description
<p>The KSAUDIO_POSITIONEX structure specifies the stream position and the associated timestamp information for a kernel streaming (KS)-based audio driver.</p>


## -syntax

````
typedef struct {
  LARGE_INTEGER    TimerFrequency;
  LARGE_INTEGER    TimeStamp1;
  KSAUDIO_POSITION Position;
  LARGE_INTEGER    TimeStamp2;
} KSAUDIO_POSITIONEX, *PKSAUDIO_POSITIONEX;
````


## -struct-fields
<dl>

### -field <b>TimerFrequency</b>

<dd>
<p>Specifies the number of ticks per second for the timer that produces the timestamps.</p>
</dd>

### -field <b>TimeStamp1</b>

<dd>
<p>Specifies the timestamp that is taken immediately prior to the acquisition of the position information.</p>
</dd>

### -field <b>Position</b>

<dd>
<p>Specifies the position of the read cursor and the write cursor in the audio buffer of an audio stream.</p>
</dd>

### -field <b>TimeStamp2</b>

<dd>
<p>Specifies the timestamp that is taken immediately after the acquisition of the position information.</p>
</dd>
</dl>

## -remarks
<p>A KS-based audio driver can use the KSAUDIO_POSITIONEX structure along with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537298">KSPROPERTY_AUDIO_POSITIONEX</a> property to return a stream position and a timestamp.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of Windows.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537298">KSPROPERTY_AUDIO_POSITIONEX</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20KSAUDIO_POSITIONEX structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
