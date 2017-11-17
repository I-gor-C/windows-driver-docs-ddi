---
UID: NS.wdm._ERESOURCE
title: ERESOURCE
author: windows-driver-content
description: 
ms.assetid: aaa23276-9e63-418a-ae70-35c9a005dda3
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: ERESOURCE, ERESOURCE, *PERESOURCE
req.header: wdm.h
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

# ERESOURCE structure

## -description



## -struct-fields

### -field union __unnamed_union_0cb3_99			
 	
### -field union __unnamed_union_0cb3_101			
 	
### -field LIST_ENTRY SystemResourcesList			
 	
### -field POWNER_ENTRY OwnerTable			
 	
### -field SHORT ActiveCount			
 	
### -field PVOID SharedWaiters			
 	
### -field PVOID ExclusiveWaiters			
 	
### -field OWNER_ENTRY OwnerEntry			
 	
### -field ULONG ActiveEntries			
 	
### -field ULONG ContentionCount			
 	
### -field ULONG NumberOfSharedWaiters			
 	
### -field ULONG NumberOfExclusiveWaiters			
 	
### -field PVOID Reserved2			
 	
### -field KSPIN_LOCK SpinLock			
 	
### -field UCHAR ReservedLowFlags			
 	
### -field UCHAR WaiterPriority			
 	
### -field USHORT Flag			
 	
### -field PVOID Address			
 	
### -field ULONG_PTR CreatorBackTraceIndex			
 	
## -remarks

## -see-also