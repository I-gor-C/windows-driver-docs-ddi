---
UID: NC.dsm.DSM_LB_GET_PATH
title: DSM_LB_GET_PATH
author: windows-driver-content
description: 
ms.assetid: 1e650124-fd6c-418c-84b0-700601bf69ac
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dsm.h
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

# DSM_LB_GET_PATH callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DSM_LB_GET_PATH DsmLbGetPath; 

// Definition

PVOID DsmLbGetPath 
(
	IN PVOID DsmContext
	IN PSCSI_REQUEST_BLOCK Srb
	IN PDSM_IDS DsmList
	IN PVOID CurrentPath
	OUT NTSTATUS *Status
)
{...}

DSM_LB_GET_PATH 


```

## -parameters

### -param DsmContext: 
### -param Srb: 
### -param DsmList: 
### -param CurrentPath: 
### -param *Status: 



## -returns

Returns PVOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also