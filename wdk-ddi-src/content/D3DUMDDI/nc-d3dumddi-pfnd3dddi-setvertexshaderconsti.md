---
UID: NC.d3dumddi.PFND3DDDI_SETVERTEXSHADERCONSTI
title: PFND3DDDI_SETVERTEXSHADERCONSTI
author: windows-driver-content
description: 
ms.assetid: 126aa842-dadb-4d43-bd48-3beba7d06f0f
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3dumddi.h
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

# PFND3DDDI_SETVERTEXSHADERCONSTI callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DDDI_SETVERTEXSHADERCONSTI Pfnd3dddiSetvertexshaderconsti; 

// Definition

HRESULT Pfnd3dddiSetvertexshaderconsti 
(
	HANDLE hDevice
	CONST D3DDDIARG_SETVERTEXSHADERCONSTI *
	CONST INT *
)
{...}

PFND3DDDI_SETVERTEXSHADERCONSTI 


```

## -parameters

### -param hDevice: 
### -param *: 
### -param *: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also