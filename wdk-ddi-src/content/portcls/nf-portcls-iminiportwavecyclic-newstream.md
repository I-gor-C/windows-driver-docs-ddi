---
UID: NF.portcls.IMiniportWaveCyclic.NewStream
title: IMiniportWaveCyclic::NewStream
author: windows-driver-content
description: The NewStream method creates a new instance of a logical stream that is associated with a specified physical channel.
old-location: audio\iminiportwavecyclic_newstream.htm
old-project: audio
ms.assetid: a83c6eb9-a29a-4695-99d3-168dff68c4a2
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: IMiniportWaveCyclic, NewStream, IMiniportWaveCyclic::NewStream
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
req.alt-api: IMiniportWaveCyclic.NewStream
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
req.iface: IMiniportWaveCyclic
---

# IMiniportWaveCyclic::NewStream method



## -description
<p>The <code>NewStream</code> method creates a new instance of a logical stream that is associated with a specified physical channel.</p>


## -syntax

````
NTSTATUS NewStream(
  [out]          PMINIPORTWAVECYCLICSTREAM *Stream,
  [in, optional] PUNKNOWN                  OuterUnknown,
  [in]           POOL_TYPE                 PoolType,
  [in]           ULONG                     Pin,
  [in]           BOOLEAN                   Capture,
  [in]           PKSDATAFORMAT             DataFormat,
  [out]          PDMACHANNEL               *DmaChannel,
  [out]          PSERVICEGROUP             *ServiceGroup
);
````


## -parameters
<dl>

### -param <i>Stream</i> [out]

<dd>
<p>Output pointer for the new stream. This parameter points to a caller-allocated pointer variable into which the method writes a pointer to the stream object's <a href="https://msdn.microsoft.com/library/windows/hardware/ff536715">IMiniportWaveCyclicStream</a> interface. The caller specifies a valid, non-<b>NULL</b> pointer value for this parameter.</p>
</dd>

### -param <i>OuterUnknown</i> [in, optional]

<dd>
<p>Pointer to the <b>IUnknown</b> interface of an object that needs to aggregate the stream object. This parameter is optional. If aggregation is not required, the caller specifies this parameter as <b>NULL</b>.</p>
</dd>

### -param <i>PoolType</i> [in]

<dd>
<p>Specifies the type of memory pool from which the storage for the DMA-channel object should be allocated. This parameter will be one of the nonpaged pool types defined in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559707">POOL_TYPE</a> enumeration.</p>
</dd>

### -param <i>Pin</i> [in]

<dd>
<p>Number of the pin that is to be opened. If the WaveCyclic miniport driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff536765">IMiniport::GetDescription</a> method outputs a filter descriptor that specifies a total of <i>n</i> pin factories on the filter, then valid values for parameter <i>Pin</i> are in the range 0 to <i>n</i>-1.</p>
</dd>

### -param <i>Capture</i> [in]

<dd>
<p>Specifies whether to create a capture stream or a render stream. This parameter is <b>TRUE</b> for a capture (input) channel, and <b>FALSE</b> for a playback (output) channel.</p>
</dd>

### -param <i>DataFormat</i> [in]

<dd>
<p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561656">KSDATAFORMAT</a> structure indicating the format to use for this instance.</p>
</dd>

### -param <i>DmaChannel</i> [out]

<dd>
<p>Output pointer to the DMA channel. This parameter points to a caller-allocated pointer variable into which the method writes a pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536547">IDmaChannel</a> interface of the miniport driver's DMA-channel object. The caller specifies a valid, non-<b>NULL</b> pointer value for this parameter. For more information, see the following Remarks section.</p>
</dd>

### -param <i>ServiceGroup</i> [out]

<dd>
<p>Output pointer for the service group. This parameter points to a caller-allocated pointer variable into which the method writes a pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536994">IServiceGroup</a> interface of the stream's service group object. This is the service group that is being registered for interrupt notification. The caller specifies a valid, non-<b>NULL</b> pointer value for this parameter.</p>
</dd>
</dl>

## -returns
<p><code>NewStream</code> returns STATUS_SUCCESS if the call was successful. Otherwise, the method returns an appropriate error code.</p>

## -remarks
<p>The <code>NewStream</code> method sets the initial state of the stream to KSSTATE_STOP and its initial position to zero. (See <a href="https://msdn.microsoft.com/library/windows/hardware/ff536720">IMiniportWaveCyclicStream::SetState</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff536716">IMiniportWaveCyclicStream::GetPosition</a>.)</p>

<p>The port driver calls only the following methods on the <i>DmaChannel</i> object:</p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536554">IDmaChannel::AllocatedBufferSize</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536556">IDmaChannel::BufferSize</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536557">IDmaChannel::CopyFrom</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536558">IDmaChannel::CopyTo</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536563">IDmaChannel::SetBufferSize</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536564">IDmaChannel::SystemAddress</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536554">IDmaChannel::AllocatedBufferSize</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536556">IDmaChannel::BufferSize</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536557">IDmaChannel::CopyFrom</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536558">IDmaChannel::CopyTo</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536563">IDmaChannel::SetBufferSize</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536564">IDmaChannel::SystemAddress</a>
</p>

<p>The <i>Stream</i>, <i>OuterUnknown</i>, <i>DmaChannel</i>, and <i>ServiceGroup</i> parameters follow the <a href="NULL">reference-counting conventions for COM objects</a>.</p>

<p>The <code>NewStream</code> method sets the initial state of the stream to KSSTATE_STOP and its initial position to zero. (See <a href="https://msdn.microsoft.com/library/windows/hardware/ff536720">IMiniportWaveCyclicStream::SetState</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff536716">IMiniportWaveCyclicStream::GetPosition</a>.)</p>

<p>The port driver calls only the following methods on the <i>DmaChannel</i> object:</p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536554">IDmaChannel::AllocatedBufferSize</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536556">IDmaChannel::BufferSize</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536557">IDmaChannel::CopyFrom</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536558">IDmaChannel::CopyTo</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536563">IDmaChannel::SetBufferSize</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536564">IDmaChannel::SystemAddress</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536554">IDmaChannel::AllocatedBufferSize</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536556">IDmaChannel::BufferSize</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536557">IDmaChannel::CopyFrom</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536558">IDmaChannel::CopyTo</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536563">IDmaChannel::SetBufferSize</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536564">IDmaChannel::SystemAddress</a>
</p>

<p>The <i>Stream</i>, <i>OuterUnknown</i>, <i>DmaChannel</i>, and <i>ServiceGroup</i> parameters follow the <a href="NULL">reference-counting conventions for COM objects</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536714">IMiniportWaveCyclic</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536715">IMiniportWaveCyclicStream</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559707">POOL_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536765">IMiniport::GetDescription</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561656">KSDATAFORMAT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536547">IDmaChannel</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536994">IServiceGroup</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IMiniportWaveCyclic::NewStream method%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
