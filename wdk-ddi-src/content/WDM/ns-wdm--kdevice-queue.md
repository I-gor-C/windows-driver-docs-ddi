---
UID: NS.wdm._KDEVICE_QUEUE
title: KDEVICE_QUEUE
author: windows-driver-content
description: 
ms.assetid: e2cf0640-b24c-4351-8bed-1b70dda8a1b6
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: KDEVICE_QUEUE, KDEVICE_QUEUE, *PKDEVICE_QUEUE, *PRKDEVICE_QUEUE
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

# KDEVICE_QUEUE structure

## -description



## -struct-fields

### -field union __unnamed_union_0cb3_92			
 	
### -field CSHORT Type			
 	
### -field CSHORT Size			
 	
### -field LIST_ENTRY DeviceListHead			
 	
### -field KSPIN_LOCK Lock			
 	
### -field BOOLEAN Busy			
 	
### -field LONG64  : 8 Reserved			
 	
### -field LONG64  : 56 Hint			
 	
### -field BOOLEAN Busy			
 	
## -remarks

## -see-also