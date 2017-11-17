---
UID: NS.61883._CIP_FRAME~r1
title: CIP_FRAME
author: windows-driver-content
description: 
ms.assetid: bcb8b632-1d07-4d08-8f4a-626d6dcd8576
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: CIP_FRAME, 
req.header: 61883.h
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

# CIP_FRAME structure

## -description



## -struct-fields

### -field union __unnamed_union_0b6a_6			
 	
### -field IN ULONG Flags			
 	
### -field IN PCIP_VALIDATE_ROUTINE pfnValidate			
 	
### -field IN PVOID ValidateContext			
 	
### -field IN PCIP_NOTIFY_ROUTINE pfnNotify			
 	
### -field IN PVOID NotifyContext			
 	
### -field OUT CYCLE_TIME Timestamp			
 	
### -field OUT ULONG Status			
 	
### -field IN OUT PUCHAR Packet			
 	
### -field OUT ULONG CompletedBytes			
 	
### -field IN PVOID Reserved			
 	
### -field IN PVOID pNext			
 	
## -remarks

## -see-also