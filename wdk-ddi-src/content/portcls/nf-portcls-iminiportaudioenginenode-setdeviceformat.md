---
UID: NF.portcls.IMiniportAudioEngineNode.SetDeviceFormat
title: IMiniportAudioEngineNode::SetDeviceFormat
author: windows-driver-content
description: Sets the audio data format for an audio device.
old-location: audio\iminiportaudioenginenode_setdeviceformat.htm
old-project: audio
ms.assetid: A6FFC14B-0736-425F-A923-DFF54494887C
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: IMiniportAudioEngineNode, SetDeviceFormat, IMiniportAudioEngineNode::SetDeviceFormat
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IMiniportAudioEngineNode.SetDeviceFormat
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
req.iface: IMiniportAudioEngineNode
---

# IMiniportAudioEngineNode::SetDeviceFormat method



## -description
<p>Sets the audio data format for an audio device.</p>


## -syntax

````
NTSTATUS SetDeviceFormat(
  [in] ULONG                     ulNodeId,
  [in] KSDATAFORMAT_WAVEFORMATEX *pFormat,
  [in] ULONG                     ulBufferSize
);
````


## -parameters
<dl>

### -param <i>ulNodeId</i> [in]

<dd>
<p>The ID of the node that represents the device.</p>
</dd>

### -param <i>pFormat</i> [in]

<dd>
<p>A structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff537095">KSDATAFORMAT_WAVEFORMATEX</a> that represents the audio data format to be set for the device.</p>
</dd>

### -param <i>ulBufferSize</i> [in]

<dd>
<p>The audio data buffer size.</p>
</dd>
</dl>

## -returns
<p><b>SetDeviceFormat</b> returns S_OK, if the call was successful. Otherwise, the method 

returns an appropriate error code.</p>

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
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn302040">IMiniportAudioEngineNode</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537095">KSDATAFORMAT_WAVEFORMATEX</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IMiniportAudioEngineNode::SetDeviceFormat method%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
