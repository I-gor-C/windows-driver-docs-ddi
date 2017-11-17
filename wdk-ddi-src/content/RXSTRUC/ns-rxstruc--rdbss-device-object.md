---
UID: NS.rxstruc._RDBSS_DEVICE_OBJECT
title: RDBSS_DEVICE_OBJECT
author: windows-driver-content
description: 
ms.assetid: d738b208-ba72-442b-a8c9-402b0589a55c
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: RDBSS_DEVICE_OBJECT, RDBSS_DEVICE_OBJECT, *PRDBSS_DEVICE_OBJECT
req.header: rxstruc.h
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

# RDBSS_DEVICE_OBJECT structure

## -description



## -struct-fields

### -field struct __unnamed_struct_0c51_2			
 	
### -field union __unnamed_union_0c51_1			
 	
### -field ULONG RegistrationControls			
 	
### -field PRDBSS_EXPORTS RdbssExports			
 	
### -field PDEVICE_OBJECT RDBSSDeviceObject			
 	
### -field PMINIRDR_DISPATCH Dispatch			
 	
### -field UNICODE_STRING DeviceName			
 	
### -field ULONG NetworkProviderPriority			
 	
### -field HANDLE MupHandle			
 	
### -field BOOLEAN RegisterUncProvider			
 	
### -field BOOLEAN RegisterMailSlotProvider			
 	
### -field BOOLEAN RegisteredAsFileSystem			
 	
### -field BOOLEAN Unused			
 	
### -field LIST_ENTRY MiniRdrListLinks			
 	
### -field __volatile ULONG NumberOfActiveFcbs			
 	
### -field __volatile ULONG NumberOfActiveContexts			
 	
### -field __deref_volatile LONG [RxMaximumWorkQueue] PostedRequestCount			
 	
### -field LONG [RxMaximumWorkQueue] OverflowQueueCount			
 	
### -field LIST_ENTRY [RxMaximumWorkQueue] OverflowQueue			
 	
### -field RX_SPIN_LOCK OverflowQueueSpinLock			
 	
### -field LONG AsynchronousRequestsPending			
 	
### -field PKEVENT pAsynchronousRequestsCompletionEvent			
 	
### -field RDBSS_STARTSTOP_CONTEXT StartStopContext			
 	
### -field RX_DISPATCHER_CONTEXT DispatcherContext			
 	
### -field PRX_PREFIX_TABLE pRxNetNameTable			
 	
### -field RX_PREFIX_TABLE RxNetNameTableInDeviceObject			
 	
### -field PRDBSS_SCAVENGER pRdbssScavenger			
 	
### -field RDBSS_SCAVENGER RdbssScavengerInDeviceObject			
 	
### -field DEVICE_OBJECT DeviceObject			
 	
## -remarks

## -see-also