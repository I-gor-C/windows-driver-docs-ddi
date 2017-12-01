---
UID: NF.portcls.IMiniportStreamAudioEngineNode.SetStreamChannelVolume
title: IMiniportStreamAudioEngineNode::SetStreamChannelVolume
author: windows-driver-content
description: Sets the volume level to be applied to the audio stream.
old-location: audio\iminiportstreamaudioenginenode_setstreamchannelvolume.htm
old-project: audio
ms.assetid: 0110979E-8C57-4394-B43E-BCC7B178A0AF
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IMiniportStreamAudioEngineNode, SetStreamChannelVolume, IMiniportStreamAudioEngineNode::SetStreamChannelVolume
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
req.alt-api: IMiniportStreamAudioEngineNode.SetStreamChannelVolume
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

# IMiniportStreamAudioEngineNode::SetStreamChannelVolume method



## -description
<p>Sets the volume level to be applied to the audio stream.</p>


## -syntax

````
NTSTATUS SetStreamChannelVolume(
  [in] UINT32           Channel,
  [in] LONG             TargetVolume,
  [in] AUDIO_CURVE_TYPE CurveType,
  [in] ULONGLONG        CurveDuration
);
````


## -parameters
<dl>

### -param <i>Channel</i> [in]

<dd>
<p>The audio stream channel.</p>
</dd>

### -param <i>TargetVolume</i> [in]

<dd>
<p>The volume level to be applied to the audio stream.</p>
</dd>

### -param <i>CurveType</i> [in]

<dd>
<p>The curve algorithm that will be used  to set the volume level. The curve types are represented by the members of the <a href="..\ksmedia\ne-ksmedia-audio-curve-type.md">AUDIO_CURVE_TYPE</a> enum.</p>
</dd>

### -param <i>CurveDuration</i> [in]

<dd>
<p>The length of time over which the curve algorithm will be applied.</p>
</dd>
</dl>

## -returns
<p><b>SetStreamChannelVolume</b> returns S_OK, if the call was successful. Otherwise, the method returns an appropriate error 

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
<a href="..\portcls\nn-portcls-iminiportstreamaudioenginenode.md">IMiniportStreamAudioEngineNode</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IMiniportStreamAudioEngineNode::SetStreamChannelVolume method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
