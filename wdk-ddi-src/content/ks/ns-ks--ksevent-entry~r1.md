---
UID: NS.ks._KSEVENT_ENTRY~r1
title: KSEVENT_ENTRY
author: windows-driver-content
description: 
ms.assetid: 2013b4b6-2609-4171-a1ac-b82a61f10ac3
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: KSEVENT_ENTRY, 
req.header: ks.h
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

# KSEVENT_ENTRY structure

## -description



## -struct-fields

### -field union __unnamed_union_0cc4_137			
 	
### -field LIST_ENTRY ListEntry			
 	
### -field PVOID Object			
 	
### -field PKSEVENTDATA EventData			
 	
### -field ULONG NotificationType			
 	
### -field const KSEVENT_SET * EventSet			
 	
### -field const KSEVENT_ITEM * EventItem			
 	
### -field PFILE_OBJECT FileObject			
 	
### -field ULONG SemaphoreAdjustment			
 	
### -field ULONG Reserved			
 	
### -field ULONG Flags			
 	
### -field PKSDPC_ITEM DpcItem			
 	
### -field PKSBUFFER_ITEM BufferItem			
 	
## -remarks

## -see-also