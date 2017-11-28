---
UID: NS.dmusprop._SYNTH_PORTPARAMS
title: SYNTH_PORTPARAMS
author: windows-driver-content
description: The SYNTH_PORTPARAMS structure contains the configuration parameters for a DirectMusic port, which is a DirectMusic term for a device that sends or receives music data.
old-location: audio\synth_portparams.htm
old-project: audio
ms.assetid: 94c953ae-519b-4659-a4c9-a97db7dc31e9
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: SYNTH_PORTPARAMS, SYNTH_PORTPARAMS, *PSYNTH_PORTPARAMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dmusprop.h
req.include-header: Dmusprop.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SYNTH_PORTPARAMS
req.alt-loc: dmusprop.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: ISynthSinkDMus
---

# SYNTH_PORTPARAMS structure



## -description
<p>The SYNTH_PORTPARAMS structure contains the configuration parameters for a DirectMusic <i>port</i>, which is a DirectMusic term for a device that sends or receives music data. (In KS terminology, a DirectMusic port does not correspond to a DMus port driver. It corresponds to a render or capture pin on a DirectMusic filter.)</p>


## -syntax

````
typedef struct _SYNTH_PORTPARAMS {
  DWORD ValidParams;
  DWORD Voices;
  DWORD ChannelGroups;
  DWORD AudioChannels;
  DWORD SampleRate;
  DWORD EffectsFlags;
  DWORD Share;
} SYNTH_PORTPARAMS, *PSYNTH_PORTPARAMS;
````


## -struct-fields
<dl>

### -field <b>ValidParams</b>

<dd>
<p>Specifies which of the SYNTH_PORTPARAMS structure members contain valid data. This member is a bitfield whose value is either zero or the bitwise OR of one or more of the following flag bits:</p>
<p></p>
<dl>

### -field <a id="SYNTH_PORTPARAMS_VOICES_"></a><a id="synth_portparams_voices_"></a>SYNTH_PORTPARAMS_VOICES 

<dd>
<p>The <b>Voices</b> field is valid.</p>
</dd>

### -field <a id="SYNTH_PORTPARAMS_CHANNELGROUPS_"></a><a id="synth_portparams_channelgroups_"></a>SYNTH_PORTPARAMS_CHANNELGROUPS 

<dd>
<p>The <b>ChannelGroups</b> field is valid.</p>
</dd>

### -field <a id="SYNTH_PORTPARAMS_AUDIOCHANNELS_"></a><a id="synth_portparams_audiochannels_"></a>SYNTH_PORTPARAMS_AUDIOCHANNELS 

<dd>
<p>The <b>AudioChannels</b> field is valid.</p>
</dd>

### -field <a id="SYNTH_PORTPARAMS_SAMPLERATE_"></a><a id="synth_portparams_samplerate_"></a>SYNTH_PORTPARAMS_SAMPLERATE 

<dd>
<p>The <b>SampleRate</b> field is valid.</p>
</dd>

### -field <a id="SYNTH_PORTPARAMS_EFFECT"></a><a id="synth_portparams_effect"></a>SYNTH_PORTPARAMS_EFFECT

<dd>
<p>The <b>EffectsFlags</b> flag is valid.</p>
</dd>

### -field <a id="SYNTH_PORTPARAMS_SHARE"></a><a id="synth_portparams_share"></a>SYNTH_PORTPARAMS_SHARE

<dd>
<p>The <b>Share</b> field is valid.</p>
</dd>
</dl>
</dd>

### -field <b>Voices</b>

<dd>
<p>Specifies the maximum number of simultaneous voices that the application wishes to play on this port.</p>
</dd>

### -field <b>ChannelGroups</b>

<dd>
<p>Specifies the number of channel groups requested for this port. Each channel group contains 16 channels.</p>
</dd>

### -field <b>AudioChannels</b>

<dd>
<p>Specifies the number of audio channels.</p>
</dd>

### -field <b>SampleRate</b>

<dd>
<p>Specifies the number of samples per second for the audio data produced by the port.</p>
</dd>

### -field <b>EffectsFlags</b>

<dd>
<p>Specifies the type of effects produced for audio output from this port. This member is a bitfield whose value is either zero or the bitwise OR of one or more of the following flag bits:</p>
<p></p>
<dl>

### -field <a id="SYNTH_EFFECT_REVERB"></a><a id="synth_effect_reverb"></a>SYNTH_EFFECT_REVERB

<dd>
<p>Reverb is enabled.</p>
</dd>

### -field <a id="SYNTH_EFFECT_CHORUS"></a><a id="synth_effect_chorus"></a>SYNTH_EFFECT_CHORUS

<dd>
<p>Chorus effect is enabled.</p>
</dd>

### -field <a id="SYNTH_EFFECT_DELAY"></a><a id="synth_effect_delay"></a>SYNTH_EFFECT_DELAY

<dd>
<p>Delay effect is enabled.</p>
</dd>
</dl>
<p>If no effects are enabled, this member is set to SYNTH_EFFECT_NONE, which is zero.</p>
</dd>

### -field <b>Share</b>

<dd>
<p>Specifies whether the port's channel groups are shared. When this member is <b>TRUE</b>, all ports use the channel groups assigned to this port. When this member is <b>FALSE</b>, the port is opened in exclusive mode and the use of the same channel groups by other ports is not allowed.</p>
</dd>
</dl>

## -remarks
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff537405">KSPROPERTY_SYNTH_PORTPARAMETERS</a> get-property request uses the SYNTH_PORTPARAMS structure for both its property descriptor and its property value.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dmusprop.h (include Dmusprop.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537405">KSPROPERTY_SYNTH_PORTPARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20SYNTH_PORTPARAMS structure%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
