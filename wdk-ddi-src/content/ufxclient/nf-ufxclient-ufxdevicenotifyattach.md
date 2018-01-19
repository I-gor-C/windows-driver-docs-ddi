---
UID : NF:ufxclient.UfxDeviceNotifyAttach
title : UfxDeviceNotifyAttach function
author : windows-driver-content
description : Notifies UFX that the device's USB cable has been attached.
old-location : buses\ufxdevicenotifyattach.htm
old-project : usbref
ms.assetid : E45FA08C-3E00-4AF6-A983-6E9C808AFA11
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : UfxDeviceNotifyAttach
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ufxclient.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 10
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : UfxDeviceNotifyAttach
req.alt-loc : ufxclient.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : DISPATCH_LEVEL
req.typenames : UFX_HARDWARE_FAILURE_CONTEXT, *PUFX_HARDWARE_FAILURE_CONTEXT
req.product : Windows 10 or later.
---


# UfxDeviceNotifyAttach function
Notifies UFX that the device's  USB cable has been attached.

## Syntax

````
VOID UfxDeviceNotifyAttach(
  [in] UFXDEVICE UfxDevice
);
````

## Parameters

`UfxDevice`

A handle to a UFX device object that the driver created by calling <a href="..\ufxclient\nf-ufxclient-ufxdevicecreate.md">UfxDeviceCreate</a>.


## Return Value

This method does not return a value.

## Remarks

When the client driver calls <b>UfxDeviceNotifyAttach</b>, the USB function class extension (UFX) does the following:

The client driver typically calls <b>UfxDeviceNotifyAttach</b> from its <a href="..\wdfinterrupt\nc-wdfinterrupt-evt_wdf_interrupt_dpc.md">EvtInterruptDpc</a> callback function, as shown in the following example.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ufxclient.h |
| **Library** |  |
| **IRQL** | DISPATCH_LEVEL |
| **DDI compliance rules** |  |