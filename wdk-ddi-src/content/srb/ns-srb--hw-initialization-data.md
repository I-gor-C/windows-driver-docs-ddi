---
UID: NS.srb._HW_INITIALIZATION_DATA
title: HW_INITIALIZATION_DATA
author: windows-driver-content
description: 
ms.assetid: cc0e7ee9-492a-4968-90f3-087fbe97f8c0
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: HW_INITIALIZATION_DATA, HW_INITIALIZATION_DATA, *PHW_INITIALIZATION_DATA
req.header: srb.h
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

# HW_INITIALIZATION_DATA structure

## -description



## -struct-fields

### -field union __unnamed_union_0af7_4			
 	
### -field ULONG HwInitializationDataSize			
 	
### -field INTERFACE_TYPE AdapterInterfaceType			
 	
### -field PHW_INITIALIZE HwInitialize			
 	
### -field PHW_STARTIO HwStartIo			
 	
### -field PHW_INTERRUPT HwInterrupt			
 	
### -field PHW_FIND_ADAPTER HwFindAdapter			
 	
### -field PHW_RESET_BUS HwResetBus			
 	
### -field PHW_DMA_STARTED HwDmaStarted			
 	
### -field PHW_ADAPTER_STATE HwAdapterState			
 	
### -field ULONG DeviceExtensionSize			
 	
### -field ULONG SpecificLuExtensionSize			
 	
### -field ULONG SrbExtensionSize			
 	
### -field ULONG NumberOfAccessRanges			
 	
### -field PVOID Reserved			
 	
### -field BOOLEAN MapBuffers			
 	
### -field BOOLEAN NeedPhysicalAddresses			
 	
### -field BOOLEAN TaggedQueuing			
 	
### -field BOOLEAN AutoRequestSense			
 	
### -field BOOLEAN MultipleRequestPerLu			
 	
### -field BOOLEAN ReceiveEvent			
 	
### -field USHORT VendorIdLength			
 	
### -field PVOID VendorId			
 	
### -field USHORT DeviceIdLength			
 	
### -field PVOID DeviceId			
 	
### -field PHW_ADAPTER_CONTROL HwAdapterControl			
 	
### -field USHORT ReservedUshort			
 	
### -field USHORT PortVersionFlags			
 	
## -remarks

## -see-also