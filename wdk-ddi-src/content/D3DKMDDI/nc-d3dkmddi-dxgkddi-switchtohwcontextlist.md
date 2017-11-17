---
UID: NC.d3dkmddi.DXGKDDI_SWITCHTOHWCONTEXTLIST
title: DXGKDDI_SWITCHTOHWCONTEXTLIST
author: windows-driver-content
description: 
ms.assetid: eeded06a-39da-48da-be26-9e769277eaeb
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3dkmddi.h
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

# DXGKDDI_SWITCHTOHWCONTEXTLIST callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_SWITCHTOHWCONTEXTLIST DxgkddiSwitchtohwcontextlist; 

// Definition

NTSTATUS DxgkddiSwitchtohwcontextlist 
(
	IN_CONST_HANDLE hAdapter
	IN_CONST_PDXGKARG_SWITCHTOHWCONTEXTLIST pHwContextList
)
{...}

DXGKDDI_SWITCHTOHWCONTEXTLIST PDXGKDDI_SWITCHTOHWCONTEXTLIST


```

## -parameters

### -param hAdapter: 
### -param pHwContextList: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also