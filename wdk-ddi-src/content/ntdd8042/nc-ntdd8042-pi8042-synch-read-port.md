---
UID: NC.ntdd8042.PI8042_SYNCH_READ_PORT
title: PI8042_SYNCH_READ_PORT
author: windows-driver-content
description: The PI8042_SYNCH_READ_PORT-typed callback routine does a synchronized read from an i8042 port. I8042prt supplies this callback.
old-location: hid\pi8042_synch_read_port.htm
old-project: hid
ms.assetid: 970bb5ed-2ddd-4d91-a90f-3df3bb7fa3f9
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: MSFC_VirtualFibrePortAttributes, MSFC_VirtualFibrePortAttributes, *PMSFC_VirtualFibrePortAttributes
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ntdd8042.h
req.include-header: Ntdd8042.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SynchReadPort
req.alt-loc: ntdd8042.h
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
req.iface: 
---

# PI8042_SYNCH_READ_PORT callback



## -description
<p>The PI8042_SYNCH_READ_PORT-typed callback routine does a synchronized read from an i8042 port. I8042prt supplies this callback.</p>


## -prototype

````
PI8042_SYNCH_READ_PORT SynchReadPort;

NTSTATUS SynchReadPort(
  _In_  PVOID   Context,
  _Out_ PUCHAR  Value,
  _In_  BOOLEAN WaitForACK
)
{ ... }
````


## -parameters
<dl>

### -param Context [in]

<dd>
<p>Pointer to a context supplied by I8042prt.</p>
</dd>

### -param Value [out]

<dd>
<p>Pointer to the UCHAR value returned by the routine.</p>
</dd>

### -param WaitForACK [in]

<dd>
<p>Not used.</p>
</dd>
</dl>

## -returns
<p>The PI8042_SYNCH_READ_PORT callback returns one of the following status values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The routine successfully returned a byte.</p><dl>
<dt><b>STATUS_IO_TIMEOUT</b></dt>
</dl><p>The hardware was not ready for a read access.</p>

<p> </p>

## -remarks
<p>The PI8042_SYNCH_READ_PORT callback can only be used in a <a href="..\ntdd8042\nc-ntdd8042-pi8042-keyboard-initialization-routine.md">PI8042_KEYBOARD_INITIALIZATION_ROUTINE</a> callback. I8042prt specifies the read port callback in the <i>ReadPort</i> parameter that I8042prt inputs to a keyboard initialization routine.</p>

<p>The routine polls the hardware until a read is returned by the hardware or an internal time-out occurs.</p>

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
<dt>Ntdd8042.h (include Ntdd8042.h)</dt>
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
<a href="..\ntdd8042\nc-ntdd8042-pi8042-keyboard-initialization-routine.md">PI8042_KEYBOARD_INITIALIZATION_ROUTINE</a>
</dt>
<dt>
<a href="..\ntdd8042\nc-ntdd8042-pi8042-synch-write-port.md">PI8042_SYNCH_WRITE_PORT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20PI8042_SYNCH_READ_PORT callback function%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
