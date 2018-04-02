---
UID: NN:portcls.IMiniportAudioEngineNode
title: IMiniportAudioEngineNode
author: windows-driver-content
description: This interface allows a miniport driver to use KS properties that access the audio engine via a KS filter handle.
old-location: audio\iminiportaudioenginenode.htm
old-project: audio
ms.assetid: 58170D54-869A-49CC-865A-AB64BFB41A4B
ms.author: windowsdriverdev
ms.date: 3/19/2018
ms.keywords: IMiniportAudioEngineNode, IMiniportAudioEngineNode interface [Audio Devices], IMiniportAudioEngineNode interface [Audio Devices], described, audio.iminiportaudioenginenode, portcls/IMiniportAudioEngineNode
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
-	IMiniportAudioEngineNode
product:
- Windows
targetos: Windows
req.typenames: PC_EXIT_LATENCY, *PPC_EXIT_LATENCY
---

# IMiniportAudioEngineNode interface

This interface allows a miniport driver to use KS properties that access the audio engine via a KS filter handle.

## Methods

<p>The <b>IMiniportAudioEngineNode</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IMiniportAudioEngineNode::GetAudioEngineDescriptor](nf-portcls-iminiportaudioenginenode-getaudioenginedescriptor.md) | Gets the descriptor for the audio engine node. |
| [IMiniportAudioEngineNode::GetBufferSizeRange](nf-portcls-iminiportaudioenginenode-getbuffersizerange.md) | Gets the minimum and maximum buffer size that the hardware audio engine can support. |
| [IMiniportAudioEngineNode::GetDeviceAttributeSteppings](nf-portcls-iminiportaudioenginenode-getdeviceattributesteppings.md) | Gets the allowed stepping value for the audio device attribute. |
| [IMiniportAudioEngineNode::GetDeviceChannelCount](nf-portcls-iminiportaudioenginenode-getdevicechannelcount.md) | Gets a count of the number of channels supported by the audio device. |
| [IMiniportAudioEngineNode::GetDeviceChannelMute](nf-portcls-iminiportaudioenginenode-getdevicechannelmute.md) | Gets the state of the Mute node for the audio device channel. |
| [IMiniportAudioEngineNode::GetDeviceChannelPeakMeter](nf-portcls-iminiportaudioenginenode-getdevicechannelpeakmeter.md) | Gets the PeakMeter value for the audio device channel. |
| [IMiniportAudioEngineNode::GetDeviceChannelVolume](nf-portcls-iminiportaudioenginenode-getdevicechannelvolume.md) | Gets the volume level for a given channel of the audio device. |
| [IMiniportAudioEngineNode::GetDeviceFormat](nf-portcls-iminiportaudioenginenode-getdeviceformat.md) | Gets the audio data format for an audio device. |
| [IMiniportAudioEngineNode::GetEngineFormatSize](nf-portcls-iminiportaudioenginenode-getengineformatsize.md) | Gets the format type and the buffer size for the audio engine's audio data format. |
| [IMiniportAudioEngineNode::GetGfxState](nf-portcls-iminiportaudioenginenode-getgfxstate.md) | Gets the state of the global effects (GFX) node in the audio engine. |
| [IMiniportAudioEngineNode::GetMixFormat](nf-portcls-iminiportaudioenginenode-getmixformat.md) | Gets the audio data format for the audio engine mixer. |
| [IMiniportAudioEngineNode::GetSupportedDeviceFormats](nf-portcls-iminiportaudioenginenode-getsupporteddeviceformats.md) | Gets the supported audio data formats for the audio device. |
| [IMiniportAudioEngineNode::SetDeviceChannelMute](nf-portcls-iminiportaudioenginenode-setdevicechannelmute.md) | Sets the state of the Mute node for the audio device channel. |
| [IMiniportAudioEngineNode::SetDeviceChannelVolume](nf-portcls-iminiportaudioenginenode-setdevicechannelvolume.md) | Sets the volume level for a given channel of the audio device. |
| [IMiniportAudioEngineNode::SetDeviceFormat](nf-portcls-iminiportaudioenginenode-setdeviceformat.md) | Sets the audio data format for an audio device. |
| [IMiniportAudioEngineNode::SetGfxState](nf-portcls-iminiportaudioenginenode-setgfxstate.md) | Sets the state of the global effects (GFX) node in the audio engine. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Windows |
| **Header** | portcls.h |