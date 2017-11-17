---
UID: NC.ndis.MINIPORT_PNP_IRP
title: MINIPORT_PNP_IRP
author: windows-driver-content
description: 
ms.assetid: f3a8594d-e219-4389-8045-9e5348caab9a
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ndis.h
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

# MINIPORT_PNP_IRP callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

MINIPORT_PNP_IRP MiniportPnpIrp; 

// Definition

NDIS_STATUS MiniportPnpIrp 
(
	NDIS_HANDLE MiniportAddDeviceContext
	PIRP Irp
)
{...}

MINIPORT_PNP_IRP 


```

## -parameters

### -param MiniportAddDeviceContext: 
### -param Irp: 



## -returns

Returns NDIS_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also