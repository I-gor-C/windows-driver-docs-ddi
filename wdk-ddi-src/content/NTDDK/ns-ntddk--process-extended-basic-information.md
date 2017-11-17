---
UID: NS.ntddk._PROCESS_EXTENDED_BASIC_INFORMATION
title: PROCESS_EXTENDED_BASIC_INFORMATION
author: windows-driver-content
description: 
ms.assetid: 628ef1af-b822-45f4-a011-cbe83c966b6d
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: PROCESS_EXTENDED_BASIC_INFORMATION, PROCESS_EXTENDED_BASIC_INFORMATION, *PPROCESS_EXTENDED_BASIC_INFORMATION
req.header: ntddk.h
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

# PROCESS_EXTENDED_BASIC_INFORMATION structure

## -description



## -struct-fields

### -field union DUMMYUNIONNAME			
 	
### -field __unnamed_union_0c2a_12 __unnamed_union_0c2a_12			
 	
### -field SIZE_T Size			
 	
### -field PROCESS_BASIC_INFORMATION BasicInfo			
 	
### -field ULONG  : 1 IsProtectedProcess			
 	
### -field ULONG  : 1 IsWow64Process			
 	
### -field ULONG  : 1 IsProcessDeleting			
 	
### -field ULONG  : 1 IsCrossSessionCreate			
 	
### -field ULONG  : 1 IsFrozen			
 	
### -field ULONG  : 1 IsBackground			
 	
### -field ULONG  : 1 IsStronglyNamed			
 	
### -field ULONG  : 1 IsSecureProcess			
 	
### -field ULONG  : 1 IsSubsystemProcess			
 	
### -field ULONG  : 23 SpareBits			
 	
### -field ULONG Flags			
 	
## -remarks

## -see-also