---
UID : NN:portcls.IMiniportWavePciStream
title : IMiniportWavePciStream
author : windows-driver-content
description : The IMiniportWavePciStream interface represents the wave stream that flows through a pin on a WavePci filter.
old-location : audio\iminiportwavepcistream.htm
old-project : audio
ms.assetid : 2341f914-d877-4a87-ac74-fb51e646510e
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : audio.iminiportwavepcistream, IMiniportWavePciStream interface [Audio Devices], IMiniportWavePciStream interface [Audio Devices], described, IMiniportWavePciStream, portcls/IMiniportWavePciStream, audmp-routines_4bb3e6fe-950d-4981-a35a-bc9106d98edb.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : portcls.h
req.include-header : 
req.target-type : Windows
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
req.lib : Portcls.lib
req.dll : 
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : PC_EXIT_LATENCY, *PPC_EXIT_LATENCY
---

# IMiniportWavePciStream interface

The <code>IMiniportWavePciStream</code> interface represents the wave stream that flows through a pin on a WavePci filter. The filter wraps a WavePci rendering or capture device and is implemented by pairing a WavePci port driver with a WavePci miniport driver. The miniport driver implements the <code>IMiniportWavePciStream</code> interface and exposes it to the port driver. The miniport driver creates a stream object with this interface when the port driver calls the miniport driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff536735">IMiniportWavePci::NewStream</a> method. <code>IMiniportWavePciStream</code> inherits from the <b>IUnknown</b> interface.

The <code>IMiniportWavePciStream</code> interface provides methods for managing a single stream of incoming or outgoing audio wave data. This is the interface that exposes most of the miniport driver's functionality.

## Methods

<p>The <b>IMiniportWavePciStream</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [portcls.IMiniportWavePciStream.GetAllocatorFraming](nf-portcls-iminiportwavepcistream-getallocatorframing.md) | The GetAllocatorFraming method gets the preferred allocator-framing parameters for the stream. |
| [portcls.IMiniportWavePciStream.GetPosition](nf-portcls-iminiportwavepcistream-getposition.md) | The GetPosition method gets the current position of the stream. |
| [portcls.IMiniportWavePciStream.MappingAvailable](nf-portcls-iminiportwavepcistream-mappingavailable.md) | The MappingAvailable method indicates that a new mapping is available. |
| [portcls.IMiniportWavePciStream.NormalizePhysicalPosition](nf-portcls-iminiportwavepcistream-normalizephysicalposition.md) | The NormalizePhysicalPosition method converts a physical buffer position to a time-based value. |
| [portcls.IMiniportWavePciStream.RevokeMappings](nf-portcls-iminiportwavepcistream-revokemappings.md) | The RevokeMappings method revokes mappings that were previously obtained through IPortWavePciStream::GetMapping. |
| [portcls.IMiniportWavePciStream.Service](nf-portcls-iminiportwavepcistream-service.md) | The Service method notifies the miniport driver of a request for service. |
| [portcls.IMiniportWavePciStream.SetFormat](nf-portcls-iminiportwavepcistream-setformat.md) | The SetFormat method sets the KS data format of the wave stream. |
| [portcls.IMiniportWavePciStream.SetState](nf-portcls-iminiportwavepcistream-setstate.md) | The SetState method changes the state of the stream transport. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | portcls.h |
| **DLL** |  |