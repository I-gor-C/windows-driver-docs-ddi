---
UID: NC.ks.PFNKSCLOCK_CORRELATEDTIME
title: PFNKSCLOCK_CORRELATEDTIME
author: windows-driver-content
description: 
ms.assetid: 7f68ad96-44c2-46ac-a56b-570b58f44091
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ks.h
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

# PFNKSCLOCK_CORRELATEDTIME callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSCLOCK_CORRELATEDTIME PfnksclockCorrelatedtime; 

// Definition

LONGLONG PfnksclockCorrelatedtime 
(
	PFILE_OBJECT FileObject
	PLONGLONG SystemTime
)
{...}

PFNKSCLOCK_CORRELATEDTIME 


```

## -parameters

### -param FileObject: 
### -param SystemTime: 



## -returns

Returns LONGLONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also