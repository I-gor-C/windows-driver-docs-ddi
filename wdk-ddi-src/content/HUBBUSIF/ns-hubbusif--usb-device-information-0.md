---
UID: NS.hubbusif._USB_DEVICE_INFORMATION_0
title: USB_DEVICE_INFORMATION_0
author: windows-driver-content
description: 
ms.assetid: bbb930f6-ea73-4b21-b02f-11915c802c3e
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: USB_DEVICE_INFORMATION_0, USB_DEVICE_INFORMATION_0, *PUSB_DEVICE_INFORMATION_0
req.header: hubbusif.h
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

# USB_DEVICE_INFORMATION_0 structure

## -description



## -struct-fields

### -field ULONG InformationLevel			
 	
### -field ULONG ActualLength			
 	
### -field ULONG PortNumber			
 	
### -field USB_DEVICE_DESCRIPTOR DeviceDescriptor			
 	
### -field UCHAR [2] DD_pad			
 	
### -field UCHAR CurrentConfigurationValue			
 	
### -field UCHAR ReservedMBZ			
 	
### -field USHORT DeviceAddress			
 	
### -field ULONG HubAddress			
 	
### -field USB_DEVICE_SPEED DeviceSpeed			
 	
### -field USB_DEVICE_TYPE DeviceType			
 	
### -field ULONG NumberOfOpenPipes			
 	
### -field USB_PIPE_INFORMATION_0 [1] PipeList			
 	
## -remarks

## -see-also