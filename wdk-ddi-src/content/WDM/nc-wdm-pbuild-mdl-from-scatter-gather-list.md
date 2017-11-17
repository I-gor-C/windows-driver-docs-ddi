---
UID: NC.wdm.PBUILD_MDL_FROM_SCATTER_GATHER_LIST
title: PBUILD_MDL_FROM_SCATTER_GATHER_LIST
author: windows-driver-content
description: 
ms.assetid: 58f9d9b8-00db-4479-86bf-802553bb601e
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# PBUILD_MDL_FROM_SCATTER_GATHER_LIST callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PBUILD_MDL_FROM_SCATTER_GATHER_LIST PbuildMdlFromScatterGatherList; 

// Definition

NTSTATUS PbuildMdlFromScatterGatherList 
(
	PDMA_ADAPTER DmaAdapter
	PSCATTER_GATHER_LIST ScatterGather
	PMDL OriginalMdl
	PMDL *TargetMdl
)
{...}

PBUILD_MDL_FROM_SCATTER_GATHER_LIST 


```

## -parameters

### -param DmaAdapter: 
### -param ScatterGather: 
### -param OriginalMdl: 
### -param *TargetMdl: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also