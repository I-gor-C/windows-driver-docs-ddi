---
UID: NS.rxworkq._RX_WORK_QUEUE_
title: RX_WORK_QUEUE_
author: windows-driver-content
description: 
ms.assetid: c735665f-9258-475a-a48f-c8555b311fae
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: RX_WORK_QUEUE_, RX_WORK_QUEUE, *PRX_WORK_QUEUE
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

# RX_WORK_QUEUE_ structure

## -description



## -struct-fields

### -field USHORT State			
 	
### -field BOOLEAN SpinUpRequestPending			
 	
### -field UCHAR Type			
 	
### -field KSPIN_LOCK SpinLock			
 	
### -field PRX_WORK_QUEUE_RUNDOWN_CONTEXT pRundownContext			
 	
### -field __volatile LONG NumberOfWorkItemsDispatched			
 	
### -field __volatile LONG NumberOfWorkItemsToBeDispatched			
 	
### -field LONG CumulativeQueueLength			
 	
### -field LONG NumberOfSpinUpRequests			
 	
### -field LONG MaximumNumberOfWorkerThreads			
 	
### -field LONG MinimumNumberOfWorkerThreads			
 	
### -field __volatile LONG NumberOfActiveWorkerThreads			
 	
### -field __volatile LONG NumberOfIdleWorkerThreads			
 	
### -field LONG NumberOfFailedSpinUpRequests			
 	
### -field __volatile LONG WorkQueueItemForSpinUpWorkerThreadInUse			
 	
### -field RX_WORK_QUEUE_ITEM WorkQueueItemForTearDownWorkQueue			
 	
### -field RX_WORK_QUEUE_ITEM WorkQueueItemForSpinUpWorkerThread			
 	
### -field RX_WORK_QUEUE_ITEM WorkQueueItemForSpinDownWorkerThread			
 	
### -field KQUEUE Queue			
 	
### -field PETHREAD * ThreadPointers			
 	
## -remarks

## -see-also