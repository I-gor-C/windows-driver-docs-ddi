---
UID: NF.ks.KsStreamIo
title: KsStreamIo
author: windows-driver-content
description: The KsStreamIo function performs a stream read or write against the specified file object. The function attempts to use FastIoDispatch if possible, or it generates a read or write request against the device object.
old-location: stream\ksstreamio.htm
old-project: stream
ms.assetid: 74c62a30-42b9-4ea7-b52a-014e263d886e
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsStreamIo
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsStreamIo
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: 
req.iface: 
---

# KsStreamIo function



## -description
<p>The <b>KsStreamIo</b> function performs a stream read or write against the specified file object. The function attempts to use <b>FastIoDispatch</b> if possible, or it generates a read or write request against the device object.</p>


## -syntax

````
NTSTATUS KsStreamIo(
  _In_     PFILE_OBJECT            FileObject ,
  _In_opt_ PKEVENT                 Event ,
  _In_opt_ PVOID                   PortContext ,
  _In_opt_ PIO_COMPLETION_ROUTINE  CompletionRoutine ,
  _In_opt_ PVOID                   CompletionContext ,
  _In_opt_ KSCOMPLETION_INVOCATION CompletionInvocationFlags ,
  _Out_    PIO_STATUS_BLOCK        IoStatusBlock ,
  _Inout_  PVOID                   StreamHeaders ,
  _In_     ULONG                   Length ,
  _In_     ULONG                   Flags ,
  _In_     KPROCESSOR_MODE         RequestorMode 
);
````


## -parameters
<dl>

### -param <i>FileObject </i> [in]

<dd>
<p>Specifies the file object to perform the I/O against.</p>
</dd>

### -param <i>Event </i> [in, optional]

<dd>
<p>Optionally contains the event to use in the I/O. If none is passed, the call is assumed to be on a synchronous file object or the caller is waiting for the file object's event, or else it can be asynchronously completed. If used, and the KSSTREAM_SYNCHRONOUS flag is not set, this must be an event allocated by the object manager. If the caller is performing asynchronous I/O, it must either wait for the file object's event or pass an event in this parameter and wait for it. If this is not done, then there is no way for the caller to know when the IoStatusBlock has been updated by the call.</p>
</dd>

### -param <i>PortContext </i> [in, optional]

<dd>
<p>Optionally contains context information for a completion port.</p>
</dd>

### -param <i>CompletionRoutine </i> [in, optional]

<dd>
<p>Optionally points to a completion routine for this IRP.</p>
</dd>

### -param <i>CompletionContext </i> [in, optional]

<dd>
<p>If <i>CompletionRoutine</i> is specified, this provides a context pointer in the completion routine callback.</p>
</dd>

### -param <i>CompletionInvocationFlags </i> [in, optional]

<dd>
<p>Specifies invocation flags specifying when the completion routine is invoked. See following table for the values used.</p>
</dd>

### -param <i>IoStatusBlock </i> [out]

<dd>
<p>Location to return the status information. This is always assumed to be a valid address, regardless of the requester mode. The value must remain valid until the call has updated the status. The caller must either perform synchronous I/O or must wait for the file object's event or an event passed in the Event parameter before allowing this address to become invalid.</p>
</dd>

### -param <i>StreamHeaders </i> [in, out]

<dd>
<p>Specifies the list of stream headers. This address, as well as the addresses of the data buffers, are assumed to have been probed for appropriate access. Kernel-mode clients submitting streaming headers must allocate the headers from NonPagedPool memory.</p>
</dd>

### -param <i>Length </i> [in]

<dd>
<p>Specifies the size of the <i>StreamHeaders</i> passed.</p>
</dd>

### -param <i>Flags </i> [in]

<dd>
<p>Specifies various flags for the I/O. See the following table for the values used.</p>
</dd>

### -param <i>RequestorMode </i> [in]

<dd>
<p>Indicates the processor mode to place in the IRP if one is needs to be generated. This variable also determines if a fast I/O call can be performed. If the requester mode is not kernel mode, but the previous mode is, then fast I/O cannot be used.</p>
</dd>
</dl>

## -returns
<p>The <b>KsStreamIo</b> function returns STATUS_SUCCESS if successful, STATUS_PENDING if action is pending, or if unsuccessful it returns an I/O error.</p>

## -remarks
<p>The following enumerated values are used for the <i>CompletionInvocationFlags</i> variable and are of type KSCOMPLETION_INVOCATION:</p>

<p>KsInvokeOnSuccess</p>

<p>Invokes the completion routine on success.</p>

<p>KsInvokeOnError</p>

<p>Invokes the completion routine on error.</p>

<p>KsInvokeOnCancel</p>

<p>Invokes the completion routine on cancellation.</p>

<p> </p>

<p>The following defined values are used for the <i>Flags</i> variable:</p>

<p>KSSTREAM_READ</p>

<p>Specifies that an IOCTL_KS_STREAMREAD IRP is to be built. This is the default.</p>

<p>KSSTREAM_WRITE</p>

<p>Specifies that an IOCTL_KS_STREAMWRITE IRP is to be built.</p>

<p>KSSTREAM_PAGED_DATA</p>

<p>Specifies that the data is pageable. This is the default and can be used at all times.</p>

<p>KSSTREAM_NONPAGED_DATA</p>

<p>Specifies that the data is nonpaged and can be used as a performance enhancement.</p>

<p>KSSTREAM_SYNCHRONOUS</p>

<p>Specifies that the IRP is synchronous. This means that if the <i>Event</i> parameter is passed, it is not treated as an object manager event and is not referenced or dereferenced.</p>

<p> </p>

<p>KSSTREAM_READ is equivalent to KSPROBE_STREAMREAD.</p>

<p>Similarly, KSSTREAM_WRITE is equivalent to KSPROBE_STREAMWRITE.</p>

<p>The following enumerated values are used for the <i>CompletionInvocationFlags</i> variable and are of type KSCOMPLETION_INVOCATION:</p>

<p>KsInvokeOnSuccess</p>

<p>Invokes the completion routine on success.</p>

<p>KsInvokeOnError</p>

<p>Invokes the completion routine on error.</p>

<p>KsInvokeOnCancel</p>

<p>Invokes the completion routine on cancellation.</p>

<p> </p>

<p>The following defined values are used for the <i>Flags</i> variable:</p>

<p>KSSTREAM_READ</p>

<p>Specifies that an IOCTL_KS_STREAMREAD IRP is to be built. This is the default.</p>

<p>KSSTREAM_WRITE</p>

<p>Specifies that an IOCTL_KS_STREAMWRITE IRP is to be built.</p>

<p>KSSTREAM_PAGED_DATA</p>

<p>Specifies that the data is pageable. This is the default and can be used at all times.</p>

<p>KSSTREAM_NONPAGED_DATA</p>

<p>Specifies that the data is nonpaged and can be used as a performance enhancement.</p>

<p>KSSTREAM_SYNCHRONOUS</p>

<p>Specifies that the IRP is synchronous. This means that if the <i>Event</i> parameter is passed, it is not treated as an object manager event and is not referenced or dereferenced.</p>

<p> </p>

<p>KSSTREAM_READ is equivalent to KSPROBE_STREAMREAD.</p>

<p>Similarly, KSSTREAM_WRITE is equivalent to KSPROBE_STREAMWRITE.</p>

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
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
</table>