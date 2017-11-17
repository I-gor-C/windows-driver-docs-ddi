---
UID: NC.wdm.PCLFS_SET_LOG_SIZE_COMPLETE_CALLBACK
title: PCLFS_SET_LOG_SIZE_COMPLETE_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 0515e073-1010-44e8-9943-20c640b2b2e1
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# PCLFS_SET_LOG_SIZE_COMPLETE_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCLFS_SET_LOG_SIZE_COMPLETE_CALLBACK PclfsSetLogSizeCompleteCallback; 

// Definition

VOID PclfsSetLogSizeCompleteCallback 
(
	PLOG_FILE_OBJECT LogFile
	NTSTATUS OperationStatus
	PVOID ClientData
)
{...}

PCLFS_SET_LOG_SIZE_COMPLETE_CALLBACK 


```

## -parameters

### -param LogFile: 
### -param OperationStatus: 
### -param ClientData: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also