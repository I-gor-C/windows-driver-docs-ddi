---
UID: NC.wdm.PCLFS_CLIENT_ADVANCE_TAIL_CALLBACK
title: PCLFS_CLIENT_ADVANCE_TAIL_CALLBACK
author: windows-driver-content
description: 
ms.assetid: ed3bc8d1-8f71-4512-a1bd-4d2b10335c79
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

# PCLFS_CLIENT_ADVANCE_TAIL_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCLFS_CLIENT_ADVANCE_TAIL_CALLBACK PclfsClientAdvanceTailCallback; 

// Definition

NTSTATUS PclfsClientAdvanceTailCallback 
(
	PLOG_FILE_OBJECT LogFile
	PCLFS_LSN TargetLsn
	PVOID ClientData
)
{...}

PCLFS_CLIENT_ADVANCE_TAIL_CALLBACK 


```

## -parameters

### -param LogFile: 
### -param TargetLsn: 
### -param ClientData: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also