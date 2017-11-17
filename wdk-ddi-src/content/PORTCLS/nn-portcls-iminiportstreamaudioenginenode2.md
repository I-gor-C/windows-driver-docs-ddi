---
UID: NN.portcls.IMiniportStreamAudioEngineNode2
title: IMiniportStreamAudioEngineNode2
author: windows-driver-content
description: The IMiniportStreamAudioEngineNode2 interface allows an audio miniport driver to extend the capabilities of the IMiniportStreamAudioEngineNode interface.
old-location: audio\iminiportstreamaudioenginenode2.htm
ms.assetid: 38888C17-31FC-47F4-A49B-A46A9DF962AF
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: interface
ms.prod: windows-hardware
ms.technology: audio
req.header: portcls.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IMiniportStreamAudioEngineNode2
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
ms.keywords: PcUnregisterIoTimeout
req.iface: 
---

# IMiniportStreamAudioEngineNode2 interface



## -description
<p>The <b>IMiniportStreamAudioEngineNode2</b> interface allows an audio miniport driver to extend the capabilities of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265090">IMiniportStreamAudioEngineNode</a> interface.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IMiniportStreamAudioEngineNode2</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IMiniportStreamAudioEngineNode2</b> also has these types of members:</p>

<p>The <b>IMiniportStreamAudioEngineNode2</b> interface has these methods.</p>

<p>Sets the current cursor position in the last audio data stream that was written to the audio buffer.</p>

<p> </p>

## -members
<p>The <b>IMiniportStreamAudioEngineNode2</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/dn338128">SetStreamCurrentWritePositionForLastBuffer</a>
</td>
<td align="left" width="63%">
<p>Sets the current cursor position in the last audio data stream that was written to the audio buffer.</p>
</td>
</tr>
</table><p>Sets the current cursor position in the last audio data stream that was written to the audio buffer.</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
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