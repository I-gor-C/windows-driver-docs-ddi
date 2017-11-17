---
UID: NC.dbghelp.PFIND_EXE_FILE_CALLBACK
title: PFIND_EXE_FILE_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 7b850925-dce4-4dd6-8569-ae19e2ee0a10
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dbghelp.h
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

# PFIND_EXE_FILE_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFIND_EXE_FILE_CALLBACK PfindExeFileCallback; 

// Definition

BOOL PfindExeFileCallback 
(
	HANDLE FileHandle
	PCSTR FileName
	PVOID CallerData
)
{...}

PFIND_EXE_FILE_CALLBACK 


```

## -parameters

### -param FileHandle: 
### -param FileName: 
### -param CallerData: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also