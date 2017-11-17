---
UID: NC.mrx.PMRX_EXTRACT_NETROOT_NAME
title: PMRX_EXTRACT_NETROOT_NAME
author: windows-driver-content
description: 
ms.assetid: 72805014-c2a2-4aba-805b-1ee743157293
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: mrx.h
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

# PMRX_EXTRACT_NETROOT_NAME callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PMRX_EXTRACT_NETROOT_NAME PmrxExtractNetrootName; 

// Definition

VOID PmrxExtractNetrootName 
(
	IN PUNICODE_STRING FilePathName
	IN PMRX_SRV_CALL SrvCall
	OUT PUNICODE_STRING NetRootName
	OUT PUNICODE_STRING RestOfName OPTIONAL
)
{...}

PMRX_EXTRACT_NETROOT_NAME 


```

## -parameters

### -param FilePathName: 
### -param SrvCall: 
### -param NetRootName: 
### -param OPTIONAL: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also