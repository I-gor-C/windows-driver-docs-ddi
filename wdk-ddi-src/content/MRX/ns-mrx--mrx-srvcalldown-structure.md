---
UID: NS.mrx._MRX_SRVCALLDOWN_STRUCTURE
title: MRX_SRVCALLDOWN_STRUCTURE
author: windows-driver-content
description: 
ms.assetid: 7a1434a4-aa42-4843-bf6c-d050b5e822d4
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: MRX_SRVCALLDOWN_STRUCTURE, MRX_SRVCALLDOWN_STRUCTURE
req.header: mrx.h
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

# MRX_SRVCALLDOWN_STRUCTURE structure

## -description



## -struct-fields

### -field KEVENT FinishEvent			
 	
### -field LIST_ENTRY SrvCalldownList			
 	
### -field PRX_CONTEXT RxContext			
 	
### -field PMRX_SRV_CALL SrvCall			
 	
### -field PMRX_SRVCALL_CALLBACK CallBack			
 	
### -field BOOLEAN CalldownCancelled			
 	
### -field ULONG NumberRemaining			
 	
### -field ULONG NumberToWait			
 	
### -field ULONG BestFinisherOrdinal			
 	
### -field PRDBSS_DEVICE_OBJECT BestFinisher			
 	
### -field MRX_SRVCALL_CALLBACK_CONTEXT [1] CallbackContexts			
 	
## -remarks

## -see-also