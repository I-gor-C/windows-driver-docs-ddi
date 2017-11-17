---
UID: NS.ntddk._ARBITER_LIST_ENTRY
title: ARBITER_LIST_ENTRY
author: windows-driver-content
description: 
ms.assetid: def0eb26-2200-4303-ae6f-025d772b4cc4
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: ARBITER_LIST_ENTRY, ARBITER_LIST_ENTRY, *PARBITER_LIST_ENTRY
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

# ARBITER_LIST_ENTRY structure

## -description



## -struct-fields

### -field LIST_ENTRY ListEntry			
 	
### -field ULONG AlternativeCount			
 	
### -field PIO_RESOURCE_DESCRIPTOR Alternatives			
 	
### -field PDEVICE_OBJECT PhysicalDeviceObject			
 	
### -field ARBITER_REQUEST_SOURCE RequestSource			
 	
### -field ULONG Flags			
 	
### -field LONG_PTR WorkSpace			
 	
### -field INTERFACE_TYPE InterfaceType			
 	
### -field ULONG SlotNumber			
 	
### -field ULONG BusNumber			
 	
### -field PCM_PARTIAL_RESOURCE_DESCRIPTOR Assignment			
 	
### -field PIO_RESOURCE_DESCRIPTOR SelectedAlternative			
 	
### -field ARBITER_RESULT Result			
 	
## -remarks

## -see-also