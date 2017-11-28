---
UID: NF.portcls.IMiniportStreamAudioEngineNode.GetStreamChannelMute
title: IMiniportStreamAudioEngineNode::GetStreamChannelMute
author: windows-driver-content
description: Gets the state of the Mute node in the path of the audio stream.
old-location: audio\iminiportstreamaudioenginenode_getstreamchannelmute.htm
old-project: audio
ms.assetid: 16010297-5B08-466C-AB79-4ED12A9539D9
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: IMiniportStreamAudioEngineNode, GetStreamChannelMute, IMiniportStreamAudioEngineNode::GetStreamChannelMute
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
req.alt-api: IMiniportStreamAudioEngineNode.GetStreamChannelMute
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
req.irql: DISPATCH_LEVEL
req.iface: IMiniportStreamAudioEngineNode
---

# IMiniportStreamAudioEngineNode::GetStreamChannelMute method



## -description
<p>Gets the state of the Mute node in the path of the audio stream.</p>


## -syntax

````
NTSTATUS GetStreamChannelMute(
  [in]  UINT32 ulChannel,
  [out] BOOL   *pbMute
);
````


## -parameters
<dl>

### -param <i>ulChannel</i> [in]

<dd>
<p>The audio stream channel.</p>
</dd>

### -param <i>pbMute</i> [out]

<dd>
<p>The state of the Mute node.</p>
</dd>
</dl>

## -returns
<p><b>GetStreamChannelMute</b> returns S_OK, if the call was successful. Otherwise, the method returns an appropriate error 

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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265090">IMiniportStreamAudioEngineNode</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IMiniportStreamAudioEngineNode::GetStreamChannelMute method%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
