---
UID: NC.ks.PFNKSFASTHANDLER
title: PFNKSFASTHANDLER
author: windows-driver-content
description: 
ms.assetid: 5262eb25-da18-44b0-bccf-436fcb2b8c99
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

# PFNKSFASTHANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSFASTHANDLER Pfnksfasthandler; 

// Definition

BOOLEAN Pfnksfasthandler 
(
	PFILE_OBJECT FileObject
	PKSIDENTIFIER Request
	ULONG RequestLength
	PVOID Data
	ULONG DataLength
	PIO_STATUS_BLOCK IoStatus
)
{...}

PFNKSFASTHANDLER 


```

## -parameters

### -param FileObject: 
### -param Request: 
### -param RequestLength: 
### -param Data: 
### -param DataLength: 
### -param IoStatus: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also