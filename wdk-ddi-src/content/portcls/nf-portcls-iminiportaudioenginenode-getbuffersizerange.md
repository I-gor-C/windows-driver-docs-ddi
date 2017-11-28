---
UID: NF.portcls.IMiniportAudioEngineNode.GetBufferSizeRange
title: IMiniportAudioEngineNode::GetBufferSizeRange
author: windows-driver-content
description: Gets the minimum and maximum buffer size that the hardware audio engine can support.
old-location: audio\iminiportaudioenginenode_getbuffersizerange.htm
old-project: audio
ms.assetid: 75CBDD4F-618F-4618-9D53-4A8DF40992B0
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: IMiniportAudioEngineNode, GetBufferSizeRange, IMiniportAudioEngineNode::GetBufferSizeRange
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
req.alt-api: IMiniportAudioEngineNode.GetBufferSizeRange
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

# IMiniportAudioEngineNode::GetBufferSizeRange method



## -description
<p>Gets the minimum and maximum buffer size that the hardware audio engine can support.</p>


## -syntax

````
NTSTATUS GetBufferSizeRange(
  [in]  ULONG                           ulNodeId,
  [in]  KSDATAFORMAT_WAVEFORMATEX       *pKsDataFormatWfx,
  [out] KSAUDIOENGINE_BUFFER_SIZE_RANGE *pBufferSizeRange
);
````


## -parameters
<dl>

### -param <i>ulNodeId</i> [in]

<dd>
<p>The ID for the node that represents the audio device.</p>
</dd>

### -param <i>pKsDataFormatWfx</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff537095">KSDATAFORMAT_WAVEFORMATEX</a> structure that represents the audio data format for the audio device.</p>
</dd>

### -param <i>pBufferSizeRange</i> [out]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/hh450864">KSAUDIOENGINE_BUFFER_SIZE_RANGE</a> structure that represents the minimum and maximum buffer size that the hardware audio engine can support at the time when it is called.</p>
</dd>
</dl>

## -returns
<p><b>GetBufferSizeRange</b> returns S_OK, if the call was successful. Otherwise, the method returns an appropriate error 

code.</p>

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
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IMiniportAudioEngineNode::GetBufferSizeRange method%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
