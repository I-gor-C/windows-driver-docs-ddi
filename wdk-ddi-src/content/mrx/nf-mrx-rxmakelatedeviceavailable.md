---
UID : NF:mrx.RxMakeLateDeviceAvailable
title : RxMakeLateDeviceAvailable function
author : windows-driver-content
description : RxMakeLateDeviceAvailable modifies the device object to make a &#0034;late device&#0034; available. A late device is one that is not created in the driver's load routine.
old-location : ifsk\rxmakelatedeviceavailable.htm
old-project : ifsk
ms.assetid : 0818907f-3346-42a2-b123-3298ea8f9a1d
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : rxref_7586550f-6abe-4e18-8154-09936c3f0488.xml, RxMakeLateDeviceAvailable, ifsk.rxmakelatedeviceavailable, RxMakeLateDeviceAvailable routine [Installable File System Drivers], mrx/RxMakeLateDeviceAvailable
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : mrx.h
req.include-header : Mrx.h, Rxstruc.h
req.target-type : Desktop
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
req.irql : "<= APC_LEVEL"
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PSetDSMCounters_IN, SetDSMCounters_IN"
---


# RxMakeLateDeviceAvailable function
<b>RxMakeLateDeviceAvailable</b> modifies the device object to make a "late device" available. A late device is one that is not created in the driver's load routine.

## Syntax

````
VOID RxMakeLateDeviceAvailable(
  _In_ PRDBSS_DEVICE_OBJECT RxDeviceObject
);
````

## Parameters

`RxDeviceObject`

A pointer to the where the created device object is to be stored.


## Return Value

None

## Remarks

<b>RxMakeLateDeviceAvailable</b> clears the DO_DEVICE_INITIALIZING bit in the <b>Flags</b> member of the device object.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | mrx.h (include Mrx.h, Rxstruc.h) |
| **Library** |  |
| **IRQL** | "<= APC_LEVEL" |
| **DDI compliance rules** |  |