---
UID: NF.portcls.IMiniportAudioEngineNode.GetAudioEngineDescriptor
title: IMiniportAudioEngineNode::GetAudioEngineDescriptor
author: windows-driver-content
description: Gets the descriptor for the audio engine node.
old-location: audio\iminiportaudioenginenode_getaudioenginedescriptor.htm
old-project: audio
ms.assetid: B8D09AB4-1F36-44E1-8D4F-33E7E4DBBFE3
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IMiniportAudioEngineNode, GetAudioEngineDescriptor, IMiniportAudioEngineNode::GetAudioEngineDescriptor
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
req.alt-api: IMiniportAudioEngineNode.GetAudioEngineDescriptor
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

# IMiniportAudioEngineNode::GetAudioEngineDescriptor method



## -description
<p>Gets the descriptor for the audio engine node.</p>


## -syntax

````
NTSTATUS GetAudioEngineDescriptor(
  [in]  ULONG                    ulNodeId,
  [out] KSAUDIOENGINE_DESCRIPTOR *pAudioEngineDescriptor
);
````


## -parameters
<dl>

### -param <i>ulNodeId</i> [in]

<dd>
<p>The ID of the audio engine node.</p>
</dd>

### -param <i>pAudioEngineDescriptor</i> [out]

<dd>
<p>Audio engine descriptor object. This parameter is of type <a href="audio.ksaudioengine_descriptor">KSAUDIOENGINE_DESCRIPTOR</a>.</p>
</dd>
</dl>

## -returns
<p><b>GetAudioEngineDescriptor</b> returns S_OK if the call was successful. Otherwise, the method returns an appropriate error code.</p>

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
<a href="..\portcls\nn-portcls-iminiportaudioenginenode.md">IMiniportAudioEngineNode</a>
</dt>
<dt>
<a href="audio.ksaudioengine_descriptor">KSAUDIOENGINE_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IMiniportAudioEngineNode::GetAudioEngineDescriptor method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
