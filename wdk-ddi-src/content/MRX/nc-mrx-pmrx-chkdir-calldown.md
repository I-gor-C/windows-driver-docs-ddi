---
UID: NC.mrx.PMRX_CHKDIR_CALLDOWN
title: PMRX_CHKDIR_CALLDOWN
author: windows-driver-content
description: 
ms.assetid: d316d20c-467c-47ad-8ca1-38253f6857a6
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

# PMRX_CHKDIR_CALLDOWN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PMRX_CHKDIR_CALLDOWN PmrxChkdirCalldown; 

// Definition

NTSTATUS PmrxChkdirCalldown 
(
	IN OUT PRX_CONTEXT RxContext
	IN PUNICODE_STRING DirectoryName
)
{...}

PMRX_CHKDIR_CALLDOWN 


```

## -parameters

### -param RxContext: 
### -param DirectoryName: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also