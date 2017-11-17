---
UID: NC.ntagp.PAGP_CHECK_GUARD_PAGE
title: PAGP_CHECK_GUARD_PAGE
author: windows-driver-content
description: 
ms.assetid: 1154a032-5f7e-4c12-829b-b39e3c9ad70b
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntagp.h
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

# PAGP_CHECK_GUARD_PAGE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PAGP_CHECK_GUARD_PAGE PagpCheckGuardPage; 

// Definition

NTSTATUS PagpCheckGuardPage 
(
	IN PVOID AgpContext
	IN ULONG Flags
	IN ULONG ULongsToCheck
)
{...}

PAGP_CHECK_GUARD_PAGE 


```

## -parameters

### -param AgpContext: 
### -param Flags: 
### -param ULongsToCheck: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also