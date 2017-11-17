---
UID: NF.ks.KsSynchronousIoControlDevice
title: KsSynchronousIoControlDevice
author: windows-driver-content
description: The KsSynchronousIoControlDevice function performs a synchronous device I/O control on the target device object. It waits in a nonalertable state until the I/O completes. This function can only be called at PASSIVE_LEVEL.
old-location: stream\kssynchronousiocontroldevice.htm
ms.assetid: 7e4ca8ea-52c1-462e-bf02-cc82e9ab2be2
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
req.alt-api: KsSynchronousIoControlDevice
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
ms.keywords: KsSynchronousIoControlDevice
req.iface: 
---

# KsSynchronousIoControlDevice function



## -description
<p>The <b>KsSynchronousIoControlDevice</b> function performs a synchronous device I/O control on the target device object. It waits in a nonalertable state until the I/O completes. This function can only be called at PASSIVE_LEVEL.</p>


## -syntax

````
NTSTATUS KsSynchronousIoControlDevice(
  _In_  PFILE_OBJECT    FileObject,
  _In_  KPROCESSOR_MODE RequesorMode,
  _In_  ULONG           IoControl,
  _In_  PVOID           InBuffer,
  _In_  ULONG           InSize,
  _Out_ PVOID           OutBuffer,
  _In_  ULONG           OutSize,
  _Out_ PULONG          BytesReturned
);
````


## -parameters
<dl>

### -param <i>FileObject</i> [in]

<dd>
<p>Indicates the file object to fill in the first stack location with.</p>
</dd>

### -param <i>RequesorMode</i> [in]

<dd>
<p>Indicates the processor mode to place in the IRP if one needs to be generated.</p>
</dd>

### -param <i>IoControl</i> [in]

<dd>
<p>Specifies the I/O control to send.</p>
</dd>

### -param <i>InBuffer</i> [in]

<dd>
<p>Points to the device input buffer.</p>
</dd>

### -param <i>InSize</i> [in]

<dd>
<p>Specifies the size in bytes of the device input buffer.</p>
</dd>

### -param <i>OutBuffer</i> [out]

<dd>
<p>Points to the device output buffer.</p>
</dd>

### -param <i>OutSize</i> [in]

<dd>
<p>Specifies the size in bytes of the device output buffer.</p>
</dd>

### -param <i>BytesReturned</i> [out]

<dd>
<p>Points to the place in which to put the number of bytes returned.</p>
</dd>
</dl>

## -returns
<p><b>KsSynchronousIoControlDevice </b>returns the result of the device I/O control.</p>

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