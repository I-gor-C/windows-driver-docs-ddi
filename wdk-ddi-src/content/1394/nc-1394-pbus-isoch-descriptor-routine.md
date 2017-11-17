---
UID: NC.1394.PBUS_ISOCH_DESCRIPTOR_ROUTINE
title: PBUS_ISOCH_DESCRIPTOR_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 6ceea228-e41a-4670-a4c2-58181ad44c1d
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: 1394.h
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

# PBUS_ISOCH_DESCRIPTOR_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PBUS_ISOCH_DESCRIPTOR_ROUTINE PbusIsochDescriptorRoutine; 

// Definition

void PbusIsochDescriptorRoutine 
(
	PVOID Context1
	PVOID Context2
)
{...}

PBUS_ISOCH_DESCRIPTOR_ROUTINE 


```

## -parameters

### -param Context1: 
### -param Context2: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also