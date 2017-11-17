---
UID: NS.usbioctl._USB_DEVICE_INFO
title: USB_DEVICE_INFO
author: windows-driver-content
description: 
ms.assetid: 6061b7ce-97db-4c5d-81f6-c11985050080
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: USB_DEVICE_INFO, USB_DEVICE_INFO, *PUSB_DEVICE_INFO
req.header: usbioctl.h
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

# USB_DEVICE_INFO structure

## -description



## -struct-fields

### -field USB_DEVICE_STATE DeviceState			
 	
### -field USHORT PortNumber			
 	
### -field USB_DEVICE_DESCRIPTOR DeviceDescriptor			
 	
### -field UCHAR CurrentConfigurationValue			
 	
### -field USB_DEVICE_SPEED Speed			
 	
### -field USHORT DeviceAddress			
 	
### -field ULONG ConnectionIndex			
 	
### -field USB_CONNECTION_STATUS ConnectionStatus			
 	
### -field WCHAR [128] PnpHardwareId			
 	
### -field WCHAR [128] PnpCompatibleId			
 	
### -field WCHAR [128] SerialNumberId			
 	
### -field WCHAR [128] PnpDeviceDescription			
 	
### -field ULONG NumberOfOpenPipes			
 	
### -field USB_PIPE_INFO [1] PipeList			
 	
## -remarks

## -see-also