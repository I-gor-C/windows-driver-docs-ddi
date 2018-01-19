---
UID : NF:wdfcompanion.WDF_COMPANION_EVENT_CALLBACKS_INIT
title : WDF_COMPANION_EVENT_CALLBACKS_INIT function
author : windows-driver-content
description : For internal use only.
old-location : wdf\wdf_companion_event_callbacks_init.htm
old-project : wdf
ms.assetid : 83fadb77-90c2-4331-949c-5d8828ce33e2
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : WDF_COMPANION_EVENT_CALLBACKS_INIT
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : wdfcompanion.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 2.23
req.alt-api : WDF_COMPANION_EVENT_CALLBACKS_INIT
req.alt-loc : wdfcompanion.h
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
req.typenames : WDF_TASK_QUEUE_DISPATCH_TYPE
req.product : Windows 10 or later.
---


# WDF_COMPANION_EVENT_CALLBACKS_INIT function
For internal use only.

## Syntax

````
FORCEINLINE VOID WDF_COMPANION_EVENT_CALLBACKS_INIT(
  _Out_ PWDF_COMPANION_EVENT_CALLBACKS Callbacks
);
````

## Parameters

`Callbacks`




## Return Value

This method does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** | 2.23 |
| **Header** | wdfcompanion.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |