---
UID: NS.ksmedia.PKSDATARANGE_MUSIC
title: PKSDATARANGE_MUSIC
author: windows-driver-content
description: The KSDATARANGE_MUSIC structure specifies a range of DirectMusic MIDI formats.
old-location: audio\ksdatarange_music.htm
ms.assetid: 2ada5d1c-9c46-4f7b-99e5-72aa8f6fee9f
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
req.alt-api: KSDATARANGE_MUSIC
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
ms.keywords: PKSDATARANGE_MUSIC, KSDATARANGE_MUSIC, *PKSDATARANGE_MUSIC
req.iface: 
---

# PKSDATARANGE_MUSIC structure



## -description
<p>The KSDATARANGE_MUSIC structure specifies a range of DirectMusic MIDI formats.</p>


## -syntax

````
typedef struct {
  KSDATARANGE DataRange;
  GUID        Technology;
  ULONG       Channels;
  ULONG       Notes;
  ULONG       ChannelMask;
} KSDATARANGE_MUSIC, *PKSDATARANGE_MUSIC;
````


## -struct-fields
<dl>

### -field <b>DataRange</b>

<dd>
<p>Specifies the MajorFormat and SubFormat GUIDs as well as the Specifier GUID for the DirectMusic data. This member is an initialized <a href="https://msdn.microsoft.com/library/windows/hardware/ff561658">KSDATARANGE</a> structure.</p>
</dd>

### -field <b>Technology</b>

<dd>
<p>Specifies the type of MIDI output device. This member can be one of the following GUIDs:</p>
<p></p>
<dl>

### -field <a id="KSMUSIC_TECHNOLOGY_PORT"></a><a id="ksmusic_technology_port"></a>KSMUSIC_TECHNOLOGY_PORT

<dd>
<p>The device is a MIDI hardware port.</p>
</dd>

### -field <a id="KSMUSIC_TECHNOLOGY_SYNTH"></a><a id="ksmusic_technology_synth"></a>KSMUSIC_TECHNOLOGY_SYNTH

<dd>
<p>The device is a synthesizer.</p>
</dd>

### -field <a id="KSMUSIC_TECHNOLOGY_SQSYNTH"></a><a id="ksmusic_technology_sqsynth"></a>KSMUSIC_TECHNOLOGY_SQSYNTH

<dd>
<p>The device is a square-wave synthesizer.</p>
</dd>

### -field <a id="KSMUSIC_TECHNOLOGY_FMSYNTH"></a><a id="ksmusic_technology_fmsynth"></a>KSMUSIC_TECHNOLOGY_FMSYNTH

<dd>
<p>The device is an FM synthesizer.</p>
</dd>

### -field <a id="KSMUSIC_TECHNOLOGY_MAPPER"></a><a id="ksmusic_technology_mapper"></a>KSMUSIC_TECHNOLOGY_MAPPER

<dd>
<p>The device is the Microsoft MIDI mapper.</p>
</dd>

### -field <a id="KSMUSIC_TECHNOLOGY_WAVETABLE"></a><a id="ksmusic_technology_wavetable"></a>KSMUSIC_TECHNOLOGY_WAVETABLE

<dd>
<p>The device is a hardware wavetable synthesizer.</p>
</dd>

### -field <a id="KSMUSIC_TECHNOLOGY_SWSYNTH"></a><a id="ksmusic_technology_swsynth"></a>KSMUSIC_TECHNOLOGY_SWSYNTH

<dd>
<p>The device is a software synthesizer.</p>
</dd>
</dl>
</dd>

### -field <b>Channels</b>

<dd>
<p>Specifies the maximum number of simultaneous channels that can be played by an internal synthesizer device. If the device is a port, this member is not meaningful and is set to zero.</p>
</dd>

### -field <b>Notes</b>

<dd>
<p>Specifies the maximum number of simultaneous notes that can be played by an internal synthesizer device. If the device is a port, this member is not meaningful and is set to zero.</p>
</dd>

### -field <b>ChannelMask</b>

<dd>
<p>Specifies which channels an internal synthesizer device responds to, where the least significant bit refers to channel 0 and the most significant bit to channel 15. Port devices that transmit on all channels set this member to 0xFFFF.</p>
</dd>
</dl>

## -remarks
<p>For examples of data ranges that use the KSDATARANGE_MUSIC structure, see <a href="NULL">MIDI Stream Data Range</a> and <a href="NULL">DirectMusic Stream Data Range</a>.</p>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20KSDATARANGE_MUSIC structure%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
