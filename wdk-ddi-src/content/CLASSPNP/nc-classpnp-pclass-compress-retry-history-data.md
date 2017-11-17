---
UID: NC.classpnp.PCLASS_COMPRESS_RETRY_HISTORY_DATA
title: PCLASS_COMPRESS_RETRY_HISTORY_DATA
author: windows-driver-content
description: 
ms.assetid: 69b6d454-c09d-4d06-ad1a-595be1117f96
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: classpnp.h
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

# PCLASS_COMPRESS_RETRY_HISTORY_DATA callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCLASS_COMPRESS_RETRY_HISTORY_DATA PclassCompressRetryHistoryData; 

// Definition

VOID PclassCompressRetryHistoryData 
(
	PDEVICE_OBJECT DeviceObject
	PSRB_HISTORY RequestHistory
)
{...}

PCLASS_COMPRESS_RETRY_HISTORY_DATA 


```

## -parameters

### -param DeviceObject: 
### -param RequestHistory: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also