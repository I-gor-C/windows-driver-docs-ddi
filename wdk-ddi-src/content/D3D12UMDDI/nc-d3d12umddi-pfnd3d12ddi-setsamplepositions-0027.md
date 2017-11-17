---
UID: NC.d3d12umddi.PFND3D12DDI_SETSAMPLEPOSITIONS_0027
title: PFND3D12DDI_SETSAMPLEPOSITIONS_0027
author: windows-driver-content
description: 
ms.assetid: dd21f4e5-42a2-4497-a448-fddfa49acf11
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3d12umddi.h
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

# PFND3D12DDI_SETSAMPLEPOSITIONS_0027 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_SETSAMPLEPOSITIONS_0027 Pfnd3d12ddiSetsamplepositions0027; 

// Definition

VOID Pfnd3d12ddiSetsamplepositions0027 
(
	 D3D12DDI_HCOMMANDLIST
	UINT NumSamplesPerPixel
	UINT NumPixels
	D3D12DDI_SAMPLE_POSITION *pSamplePositions
)
{...}

PFND3D12DDI_SETSAMPLEPOSITIONS_0027 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param NumSamplesPerPixel: 
### -param NumPixels: 
### -param *pSamplePositions: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also