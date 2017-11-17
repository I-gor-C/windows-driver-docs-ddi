---
UID: NS.miniport._CM_EISA_FUNCTION_INFORMATION
title: CM_EISA_FUNCTION_INFORMATION
author: windows-driver-content
description: 
ms.assetid: 319c64aa-1fe4-4b2a-859d-0250fb3b243c
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: CM_EISA_FUNCTION_INFORMATION, CM_EISA_FUNCTION_INFORMATION, *PCM_EISA_FUNCTION_INFORMATION
req.header: miniport.h
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

# CM_EISA_FUNCTION_INFORMATION structure

## -description



## -struct-fields

### -field ULONG CompressedId			
 	
### -field UCHAR IdSlotFlags1			
 	
### -field UCHAR IdSlotFlags2			
 	
### -field UCHAR MinorRevision			
 	
### -field UCHAR MajorRevision			
 	
### -field UCHAR [26] Selections			
 	
### -field UCHAR FunctionFlags			
 	
### -field UCHAR [80] TypeString			
 	
### -field EISA_MEMORY_CONFIGURATION [9] EisaMemory			
 	
### -field EISA_IRQ_CONFIGURATION [7] EisaIrq			
 	
### -field EISA_DMA_CONFIGURATION [4] EisaDma			
 	
### -field EISA_PORT_CONFIGURATION [20] EisaPort			
 	
### -field UCHAR [60] InitializationData			
 	
## -remarks

## -see-also