---
UID: NN:portcls.IMiniportStreamAudioEngineNode
title: IMiniportStreamAudioEngineNode
author: windows-driver-content
description: This interface allows a miniport driver to use KS properties that access the audio engine via a pin instance handle.
old-location: audio\iminiportstreamaudioenginenode.htm
old-project: audio
ms.assetid: B3F7D3AC-C756-47D2-9E7C-7930621753C3
ms.author: windowsdriverdev
ms.date: 3/19/2018
ms.keywords: IMiniportStreamAudioEngineNode, IMiniportStreamAudioEngineNode interface [Audio Devices], IMiniportStreamAudioEngineNode interface [Audio Devices], described, audio.iminiportstreamaudioenginenode, portcls/IMiniportStreamAudioEngineNode
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
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Portcls.lib
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	Portcls.h
api_name:
-	IMiniportStreamAudioEngineNode
product:
- Windows
targetos: Windows
req.typenames: PC_EXIT_LATENCY, *PPC_EXIT_LATENCY
---

# IMiniportStreamAudioEngineNode interface

This interface allows a miniport driver to use KS properties that access the audio engine via a pin instance handle.

## Methods

<p>The <b>IMiniportStreamAudioEngineNode</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IMiniportStreamAudioEngineNode::GetLfxState](nf-portcls-iminiportstreamaudioenginenode-getlfxstate.md) | Gets the state of the local effects (LFX) node that is in the path of the audio stream. |
| [IMiniportStreamAudioEngineNode::GetStreamAttributeSteppings](nf-portcls-iminiportstreamaudioenginenode-getstreamattributesteppings.md) | Gets the allowed stepping value for the audio stream attribute. |
| [IMiniportStreamAudioEngineNode::GetStreamChannelCount](nf-portcls-iminiportstreamaudioenginenode-getstreamchannelcount.md) | Gets a count of the number of channels available for the stream. |
| [IMiniportStreamAudioEngineNode::GetStreamChannelMute](nf-portcls-iminiportstreamaudioenginenode-getstreamchannelmute.md) | Gets the state of the Mute node in the path of the audio stream. |
| [IMiniportStreamAudioEngineNode::GetStreamChannelPeakMeter](nf-portcls-iminiportstreamaudioenginenode-getstreamchannelpeakmeter.md) | Gets the value of the PeakMeter node in the path of the audio stream. |
| [IMiniportStreamAudioEngineNode::GetStreamChannelVolume](nf-portcls-iminiportstreamaudioenginenode-getstreamchannelvolume.md) | Gets the current volume level that is applied to the audio stream. |
| [IMiniportStreamAudioEngineNode::GetStreamLinearBufferPosition](nf-portcls-iminiportstreamaudioenginenode-getstreamlinearbufferposition.md) | Gets the number of bytes that the DMA has fetched from the audio buffer since the beginning of the stream. |
| [IMiniportStreamAudioEngineNode::GetStreamPresentationPosition](nf-portcls-iminiportstreamaudioenginenode-getstreampresentationposition.md) | Gets the current cursor position in the audio data stream that is being rendered to the endpoint. |
| [IMiniportStreamAudioEngineNode::SetLfxState](nf-portcls-iminiportstreamaudioenginenode-setlfxstate.md) | Sets the state of the local effects (LFX) node that is in the path of the audio stream. |
| [IMiniportStreamAudioEngineNode::SetStreamChannelMute](nf-portcls-iminiportstreamaudioenginenode-setstreamchannelmute.md) | Sets the state of the Mute node in the path of the audio stream. |
| [IMiniportStreamAudioEngineNode::SetStreamChannelVolume](nf-portcls-iminiportstreamaudioenginenode-setstreamchannelvolume.md) | Sets the volume level to be applied to the audio stream. |
| [IMiniportStreamAudioEngineNode::SetStreamCurrentWritePosition](nf-portcls-iminiportstreamaudioenginenode-setstreamcurrentwriteposition.md) | Sets the current cursor position in the audio data stream that is being captured from the endpoint. |
| [IMiniportStreamAudioEngineNode::SetStreamLoopbackProtection](nf-portcls-iminiportstreamaudioenginenode-setstreamloopbackprotection.md) | Sets the loopback protection status of the audio engine node. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Windows |
| **Header** | portcls.h |