---
UID: NS.wdm._KDPC~r1
title: KDPC
author: windows-driver-content
description: 
ms.assetid: 7a579c6f-8238-40be-b4f8-aaf602d35371
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: KDPC, KDPC, *PKDPC, *PRKDPC
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

# KDPC structure

## -description



## -struct-fields

### -field union DUMMYUNIONNAME			
 	
### -field __unnamed_union_0cb3_54 __unnamed_union_0cb3_54			
 	
### -field SINGLE_LIST_ENTRY DpcListEntry			
 	
### -field KAFFINITY ProcessorHistory			
 	
### -field PKDEFERRED_ROUTINE DeferredRoutine			
 	
### -field PVOID DeferredContext			
 	
### -field PVOID SystemArgument1			
 	
### -field PVOID SystemArgument2			
 	
### -field __volatile PVOID DpcData			
 	
### -field UCHAR Type			
 	
### -field UCHAR Importance			
 	
### -field USHORT Number			
 	
### -field ULONG TargetInfoAsUlong			
 	
## -remarks

## -see-also