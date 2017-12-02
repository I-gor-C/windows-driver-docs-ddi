---
UID: NF.portcls.IMiniportStreamAudioEngineNode2.SetStreamCurrentWritePositionForLastBuffer
title: IMiniportStreamAudioEngineNode2::SetStreamCurrentWritePositionForLastBuffer
author: windows-driver-content
description: Sets the current cursor position in the last audio data stream that was written to the audio buffer.
old-location: audio\iminiportstreamaudioenginenode2_setstreamcurrentwritepositionforlastbuffer.htm
old-project: audio
ms.assetid: 93E3D03B-6FA1-49D5-AF38-6C2FEA3FC95D
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IMiniportStreamAudioEngineNode2, SetStreamCurrentWritePositionForLastBuffer, IMiniportStreamAudioEngineNode2::SetStreamCurrentWritePositionForLastBuffer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IMiniportStreamAudioEngineNode2.SetStreamCurrentWritePositionForLastBuffer
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
req.iface: IMiniportStreamAudioEngineNode2
---

# IMiniportStreamAudioEngineNode2::SetStreamCurrentWritePositionForLastBuffer method



## -description
<p>Sets the current cursor position in the last audio data stream that was written to the audio buffer.</p>


## -syntax

````
NTSTATUS SetStreamCurrentWritePositionForLastBuffer(
  [in] ULONG ulWritePosition
);
````


## -parameters
<dl>

### -param ulWritePosition [in]

<dd>
<p>The current cursor position in the last audio data stream.</p>
</dd>
</dl>

## -returns
<p><b>SetStreamCurrentWritePositionForLastBuffer</b> returns S_OK if the call was successful. Otherwise, the method returns an appropriate error code.</p>

## -remarks
<p>When a client app performs the very last write operation to the audio buffer to be processed by the audio  driver of an offloaded stream, the audio driver calls <b>SetStreamCurrentWritePositionForLastBuffer</b>.  The <b>SetStreamCurrentWritePositionForLastBuffer</b> method indicates the “write position” of the very last buffer in a stream. Note that this last buffer could be only partially filled.</p>

<p>If the buffer is only partially filled, then the audio driver needs to notify the audio engine when the last valid byte in the buffer has been <i>rendered</i>.  This differs from the normal functionality where the audio driver notified the audio engine when the driver <i>fetched</i> the last byte in the buffer.</p>

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
<a href="..\portcls\nn-portcls-iminiportstreamaudioenginenode2.md">IMiniportStreamAudioEngineNode2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn292492">KSPROPERTY_AUDIO_WAVERT_CURRENT_WRITE_LASTBUFFER_POSITION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IMiniportStreamAudioEngineNode2::SetStreamCurrentWritePositionForLastBuffer method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
