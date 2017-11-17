---
UID: NC.extsfns.PGET_IRP_INFO
title: PGET_IRP_INFO
author: windows-driver-content
description: 
ms.assetid: ba76ec14-6a25-4f4d-9003-d02b3b10f7a2
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: extsfns.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.irql: 
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# PGET_IRP_INFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PGET_IRP_INFO PgetIrpInfo; 

// Definition

HRESULT PgetIrpInfo 
(
	IN PDEBUG_CLIENT Client
	IN ULONG64 Irp
	OUT PDEBUG_IRP_INFO IrpInfo
)
{...}

PGET_IRP_INFO 


```

## -parameters

### -param Client: 
### -param Irp: 
### -param IrpInfo: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also