---
UID: NS.wdm._KWAIT_BLOCK
title: KWAIT_BLOCK
author: windows-driver-content
description: 
ms.assetid: 6b32e192-3f9a-498e-a303-5d72c9942db8
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: KWAIT_BLOCK, KWAIT_BLOCK, *PKWAIT_BLOCK, *PRKWAIT_BLOCK
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

# KWAIT_BLOCK structure

## -description



## -struct-fields

### -field union __unnamed_union_0cb3_91			
 	
### -field LIST_ENTRY WaitListEntry			
 	
### -field UCHAR WaitType			
 	
### -field UCHAR BlockState			
 	
### -field USHORT WaitKey			
 	
### -field LONG SpareLong			
 	
### -field PVOID Object			
 	
### -field PVOID SparePtr			
 	
### -field _KTHREAD * Thread			
 	
### -field _KQUEUE * NotificationQueue			
 	
## -remarks

## -see-also