---
UID : NS:ksi.KSIDEFAULTCLOCK
title : KSIDEFAULTCLOCK
author : windows-driver-content
description : .
old-location : stream\ksidefaultclock.htm
old-project : stream
ms.assetid : 08509C28-DDD4-4060-A16A-857A6BF6F6E1
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : KSIDEFAULTCLOCK, KSIDEFAULTCLOCK, *PKSIDEFAULTCLOCK
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ksi.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : KSIDEFAULTCLOCK
req.alt-loc : Ksi.h
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
req.typenames : KSIDEFAULTCLOCK, *PKSIDEFAULTCLOCK
---

# KSIDEFAULTCLOCK structure


## Syntax
````
typedef struct {
  LONGLONG                  Frequency;
  LONGLONG                  LastDueTime;
  LONGLONG                  RunningTimeDelta;
  LONGLONG                  LastRunningTime;
  KSPIN_LOCK                TimeAccessLock;
  LIST_ENTRY                EventQueue;
  KSPIN_LOCK                EventQueueLock;
  KTIMER                    QueueTimer;
  KDPC                      QueueDpc;
  LONG                      ReferenceCount;
  KSSTATE                   State;
  LONGLONG                  SuspendDelta;
  LONGLONG                  SuspendTime;
  PFNKSSETTIMER             SetTimer;
  PFNKSCANCELTIMER          CancelTimer;
  PFNKSCLOCK_CORRELATEDTIME CorrelatedTime;
  PVOID                     Context;
  KSRESOLUTION              Resolution;
  KEVENT                    FreeEvent;
  LONG                      ExternalTimeReferenceCount;
  BOOLEAN                   ExternalTimeValid;
  LONGLONG                  LastStreamTime;
} KSIDEFAULTCLOCK, *PKSIDEFAULTCLOCK;
````

## Members

        
            `CancelTimer`

            
        
            `Context`

            
        
            `CorrelatedTime`

            
        
            `EventQueue`

            
        
            `EventQueueLock`

            
        
            `ExternalTimeReferenceCount`

            
        
            `ExternalTimeValid`

            
        
            `FreeEvent`

            
        
            `Frequency`

            
        
            `LastDueTime`

            
        
            `LastRunningTime`

            
        
            `LastStreamTime`

            
        
            `QueueDpc`

            
        
            `QueueTimer`

            
        
            `ReferenceCount`

            
        
            `Resolution`

            
        
            `RunningTimeDelta`

            
        
            `SetTimer`

            
        
            `State`

            
        
            `SuspendDelta`

            
        
            `SuspendTime`

            
        
            `TimeAccessLock`

            


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ksi.h |