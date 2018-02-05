---
UID : NF:dmusicks.IMiniportDMus.NewStream
title : IMiniportDMus::NewStream method
author : windows-driver-content
description : The NewStream method creates a new instance of a logical stream associated with a specified physical channel.
old-location : audio\iminiportdmus_newstream.htm
old-project : audio
ms.assetid : aa221279-8d59-4f6f-8fc6-ad09e36a12a9
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : audmp-routines_a6630d1b-4a9d-4d4e-973a-09d541d7db70.xml, IMiniportDMus, NewStream method [Audio Devices], IMiniportDMus interface, dmusicks/IMiniportDMus::NewStream, audio.iminiportdmus_newstream, IMiniportDMus interface [Audio Devices], NewStream method, NewStream method [Audio Devices], NewStream, IMiniportDMus::NewStream
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : method
req.header : dmusicks.h
req.include-header : Dmusicks.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : dmusicks.h
req.dll : 
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : DMUS_STREAM_TYPE
---


# NewStream method
The <code>NewStream</code> method creates a new instance of a logical stream associated with a specified physical channel.

## Syntax

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

## Parameters

`MXF`



`OuterUnknown`



`PoolType`

Specifies the type of memory pool from which the storage for the DMA-channel object should be allocated. This parameter is set to one of the <a href="..\wdm\ne-wdm-_pool_type.md">POOL_TYPE</a> enumeration values.

`PinID`



`StreamType`

Specifies the type of data stream to create. This parameter is set to one of the following DMUS_STREAM_TYPE enumeration values:



For more information, see the following Remarks section.


#### DMUS_STREAM_MIDI_CAPTURE

Specifies a MIDI input stream.


#### DMUS_STREAM_MIDI_RENDER

Specifies a MIDI output (playback) stream.


#### DMUS_STREAM_WAVE_SINK

Specifies a wave output stream.

`DataFormat`



`ServiceGroup`



`AllocatorMXF`



`MasterClock`



`SchedulePreFetch`




## Return Value

<code>NewStream</code> returns S_OK if the call was successful. Otherwise, the method returns an appropriate error code.

## Remarks

Note that the port driver creates the <b>IAllocatorMXF</b> object that the <code>NewStream</code> method inputs through the <i>pAllocatorMXF</i> parameter, but the miniport driver creates the <b>IMXF</b> object that the method outputs through the <i>ppMXF</i> parameter. For more information about <b>IMXF</b> and <b>IAllocatorMXF</b>, see <a href="https://msdn.microsoft.com/ce9ec589-0aea-4ed9-a60d-50f2ddfb0c13">MIDI Transport</a>.

The meaning of the <code>IMiniportDMus::NewStream</code> method's <i>StreamType</i> parameter is similar to that of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536710">IMiniportMidi::NewStream</a> method's <i>Capture</i> parameter:
<ul>
<li>
When creating a stream on a MIDI pin, the <b>IMiniportMidi::NewStream</b> method's <i>Capture</i> parameter indicates whether the pin is to serve as the sink for a MIDI render stream (<i>Capture</i> = <b>FALSE</b>) or as the source of a MIDI capture stream (<i>Capture</i> = <b>TRUE</b>).

</li>
<li>
Similarly, when creating a stream on a MIDI or DirectMusic pin, the <code>IMiniportDMus::NewStream</code> method's <i>StreamType</i> parameter can indicate whether the pin is to serve as the sink for a MIDI render stream (<i>StreamType</i> = DMUS_STREAM_MIDI_RENDER) or as the source of a MIDI capture stream (<i>StreamType</i> = DMUS_STREAM_MIDI_CAPTURE).

</li>
</ul>However, a pin on a DirectMusic filter can support a third option that is not available with a MIDI filter. A pin can serve as the source of a wave output stream (<i>StreamType</i> = DMUS_STREAM_WAVE_SINK). The DMus port driver implements the wave sink for this stream. After creating the wave output stream, the DMus port driver queries the stream object (which the port driver obtains through the <code>IMiniportDMus::NewStream</code> method's <i>ppMXF</i> output parameter) for its <a href="..\dmusicks\nn-dmusicks-isynthsinkdmus.md">ISynthSinkDMus</a> interface. The port driver's wave sink calls the <b>Render</b> method on this interface to pull wave data from the software synthesizer. For more information, see <a href="https://msdn.microsoft.com/37ba9ad5-8b35-4252-a6fd-46dead924294">A Wave Sink for Kernel-Mode Software Synthesizers</a>.

The <i>ppMXF</i>, <i>pOuterUnknown</i>, <i>ppServiceGroup</i>, <i>pAllocatorMXF</i>, and <i>pMasterClock</i> parameters follow the <a href="https://msdn.microsoft.com/e6b19110-37e2-4d23-a528-6393c12ab650">reference-counting conventions for COM objects</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | dmusicks.h (include Dmusicks.h) |
| **Library** | dmusicks.h |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="..\dmusicks\ns-dmusicks-_dmus_kernel_event.md">DMUS_KERNEL_EVENT</a>

<a href="..\ks\ns-ks-ksdataformat.md">KSDATAFORMAT</a>

<a href="..\dmusicks\nn-dmusicks-isynthsinkdmus.md">ISynthSinkDMus</a>

<a href="..\dmusicks\nn-dmusicks-iallocatormxf.md">IAllocatorMXF</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff536710">IMiniportMidi::NewStream</a>

<a href="..\wdm\ne-wdm-_pool_type.md">POOL_TYPE</a>

<a href="..\dmusicks\nn-dmusicks-imxf.md">IMXF</a>

<a href="..\portcls\nn-portcls-iservicegroup.md">IServiceGroup</a>

<a href="..\dmusicks\nn-dmusicks-iminiportdmus.md">IMiniportDMus</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff536765">IMiniport::GetDescription</a>

<a href="..\dmusicks\nn-dmusicks-imasterclock.md">IMasterClock</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IMiniportDMus::NewStream method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>