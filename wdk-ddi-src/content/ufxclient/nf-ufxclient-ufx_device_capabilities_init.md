---
UID : NF:ufxclient.UFX_DEVICE_CAPABILITIES_INIT
title : UFX_DEVICE_CAPABILITIES_INIT function
author : windows-driver-content
description : The UFX_DEVICE_CAPABILITIES_INIT macro the initializes the UFX_DEVICE_CAPABILITIES structure.
old-location : buses\ufx_device_capabilities_init.htm
old-project : usbref
ms.assetid : 7C55EB8D-1B68-484A-B95A-E0150FBA9AB8
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : ufxclient/UFX_DEVICE_CAPABILITIES_INIT, UFX_DEVICE_CAPABILITIES_INIT function [Buses], UFX_DEVICE_CAPABILITIES_INIT, buses.ufx_device_capabilities_init
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ufxclient.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : NtosKrnl.exe
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : UFX_HARDWARE_FAILURE_CONTEXT, *PUFX_HARDWARE_FAILURE_CONTEXT
req.product : Windows 10 or later.
---


# UFX_DEVICE_CAPABILITIES_INIT function
The <b>UFX_DEVICE_CAPABILITIES_INIT</b> macro the initializes the <a href="..\ufxbase\ns-ufxbase-_ufx_device_capabilities.md">UFX_DEVICE_CAPABILITIES</a> structure.

## Syntax

````
void UFX_DEVICE_CAPABILITIES_INIT(
  _Out_ PUFX_DEVICE_CAPABILITIES Capabilities
);
````

## Parameters

`Capabilities`

Pointer to the <a href="..\ufxbase\ns-ufxbase-_ufx_device_capabilities.md">UFX_DEVICE_CAPABILITIES</a> structure.


## Return Value

This function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ufxclient.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |