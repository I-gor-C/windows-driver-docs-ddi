---
UID: NS.usbspec._USB_DEVICE_CAPABILITY_POWER_DELIVERY_DESCRIPTOR
title: USB_DEVICE_CAPABILITY_POWER_DELIVERY_DESCRIPTOR
author: windows-driver-content
description: 
ms.assetid: 5e475cd0-14e2-4398-bf9a-6965f2d41519
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: USB_DEVICE_CAPABILITY_POWER_DELIVERY_DESCRIPTOR, USB_DEVICE_CAPABILITY_POWER_DELIVERY_DESCRIPTOR, *PUSB_DEVICE_CAPABILITY_POWER_DELIVERY_DESCRIPTOR
req.header: usbspec.h
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

# USB_DEVICE_CAPABILITY_POWER_DELIVERY_DESCRIPTOR structure

## -description



## -struct-fields

### -field union bmAttributes			
 	
### -field __unnamed_union_0b00_8 __unnamed_union_0b00_8			
 	
### -field UCHAR bLength			
 	
### -field UCHAR bDescriptorType			
 	
### -field UCHAR bDevCapabilityType			
 	
### -field UCHAR bReserved			
 	
### -field USHORT bmProviderPorts			
 	
### -field USHORT bmConsumerPorts			
 	
### -field USHORT bcdBCVersion			
 	
### -field USHORT bcdPDVersion			
 	
### -field USHORT bcdUSBTypeCVersion			
 	
### -field ULONG  : 1 Reserved1			
 	
### -field ULONG  : 1 BatteryCharging			
 	
### -field ULONG  : 1 USBPowerDelivery			
 	
### -field ULONG  : 1 Provider			
 	
### -field ULONG  : 1 Consumer			
 	
### -field ULONG  : 1 ChargingPolicy			
 	
### -field ULONG  : 1 TypeCCurrent			
 	
### -field ULONG  : 1 Reserved2			
 	
### -field ULONG  : 1 ACSupply			
 	
### -field ULONG  : 1 Battery			
 	
### -field ULONG  : 1 Other			
 	
### -field ULONG  : 3 NumBatteries			
 	
### -field ULONG  : 1 UsesVbus			
 	
### -field ULONG  : 17 Reserved3			
 	
### -field ULONG AsUlong			
 	
## -remarks

## -see-also