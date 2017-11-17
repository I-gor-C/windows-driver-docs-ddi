---
UID: NS.srb._PORT_CONFIGURATION_INFORMATION
title: PORT_CONFIGURATION_INFORMATION
author: windows-driver-content
description: 
ms.assetid: 62095495-3558-4c63-8ff1-6881353d1027
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: PORT_CONFIGURATION_INFORMATION, PORT_CONFIGURATION_INFORMATION, *PPORT_CONFIGURATION_INFORMATION
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

# PORT_CONFIGURATION_INFORMATION structure

## -description



## -struct-fields

### -field ULONG Length			
 	
### -field ULONG SystemIoBusNumber			
 	
### -field INTERFACE_TYPE AdapterInterfaceType			
 	
### -field ULONG BusInterruptLevel			
 	
### -field ULONG BusInterruptVector			
 	
### -field KINTERRUPT_MODE InterruptMode			
 	
### -field ULONG MaximumTransferLength			
 	
### -field ULONG NumberOfPhysicalBreaks			
 	
### -field ULONG DmaChannel			
 	
### -field ULONG DmaPort			
 	
### -field DMA_WIDTH DmaWidth			
 	
### -field DMA_SPEED DmaSpeed			
 	
### -field ULONG AlignmentMask			
 	
### -field ULONG NumberOfAccessRanges			
 	
### -field ACCESS_RANGE(* )[] AccessRanges			
 	
### -field PVOID Reserved			
 	
### -field UCHAR NumberOfBuses			
 	
### -field UCHAR [8] InitiatorBusId			
 	
### -field BOOLEAN ScatterGather			
 	
### -field BOOLEAN Master			
 	
### -field BOOLEAN CachesData			
 	
### -field BOOLEAN AdapterScansDown			
 	
### -field BOOLEAN AtdiskPrimaryClaimed			
 	
### -field BOOLEAN AtdiskSecondaryClaimed			
 	
### -field BOOLEAN Dma32BitAddresses			
 	
### -field BOOLEAN DemandMode			
 	
### -field BOOLEAN MapBuffers			
 	
### -field BOOLEAN NeedPhysicalAddresses			
 	
### -field BOOLEAN TaggedQueuing			
 	
### -field BOOLEAN AutoRequestSense			
 	
### -field BOOLEAN MultipleRequestPerLu			
 	
### -field BOOLEAN ReceiveEvent			
 	
### -field BOOLEAN RealModeInitialized			
 	
### -field BOOLEAN BufferAccessScsiPortControlled			
 	
### -field UCHAR MaximumNumberOfTargets			
 	
### -field UCHAR [2] ReservedUchars			
 	
### -field ULONG SlotNumber			
 	
### -field ULONG BusInterruptLevel2			
 	
### -field ULONG BusInterruptVector2			
 	
### -field KINTERRUPT_MODE InterruptMode2			
 	
### -field ULONG DmaChannel2			
 	
### -field ULONG DmaPort2			
 	
### -field DMA_WIDTH DmaWidth2			
 	
### -field DMA_SPEED DmaSpeed2			
 	
### -field ULONG DeviceExtensionSize			
 	
### -field ULONG SpecificLuExtensionSize			
 	
### -field ULONG SrbExtensionSize			
 	
### -field UCHAR Dma64BitAddresses			
 	
### -field BOOLEAN ResetTargetSupported			
 	
### -field UCHAR MaximumNumberOfLogicalUnits			
 	
### -field BOOLEAN WmiDataProvider			
 	
## -remarks

## -see-also