---
UID: NC.extsfns.PENUMERATE_JOB_PROCESSES
title: PENUMERATE_JOB_PROCESSES
author: windows-driver-content
description: 
ms.assetid: e356ff51-fd1a-41b4-8eed-242f139ac5e5
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

# PENUMERATE_JOB_PROCESSES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PENUMERATE_JOB_PROCESSES PenumerateJobProcesses; 

// Definition

HRESULT PenumerateJobProcesses 
(
	PDEBUG_CLIENT Client
	ULONG64 Job
	EXTS_JOB_PROCESS_CALLBACK Callback
	PVOID Context
)
{...}

PENUMERATE_JOB_PROCESSES 


```

## -parameters

### -param Client: 
### -param Job: 
### -param Callback: 
### -param Context: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also