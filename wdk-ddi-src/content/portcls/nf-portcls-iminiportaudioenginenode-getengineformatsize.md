---
UID: NF.portcls.IMiniportAudioEngineNode.GetEngineFormatSize
title: IMiniportAudioEngineNode::GetEngineFormatSize
author: windows-driver-content
description: Gets the format type and the buffer size for the audio engine's audio data format.
old-location: audio\iminiportaudioenginenode_getengineformatsize.htm
old-project: audio
ms.assetid: 0874EC25-3ABE-410B-B5AC-E98020378D7E
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IMiniportAudioEngineNode, GetEngineFormatSize, IMiniportAudioEngineNode::GetEngineFormatSize
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
req.alt-api: IMiniportAudioEngineNode.GetEngineFormatSize
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

# IMiniportAudioEngineNode::GetEngineFormatSize method



## -description
<p>Gets the format type and the buffer size for the audio engine's audio data format.</p>


## -syntax

````
NTSTATUS GetEngineFormatSize(
  [in]  ULONG             ulNodeId,
  [in]  eEngineFormatType formatType,
  [out] ULONG             *pulFormatSize
);
````


## -parameters
<dl>

### -param <i>ulNodeId</i> [in]

<dd>
<p>The ID of the audio engine node.</p>
</dd>

### -param <i>formatType</i> [in]

<dd>
<p>An enum of type <a href="..\portcls\ne-portcls-eengineformattype.md">eEngineFormatType</a> that represents the audio data format type.</p>
</dd>

### -param <i>pulFormatSize</i> [out]

<dd>
<p>The data buffer size for the format type.</p>
</dd>
</dl>

## -returns
<p><b>GetEngineFormatSize</b> returns S_OK, if the call was successful. Otherwise, the method returns an appropriate error code.</p>

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
<a href="..\portcls\ne-portcls-eengineformattype.md">eEngineFormatType</a>
</dt>
<dt>
<a href="..\portcls\nn-portcls-iminiportaudioenginenode.md">IMiniportAudioEngineNode</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IMiniportAudioEngineNode::GetEngineFormatSize method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
