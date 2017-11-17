---
UID: NF.ks.KsReadFile
title: KsReadFile
author: windows-driver-content
description: The KsReadFile function performs a read against the specified file object.
old-location: stream\ksreadfile.htm
ms.assetid: e3bb6ead-8129-4605-8755-3a56d4b3d8f6
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsReadFile
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
ms.keywords: KsReadFile
req.iface: 
---

# KsReadFile function



## -description
<p>The <b>KsReadFile</b> function performs a read against the specified file object. It is assumed the caller is serializing access to the file for operations against a FO_SYNCHRONOUS_IO file object. The function attempts to use <b>FastIoDispatch</b> if possible, or generates a read request against the device object. All relevant statistics are updated.</p>


## -syntax

````
NTSTATUS KsReadFile(
  _In_     PFILE_OBJECT     FileObject,
  _In_opt_ PKEVENT          Event,
  _In_opt_ PVOID            PortContext,
  _Out_    PIO_STATUS_BLOCK IoStatusBlock,
  _Out_    PVOID            Buffer,
  _In_     ULONG            Length,
  _In_opt_ ULONG            Key,
  _In_     KPROCESSOR_MODE  RequestorMode
);
````


## -parameters
<dl>

### -param <i>FileObject</i> [in]

<dd>
<p>Specifies the file object to perform the read against.</p>
</dd>

### -param <i>Event</i> [in, optional]

<dd>
<p>Optionally contains the event to use in the read. If no event is passed, the call is assumed to be on a synchronous file object. If not, the caller is waiting for the file object's event, or it may be asynchronously completed. If the file has been opened for synchronous I/O, this must be <b>NULL</b>. If the variable is used, it must be an event allocated by the object manager.</p>
</dd>

### -param <i>PortContext</i> [in, optional]

<dd>
<p>Optionally contains context information for a completion port.</p>
</dd>

### -param <i>IoStatusBlock</i> [out]

<dd>
<p>Specifies the address where the status information is to be returned. This is always assumed to be a valid address, regardless of the requester mode.</p>
</dd>

### -param <i>Buffer</i> [out]

<dd>
<p>Specifies the buffer in which to place the data read. If the buffer needs to be probed and locked, an exception handler is used, along with <i>RequesterMode</i>.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Specifies the size of the buffer passed.</p>
</dd>

### -param <i>Key</i> [in, optional]

<dd>
<p>Optionally contains a key, or zero if none</p>
</dd>

### -param <i>RequestorMode</i> [in]

<dd>
<p>Indicates the processor mode to place in the read IRP if one needs to be generated. Additionally, it is used if the buffer needs to be probed and locked. This variable also determines if a fast I/O call can be performed. If the requester mode is not KernelMode, but the previous mode was, then fast I/O cannot be used.</p>
</dd>
</dl>

## -returns
<p>The <b>KsReadFile</b> function returns STATUS_SUCCESS if successful, STATUS_PENDING if action is pending, or it returns a read error if unsuccessful.</p>

## -remarks


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