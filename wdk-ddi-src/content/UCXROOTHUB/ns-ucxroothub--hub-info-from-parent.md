---
UID: NS.ucxroothub._HUB_INFO_FROM_PARENT
title: HUB_INFO_FROM_PARENT
author: windows-driver-content
description: 
ms.assetid: facece1f-5cbc-4e66-be7e-0b74fd66c4b8
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: HUB_INFO_FROM_PARENT, HUB_INFO_FROM_PARENT, *PHUB_INFO_FROM_PARENT
req.header: ucxroothub.h
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

# HUB_INFO_FROM_PARENT structure

## -description



## -struct-fields

### -field PDEVICE_OBJECT IoTarget			
 	
### -field USB_DEVICE_DESCRIPTOR DeviceDescriptor			
 	
### -field USHORT U1ExitLatency			
 	
### -field USHORT U2ExitLatency			
 	
### -field USHORT ExitLatencyOfSlowestLinkForU1			
 	
### -field UCHAR DepthOfSlowestLinkForU1			
 	
### -field USHORT ExitLatencyOfSlowestLinkForU2			
 	
### -field UCHAR DepthOfSlowestLinkForU2			
 	
### -field USHORT HostInitiatedU1ExitLatency			
 	
### -field USHORT HostInitiatedU2ExitLatency			
 	
### -field UCHAR TotalHubDepth			
 	
### -field USHORT TotalTPPropogationDelay			
 	
### -field PARENT_HUB_FLAGS HubFlags			
 	
### -field PUSB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_SPEED SublinkSpeedAttr			
 	
### -field ULONG SublinkSpeedAttrCount			
 	
## -remarks

## -see-also