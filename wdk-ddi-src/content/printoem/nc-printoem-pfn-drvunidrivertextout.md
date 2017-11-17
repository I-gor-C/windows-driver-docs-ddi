---
UID: NC.printoem.PFN_DrvUnidriverTextOut
title: PFN_DrvUnidriverTextOut
author: windows-driver-content
description: 
ms.assetid: f8d92c78-12e1-4b3a-8130-65e4b7379022
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: printoem.h
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

# PFN_DrvUnidriverTextOut callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_DrvUnidriverTextOut PfnDrvunidrivertextout; 

// Definition

BOOL PfnDrvunidrivertextout 
(
	SURFOBJ *pso
	STROBJ *pstro
	FONTOBJ *pfo
	CLIPOBJ *pco
	RECTL *prclExtra
	RECTL *prclOpaque
	BRUSHOBJ *pboFore
	BRUSHOBJ *pboOpaque
	POINTL *pptlBrushOrg
	MIX mix
)
{...}

PFN_DrvUnidriverTextOut 


```

## -parameters

### -param *pso: 
### -param *pstro: 
### -param *pfo: 
### -param *pco: 
### -param *prclExtra: 
### -param *prclOpaque: 
### -param *pboFore: 
### -param *pboOpaque: 
### -param *pptlBrushOrg: 
### -param mix: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also