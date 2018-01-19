---
UID : NF:poscx.PosCxRetainDevice
title : PosCxRetainDevice function
author : windows-driver-content
description : PosCxRetainDevice is called to extend the ownership of the device.
old-location : pos\poscxretaindevice.htm
old-project : pos
ms.assetid : 0DF5E1DA-35BA-406A-A708-461534373F12
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : PosCxRetainDevice
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : poscx.h
req.include-header : Poscx.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : PosCxRetainDevice
req.alt-loc : poscx.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : POS_CX_EVENT_PRIORITY
req.product : Windows 10 or later.
---


# PosCxRetainDevice function
PosCxRetainDevice is called to extend the ownership of the device.

## Syntax

````
NTSTATUS PosCxRetainDevice(
  _In_ WDFDEVICE  device,
  _In_ WDFREQUEST request
);
````

## Parameters

`device`

A handle to a framework device object that represents the device.

`request`

A handle to a framework request object that represents the request. This request must come from a WDF IO queue. The caller must always complete the request.


## Return Value

Possible return values are:


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | poscx.h (include Poscx.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |