---
UID: NF.ks.KsDispatchFastIoDeviceControlFailure
title: KsDispatchFastIoDeviceControlFailure
author: windows-driver-content
description: The KsDispatchFastIoDeviceControlFailure function is used in a KSDISPATCH_TABLE.FastDeviceIoControl entry that are not handled. The function should always return FALSE.
old-location: stream\ksdispatchfastiodevicecontrolfailure.htm
old-project: stream
ms.assetid: 7fb83c8d-e815-46c6-8011-75b25a4c0dd7
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsDispatchFastIoDeviceControlFailure
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
req.alt-api: KsDispatchFastIoDeviceControlFailure
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

# KsDispatchFastIoDeviceControlFailure function



## -description
<p>The <b>KsDispatchFastIoDeviceControlFailure</b> function is used in a KSDISPATCH_TABLE.FastDeviceIoControl entry that are not handled. The function should always return <b>FALSE</b>. </p>


## -syntax

````
BOOLEAN KsDispatchFastIoDeviceControlFailure(
  _In_      PFILE_OBJECT     FileObject,
  _In_      BOOLEAN          Wait,
  _In_opt_  PVOID            InputBuffer,
  _In_      ULONG            InputBufferLength,
  _Out_opt_ PVOID            OutputBuffer,
  _In_      ULONG            OutputBufferLength,
  _In_      ULONG            IoControlCode,
  _Out_     PIO_STATUS_BLOCK IoStatus,
  _In_      PDEVICE_OBJECT   DeviceObject
);
````


## -parameters
<dl>

### -param <i>FileObject</i> [in]

<dd>
<p>Not used.</p>
</dd>

### -param <i>Wait</i> [in]

<dd>
<p>Not used.</p>
</dd>

### -param <i>InputBuffer</i> [in, optional]

<dd>
<p>Not used.</p>
</dd>

### -param <i>InputBufferLength</i> [in]

<dd>
<p>Not used.</p>
</dd>

### -param <i>OutputBuffer</i> [out, optional]

<dd>
<p>Not used.</p>
</dd>

### -param <i>OutputBufferLength</i> [in]

<dd>
<p>Not used.</p>
</dd>

### -param <i>IoControlCode</i> [in]

<dd>
<p>Not used.</p>
</dd>

### -param <i>IoStatus</i> [out]

<dd>
<p>Not used.</p>
</dd>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Not used.</p>
</dd>
</dl>

## -returns
<p>The <b>KsDispatchFastIoDeviceControlFailure</b> function returns <b>FALSE</b>.</p>

## -remarks
<p>The <b>KsDispatchFastIoDeviceControlFailure</b> function is needed since the dispatch table for a particular opened instance of a device may not handle a specific major function that another opened instance needs to handle. Therefore, the function pointer in the driver object must always point to a function, such as the <b>KsDispatchFastIoDeviceControlFailure</b> function, that calls a dispatch table entry.</p>

<p>The <b>KsDispatchFastIoDeviceControlFailure</b> function is needed since the dispatch table for a particular opened instance of a device may not handle a specific major function that another opened instance needs to handle. Therefore, the function pointer in the driver object must always point to a function, such as the <b>KsDispatchFastIoDeviceControlFailure</b> function, that calls a dispatch table entry.</p>

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