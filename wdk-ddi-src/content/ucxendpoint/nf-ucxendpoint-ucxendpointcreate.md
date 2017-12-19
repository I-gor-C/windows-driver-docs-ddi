---
UID: NF.ucxendpoint.UcxEndpointCreate
title: UcxEndpointCreate function
author: windows-driver-content
description: Creates an endpoint on the specified USB device object.
old-location: buses\_ucxendpointcreate.htm
old-project: UsbRef
ms.assetid: 2BB3B2CE-FD15-4D28-BBDA-29C3BB523874
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: UcxEndpointCreate
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ucxendpoint.h
req.include-header: Ucxclass.h, Ucxendpoint.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: UcxEndpointCreate
req.alt-loc: ucxendpoint.h
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
req.product: Windows 10 or later.
---

# UcxEndpointCreate function



## -description
Creates an endpoint on the specified USB device object.



## -syntax

````
NTSTATUS UcxEndpointCreate(
  [in]           UCXUSBDEVICE           UsbDevice,
  [out]          PUCXENDPOINT_INIT      *EndpointInit,
  [in, optional] PWDF_OBJECT_ATTRIBUTES Attributes,
  [out]          UCXENDPOINT            *Endpoint
);
````


## -parameters

### -param UsbDevice [in]

A handle to the USB device object that contains the endpoint. The client driver retrieved the handle in a previous call to <a href="buses._ucxusbdevicecreate">UcxUsbDeviceCreate</a>.


### -param EndpointInit [out]

A pointer to a <b>UCXENDPOINT_INIT</b> structure that describes various configuration
        operations for creating the endpoint object. The driver specifies function pointers to its callback functions in this structure.
    This structure is managed by UCX.


### -param Attributes [in, optional]

A pointer to a caller-allocated <a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a> structure that specifies attributes for the endpoint object. 


### -param Endpoint [out]

A pointer to a variable that receives a handle to the new endpoint object.


## -returns
The method returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one an appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> error code. 


## -remarks
The client driver for the host controller must call this method after the <a href="wdf.wdfdevicecreate">WdfDeviceCreate</a> call. The parent of the new endpoint object is the USB device object. 

The method initializes the endpoint object with information such as the type of endpoint, pipe, transfer, and maximum transfers size.

For a code example, see <a href="..\ucxusbdevice\nc-ucxusbdevice-evt_ucx_usbdevice_endpoint_add.md">EVT_UCX_USBDEVICE_ENDPOINT_ADD</a>.


## -requirements
<table>
<tr>
<th width="30%">
Minimum support

</th>
<td width="70%">
Windows 10

</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.0

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
2.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ucxendpoint.h (include Ucxclass.h or Ucxendpoint.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
</table>