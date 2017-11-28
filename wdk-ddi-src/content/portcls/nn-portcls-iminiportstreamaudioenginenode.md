---
UID: NN.portcls.IMiniportStreamAudioEngineNode
title: IMiniportStreamAudioEngineNode
author: windows-driver-content
description: This interface allows a miniport driver to use KS properties that access the audio engine via a pin instance handle.
old-location: audio\iminiportstreamaudioenginenode.htm
old-project: audio
ms.assetid: B3F7D3AC-C756-47D2-9E7C-7930621753C3
ms.author: windowsdriverdev
ms.date: 11/21/2017
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
req.alt-api: IMiniportStreamAudioEngineNode
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

# IMiniportStreamAudioEngineNode interface



## -description
<p>This interface allows a miniport driver to use KS properties that access the audio engine via a pin instance handle.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IMiniportStreamAudioEngineNode</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IMiniportStreamAudioEngineNode</b> also has these types of members:</p>

<p>The <b>IMiniportStreamAudioEngineNode</b> interface has these methods.</p>

<p>Gets the state of the local effects (LFX) node that is in the path of the audio stream.</p>

<p>Gets the allowed stepping value for the audio stream attribute.</p>

<p>Gets a count of the number of channels available for the stream.</p>

<p>Gets the state of the Mute node in the path of the audio stream.</p>

<p>Gets the value of the PeakMeter node in the path of the audio stream.</p>

<p>Gets the current volume level that is applied to the audio stream.</p>

<p>	Gets the number of bytes that the DMA has fetched from the audio buffer since the beginning of the stream.</p>

<p>Gets the current cursor position in the audio data stream that is being rendered to the endpoint.</p>

<p>Sets the state of the local effects (LFX) node that is in the path of the audio stream.</p>

<p>Sets the state of the Mute node in the path of the audio stream.</p>

<p>Sets the volume level to be applied to the audio stream.</p>

<p>Sets the current cursor position in the audio data stream that is being captured from the endpoint.</p>

<p>Sets the loopback protection status of the audio engine node.</p>

<p> </p>

## -members
<p>The <b>IMiniportStreamAudioEngineNode</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265091">GetLfxState</a>
</td>
<td align="left" width="63%">
<p>Gets the state of the local effects (LFX) node that is in the path of the audio stream.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265092">GetStreamAttributeSteppings</a>
</td>
<td align="left" width="63%">
<p>Gets the allowed stepping value for the audio stream attribute.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265093">GetStreamChannelCount</a>
</td>
<td align="left" width="63%">
<p>Gets a count of the number of channels available for the stream.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265094">GetStreamChannelMute</a>
</td>
<td align="left" width="63%">
<p>Gets the state of the Mute node in the path of the audio stream.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265095">GetStreamChannelPeakMeter</a>
</td>
<td align="left" width="63%">
<p>Gets the value of the PeakMeter node in the path of the audio stream.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265096">GetStreamChannelVolume</a>
</td>
<td align="left" width="63%">
<p>Gets the current volume level that is applied to the audio stream.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265097">GetStreamLinearBufferPosition</a>
</td>
<td align="left" width="63%">
<p>	Gets the number of bytes that the DMA has fetched from the audio buffer since the beginning of the stream.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265098">GetStreamPresentationPosition</a>
</td>
<td align="left" width="63%">
<p>Gets the current cursor position in the audio data stream that is being rendered to the endpoint.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265099">SetLfxState</a>
</td>
<td align="left" width="63%">
<p>Sets the state of the local effects (LFX) node that is in the path of the audio stream.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265100">SetStreamChannelMute</a>
</td>
<td align="left" width="63%">
<p>Sets the state of the Mute node in the path of the audio stream.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265101">SetStreamChannelVolume</a>
</td>
<td align="left" width="63%">
<p>Sets the volume level to be applied to the audio stream.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265102">SetStreamCurrentWritePosition</a>
</td>
<td align="left" width="63%">
<p>Sets the current cursor position in the audio data stream that is being captured from the endpoint.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265103">SetStreamLoopbackProtection</a>
</td>
<td align="left" width="63%">
<p>Sets the loopback protection status of the audio engine node.</p>
</td>
</tr>
</table><p>Gets the state of the local effects (LFX) node that is in the path of the audio stream.</p>

<p>Gets the allowed stepping value for the audio stream attribute.</p>

<p>Gets a count of the number of channels available for the stream.</p>

<p>Gets the state of the Mute node in the path of the audio stream.</p>

<p>Gets the value of the PeakMeter node in the path of the audio stream.</p>

<p>Gets the current volume level that is applied to the audio stream.</p>

<p>	Gets the number of bytes that the DMA has fetched from the audio buffer since the beginning of the stream.</p>

<p>Gets the current cursor position in the audio data stream that is being rendered to the endpoint.</p>

<p>Sets the state of the local effects (LFX) node that is in the path of the audio stream.</p>

<p>Sets the state of the Mute node in the path of the audio stream.</p>

<p>Sets the volume level to be applied to the audio stream.</p>

<p>Sets the current cursor position in the audio data stream that is being captured from the endpoint.</p>

<p>Sets the loopback protection status of the audio engine node.</p>

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