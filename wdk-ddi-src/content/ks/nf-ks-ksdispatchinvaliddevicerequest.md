---
UID: NF.ks.KsDispatchInvalidDeviceRequest
title: KsDispatchInvalidDeviceRequest
author: windows-driver-content
description: The KsDispatchInvalidDeviceRequest function is used in KSDISPATCH_TABLE entries that are not handled and that need to return STATUS_INVALID_DEVICE_REQUEST.
old-location: stream\ksdispatchinvaliddevicerequest.htm
old-project: stream
ms.assetid: 7c30bc5b-2bd5-4db9-acaf-0c0347035ae3
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsDispatchInvalidDeviceRequest
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
req.alt-api: KsDispatchInvalidDeviceRequest
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

# KsDispatchInvalidDeviceRequest function



## -description
<p>The <b>KsDispatchInvalidDeviceRequest</b> function is used in KSDISPATCH_TABLE entries that are not handled and that need to return STATUS_INVALID_DEVICE_REQUEST. </p>


## -syntax

````
NTSTATUS KsDispatchInvalidDeviceRequest(
  _In_ PDEVICE_OBJECT DeviceObject,
  _In_ PIRP           Irp
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Specifies the device object associated with the IRP.</p>
</dd>

### -param <i>Irp</i> [in]

<dd>
<p>Specifies the IRP that is not being handled.</p>
</dd>
</dl>

## -returns
<p>The <b>KsDispatchInvalidDeviceRequest</b> function returns STATUS_INVALID_DEVICE_REQUEST and completes the IRP.</p>

## -remarks
<p>The <b>KsDispatchInvalidDeviceRequest</b> function is needed because the dispatch table for an opened instance of a device may not handle a specific major function that another opened instance needs to handle. Therefore, the function pointer in the driver object must always point to a function that calls a dispatch table entry.</p>

<p>The <b>KsDispatchInvalidDeviceRequest</b> function is needed because the dispatch table for an opened instance of a device may not handle a specific major function that another opened instance needs to handle. Therefore, the function pointer in the driver object must always point to a function that calls a dispatch table entry.</p>

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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561699">KsDispatchFastIoDeviceControlFailure</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561706">KsDispatchFastWriteFailure</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561703">KsDispatchFastReadFailure</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsDispatchInvalidDeviceRequest function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
