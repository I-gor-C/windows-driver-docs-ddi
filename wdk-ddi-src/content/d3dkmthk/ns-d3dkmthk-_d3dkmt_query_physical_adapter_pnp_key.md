---
UID : NS:d3dkmthk._D3DKMT_QUERY_PHYSICAL_ADAPTER_PNP_KEY
title : _D3DKMT_QUERY_PHYSICAL_ADAPTER_PNP_KEY
author : windows-driver-content
description : A structure that holds information to query the physical adapter PNP key.
old-location : display\d3dkmt_query_physical_adapter_pnp_key.htm
old-project : display
ms.assetid : 58E5D200-56C3-48BA-A7C9-C9DC01592554
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _D3DKMT_QUERY_PHYSICAL_ADAPTER_PNP_KEY, D3DKMT_QUERY_PHYSICAL_ADAPTER_PNP_KEY
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dkmthk.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : D3DKMT_QUERY_PHYSICAL_ADAPTER_PNP_KEY
req.alt-loc : d3dkmthk.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : D3DKMT_QUERY_PHYSICAL_ADAPTER_PNP_KEY
---

# _D3DKMT_QUERY_PHYSICAL_ADAPTER_PNP_KEY structure
A structure that holds information to query the physical adapter PNP key.

## Syntax
````
typedef struct _D3DKMT_QUERY_PHYSICAL_ADAPTER_PNP_KEY {
  UINT                PhysicalAdapterIndex;
  D3DKMT_PNP_KEY_TYPE PnPKeyType;
  WCHAR               *pDest;
   UINT               *pCchDest;
} D3DKMT_QUERY_PHYSICAL_ADAPTER_PNP_KEY;
````

## Members

        
            `pCchDest`

            A UINT value representing the pCchDest.
        
            `pDest`

            A WCHAR value respresenting the pDest.
        
            `PhysicalAdapterIndex`

            The physical adapter index.
        
            `PnPKeyType`

            The type of the PNP key being queried.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmthk.h |