---
UID : NN:portcls.IMiniportMidiStream
title : IMiniportMidiStream
author : windows-driver-content
description : The IMiniportMidiStream interface represents the MIDI stream that flows through a pin on a MIDI filter.
old-location : audio\iminiportmidistream.htm
old-project : audio
ms.assetid : a3b763af-2800-4e6d-b9f8-060ba80de7e6
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : PcUnregisterIoTimeout
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
req.alt-api : IMiniportMidiStream
req.alt-loc : portcls.h
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
req.typenames : PC_EXIT_LATENCY, *PPC_EXIT_LATENCY
---

# IMiniportMidiStream interface

The <code>IMiniportMidiStream</code> interface represents the MIDI stream that flows through a pin on a MIDI filter. The filter wraps a MIDI synthesizer or capture device and is implemented by pairing a MIDI port driver with a MIDI miniport driver. The miniport driver implements the <code>IMiniportMidiStream</code> interface and exposes it to the port driver. The port driver creates a stream object with this interface by calling the miniport driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff536710">IMiniportMidi::NewStream</a> method. <code>IMiniportMidiStream</code> inherits from the <b>IUnknown</b> interface.

 This interface provides methods for reading and writing a MIDI stream and for setting the format and state of a MIDI stream.

## Methods

<p>The <b>IMiniportMidiStream</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [portcls.IMiniportMidiStream.Read](nf-portcls-iminiportmidistream-read.md) | The Read method reads data from an incoming MIDI stream. |
| [portcls.IMiniportMidiStream.SetFormat](nf-portcls-iminiportmidistream-setformat.md) | The SetFormat method sets the KS data format of the MIDI stream. |
| [portcls.IMiniportMidiStream.SetState](nf-portcls-iminiportmidistream-setstate.md) | The SetState method sets the stream's transport state to a new state value. |
| [portcls.IMiniportMidiStream.Write](nf-portcls-iminiportmidistream-write.md) | The Write method writes data to an outgoing MIDI stream. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | portcls.h |
| **DLL** |  |