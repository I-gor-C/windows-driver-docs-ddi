---
UID: NS.dmusprop._SYNTH_STATS
title: SYNTH_STATS
author: windows-driver-content
description: The SYNTH_STATS structure specifies synthesizer performance statistics such as the number of voices playing, CPU usage, number of notes lost, amount of free memory, and peak volume level.
old-location: audio\synth_stats.htm
old-project: audio
ms.assetid: bbe3552b-0289-4f7f-bdaa-8a6437594247
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: SYNTH_STATS, SYNTH_STATS, *PSYNTH_STATS
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
req.alt-api: SYNTH_STATS
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

# SYNTH_STATS structure



## -description
<p>The SYNTH_STATS structure specifies synthesizer performance statistics such as the number of voices playing, CPU usage, number of notes lost, amount of free memory, and peak volume level.</p>


## -syntax

````
typedef struct _SYNTH_STATS {
  DWORD ValidStats;
  DWORD Voices;
  DWORD TotalCPU;
  DWORD CPUPerVoice;
  DWORD LostNotes;
  DWORD FreeMemory;
  LONG  PeakVolume;
} SYNTH_STATS, *PSYNTH_STATS;
````


## -struct-fields
<dl>

### -field <b>ValidStats</b>

<dd>
<p>Specifies which members of the SYNTH_STATS structure contain valid data. This member is a bitfield whose value is either zero or a bitwise OR of one or more of the following flag bits:</p>
<p></p>
<dl>

### -field <a id="SYNTH_STATS_VOICES"></a><a id="synth_stats_voices"></a>SYNTH_STATS_VOICES

<dd>
<p>The <b>Voices</b> field contains valid data.</p>
</dd>

### -field <a id="SYNTH_STATS_TOTAL_CPU"></a><a id="synth_stats_total_cpu"></a>SYNTH_STATS_TOTAL_CPU

<dd>
<p>The <b>TotalCPU</b> field contains valid data.</p>
</dd>

### -field <a id="SYNTH_STATS_CPU_PER_VOICE"></a><a id="synth_stats_cpu_per_voice"></a>SYNTH_STATS_CPU_PER_VOICE

<dd>
<p>The <b>CPUPerVoice</b> field contains valid data.</p>
</dd>

### -field <a id="SYNTH_STATS_LOST_NOTES"></a><a id="synth_stats_lost_notes"></a>SYNTH_STATS_LOST_NOTES

<dd>
<p>The <b>LostNotes </b>field contains valid data.</p>
</dd>

### -field <a id="SYNTH_STATS_PEAK_VOLUME"></a><a id="synth_stats_peak_volume"></a>SYNTH_STATS_PEAK_VOLUME

<dd>
<p>The <b>PeakVolume </b>field contains valid data.</p>
</dd>

### -field <a id="SYNTH_STATS_FREE_MEMORY"></a><a id="synth_stats_free_memory"></a>SYNTH_STATS_FREE_MEMORY

<dd>
<p>The <b>FreeMemory</b> field contains valid data.</p>
</dd>
</dl>
</dd>

### -field <b>Voices</b>

<dd>
<p>Specifies the average number of voices playing.</p>
</dd>

### -field <b>TotalCPU</b>

<dd>
<p>Specifies the total CPU usage (all voices), which is expressed as a percentage (a fraction multiplied by 100).</p>
</dd>

### -field <b>CPUPerVoice</b>

<dd>
<p>Specifies the CPU usage per voice, which is expressed as a percentage (a fraction multiplied by 100).</p>
</dd>

### -field <b>LostNotes</b>

<dd>
<p>Specifies the number of notes lost. Notes can be dropped if the number of simultaneous voices exceeds the maximum specified by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537405">KSPROPERTY_SYNTH_PORTPARAMETERS</a> property. For additional information, see <a href="NULL">Voice Allocation</a>.</p>
</dd>

### -field <b>FreeMemory</b>

<dd>
<p>Specifies the amount of free memory in bytes. This is the storage that remains available for downloading additional DLS data resources.</p>
</dd>

### -field <b>PeakVolume</b>

<dd>
<p>Specifies the peak volume level expressed as decibels multiplied by 100.</p>
</dd>
</dl>

## -remarks
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff537406">KSPROPERTY_SYNTH_RUNNINGSTATS</a> property uses the SYNTH_STATS structure to query a DirectMusic miniport driver for statistics about a synthesizer.</p>

<p>The SYNTH_STATS structure is similar to the DMUS_SYNTHSTATS structure, which is described in the Microsoft Windows SDK documentation.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537406">KSPROPERTY_SYNTH_RUNNINGSTATS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537405">KSPROPERTY_SYNTH_PORTPARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20SYNTH_STATS structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
