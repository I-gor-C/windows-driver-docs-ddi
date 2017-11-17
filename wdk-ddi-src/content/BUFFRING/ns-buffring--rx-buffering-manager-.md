---
UID: NS.buffring._RX_BUFFERING_MANAGER_
title: RX_BUFFERING_MANAGER_
author: windows-driver-content
description: 
ms.assetid: 0b579142-e8cf-40a4-b803-e7b2625b7784
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: RX_BUFFERING_MANAGER_, RX_BUFFERING_MANAGER, *PRX_BUFFERING_MANAGER
req.header: buffring.h
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

# RX_BUFFERING_MANAGER_ structure

## -description



## -struct-fields

### -field BOOLEAN DispatcherActive			
 	
### -field BOOLEAN HandlerInactive			
 	
### -field BOOLEAN LastChanceHandlerActive			
 	
### -field UCHAR Pad			
 	
### -field KSPIN_LOCK SpinLock			
 	
### -field __volatile LONG CumulativeNumberOfBufferingChangeRequests			
 	
### -field LONG NumberOfUnhandledRequests			
 	
### -field LONG NumberOfUndispatchedRequests			
 	
### -field __volatile LONG NumberOfOutstandingOpens			
 	
### -field LIST_ENTRY DispatcherList			
 	
### -field LIST_ENTRY HandlerList			
 	
### -field LIST_ENTRY LastChanceHandlerList			
 	
### -field RX_WORK_QUEUE_ITEM DispatcherWorkItem			
 	
### -field RX_WORK_QUEUE_ITEM HandlerWorkItem			
 	
### -field RX_WORK_QUEUE_ITEM LastChanceHandlerWorkItem			
 	
### -field FAST_MUTEX Mutex			
 	
### -field LIST_ENTRY [1] SrvOpenLists			
 	
## -remarks

## -see-also