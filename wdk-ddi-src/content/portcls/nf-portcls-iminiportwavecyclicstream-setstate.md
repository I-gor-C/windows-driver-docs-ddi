---
UID: NF.portcls.IMiniportWaveCyclicStream.SetState
title: IMiniportWaveCyclicStream::SetState
author: windows-driver-content
description: The SetState method sets the new state of playback or recording for the stream.
old-location: audio\iminiportwavecyclicstream_setstate.htm
old-project: audio
ms.assetid: 61d7252e-04af-46f1-a885-4720698ae930
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: IMiniportWaveCyclicStream, SetState, IMiniportWaveCyclicStream::SetState
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
req.alt-api: IMiniportWaveCyclicStream.SetState
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
req.irql: PASSIVE_LEVEL
req.iface: IMiniportWaveCyclicStream
---

# IMiniportWaveCyclicStream::SetState method



## -description
<p>The <code>SetState</code> method sets the new state of playback or recording for the stream.</p>


## -syntax

````
NTSTATUS SetState(
  [in] KSSTATE State
);
````


## -parameters
<dl>

### -param <i>State</i> [in]

<dd>
<p>Specifies the new state for the stream. This parameter is a <a href="https://msdn.microsoft.com/library/windows/hardware/ff566856">KSSTATE</a> enumeration value. For more information, see the following Remarks section.</p>
</dd>
</dl>

## -returns
<p><code>SetState</code> returns STATUS_SUCCESS if the call was successful. Otherwise, the method returns an appropriate error code.</p>

## -remarks
<p>For an audio filter graph, the four <a href="https://msdn.microsoft.com/library/windows/hardware/ff566856">KSSTATE</a> enumeration values are interpreted as follows:</p>

<p>KSSTATE_RUN </p>

<p>Data transport in the current audio filter graph is running and functioning as normal.</p>

<p>KSSTATE_ACQUIRE </p>

<p>This is a transitional state that helps to manage the transition between KSSTATE_RUN and KSSTATE_STOP.</p>

<p>KSSTATE_PAUSE </p>

<p>This is a transitional state that helps to manage the transition between KSSTATE_RUN and KSSTATE_STOP. </p>

<p>KSSTATE_STOP </p>

<p>Data transport is stopped in the current audio filter graph.</p>

<p>For most miniport drivers, KSSTATE_ACQUIRE and KSSTATE_PAUSE are indistinguishable.</p>

<p>Transitions always occur in one of the following two sequences:</p>

<p>STOP -&gt; ACQUIRE -&gt; PAUSE -&gt; RUN</p>

<p>RUN -&gt; PAUSE -&gt; ACQUIRE -&gt; STOP</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff536723">IMiniportWaveCyclic::NewStream</a> method sets the initial state of the stream to KSSTATE_STOP. </p>

<p>For an audio filter graph, the four <a href="https://msdn.microsoft.com/library/windows/hardware/ff566856">KSSTATE</a> enumeration values are interpreted as follows:</p>

<p>KSSTATE_RUN </p>

<p>Data transport in the current audio filter graph is running and functioning as normal.</p>

<p>KSSTATE_ACQUIRE </p>

<p>This is a transitional state that helps to manage the transition between KSSTATE_RUN and KSSTATE_STOP.</p>

<p>KSSTATE_PAUSE </p>

<p>This is a transitional state that helps to manage the transition between KSSTATE_RUN and KSSTATE_STOP. </p>

<p>KSSTATE_STOP </p>

<p>Data transport is stopped in the current audio filter graph.</p>

<p>For most miniport drivers, KSSTATE_ACQUIRE and KSSTATE_PAUSE are indistinguishable.</p>

<p>Transitions always occur in one of the following two sequences:</p>

<p>STOP -&gt; ACQUIRE -&gt; PAUSE -&gt; RUN</p>

<p>RUN -&gt; PAUSE -&gt; ACQUIRE -&gt; STOP</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff536723">IMiniportWaveCyclic::NewStream</a> method sets the initial state of the stream to KSSTATE_STOP. </p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536715">IMiniportWaveCyclicStream</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566856">KSSTATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565110">KSPROPERTY_CONNECTION_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536723">IMiniportWaveCyclic::NewStream</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IMiniportWaveCyclicStream::SetState method%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
