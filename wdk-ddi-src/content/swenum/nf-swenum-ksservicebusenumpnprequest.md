---
UID: NF.swenum.KsServiceBusEnumPnpRequest
title: KsServiceBusEnumPnpRequest
author: windows-driver-content
description: The KsServiceBusEnumPnpRequest function services IRP_MJ_PNP requests on behalf of the demand-load bus enumerator object that was created with KsCreateBusEnumObject.
old-location: stream\ksservicebusenumpnprequest.htm
old-project: stream
ms.assetid: cdf0017f-e8c0-4e95-bea6-8bc2509c090c
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsServiceBusEnumPnpRequest
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: swenum.h
req.include-header: Swenum.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsServiceBusEnumPnpRequest
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
req.product: Windows 10 or later.
---

# KsServiceBusEnumPnpRequest function



## -description
<p><i>This function is intended for internal use only.</i></p>
<p>The <b>KsServiceBusEnumPnpRequest</b> function services IRP_MJ_PNP requests on behalf of the demand-load bus enumerator object that was created with <b>KsCreateBusEnumObject</b>. </p>


## -syntax

````
NTSTATUS KsServiceBusEnumPnpRequest(
  _In_    PDEVICE_OBJECT DeviceObject,
  _Inout_ PIRP           Irp
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Pointer to the device object.</p>
</dd>

### -param <i>Irp</i> [in, out]

<dd>
<p>Pointer to the IRP associated with the device object.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_NOT_SUPPORTED if the IRP is not handled by <b>KsServiceBusEnumPnpRequest</b> or STATUS_INVALID_DEVICE_REQUEST if the device object is neither a parent or child of the demand-load bus enumerator object. Otherwise, it returns the status code for the IRP processing.</p>

## -remarks
<p><b>KsServiceBusEnumPnpRequest</b> services the following Plug and Play IRPs for an FDO or parent device:</p>

<p>IRP_MN_START_DEVICE</p>

<p>IRP_MN_QUERY_BUS_INFORMATION</p>

<p>IRP_MN_QUERY_DEVICE_RELATIONS</p>

<p>IRP_MN_QUERY_STOP_DEVICE</p>

<p>IRP_MN_QUERY_REMOVE_DEVICE</p>

<p>IRP_MN_CANCEL_STOP_DEVICE</p>

<p>IRP_MN_CANCEL_REMOVE_DEVICE</p>

<p>IRP_MN_STOP_DEVICE</p>

<p>IRP_MN_REMOVE_DEVICE</p>

<p><b>KsServiceBusEnumPnpRequest</b> services the following Plug and Play IRPs for a PDO or child device:</p>

<p>IRP_MN_QUERY_DEVICE_RELATIONS (TargetDeviceRelations)</p>

<p>IRP_MN_QUERY_PNP_DEVICE_STATE</p>

<p>IRP_MN_QUERY_ID</p>

<p>IRP_MN_QUERY_INTERFACE</p>

<p>IRP_MN_QUERY_RESOURCES</p>

<p>IRP_MN_QUERY_RESOURCE_REQUIREMENTS</p>

<p>IRP_MN_READ_CONFIG</p>

<p>IRP_MN_WRITE_CONFIG</p>

<p>IRP_MN_QUERY_CAPABILITIES</p>

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
<dt>Swenum.h (include Swenum.h)</dt>
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
<a href="..\swenum\nf-swenum-kscreatebusenumobject.md">KsCreateBusEnumObject</a>
</dt>
<dt>
<a href="..\swenum\nf-swenum-ksisbusenumchilddevice.md">KsIsBusEnumChildDevice</a>
</dt>
<dt>
<a href="..\swenum\nf-swenum-ksservicebusenumcreaterequest.md">KsServiceBusEnumCreateRequest</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsServiceBusEnumPnpRequest function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
