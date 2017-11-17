---
UID: NS.rxworkq._RX_DISPATCHER_
title: RX_DISPATCHER_
author: windows-driver-content
description: 
ms.assetid: ddd87169-d531-4215-9115-f2639a145e80
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: RX_DISPATCHER_, RX_DISPATCHER, *PRX_DISPATCHER
req.header: rxworkq.h
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

# RX_DISPATCHER_ structure

## -description



## -struct-fields

### -field LONG NumberOfProcessors			
 	
### -field PEPROCESS OwnerProcess			
 	
### -field PRX_WORK_QUEUE_DISPATCHER pWorkQueueDispatcher			
 	
### -field RX_DISPATCHER_STATE State			
 	
### -field LIST_ENTRY SpinUpRequests			
 	
### -field KSPIN_LOCK SpinUpRequestsLock			
 	
### -field KEVENT SpinUpRequestsEvent			
 	
### -field KEVENT SpinUpRequestsTearDownEvent			
 	
## -remarks

## -see-also