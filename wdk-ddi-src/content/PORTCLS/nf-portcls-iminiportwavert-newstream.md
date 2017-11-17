---
UID: NF.portcls.IMiniportWaveRT.NewStream
title: IMiniportWaveRT::NewStream
author: windows-driver-content
description: The NewStream method creates a new instance of a WaveRT stream object.
old-location: audio\iminiportwavert_newstream.htm
ms.assetid: efd2eea8-2b05-49a2-b136-a3e1e3e739c5
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: audio
req.header: portcls.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IMiniportWaveRT.NewStream
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
req.irql: Passive level.
ms.keywords: IMiniportWaveRT, NewStream, IMiniportWaveRT::NewStream
req.iface: IMiniportWaveRT
---

# IMiniportWaveRT::NewStream method



## -description
<p>The <code>NewStream</code> method creates a new instance of a WaveRT stream object.</p>


## -syntax

````
NTSTATUS NewStream(
  [out] PMINIPORTWAVERTSTREAM *Stream,
  [in]  PPORTWAVERTSTREAM     PortStream,
  [in]  ULONG                 Pin,
  [in]  BOOLEAN               Capture,
  [in]  PKSDATAFORMAT         DataFormat
);
````


## -parameters
<dl>

### -param <i>Stream</i> [out]

<dd>
<p>Output pointer for the new stream. This parameter points to a caller-allocated pointer variable, into which the <code>NewStream</code> method writes a pointer to the <b>IMiniportWaveRTStream</b> interface of the new stream object. The caller specifies a valid, non-<b>NULL</b> pointer for this parameter.</p>
</dd>

### -param <i>PortStream</i> [in]

<dd>
<p>Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536922">IPortWaveRTStream</a>.</p>
</dd>

### -param <i>Pin</i> [in]

<dd>
<p>Specifies a pin ID that identifies the pin to be opened. If the filter descriptor of the WaveRT miniport driver specifies a total of <i>n</i> pin factories on the filter, valid values for the <i>Pin</i> parameter are in the range 0 to <i>n</i>-1. For more information about filter descriptors, see the <a href="NULL">Filter Factories</a> topic. </p>
</dd>

### -param <i>Capture</i> [in]

<dd>
<p>Specifies a Boolean value that indicates whether to create a capture stream or a render stream. This parameter is <b>TRUE</b> for a capture (input) stream, and <b>FALSE</b> for a playback (output) stream.</p>
</dd>

### -param <i>DataFormat</i> [in]

<dd>
<p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561656">KSDATAFORMAT</a> structure that specifies the data format of the new stream. For more information, see the following Remarks section.</p>
</dd>
</dl>

## -returns
<p><code>NewStream</code> returns STATUS_SUCCESS if the call was successful. Otherwise, the method returns an appropriate error status code.</p>

## -remarks
<p>The <code>NewStream</code> method sets the initial state of the stream to <a href="https://msdn.microsoft.com/c71fd395-28aa-4421-9443-b5b0a1f3ac7e">KSSTATE_STOP</a> and its initial position to 0. For more information, see related methods <a href="https://msdn.microsoft.com/library/windows/hardware/ff536756">IMiniportWaveRTStream::SetState</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff536749">IMiniportWaveRTStream::GetPosition</a>.</p>

<p>The <i>DataFormat</i> parameter, which specifies the data format of the stream, points to one of the following audio-specific, extended versions of the KSDATAFORMAT structure:</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537095">KSDATAFORMAT_WAVEFORMATEX</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537094">KSDATAFORMAT_DSOUND</a>
</p>

<p>The <i>Stream</i> and <i>PortStream</i> parameters follow the reference-counting conventions for COM objects.</p>

<p>The <code>NewStream</code> method sets the initial state of the stream to <a href="https://msdn.microsoft.com/c71fd395-28aa-4421-9443-b5b0a1f3ac7e">KSSTATE_STOP</a> and its initial position to 0. For more information, see related methods <a href="https://msdn.microsoft.com/library/windows/hardware/ff536756">IMiniportWaveRTStream::SetState</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff536749">IMiniportWaveRTStream::GetPosition</a>.</p>

<p>The <i>DataFormat</i> parameter, which specifies the data format of the stream, points to one of the following audio-specific, extended versions of the KSDATAFORMAT structure:</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537095">KSDATAFORMAT_WAVEFORMATEX</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537094">KSDATAFORMAT_DSOUND</a>
</p>

<p>The <i>Stream</i> and <i>PortStream</i> parameters follow the reference-counting conventions for COM objects.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later Windows operating systems.</p>
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
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Passive level.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536922">IPortWaveRTStream</a>
</dt>
<dt>IMiniportWaveRTStream</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536756">IMiniportWaveRTStream::SetState</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536749">IMiniportWaveRTStream::GetPosition</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IMiniportWaveRT::NewStream method%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
