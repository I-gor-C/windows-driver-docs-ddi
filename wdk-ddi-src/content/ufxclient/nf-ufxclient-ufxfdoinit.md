---
UID: NF.ufxclient.UfxFdoInit
title: UfxFdoInit function
author: windows-driver-content
description: Initializes the WDFDEVICE_INIT structure that the client driver subsequently provides when it calls WdfDeviceCreate.
old-location: buses\ufxfdoinit.htm
old-project: usbref
ms.assetid: 11CDA6DA-6B26-41BC-8F0B-2F18FC03B3C2
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: UfxFdoInit
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ufxclient.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UfxFdoInit
req.alt-loc: ufxclient.h
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

# UfxFdoInit function



## -description
Initializes the WDFDEVICE_INIT structure that the client driver subsequently provides when it calls <a href="wdf.wdfdevicecreate">WdfDeviceCreate</a>.


## -syntax

````
NTSTATUS UfxFdoInit(
  [in]      WDFDRIVER              WdfDriver,
  [in, out] PWDFDEVICE_INIT        DeviceInit,
  [in, out] PWDF_OBJECT_ATTRIBUTES FdoAttributes
);
````


## -parameters

### -param WdfDriver [in]

A handle to the driver's WDF driver object that the driver obtained from a previous call to <a href="wdf.wdfdrivercreate">WdfDriverCreate</a> or <a href="wdf.wdfgetdriver">WdfGetDriver</a>.

### -param DeviceInit [in, out]

A pointer to a <a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a> structure.

### -param FdoAttributes [in, out]

A pointer to a caller-allocated <a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a> structure that describes object attributes for the 

## -returns
If the operation is successful, the method returns STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise it returns a status value for which NT_SUCCESS(status) equals FALSE.

## -remarks
The client driver receives a pointer to a framework-allocated <a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a> structure in its <a href="..\wdfdriver\nc-wdfdriver-evt_wdf_driver_device_add.md">EvtDriverDeviceAdd</a> callback function.  It then calls <b>UfxFdoInit</b> with this pointer before calling <a href="wdf.wdfdevicecreate">WdfDeviceCreate</a> to create the WDFDEVICE object.

By default, for WDF drivers, the device's function driver is the power policy owner.

The following code snippet shows how to call <b>UfxFdoInit</b>.

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
Header
</th>
<td width="70%">
<dl>
<dt>Ufxclient.h</dt>
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