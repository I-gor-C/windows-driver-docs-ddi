---
UID : NF:swenum.KsGetBusEnumParentFDOFromChildPDO
title : KsGetBusEnumParentFDOFromChildPDO function
author : windows-driver-content
description : The KsGetBusEnumParentFDOFromChildPDO function retrieves the FDO of the parent of the given child PDO.
old-location : stream\ksgetbusenumparentfdofromchildpdo.htm
old-project : stream
ms.assetid : 5d860c5c-e29e-4ea2-b6f7-bcaab0d4584d
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : KsGetBusEnumParentFDOFromChildPDO function [Streaming Media Devices], stream.ksgetbusenumparentfdofromchildpdo, KsGetBusEnumParentFDOFromChildPDO, ksfunc_592bfe23-7135-4118-9acf-6783691c55ea.xml, swenum/KsGetBusEnumParentFDOFromChildPDO
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : swenum.h
req.include-header : Swenum.h
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
req.typenames : STREAM_TIME_REFERENCE, *PSTREAM_TIME_REFERENCE
req.product : Windows 10 or later.
---


# KsGetBusEnumParentFDOFromChildPDO function
<i>This function is intended for internal use only.</i>

The <b>KsGetBusEnumParentFDOFromChildPDO </b>function retrieves the FDO of the parent of the given child PDO.

## Syntax

````
NTSTATUS KsGetBusEnumParentFDOFromChildPDO(
  _In_  PDEVICE_OBJECT DeviceObject,
  _Out_ PDEVICE_OBJECT *FunctionalDeviceObject
);
````

## Parameters

`DeviceObject`

Pointer to the child's PDO.

`FunctionalDeviceObject`

Pointer to the device object to receive the parent's FDO.


## Return Value

Returns STATUS_SUCCESS if successful, or STATUS_INVALID_PARAMETER if <i>DeviceObject</i> does not contain a device extension, or if the device extension specified in <i>DeviceObject </i>is not that of a PDO.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | swenum.h (include Swenum.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |