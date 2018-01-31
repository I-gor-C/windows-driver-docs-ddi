---
UID : NC:ucxusbdevice.EVT_UCX_USBDEVICE_GET_CHARACTERISTIC
title : EVT_UCX_USBDEVICE_GET_CHARACTERISTIC
author : windows-driver-content
description : UCX invokes this callback to retrieve the device characteristics.
old-location : buses\evt_ucx_usbdevice_get_characteristic.htm
old-project : usbref
ms.assetid : EE8568F6-3D88-477E-9F0D-044D014EBCF3
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : buses.evt_ucx_usbdevice_get_characteristic, EvtUcxDeviceGetCharacteristic callback function [Buses], EvtUcxDeviceGetCharacteristic, EVT_UCX_USBDEVICE_GET_CHARACTERISTIC, EVT_UCX_USBDEVICE_GET_CHARACTERISTIC, ucxusbdevice/EvtUcxDeviceGetCharacteristic, *PFN_UCX_USBDEVICE_GET_CHARACTERISTIC callback function pointer [Buses], *PFN_UCX_USBDEVICE_GET_CHARACTERISTIC
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : ucxusbdevice.h
req.include-header : Ucxclass.h
req.target-type : Windows
req.target-min-winverclnt : Windows 10, version 1709
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 1.0
req.umdf-ver : 2.0
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : "<=DISPATCH_LEVEL"
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : STREAM_INFO, *PSTREAM_INFO
req.product : Windows 10 or later.
---


# EVT_UCX_USBDEVICE_GET_CHARACTERISTIC function
UCX invokes this callback to retrieve the device characteristics.

## Syntax

```
EVT_UCX_USBDEVICE_GET_CHARACTERISTIC EvtUcxUsbdeviceGetCharacteristic;

NTSTATUS EvtUcxUsbdeviceGetCharacteristic(
  UCXCONTROLLER UcxController,
  UCXUSBDEVICE UcxUsbDevice,
  PUCX_USBDEVICE_CHARACTERISTIC UcxUsbDeviceCharacteristic
)
{...}
```

## Parameters

`UcxController`

A handle to the UCX controller that the client driver received in a previous call to  the <a href="https://msdn.microsoft.com/library/windows/hardware/mt188033">UcxControllerCreate</a> method.

`UcxUsbDevice`

A handle to a UCX object that represents the USB device that the client driver received in a previous call to the <a href="..\ucxusbdevice\nf-ucxusbdevice-ucxusbdevicecreate.md">UcxUsbDeviceCreate</a> method.

`UcxUsbDeviceCharacteristic`

A pointer to a <a href="..\ucxusbdevice\ns-ucxusbdevice-_ucx_usbdevice_characteristic.md">UCX_USBDEVICE_CHARACTERISTIC</a> structure that contains the type of characteristic in which the caller is interested. The client driver fills the value of the requested  characteristic. For example, if the type indicates <a href="..\ucxusbdevice\ns-ucxusbdevice-_ucx_usbdevice_characteristic_path_delay.md">UCX_USBDEVICE_CHARACTERISTIC_PATH_DELAY</a>, the driver fills the <b>UCX_USBDEVICE_CHARACTERISTIC_PATH_DELAY</b> structure, pointed to by <b>PathDelay</b> member, with the appropriate maximum and send path delay values.


## Return Value

If the operation is successful, the callback function must return STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise it must return a status value for which NT_SUCCESS(status) equals FALSE.

## Remarks

The UCX client driver registers its implementation with the USB host controller extension (UCX) by calling the <a href="..\ucxusbdevice\nf-ucxusbdevice-ucxusbdevicecreate.md">UcxUsbDeviceCreate</a> method.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | ucxusbdevice.h (include Ucxclass.h) |
| **Library** |  |
| **IRQL** | "<=DISPATCH_LEVEL" |
| **DDI compliance rules** |  |