---
UID: NS.ndis._NDIS_MINIPORT_INTERRUPT
title: NDIS_MINIPORT_INTERRUPT
author: windows-driver-content
description: 
ms.assetid: 8b3574ba-305b-4cba-b1a3-26c0d700427a
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: NDIS_MINIPORT_INTERRUPT, NDIS_MINIPORT_INTERRUPT, *PNDIS_MINIPORT_INTERRUPT
req.header: ndis.h
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

# NDIS_MINIPORT_INTERRUPT structure

## -description



## -struct-fields

### -field union __unnamed_union_0c0c_107			
 	
### -field PKINTERRUPT InterruptObject			
 	
### -field PVOID Reserved			
 	
### -field W_ISR_HANDLER MiniportIsr			
 	
### -field W_HANDLE_INTERRUPT_HANDLER MiniportDpc			
 	
### -field KDPC InterruptDpc			
 	
### -field PNDIS_MINIPORT_BLOCK Miniport			
 	
### -field LONG DpcCount			
 	
### -field KEVENT DpcsCompletedEvent			
 	
### -field BOOLEAN SharedInterrupt			
 	
### -field BOOLEAN IsrRequested			
 	
### -field BOOLEAN IsDeregistered			
 	
### -field KSPIN_LOCK DpcCountLock			
 	
## -remarks

## -see-also