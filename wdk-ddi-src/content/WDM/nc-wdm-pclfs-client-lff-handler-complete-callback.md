---
UID: NC.wdm.PCLFS_CLIENT_LFF_HANDLER_COMPLETE_CALLBACK
title: PCLFS_CLIENT_LFF_HANDLER_COMPLETE_CALLBACK
author: windows-driver-content
description: 
ms.assetid: b7299f0b-9114-40e8-8199-e42b66cd7a47
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

# PCLFS_CLIENT_LFF_HANDLER_COMPLETE_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCLFS_CLIENT_LFF_HANDLER_COMPLETE_CALLBACK PclfsClientLffHandlerCompleteCallback; 

// Definition

VOID PclfsClientLffHandlerCompleteCallback 
(
	PLOG_FILE_OBJECT LogFile
	NTSTATUS OperationStatus
	BOOLEAN LogIsPinned
	PVOID ClientData
)
{...}

PCLFS_CLIENT_LFF_HANDLER_COMPLETE_CALLBACK 


```

## -parameters

### -param LogFile: 
### -param OperationStatus: 
### -param LogIsPinned: 
### -param ClientData: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also