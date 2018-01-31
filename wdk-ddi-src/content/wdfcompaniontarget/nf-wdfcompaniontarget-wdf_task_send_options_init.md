---
UID : NF:wdfcompaniontarget.WDF_TASK_SEND_OPTIONS_INIT
title : WDF_TASK_SEND_OPTIONS_INIT function
author : windows-driver-content
description : For internal use only.
old-location : wdf\wdf_task_send_options_init.htm
old-project : wdf
ms.assetid : ba10c012-f64c-42cd-bedc-72f620818aa5
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : wdfcompaniontarget/WDF_TASK_SEND_OPTIONS_INIT, wdf.wdf_task_send_options_init, WDF_TASK_SEND_OPTIONS_INIT method, WDF_TASK_SEND_OPTIONS_INIT
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : wdfcompaniontarget.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 1.23
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
req.typenames : WDF_TASK_SEND_OPTIONS_FLAGS
req.product : Windows 10 or later.
---


# WDF_TASK_SEND_OPTIONS_INIT function
For internal use only.

## Syntax

````
FORCEINLINE VOID WDF_TASK_SEND_OPTIONS_INIT(
  _Out_ PWDF_TASK_SEND_OPTIONS Options,
  _In_  ULONG                  Flags
);
````

## Parameters

`Options`



`Flags`




## Return Value

This method does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** | 1.23 |
| **Minimum UMDF version** |  |
| **Header** | wdfcompaniontarget.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |