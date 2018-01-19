---
UID : NF:ntifs.IoQueueThreadIrp
title : IoQueueThreadIrp function
author : windows-driver-content
description : Reserved for system use.
old-location : ifsk\ioqueuethreadirp.htm
old-project : ifsk
ms.assetid : 165eaae5-ce68-462e-902c-64120fba91c5
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : IoQueueThreadIrp
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ntifs.h
req.include-header : Ntifs.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IoQueueThreadIrp
req.alt-loc : ntifs.h
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
req.typenames : TOKEN_TYPE
---


# IoQueueThreadIrp function
The <b>IoQueueThreadIrp</b> routine is reserved for system use. See <a href="..\wdm\nf-wdm-iobuilddeviceiocontrolrequest.md">IoBuildDeviceIoControlRequest</a> and <a href="..\wdm\nf-wdm-iobuildsynchronousfsdrequest.md">IoBuildSynchronousFsdRequest</a>.

## Syntax

````
  IoQueueThreadIrp(
    
);
````

## Parameters

`Irp`




## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntifs.h (include Ntifs.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |