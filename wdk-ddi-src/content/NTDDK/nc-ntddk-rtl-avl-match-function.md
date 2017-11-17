---
UID: NC.ntddk.RTL_AVL_MATCH_FUNCTION
title: RTL_AVL_MATCH_FUNCTION
author: windows-driver-content
description: 
ms.assetid: 05990def-86cb-4d2f-8fbb-ada1d3e80c91
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntddk.h
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

# RTL_AVL_MATCH_FUNCTION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

RTL_AVL_MATCH_FUNCTION RtlAvlMatchFunction; 

// Definition

NTSTATUS RtlAvlMatchFunction 
(
	_RTL_AVL_TABLE * Table
	PVOID UserData
	PVOID MatchData
)
{...}

RTL_AVL_MATCH_FUNCTION PRTL_AVL_MATCH_FUNCTION


```

## -parameters

### -param Table: 
### -param UserData: 
### -param MatchData: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also