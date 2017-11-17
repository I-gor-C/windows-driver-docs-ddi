---
UID: NS.d3dkmthk._D3DKMT_GET_PTE
title: D3DKMT_GET_PTE
author: windows-driver-content
description: 
ms.assetid: f8b53fc0-f6a9-4c25-a3a7-fd8278253752
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: D3DKMT_GET_PTE, D3DKMT_GET_PTE
req.header: d3dkmthk.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
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

# D3DKMT_GET_PTE structure

## -description



## -struct-fields

### -field UINT PhysicalAdapterIndex			
 	
### -field UINT PageTableLevel			
 	
### -field UINT [DXGK_MAX_PAGE_TABLE_LEVEL_COUNT] PageTableIndex			
 	
### -field BOOLEAN b64KBPte			
 	
### -field UINT NumPtes			
 	
### -field DXGK_PTE [D3DKMT_GET_PTE_MAX] Pte			
 	
### -field UINT NumValidEntries			
 	
## -remarks

## -see-also