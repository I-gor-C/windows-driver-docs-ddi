---
UID: NC.d3d10umddi.PFND3D10DDI_SETVERTEXPIPELINEOUTPUT
title: PFND3D10DDI_SETVERTEXPIPELINEOUTPUT
author: windows-driver-content
description: 
ms.assetid: 64888a9d-2925-4bcc-8cca-cde114fe6906
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3d10umddi.h
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

# PFND3D10DDI_SETVERTEXPIPELINEOUTPUT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D10DDI_SETVERTEXPIPELINEOUTPUT Pfnd3d10ddiSetvertexpipelineoutput; 

// Definition

VOID Pfnd3d10ddiSetvertexpipelineoutput 
(
	 D3D10DDI_HDEVICE
	CONST D3D10DDIARG_VERTEXPIPELINEOUTPUT *
)
{...}

PFND3D10DDI_SETVERTEXPIPELINEOUTPUT 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param *: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also