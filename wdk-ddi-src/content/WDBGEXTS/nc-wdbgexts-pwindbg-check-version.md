---
UID: NC.wdbgexts.PWINDBG_CHECK_VERSION
title: PWINDBG_CHECK_VERSION
author: windows-driver-content
description: 
ms.assetid: 477eae6b-0ac2-491e-82c1-36e018092350
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdbgexts.h
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

# PWINDBG_CHECK_VERSION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PWINDBG_CHECK_VERSION PwindbgCheckVersion; 

// Definition

ULONG PwindbgCheckVersion 
(
	VOID 
)
{...}

PWINDBG_CHECK_VERSION 


```

## -parameters

### -param : 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also