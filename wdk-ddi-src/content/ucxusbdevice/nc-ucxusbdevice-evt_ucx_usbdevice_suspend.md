---
UID : NC:ucxusbdevice.EVT_UCX_USBDEVICE_SUSPEND
title : EVT_UCX_USBDEVICE_SUSPEND
author : windows-driver-content
description : UCX invokes this callback function to send a device suspend state.
old-location : buses\evt_ucx_usbdevice_suspend.htm
old-project : usbref
ms.assetid : 809F946C-DDD4-4C4D-9F0F-F2B4A4657D12
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : buses.evt_ucx_usbdevice_suspend, EvtUcxDeviceSuspend callback function [Buses], EvtUcxDeviceSuspend, EVT_UCX_USBDEVICE_SUSPEND, EVT_UCX_USBDEVICE_SUSPEND, ucxusbdevice/EvtUcxDeviceSuspend, *PFN_UCX_USBDEVICE_SUSPEND callback function [Buses], *PFN_UCX_USBDEVICE_SUSPEND
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
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PSTREAM_INFO, STREAM_INFO"
req.product : Windows 10 or later.
---


# EVT_UCX_USBDEVICE_SUSPEND function
UCX invokes this callback function to send a device suspend state.

## Syntax

```
EVT_UCX_USBDEVICE_SUSPEND EvtUcxUsbdeviceSuspend;

void EvtUcxUsbdeviceSuspend(
  UCXCONTROLLER UcxController,
  UCXUSBDEVICE UcxUsbDevice
)
{...}
```

## Parameters

`UcxController`

A handle to the UCX controller that the client driver received in a previous call to  the <a href="https://msdn.microsoft.com/library/windows/hardware/mt188033">UcxControllerCreate</a> method.

`UcxUsbDevice`

A handle to a UCX object that represents the USB device that the client driver received in a previous call to the <a href="..\ucxusbdevice\nf-ucxusbdevice-ucxusbdevicecreate.md">UcxUsbDeviceCreate</a> method.


## Return Value

This callback function does not return a value.

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
| **IRQL** | PASSIVE_LEVEL |
| **DDI compliance rules** |  |