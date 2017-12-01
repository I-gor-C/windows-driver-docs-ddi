---
UID: NF.dmusicks.IMiniportDMus.NewStream
title: IMiniportDMus::NewStream
author: windows-driver-content
description: The NewStream method creates a new instance of a logical stream associated with a specified physical channel.
old-location: audio\iminiportdmus_newstream.htm
old-project: audio
ms.assetid: aa221279-8d59-4f6f-8fc6-ad09e36a12a9
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IMiniportDMus, NewStream, IMiniportDMus::NewStream
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dmusicks.h
req.include-header: Dmusicks.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IMiniportDMus.NewStream
req.alt-loc: dmusicks.h
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
req.iface: IMiniportDMus
---

# IMiniportDMus::NewStream method



## -description
<p>The <code>NewStream</code> method creates a new instance of a logical stream associated with a specified physical channel.</p>


## -syntax

````
NTSTATUS NewStream(
  [out]          PMXF             *ppMXF,
  [in, optional] PUNKNOWN         pOuterUnknown,
  [in]           POOL_TYPE        PoolType,
  [in]           ULONG            uPinId,
  [in]           DMUS_STREAM_TYPE StreamType,
  [in]           PKSDATAFORMAT    pDataFormat ,
  [out]          PSERVICEGROUP    *ppServiceGroup ,
  [in]           PAllocatorMXF    pAllocatorMXF,
  [in]           PMASTERCLOCK     pMasterClock,
  [out]          PULONGLONG       puuSchedulePreFetch
);
````


## -parameters
<dl>

### -param <i>ppMXF</i> [out]

<dd>
<p>Output pointer for the new stream. This parameter points to a caller-allocated pointer variable into which the method writes a pointer to the stream object's <a href="..\dmusicks\nn-dmusicks-imxf~r1.md">IMXF</a> interface.</p>
</dd>

### -param <i>pOuterUnknown</i> [in, optional]

<dd>
<p>Pointer to the <b>IUnknown</b> interface of an object that needs to aggregate the stream object. This parameter is optional. If aggregation is not required, the caller specifies this parameter as <b>NULL</b>.</p>
</dd>

### -param <i>PoolType</i> [in]

<dd>
<p>Specifies the type of memory pool from which the storage for the DMA-channel object should be allocated. This parameter is set to one of the <a href="..\wdm\ne-wdm--pool-type.md">POOL_TYPE</a> enumeration values.</p>
</dd>

### -param <i>uPinId</i> [in]

<dd>
<p>Specifies the pin ID. This parameter identifies the pin that is to be opened. If the DMus miniport driver's <a href="audio.iminiport_getdescription">IMiniport::GetDescription</a> method outputs a filter descriptor that specifies a total of <i>n</i> pin factories on the filter, then valid pin IDs are in the range 0 to <i>n</i>-1.</p>
</dd>

### -param <i>StreamType</i> [in]

<dd>
<p>Specifies the type of data stream to create. This parameter is set to one of the following DMUS_STREAM_TYPE enumeration values:</p>
<p></p>
<dl>

### -param <a id="DMUS_STREAM_MIDI_RENDER"></a><a id="dmus_stream_midi_render"></a>DMUS_STREAM_MIDI_RENDER

<dd>
<p>Specifies a MIDI output (playback) stream.</p>
</dd>

### -param <a id="DMUS_STREAM_MIDI_CAPTURE"></a><a id="dmus_stream_midi_capture"></a>DMUS_STREAM_MIDI_CAPTURE

<dd>
<p>Specifies a MIDI input stream.</p>
</dd>

### -param <a id="DMUS_STREAM_WAVE_SINK"></a><a id="dmus_stream_wave_sink"></a>DMUS_STREAM_WAVE_SINK

<dd>
<p>Specifies a wave output stream.</p>
</dd>
</dl>
<p>For more information, see the following Remarks section.</p>
</dd>

### -param <i>pDataFormat </i> [in]

<dd>
<p>Pointer to a kernel streaming <a href="stream.ksdataformat">KSDATAFORMAT</a> structure specifying the data format to use for this instance</p>
</dd>

### -param <i>ppServiceGroup </i> [out]

<dd>
<p>Output pointer for service group. This parameter points to a caller-allocated pointer variable into which the method writes a pointer to the <a href="..\portcls\nn-portcls-iservicegroup.md">IServiceGroup</a> interface of the stream's service group object. This is the service group that is being registered for interrupt notification.</p>
</dd>

### -param <i>pAllocatorMXF</i> [in]

<dd>
<p>Pointer to an <a href="..\dmusicks\nn-dmusicks-iallocatormxf~r1.md">IAllocatorMXF</a> object. This is the port driver's memory allocator, which is needed to recycle <a href="..\dmusicks\ns-dmusicks--dmus-kernel-event.md">DMUS_KERNEL_EVENT</a> structures.</p>
</dd>

