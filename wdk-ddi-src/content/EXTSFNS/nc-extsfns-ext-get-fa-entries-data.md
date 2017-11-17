---
UID: NC.extsfns.EXT_GET_FA_ENTRIES_DATA
title: EXT_GET_FA_ENTRIES_DATA
author: windows-driver-content
description: 
ms.assetid: 8e68f706-85ea-44b1-ae82-290df9083039
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

# EXT_GET_FA_ENTRIES_DATA callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EXT_GET_FA_ENTRIES_DATA ExtGetFaEntriesData; 

// Definition

HRESULT ExtGetFaEntriesData 
(
	IN PDEBUG_CLIENT4 Client
	IN PULONG Count
	OUT PFA_ENTRY *Entries
)
{...}

EXT_GET_FA_ENTRIES_DATA 


```

## -parameters

### -param Client: 
### -param Count: 
### -param *Entries: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also