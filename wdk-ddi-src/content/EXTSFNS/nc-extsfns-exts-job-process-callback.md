---
UID: NC.extsfns.EXTS_JOB_PROCESS_CALLBACK
title: EXTS_JOB_PROCESS_CALLBACK
author: windows-driver-content
description: 
ms.assetid: fe0e320d-0766-474f-8a14-615c907f269c
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

# EXTS_JOB_PROCESS_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EXTS_JOB_PROCESS_CALLBACK ExtsJobProcessCallback; 

// Definition

BOOLEAN ExtsJobProcessCallback 
(
	ULONG64 Job
	ULONG64 Process
	PVOID Context
)
{...}

EXTS_JOB_PROCESS_CALLBACK 


```

## -parameters

### -param Job: 
### -param Process: 
### -param Context: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also