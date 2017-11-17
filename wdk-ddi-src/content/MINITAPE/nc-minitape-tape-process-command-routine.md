---
UID: NC.minitape.TAPE_PROCESS_COMMAND_ROUTINE
title: TAPE_PROCESS_COMMAND_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 5909ca9f-1a1d-4552-9b45-dcf945172caa
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

# TAPE_PROCESS_COMMAND_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

TAPE_PROCESS_COMMAND_ROUTINE TapeProcessCommandRoutine; 

// Definition

TAPE_STATUS TapeProcessCommandRoutine 
(
	PVOID MinitapeExtension
	PVOID CommandExtension
	PVOID CommandParameters
	PSCSI_REQUEST_BLOCK Srb
	ULONG CallNumber
	TAPE_STATUS StatusOfLastCommand
	PULONG RetryFlags
)
{...}

TAPE_PROCESS_COMMAND_ROUTINE 


```

## -parameters

### -param MinitapeExtension: 
### -param CommandExtension: 
### -param CommandParameters: 
### -param Srb: 
### -param CallNumber: 
### -param StatusOfLastCommand: 
### -param RetryFlags: 



## -returns

Returns TAPE_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also