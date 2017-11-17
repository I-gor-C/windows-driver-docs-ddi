---
UID: NS.usb._URB_OS_FEATURE_DESCRIPTOR_REQUEST
title: URB_OS_FEATURE_DESCRIPTOR_REQUEST
author: windows-driver-content
description: 
ms.assetid: 95093b32-a666-4874-9c81-6d7e65cde890
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: URB_OS_FEATURE_DESCRIPTOR_REQUEST, 
req.header: usb.h
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

# URB_OS_FEATURE_DESCRIPTOR_REQUEST structure

## -description



## -struct-fields

### -field struct Hdr			
 	
### -field _URB_HEADER _URB_HEADER			
 	
### -field struct _URB			
 	
### -field _URB * UrbLink			
 	
### -field struct hca			
 	
### -field _URB_HCD_AREA _URB_HCD_AREA			
 	
### -field PVOID Reserved			
 	
### -field ULONG Reserved0			
 	
### -field ULONG TransferBufferLength			
 	
### -field PVOID TransferBuffer			
 	
### -field PMDL TransferBufferMDL			
 	
### -field UCHAR  : 5 Recipient			
 	
### -field UCHAR  : 3 Reserved1			
 	
### -field UCHAR Reserved2			
 	
### -field UCHAR InterfaceNumber			
 	
### -field UCHAR MS_PageIndex			
 	
### -field USHORT MS_FeatureDescriptorIndex			
 	
### -field USHORT Reserved3			
 	
## -remarks

## -see-also