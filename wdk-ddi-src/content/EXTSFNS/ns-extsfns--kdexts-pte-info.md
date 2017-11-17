---
UID: NS.extsfns._KDEXTS_PTE_INFO
title: KDEXTS_PTE_INFO
author: windows-driver-content
description: 
ms.assetid: 6b63956d-81a8-448a-bee3-911406515484
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: KDEXTS_PTE_INFO, KDEXTS_PTE_INFO, *PKDEXTS_PTE_INFO
req.header: extsfns.h
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

# KDEXTS_PTE_INFO structure

## -description



## -struct-fields

### -field ULONG SizeOfStruct			
 	
### -field ULONG64 VirtualAddress			
 	
### -field ULONG64 PpeAddress			
 	
### -field ULONG64 PdeAddress			
 	
### -field ULONG64 PteAddress			
 	
### -field ULONG64 Pfn			
 	
### -field ULONG64 Levels			
 	
### -field ULONG  : 1 PteValid			
 	
### -field ULONG  : 1 PteTransition			
 	
### -field ULONG  : 1 Prototype			
 	
### -field ULONG  : 1 Protection			
 	
### -field ULONG  : 28 Reserved			
 	
### -field ULONG  : 1 ReadInProgress			
 	
### -field ULONG  : 1 WriteInProgress			
 	
### -field ULONG  : 1 Modified			
 	
## -remarks

## -see-also