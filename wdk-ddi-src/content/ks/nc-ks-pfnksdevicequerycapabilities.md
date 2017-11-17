---
UID: NC.ks.PFNKSDEVICEQUERYCAPABILITIES
title: PFNKSDEVICEQUERYCAPABILITIES
author: windows-driver-content
description: 
ms.assetid: fd567e76-733a-4dc1-be52-a52dd9749a78
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ks.h
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

# PFNKSDEVICEQUERYCAPABILITIES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSDEVICEQUERYCAPABILITIES Pfnksdevicequerycapabilities; 

// Definition

NTSTATUS Pfnksdevicequerycapabilities 
(
	PKSDEVICE Device
	PIRP Irp
	PDEVICE_CAPABILITIES Capabilities
)
{...}

PFNKSDEVICEQUERYCAPABILITIES 


```

## -parameters

### -param Device: 
### -param Irp: 
### -param Capabilities: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also