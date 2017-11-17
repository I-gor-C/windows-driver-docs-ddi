---
UID: NC.mcd.CHANGER_INITIALIZE
title: CHANGER_INITIALIZE
author: windows-driver-content
description: 
ms.assetid: 4f4aac77-f978-487c-a442-0796f2a087e8
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: mcd.h
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

# CHANGER_INITIALIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

CHANGER_INITIALIZE ChangerInitialize; 

// Definition

NTSTATUS ChangerInitialize 
(
	PDEVICE_OBJECT DeviceObject
)
{...}

CHANGER_INITIALIZE 


```

## -parameters

### -param DeviceObject: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also