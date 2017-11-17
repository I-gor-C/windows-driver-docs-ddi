---
UID: NC.ntddk.PGET_LOCATION_STRING
title: PGET_LOCATION_STRING
author: windows-driver-content
description: 
ms.assetid: 2daf9400-5be5-4b43-917f-23d39f3bab02
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

# PGET_LOCATION_STRING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PGET_LOCATION_STRING PgetLocationString; 

// Definition

NTSTATUS PgetLocationString 
(
	PVOID Context
	PZZWSTR *LocationStrings
)
{...}

PGET_LOCATION_STRING 


```

## -parameters

### -param Context: 
### -param *LocationStrings: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also