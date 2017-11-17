---
UID: NS.usbioctl._USB_DEVICE_PERFORMANCE_INFO
title: USB_DEVICE_PERFORMANCE_INFO
author: windows-driver-content
description: 
ms.assetid: 89e2d699-f991-46ee-8cde-ccc28252e340
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: USB_DEVICE_PERFORMANCE_INFO, USB_DEVICE_PERFORMANCE_INFO, *PUSB_DEVICE_PERFORMANCE_INFO
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

# USB_DEVICE_PERFORMANCE_INFO structure

## -description



## -struct-fields

### -field ULONG BulkBytes			
 	
### -field ULONG ControlDataBytes			
 	
### -field ULONG IsoBytes			
 	
### -field ULONG InterruptBytes			
 	
### -field ULONG BulkUrbCount			
 	
### -field ULONG ControlUrbCount			
 	
### -field ULONG IsoUrbCount			
 	
### -field ULONG InterruptUrbCount			
 	
### -field ULONG [6] AllocedInterrupt			
 	
### -field ULONG AllocedIso			
 	
### -field ULONG Total32secBandwidth			
 	
### -field ULONG TotalTtBandwidth			
 	
### -field WCHAR [60] DeviceDescription			
 	
### -field USB_DEVICE_SPEED DeviceSpeed			
 	
### -field ULONG TotalIsoLatency			
 	
### -field ULONG DroppedIsoPackets			
 	
### -field ULONG TransferErrors			
 	
### -field ULONG PciInterruptCount			
 	
### -field ULONG HcIdleState			
 	
### -field ULONG HcAsyncIdleState			
 	
### -field ULONG HcAsyncCacheFlushCount			
 	
### -field ULONG HcPeriodicIdleState			
 	
### -field ULONG HcPeriodicCacheFlushCount			
 	
## -remarks

## -see-also