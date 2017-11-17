---
UID: NS.ks._KSFILTER_DESCRIPTOR~r1
title: KSFILTER_DESCRIPTOR
author: windows-driver-content
description: 
ms.assetid: 8da8937a-7be3-4ee1-a06c-722cb76f6982
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: KSFILTER_DESCRIPTOR, 
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

# KSFILTER_DESCRIPTOR structure

## -description



## -struct-fields

### -field const KSFILTER_DISPATCH * Dispatch			
 	
### -field const KSAUTOMATION_TABLE * AutomationTable			
 	
### -field ULONG Version			
 	
### -field ULONG Flags			
 	
### -field const GUID * ReferenceGuid			
 	
### -field ULONG PinDescriptorsCount			
 	
### -field ULONG PinDescriptorSize			
 	
### -field const KSPIN_DESCRIPTOR_EX * PinDescriptors			
 	
### -field ULONG CategoriesCount			
 	
### -field const GUID * Categories			
 	
### -field ULONG NodeDescriptorsCount			
 	
### -field ULONG NodeDescriptorSize			
 	
### -field const KSNODE_DESCRIPTOR * NodeDescriptors			
 	
### -field ULONG ConnectionsCount			
 	
### -field const KSTOPOLOGY_CONNECTION * Connections			
 	
### -field const KSCOMPONENTID * ComponentId			
 	
## -remarks

## -see-also