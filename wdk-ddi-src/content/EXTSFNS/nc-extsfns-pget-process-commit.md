---
UID: NC.extsfns.PGET_PROCESS_COMMIT
title: PGET_PROCESS_COMMIT
author: windows-driver-content
description: 
ms.assetid: d1404f67-4d6b-4cd2-8fb3-aa6230f7256c
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

# PGET_PROCESS_COMMIT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PGET_PROCESS_COMMIT PgetProcessCommit; 

// Definition

HRESULT PgetProcessCommit 
(
	PDEBUG_CLIENT Client
	PULONG64 TotalCommitCharge
	PULONG NumberOfProcesses
	PPROCESS_COMMIT_USAGE *CommitData
)
{...}

PGET_PROCESS_COMMIT 


```

## -parameters

### -param Client: 
### -param TotalCommitCharge: 
### -param NumberOfProcesses: 
### -param *CommitData: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also