---
UID: NC.wdm.PREPLACE_BEGIN
title: PREPLACE_BEGIN
author: windows-driver-content
description: 
ms.assetid: e7d8b0fe-cf7e-433a-bae9-d24ccf0f0cbc
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

# PREPLACE_BEGIN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PREPLACE_BEGIN PreplaceBegin; 

// Definition

NTSTATUS PreplaceBegin 
(
	PPNP_REPLACE_PARAMETERS Parameters
	PVOID *Context
)
{...}

PREPLACE_BEGIN 


```

## -parameters

### -param Parameters: 
### -param *Context: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also