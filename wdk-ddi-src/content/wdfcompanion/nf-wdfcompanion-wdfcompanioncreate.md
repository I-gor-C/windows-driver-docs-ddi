---
UID : NF:wdfcompanion.WdfCompanionCreate
title : WdfCompanionCreate function
author : windows-driver-content
description : For internal use only.
old-location : wdf\wdfcompanioncreate.htm
old-project : wdf
ms.assetid : 78b9eccf-34ef-40ae-b7fc-6fa8400f8c2a
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : wdf.wdfcompanioncreate, wdfcompanion/WdfCompanionCreate, WdfCompanionCreate, WdfCompanionCreate method
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
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : NtosKrnl.exe
req.dll : 
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : WDF_TASK_QUEUE_DISPATCH_TYPE
req.product : Windows 10 or later.
---


# WdfCompanionCreate function
For internal use only.

## Syntax

````
NTSTATUS WdfCompanionCreate(
  _Inout_  PWDFDEVICE_INIT        *DeviceInit,
  _In_opt_ PWDF_OBJECT_ATTRIBUTES DeviceAttributes,
  _Out_    WDFCOMPANION           *Companion
);
````

## Parameters

`DeviceInit`



`DeviceAttributes`



`Companion`




## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** | 2.23 |
| **Header** | wdfcompanion.h |
| **Library** |  |
| **IRQL** | PASSIVE_LEVEL |
| **DDI compliance rules** |  |