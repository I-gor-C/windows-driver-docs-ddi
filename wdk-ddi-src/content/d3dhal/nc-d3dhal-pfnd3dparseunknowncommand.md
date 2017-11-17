---
UID: NC.d3dhal.PFND3DPARSEUNKNOWNCOMMAND
title: PFND3DPARSEUNKNOWNCOMMAND
author: windows-driver-content
description: 
ms.assetid: 3bd72a08-d52e-420f-a632-8d681d0f522a
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3dhal.h
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

# PFND3DPARSEUNKNOWNCOMMAND callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DPARSEUNKNOWNCOMMAND Pfnd3dparseunknowncommand; 

// Definition

HRESULT Pfnd3dparseunknowncommand 
(
	LPVOID lpvCommands
	LPVOID *lplpvReturnedCommand
)
{...}

PFND3DPARSEUNKNOWNCOMMAND 


```

## -parameters

### -param lpvCommands: 
### -param *lplpvReturnedCommand: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also