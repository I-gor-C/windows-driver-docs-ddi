---
UID: NC.wdm.PCLFS_CLIENT_LOG_UNPINNED_CALLBACK
title: PCLFS_CLIENT_LOG_UNPINNED_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 77cf3e12-3270-4399-8c98-e63a8c402cce
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

# PCLFS_CLIENT_LOG_UNPINNED_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCLFS_CLIENT_LOG_UNPINNED_CALLBACK PclfsClientLogUnpinnedCallback; 

// Definition

VOID PclfsClientLogUnpinnedCallback 
(
	PLOG_FILE_OBJECT LogFile
	PVOID ClientData
)
{...}

PCLFS_CLIENT_LOG_UNPINNED_CALLBACK 


```

## -parameters

### -param LogFile: 
### -param ClientData: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also