### -param <i>pMasterClock</i> [in]

<dd>
<p>Pointer to an <a href="audio.imasterclock">IMasterClock</a> object. This master clock passes a wrapper for the KS clock to the miniport driver. The master-clock pointer is required to sync to reference time.</p>
</dd>

### -param <i>puuSchedulePreFetch</i> [out]

<dd>
<p>Output pointer for the schedule-prefetch time. This parameter is a pointer to a caller-allocated ULONGLONG variable into which the method writes a time value that specifies how far ahead to query for events. The time is specified in 100-nanosecond units. The port driver is responsible for sequencing any events that exceed the amount of time that the miniport driver specifies here.</p>
</dd>
</dl>

## -returns
<p><code>NewStream</code> returns S_OK if the call was successful. Otherwise, the method returns an appropriate error code.</p>

## -remarks
<p>Note that the port driver creates the <b>IAllocatorMXF</b> object that the <code>NewStream</code> method inputs through the <i>pAllocatorMXF</i> parameter, but the miniport driver creates the <b>IMXF</b> object that the method outputs through the <i>ppMXF</i> parameter. For more information about <b>IMXF</b> and <b>IAllocatorMXF</b>, see <a href="NULL">MIDI Transport</a>.</p>

<p>The meaning of the <code>IMiniportDMus::NewStream</code> method's <i>StreamType</i> parameter is similar to that of the <a href="audio.iminiportmidi_newstream">IMiniportMidi::NewStream</a> method's <i>Capture</i> parameter:</p>

<p>When creating a stream on a MIDI pin, the <b>IMiniportMidi::NewStream</b> method's <i>Capture</i> parameter indicates whether the pin is to serve as the sink for a MIDI render stream (<i>Capture</i> = <b>FALSE</b>) or as the source of a MIDI capture stream (<i>Capture</i> = <b>TRUE</b>).</p>

<p>Similarly, when creating a stream on a MIDI or DirectMusic pin, the <code>IMiniportDMus::NewStream</code> method's <i>StreamType</i> parameter can indicate whether the pin is to serve as the sink for a MIDI render stream (<i>StreamType</i> = DMUS_STREAM_MIDI_RENDER) or as the source of a MIDI capture stream (<i>StreamType</i> = DMUS_STREAM_MIDI_CAPTURE).</p>

<p>However, a pin on a DirectMusic filter can support a third option that is not available with a MIDI filter. A pin can serve as the source of a wave output stream (<i>StreamType</i> = DMUS_STREAM_WAVE_SINK). The DMus port driver implements the wave sink for this stream. After creating the wave output stream, the DMus port driver queries the stream object (which the port driver obtains through the <code>IMiniportDMus::NewStream</code> method's <i>ppMXF</i> output parameter) for its <a href="..\dmusicks\nn-dmusicks-isynthsinkdmus.md">ISynthSinkDMus</a> interface. The port driver's wave sink calls the <b>Render</b> method on this interface to pull wave data from the software synthesizer. For more information, see <a href="NULL">A Wave Sink for Kernel-Mode Software Synthesizers</a>.</p>

<p>The <i>ppMXF</i>, <i>pOuterUnknown</i>, <i>ppServiceGroup</i>, <i>pAllocatorMXF</i>, and <i>pMasterClock</i> parameters follow the <a href="NULL">reference-counting conventions for COM objects</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dmusicks.h (include Dmusicks.h)</dt>
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
<a href="..\dmusicks\nn-dmusicks-iminiportdmus.md">IMiniportDMus</a>
</dt>
<dt>
<a href="..\dmusicks\nn-dmusicks-imxf~r1.md">IMXF</a>
</dt>
<dt>
<a href="..\wdm\ne-wdm--pool-type.md">POOL_TYPE</a>
</dt>
<dt>
<a href="audio.iminiport_getdescription">IMiniport::GetDescription</a>
</dt>
<dt>
<a href="stream.ksdataformat">KSDATAFORMAT</a>
</dt>
<dt>
<a href="..\portcls\nn-portcls-iservicegroup.md">IServiceGroup</a>
</dt>
<dt>
<a href="..\dmusicks\nn-dmusicks-iallocatormxf~r1.md">IAllocatorMXF</a>
</dt>
<dt>
<a href="..\dmusicks\ns-dmusicks--dmus-kernel-event.md">DMUS_KERNEL_EVENT</a>
</dt>
<dt>
<a href="audio.imasterclock">IMasterClock</a>
</dt>
<dt>
<a href="audio.iminiportmidi_newstream">IMiniportMidi::NewStream</a>
</dt>
<dt>
<a href="..\dmusicks\nn-dmusicks-isynthsinkdmus.md">ISynthSinkDMus</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IMiniportDMus::NewStream method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
