---
UID: NC.classpnp.PCLASS_ERROR
title: PCLASS_ERROR
author: windows-driver-content
description: 
ms.assetid: a3ba5f97-a0f2-487a-b117-de4594a38db3
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: classpnp.h
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

# PCLASS_ERROR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCLASS_ERROR PclassError; 

// Definition

VOID PclassError 
(
	PDEVICE_OBJECT DeviceObject
	PSCSI_REQUEST_BLOCK Srb
	NTSTATUS *Status
	BOOLEAN *Retry
)
{...}

PCLASS_ERROR 


```

## -parameters

### -param DeviceObject: 
### -param Srb: 
### -param *Status: 
### -param *Retry: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also