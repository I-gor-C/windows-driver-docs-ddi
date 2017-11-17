---
UID: NC.d3d10umddi.PFND3DWDDM2_0DDI_RETRIEVE_SHADER_COMMENT
title: PFND3DWDDM2_0DDI_RETRIEVE_SHADER_COMMENT
author: windows-driver-content
description: 
ms.assetid: 11245a0f-fa3e-4556-a330-be64411c0e87
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

# PFND3DWDDM2_0DDI_RETRIEVE_SHADER_COMMENT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_0DDI_RETRIEVE_SHADER_COMMENT Pfnd3dwddm20DdiRetrieveShaderComment; 

// Definition

HRESULT Pfnd3dwddm20DdiRetrieveShaderComment 
(
	 D3D10DDI_HDEVICE
	 D3D10DDI_HSHADER
	WCHAR *pBuffer
	SIZE_T *CharacterCountIncludingNullTerminator
)
{...}

PFND3DWDDM2_0DDI_RETRIEVE_SHADER_COMMENT 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param D3D10DDI_HSHADER: 
### -param *pBuffer: 
### -param *CharacterCountIncludingNullTerminator: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also