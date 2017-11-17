---
UID: NS.wdm._KAPC
title: KAPC
author: windows-driver-content
description: 
ms.assetid: 8629d6e8-ba38-400d-b6ae-7d65ebc06bb9
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: KAPC, KAPC, *PKAPC, *PRKAPC
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

# KAPC structure

## -description



## -struct-fields

### -field struct _KTHREAD			
 	
### -field _KTHREAD * Thread			
 	
### -field UCHAR Type			
 	
### -field UCHAR SpareByte0			
 	
### -field UCHAR Size			
 	
### -field UCHAR SpareByte1			
 	
### -field ULONG SpareLong0			
 	
### -field LIST_ENTRY ApcListEntry			
 	
### -field PVOID [3] Reserved			
 	
### -field PVOID NormalContext			
 	
### -field PVOID SystemArgument1			
 	
### -field PVOID SystemArgument2			
 	
### -field CCHAR ApcStateIndex			
 	
### -field KPROCESSOR_MODE ApcMode			
 	
### -field BOOLEAN Inserted			
 	
## -remarks

## -see-also