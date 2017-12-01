---
UID: NN.portcls.IMiniportAudioEngineNode
title: IMiniportAudioEngineNode
author: windows-driver-content
description: This interface allows a miniport driver to use KS properties that access the audio engine via a KS filter handle.
old-location: audio\iminiportaudioenginenode.htm
old-project: audio
ms.assetid: 58170D54-869A-49CC-865A-AB64BFB41A4B
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PcUnregisterIoTimeout
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: portcls.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IMiniportAudioEngineNode
req.alt-loc: Portcls.h
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
req.iface: 
---

# IMiniportAudioEngineNode interface



## -description
<p>This interface allows a miniport driver to use KS properties that access the audio engine via a KS filter handle.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IMiniportAudioEngineNode</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IMiniportAudioEngineNode</b> also has these types of members:</p>

<p>The <b>IMiniportAudioEngineNode</b> interface has these methods.</p>

<p>Gets the descriptor for the audio engine node.</p>

<p>Gets the minimum and maximum buffer size that the hardware audio engine can support.</p>

<p>Gets the allowed stepping value for the audio device attribute.</p>

<p>Gets a count of the number of channels supported by the audio device.</p>

<p>Gets the state of the Mute node for the audio device channel.</p>

<p>Gets the PeakMeter value  for the audio device channel.</p>

<p>Gets the volume level for a given channel of the audio device.</p>

<p>Gets the audio data format for an audio device.</p>

<p>Gets the format type and the buffer size for the audio engine's audio data format.</p>

<p>Gets the state of the global effects (GFX) node in the audio engine.</p>

<p>Gets the audio data format for the audio engine mixer.</p>

<p>Gets the supported audio data formats for the audio device.</p>

<p>Sets the state of the Mute node for the audio device channel.</p>

<p>Sets the volume level for a given channel of the audio device.</p>

<p>Sets the audio data format for an audio device.</p>

<p>Sets the state of the global effects (GFX) node in the audio engine.</p>

<p> </p>

## -members
<p>The <b>IMiniportAudioEngineNode</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iminiportaudioenginenode_getaudioenginedescriptor">GetAudioEngineDescriptor</a>
</td>
<td align="left" width="63%">
<p>Gets the descriptor for the audio engine node.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iminiportaudioenginenode_getbuffersizerange">GetBufferSizeRange</a>
</td>
<td align="left" width="63%">
<p>Gets the minimum and maximum buffer size that the hardware audio engine can support.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iminiportaudioenginenode_getdeviceattributesteppings">GetDeviceAttributeSteppings</a>
</td>
<td align="left" width="63%">
<p>Gets the allowed stepping value for the audio device attribute.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iminiportaudioenginenode_getdevicechannelcount">GetDeviceChannelCount</a>
</td>
<td align="left" width="63%">
<p>Gets a count of the number of channels supported by the audio device.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iminiportaudioenginenode_getdevicechannelmute">GetDeviceChannelMute</a>
</td>
<td align="left" width="63%">
<p>Gets the state of the Mute node for the audio device channel.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iminiportaudioenginenode_getdevicechannelpeakmeter">GetDeviceChannelPeakMeter</a>
</td>
<td align="left" width="63%">
<p>Gets the PeakMeter value  for the audio device channel.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iminiportaudioenginenode_getdevicechannelvolume">GetDeviceChannelVolume</a>
</td>
<td align="left" width="63%">
<p>Gets the volume level for a given channel of the audio device.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iminiportaudioenginenode_getdeviceformat">GetDeviceFormat</a>
</td>
<td align="left" width="63%">
<p>Gets the audio data format for an audio device.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iminiportaudioenginenode_getengineformatsize">GetEngineFormatSize</a>
</td>
<td align="left" width="63%">
<p>Gets the format type and the buffer size for the audio engine's audio data format.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iminiportaudioenginenode_getgfxstate">GetGfxState</a>
</td>
<td align="left" width="63%">
<p>Gets the state of the global effects (GFX) node in the audio engine.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iminiportaudioenginenode_getmixformat">GetMixFormat</a>
</td>
<td align="left" width="63%">
<p>Gets the audio data format for the audio engine mixer.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iminiportaudioenginenode_getsupporteddeviceformats">GetSupportedDeviceFormats</a>
</td>
<td align="left" width="63%">
<p>Gets the supported audio data formats for the audio device.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iminiportaudioenginenode_setdevicechannelmute">SetDeviceChannelMute</a>
</td>
<td align="left" width="63%">
<p>Sets the state of the Mute node for the audio device channel.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iminiportaudioenginenode_setdevicechannelvolume">SetDeviceChannelVolume</a>
</td>
<td align="left" width="63%">
<p>Sets the volume level for a given channel of the audio device.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iminiportaudioenginenode_setdeviceformat">SetDeviceFormat</a>
</td>
<td align="left" width="63%">
<p>Sets the audio data format for an audio device.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iminiportaudioenginenode_setgfxstate">SetGfxState</a>
</td>
<td align="left" width="63%">
<p>Sets the state of the global effects (GFX) node in the audio engine.</p>
</td>
</tr>
</table><p>Gets the descriptor for the audio engine node.</p>

<p>Gets the minimum and maximum buffer size that the hardware audio engine can support.</p>

<p>Gets the allowed stepping value for the audio device attribute.</p>

<p>Gets a count of the number of channels supported by the audio device.</p>

<p>Gets the state of the Mute node for the audio device channel.</p>

<p>Gets the PeakMeter value  for the audio device channel.</p>

<p>Gets the volume level for a given channel of the audio device.</p>

<p>Gets the audio data format for an audio device.</p>

<p>Gets the format type and the buffer size for the audio engine's audio data format.</p>

<p>Gets the state of the global effects (GFX) node in the audio engine.</p>

<p>Gets the audio data format for the audio engine mixer.</p>

<p>Gets the supported audio data formats for the audio device.</p>

<p>Sets the state of the Mute node for the audio device channel.</p>

<p>Sets the volume level for a given channel of the audio device.</p>

<p>Sets the audio data format for an audio device.</p>

<p>Sets the state of the global effects (GFX) node in the audio engine.</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h</dt>
</dl>
</td>
</tr>
</table>