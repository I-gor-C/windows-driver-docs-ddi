---
UID: NC.dbghelp.PDBGHELP_CREATE_USER_DUMP_CALLBACK
title: PDBGHELP_CREATE_USER_DUMP_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 3e9af9ff-1359-4aa2-bb70-9d1cdd9506eb
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

# PDBGHELP_CREATE_USER_DUMP_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PDBGHELP_CREATE_USER_DUMP_CALLBACK PdbghelpCreateUserDumpCallback; 

// Definition

BOOL PdbghelpCreateUserDumpCallback 
(
	DWORD DataType
	PVOID *Data
	LPDWORD DataLength
	PVOID UserData
)
{...}

PDBGHELP_CREATE_USER_DUMP_CALLBACK 


```

## -parameters

### -param DataType: 
### -param *Data: 
### -param DataLength: 
### -param UserData: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also