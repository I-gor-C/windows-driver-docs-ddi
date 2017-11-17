---
UID: NC.minitape.TAPE_ERROR_ROUTINE
title: TAPE_ERROR_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 04807ac7-0ba5-4f7a-9d23-fea659d1a62a
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: minitape.h
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

# TAPE_ERROR_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

TAPE_ERROR_ROUTINE TapeErrorRoutine; 

// Definition

VOID TapeErrorRoutine 
(
	PVOID MinitapeExtension
	PSCSI_REQUEST_BLOCK Srb
	PTAPE_STATUS TapeStatus
)
{...}

TAPE_ERROR_ROUTINE 


```

## -parameters

### -param MinitapeExtension: 
### -param Srb: 
### -param TapeStatus: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also