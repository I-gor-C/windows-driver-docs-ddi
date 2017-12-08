---
UID: NF.portcls.IPreFetchOffset.SetPreFetchOffset
title: IPreFetchOffset::SetPreFetchOffset
author: windows-driver-content
description: The SetPreFetchOffset method sets the prefetch offset, which is the number of bytes of data separating the write cursor from the play cursor in a DirectSound output stream.
old-location: audio\iprefetchoffset_setprefetchoffset.htm
old-project: audio
ms.assetid: fef8e8b8-7e79-4d88-b643-9b371e4297fd
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IPreFetchOffset, SetPreFetchOffset, IPreFetchOffset::SetPreFetchOffset
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPreFetchOffset.SetPreFetchOffset
req.alt-loc: portcls.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level
req.iface: IPreFetchOffset
---

# IPreFetchOffset::SetPreFetchOffset method



## -description
<p>The <code>SetPreFetchOffset</code> method sets the prefetch offset, which is the number of bytes of data separating the write cursor from the play cursor in a DirectSound output stream.</p>


## -syntax

````
VOID SetPreFetchOffset(
  [in] ULONG PreFetchOffset
);
````


## -parameters
<dl>

### -param PreFetchOffset [in]

<dd>
<p>Specifies the prefetch offset size in bytes.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A WavePci miniport driver calls the <code>SetPreFetchOffset</code> method to specify the prefetch offset of a hardware-accelerated DirectSound output stream.</p>

<p>The prefetch offset is the number of bytes of data separating the write cursor from the play cursor in the audio device's hardware buffer:</p>

<p>The write cursor specifies the buffer position into which a DirectSound application can safely write the next sound sample.</p>

<p>The play cursor specifies the buffer position of the sound sample that is currently being played by the audio device.</p>

<p>For more information about write cursors and play cursors, see <a href="audio.ksaudio_position">KSAUDIO_POSITION</a>.</p>

<p>For information about using <code>SetPreFetchOffset</code> to control a DirectSound stream's prefetch offset, see <a href="https://msdn.microsoft.com/92a0163f-29b1-4e15-88ab-67e1097d015e">Prefetch Offsets</a>.</p>

## -requirements
<table>
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
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\portcls\nn-portcls-iprefetchoffset.md">IPreFetchOffset</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537297">KSPROPERTY_AUDIO_POSITION</a>
</dt>
<dt>
<a href="audio.ksaudio_position">KSAUDIO_POSITION</a>
</dt>
<dt>
<a href="audio.iminiportwavepcistream_getposition">IMiniportWavePciStream::GetPosition</a>
</dt>
<dt>
<a href="audio.iportwavepcistream_getmapping">IPortWavePciStream::GetMapping</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IPreFetchOffset::SetPreFetchOffset method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
