---
UID: NS.ksmedia.PKSAC3_ALTERNATE_AUDIO
title: PKSAC3_ALTERNATE_AUDIO
author: windows-driver-content
description: The KSAC3_ALTERNATE_AUDIO structure specifies whether the two mono channels in an AC-3-encoded stream should be interpreted as a stereo pair or as two independent program channels.
old-location: audio\ksac3_alternate_audio.htm
old-project: audio
ms.assetid: 9b97deb9-7e64-49a1-8278-08084c8b7c84
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSAC3_ALTERNATE_AUDIO, KSAC3_ALTERNATE_AUDIO, *PKSAC3_ALTERNATE_AUDIO
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
req.alt-api: KSAC3_ALTERNATE_AUDIO
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

# PKSAC3_ALTERNATE_AUDIO structure



## -description
<p>The KSAC3_ALTERNATE_AUDIO structure specifies whether the two mono channels in an AC-3-encoded stream should be interpreted as a stereo pair or as two independent program channels.</p>


## -syntax

````
typedef struct {
  BOOL  fStereo;
  ULONG DualMode;
} KSAC3_ALTERNATE_AUDIO, *PKSAC3_ALTERNATE_AUDIO;
````


## -struct-fields
<dl>

### -field fStereo

<dd>
<p>Specifies whether the two mono channels should be interpreted as a stereo pair. If <b>TRUE</b>, the two mono channels are treated as a stereo pair. If <b>FALSE</b>, <b>DualMode</b>=0x03 causes the two mono channels to be mixed before being output by the decoder.</p>
</dd>

### -field DualMode

<dd>
<p>When two independent channels of audio are encoded in the stream, this member specifies whether to use the audio track in channel 1, channel 2, or both. A value of 0x01 selects channel 1, 0x02 selects channel 2, and 0x03 selects both. Specify the value of this member as one of the following constants:</p>
<table>
<tr>
<th>Constant name</th>
<th>Value</th>
</tr>
<tr>
<td>
<p>KSAC3_ALTERNATE_AUDIO_1</p>
</td>
<td>
<p>0x01</p>
</td>
</tr>
<tr>
<td>
<p>KSAC3_ALTERNATE_AUDIO_2</p>
</td>
<td>
<p>0x02</p>
</td>
</tr>
<tr>
<td>
<p>KSAC3_ALTERNATE_AUDIO_BOTH</p>
</td>
<td>
<p>0x03</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks
<p>This structure is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537210">KSPROPERTY_AC3_ALTERNATE_AUDIO</a> property.</p>

<p>For more information about the encoding of AC-3 program channels, see the AC-3 specification at the <a href="http://go.microsoft.com/fwlink/p/?linkid=8730">Dolby Laboratories</a> website. The specification is titled Digital Audio Compression Standard (AC-3).</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537210">KSPROPERTY_AC3_ALTERNATE_AUDIO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20KSAC3_ALTERNATE_AUDIO structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
