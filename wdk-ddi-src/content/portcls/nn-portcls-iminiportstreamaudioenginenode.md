---
UID : NN:portcls.IMiniportStreamAudioEngineNode
title : IMiniportStreamAudioEngineNode
author : windows-driver-content
description : This interface allows a miniport driver to use KS properties that access the audio engine via a pin instance handle.
old-location : audio\iminiportstreamaudioenginenode.htm
old-project : audio
ms.assetid : B3F7D3AC-C756-47D2-9E7C-7930621753C3
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : PcUnregisterIoTimeout
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : portcls.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 8
req.target-min-winversvr : Windows Server 2012
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IMiniportStreamAudioEngineNode
req.alt-loc : Portcls.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Portcls.lib
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : PC_EXIT_LATENCY, *PPC_EXIT_LATENCY
---

# IMiniportStreamAudioEngineNode interface

This interface allows a miniport driver to use KS properties that access the audio engine via a pin instance handle.

## Methods

<p>The <b>IMiniportStreamAudioEngineNode</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [portcls.IMiniportStreamAudioEngineNode.GetLfxState](nf-portcls-iminiportstreamaudioenginenode-getlfxstate.md) | Gets the state of the local effects (LFX) node that is in the path of the audio stream. |
| [portcls.IMiniportStreamAudioEngineNode.GetStreamAttributeSteppings](nf-portcls-iminiportstreamaudioenginenode-getstreamattributesteppings.md) | Gets the allowed stepping value for the audio stream attribute. |
| [portcls.IMiniportStreamAudioEngineNode.GetStreamChannelCount](nf-portcls-iminiportstreamaudioenginenode-getstreamchannelcount.md) | Gets a count of the number of channels available for the stream. |
| [portcls.IMiniportStreamAudioEngineNode.GetStreamChannelMute](nf-portcls-iminiportstreamaudioenginenode-getstreamchannelmute.md) | Gets the state of the Mute node in the path of the audio stream. |
| [portcls.IMiniportStreamAudioEngineNode.GetStreamChannelPeakMeter](nf-portcls-iminiportstreamaudioenginenode-getstreamchannelpeakmeter.md) | Gets the value of the PeakMeter node in the path of the audio stream. |
| [portcls.IMiniportStreamAudioEngineNode.GetStreamChannelVolume](nf-portcls-iminiportstreamaudioenginenode-getstreamchannelvolume.md) | Gets the current volume level that is applied to the audio stream. |
| [portcls.IMiniportStreamAudioEngineNode.GetStreamLinearBufferPosition](nf-portcls-iminiportstreamaudioenginenode-getstreamlinearbufferposition.md) | Gets the number of bytes that the DMA has fetched from the audio buffer since the beginning of the stream. |
| [portcls.IMiniportStreamAudioEngineNode.GetStreamPresentationPosition](nf-portcls-iminiportstreamaudioenginenode-getstreampresentationposition.md) | Gets the current cursor position in the audio data stream that is being rendered to the endpoint. |
| [portcls.IMiniportStreamAudioEngineNode.SetLfxState](nf-portcls-iminiportstreamaudioenginenode-setlfxstate.md) | Sets the state of the local effects (LFX) node that is in the path of the audio stream. |
| [portcls.IMiniportStreamAudioEngineNode.SetStreamChannelMute](nf-portcls-iminiportstreamaudioenginenode-setstreamchannelmute.md) | Sets the state of the Mute node in the path of the audio stream. |
| [portcls.IMiniportStreamAudioEngineNode.SetStreamChannelVolume](nf-portcls-iminiportstreamaudioenginenode-setstreamchannelvolume.md) | Sets the volume level to be applied to the audio stream. |
| [portcls.IMiniportStreamAudioEngineNode.SetStreamCurrentWritePosition](nf-portcls-iminiportstreamaudioenginenode-setstreamcurrentwriteposition.md) | Sets the current cursor position in the audio data stream that is being captured from the endpoint. |
| [portcls.IMiniportStreamAudioEngineNode.SetStreamLoopbackProtection](nf-portcls-iminiportstreamaudioenginenode-setstreamloopbackprotection.md) | Sets the loopback protection status of the audio engine node. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | portcls.h |
| **DLL** |  |