---
UID: NF.portcls.IMiniportAudioEngineNode.GetGfxState
title: IMiniportAudioEngineNode::GetGfxState
author: windows-driver-content
description: Gets the state of the global effects (GFX) node in the audio engine.
old-location: audio\iminiportaudioenginenode_getgfxstate.htm
ms.assetid: C2D4EB3E-0A39-4458-B0E7-C6D943AB4203
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: audio
req.header: portcls.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IMiniportAudioEngineNode.GetGfxState
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
ms.keywords: IMiniportAudioEngineNode, GetGfxState, IMiniportAudioEngineNode::GetGfxState
req.iface: IMiniportAudioEngineNode
---

# IMiniportAudioEngineNode::GetGfxState method



## -description
<p>Gets the state of the global effects (GFX) node in the audio engine.</p>


## -syntax

````
NTSTATUS GetGfxState(
  [in]  ULONG ulNodeId,
  [out] BOOL  *pbEnable
);
````


## -parameters
<dl>

### -param <i>ulNodeId</i> [in]

<dd>
<p>The ID of the GFX node.</p>
</dd>

### -param <i>pbEnable</i> [out]

<dd>
<p>Pointer to a <b>BOOL</b> data type.</p>
</dd>
</dl>

## -returns
<p><b>GetGfxState</b> returns S_OK if the call was successful. Otherwise, the method returns an appropriate error code.</p>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IMiniportAudioEngineNode::GetGfxState method%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
