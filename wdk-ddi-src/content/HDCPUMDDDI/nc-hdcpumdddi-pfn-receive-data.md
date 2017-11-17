---
UID: NC.hdcpumdddi.PFN_RECEIVE_DATA
title: PFN_RECEIVE_DATA
author: windows-driver-content
description: 
ms.assetid: 7af3c451-4771-4025-b421-f38632dd8f55
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: hdcpumdddi.h
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

# PFN_RECEIVE_DATA callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_RECEIVE_DATA PfnReceiveData; 

// Definition

VOID PfnReceiveData 
(
	PVOID pDriverContext
	PVOID pData
	UINT cbDataSize
)
{...}

PFN_RECEIVE_DATA 


```

## -parameters

### -param pDriverContext: 
### -param pData: 
### -param cbDataSize: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also