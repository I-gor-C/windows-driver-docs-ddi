---
UID: NF.portcls.IMiniportMidiStream.Read
title: IMiniportMidiStream::Read
author: windows-driver-content
description: The Read method reads data from an incoming MIDI stream.
old-location: audio\iminiportmidistream_read.htm
ms.assetid: 448dc408-c47f-4c8b-8baf-a831c69c3020
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: audio
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IMiniportMidiStream.Read
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
req.irql: DISPATCH_LEVEL
ms.keywords: IMiniportMidiStream, Read, IMiniportMidiStream::Read
req.iface: IMiniportMidiStream
---

# IMiniportMidiStream::Read method



## -description
<p>The <code>Read</code> method reads data from an incoming MIDI stream.</p>


## -syntax

````
NTSTATUS Read(
  [in]  PVOID  BufferAddress,
  [in]  ULONG  BufferLength,
  [out] PULONG BytesRead
);
````


## -parameters
<dl>

### -param <i>BufferAddress</i> [in]

<dd>
<p>Specifies the address of a caller-allocated buffer. The method copies the incoming MIDI data from the device to the buffer. The allocated size of this buffer must be greater than or equal to <i>BufferLength</i>.</p>
</dd>

### -param <i>BufferLength</i> [in]

<dd>
<p>Specifies the length in bytes of the buffer pointed to by <i>BufferAddress</i>.</p>
</dd>

### -param <i>BytesRead</i> [out]

<dd>
<p>Output pointer to a caller-allocated variable into which the method writes a count specifying the actual number of bytes successfully read from the device into the buffer.</p>
</dd>
</dl>

## -returns
<p><code>Read</code> returns STATUS_SUCCESS if the call was successful. Otherwise, the method returns an appropriate error code. The following table shows some of the possible return status codes.</p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>Invalid device request (for example, calling <code>Read</code> on a MIDI output stream).</p>

<p> </p>

## -remarks
<p>The miniport driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff536893">IPortMidi::Notify</a> to notify the port driver when incoming MIDI data becomes available from the capture device. The port driver calls <b>IMiniportMidi::Read</b> to retrieve the data. The port driver continues to call <code>Read</code> as long as more data is available.</p>

<p>The <code>Read</code> method returns STATUS_SUCCESS and a <i>BytesRead</i> count of zero to indicate that no more MIDI input data is currently available from the device. </p>

<p>The miniport driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff536893">IPortMidi::Notify</a> to notify the port driver when incoming MIDI data becomes available from the capture device. The port driver calls <b>IMiniportMidi::Read</b> to retrieve the data. The port driver continues to call <code>Read</code> as long as more data is available.</p>

<p>The <code>Read</code> method returns STATUS_SUCCESS and a <i>BytesRead</i> count of zero to indicate that no more MIDI input data is currently available from the device. </p>

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
<p>DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536893">IPortMidi::Notify</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536708">IMiniportMidiStream::Write</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IMiniportMidiStream::Read method%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
