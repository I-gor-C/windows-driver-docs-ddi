---
UID: NS.ksmedia.PKSDATARANGE_AUDIO
title: PKSDATARANGE_AUDIO
author: windows-driver-content
description: The KSDATARANGE_AUDIO structure specifies a range of audio formats.
old-location: audio\ksdatarange_audio.htm
ms.assetid: 53631f26-8377-4ab5-83db-ed241c11643a
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: audio
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSDATARANGE_AUDIO
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
ms.keywords: PKSDATARANGE_AUDIO, KSDATARANGE_AUDIO, *PKSDATARANGE_AUDIO
req.iface: 
---

# PKSDATARANGE_AUDIO structure



## -description
<p>The KSDATARANGE_AUDIO structure specifies a range of audio formats.</p>


## -syntax

````
typedef struct {
  KSDATARANGE DataRange;
  ULONG       MaximumChannels;
  ULONG       MinimumBitsPerSample;
  ULONG       MaximumBitsPerSample;
  ULONG       MinimumSampleFrequency;
  ULONG       MaximumSampleFrequency;
} KSDATARANGE_AUDIO, *PKSDATARANGE_AUDIO;
````


## -struct-fields
<dl>

### -field <b>DataRange</b>

<dd>
<p>Specifies the MajorFormat and SubFormat GUIDs as well as the Specifier GUID for the audio data. This member is an initialized <a href="https://msdn.microsoft.com/library/windows/hardware/ff561658">KSDATARANGE</a> structure.</p>
</dd>

### -field <b>MaximumChannels</b>

<dd>
<p>Specifies the maximum number of channels supported. A value of (ULONG)-1 for this member means that the number of channels has no explicit limit, although the number of channels might be practically limited by the availability of resources such as memory or processing power.</p>
</dd>

### -field <b>MinimumBitsPerSample</b>

<dd>
<p>Specifies the minimum bits per sample supported.</p>
</dd>

### -field <b>MaximumBitsPerSample</b>

<dd>
<p>Specifies the maximum bits per sample supported.</p>
</dd>

### -field <b>MinimumSampleFrequency</b>

<dd>
<p>Specifies the minimum frequency allowed.</p>
</dd>

### -field <b>MaximumSampleFrequency</b>

<dd>
<p>Specifies the maximum frequency allowed.</p>
</dd>
</dl>

## -remarks
<p>For examples of data ranges that use the KSDATARANGE_AUDIO structure, see <a href="NULL">PCM Stream Data Range</a>, <a href="NULL">DirectSound Stream Data Range</a>, and <a href="NULL">Specifying AC-3 Data Ranges</a>.</p>

<p>For information about data ranges and intersection handling, see <a href="NULL">Data-Intersection Handlers</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561658">KSDATARANGE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20KSDATARANGE_AUDIO structure%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
