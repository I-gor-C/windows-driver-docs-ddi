---
UID: NC.extsfns.EXT_ANALYSIS_PLUGIN
title: EXT_ANALYSIS_PLUGIN
author: windows-driver-content
description: 
ms.assetid: 74d9af39-3a46-4310-b264-196d9bc20254
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: extsfns.h
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

# EXT_ANALYSIS_PLUGIN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EXT_ANALYSIS_PLUGIN ExtAnalysisPlugin; 

// Definition

HRESULT ExtAnalysisPlugin 
(
	PDEBUG_CLIENT4 Client
	FA_EXTENSION_PLUGIN_PHASE CallPhase
	PDEBUG_FAILURE_ANALYSIS2 pAnalysis
)
{...}

EXT_ANALYSIS_PLUGIN 


```

## -parameters

### -param Client: 
### -param CallPhase: 
### -param pAnalysis: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also