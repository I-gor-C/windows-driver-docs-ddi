---
UID : NF:ks.KsDispatchSetSecurity
title : KsDispatchSetSecurity function
author : windows-driver-content
description : The KsDispatchSetSecurity function is used in the KSDISPATCH_TABLE.SetSecurity entry to handle setting the current security descriptor.
old-location : stream\ksdispatchsetsecurity.htm
old-project : stream
ms.assetid : c1af342a-438d-4c83-be2d-a4c4c9f204b5
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : ks/KsDispatchSetSecurity, ksfunc_b643b100-dc1c-4df4-b1e4-32ac7ae59b2a.xml, stream.ksdispatchsetsecurity, KsDispatchSetSecurity function [Streaming Media Devices], KsDispatchSetSecurity
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ks.h
req.include-header : Ks.h
req.target-type : Universal
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
req.lib : Ks.lib
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : 
---


# KsDispatchSetSecurity function
The <b>KsDispatchSetSecurity</b> function is used in the KSDISPATCH_TABLE.SetSecurity entry to handle setting the current security descriptor. The assumption is that the KSOBJECT_HEADER structure is being used in the <b>FsContext</b> data structure and that the <b>CreateItem</b> points to a valid item that optionally contains a security descriptor.

## Syntax

````
NTSTATUS KsDispatchSetSecurity(
  _In_ PDEVICE_OBJECT DeviceObject,
  _In_ PIRP           Irp
);
````

## Parameters

`DeviceObject`

Specifies the device object associated with the IRP.

`Irp`

Specifies the IRP that is being handled.


## Return Value

The <b>KsDispatchSetSecurity</b> function returns the security set status and completes the IRP.

## Remarks

This security descriptor must be allocated in its own piece of pool memory, since <b>KsDispatchSetSecurity</b> will replace the existing descriptor with a new allocation. Therefore, it cannot be shared with <b>CreateItem</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ks.h (include Ks.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |