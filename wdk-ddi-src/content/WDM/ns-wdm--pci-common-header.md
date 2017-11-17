---
UID: NS.wdm._PCI_COMMON_HEADER
title: PCI_COMMON_HEADER
author: windows-driver-content
description: 
ms.assetid: c8b63362-daff-4aca-9414-0bff90920a0a
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: PCI_COMMON_HEADER, PCI_COMMON_HEADER, *PPCI_COMMON_HEADER
req.header: wdm.h
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

# PCI_COMMON_HEADER structure

## -description



## -struct-fields

### -field union u			
 	
### -field __unnamed_union_0cb3_186 __unnamed_union_0cb3_186			
 	
### -field USHORT VendorID			
 	
### -field USHORT DeviceID			
 	
### -field USHORT Command			
 	
### -field USHORT Status			
 	
### -field UCHAR RevisionID			
 	
### -field UCHAR ProgIf			
 	
### -field UCHAR SubClass			
 	
### -field UCHAR BaseClass			
 	
### -field UCHAR CacheLineSize			
 	
### -field UCHAR LatencyTimer			
 	
### -field UCHAR HeaderType			
 	
### -field UCHAR BIST			
 	
### -field ULONG [PCI_TYPE0_ADDRESSES] BaseAddresses			
 	
### -field ULONG CIS			
 	
### -field USHORT SubVendorID			
 	
### -field USHORT SubSystemID			
 	
### -field ULONG ROMBaseAddress			
 	
### -field UCHAR CapabilitiesPtr			
 	
### -field UCHAR [3] Reserved1			
 	
### -field ULONG Reserved2			
 	
### -field UCHAR InterruptLine			
 	
### -field UCHAR InterruptPin			
 	
### -field UCHAR MinimumGrant			
 	
### -field UCHAR MaximumLatency			
 	
### -field ULONG [PCI_TYPE1_ADDRESSES] BaseAddresses			
 	
### -field UCHAR PrimaryBus			
 	
### -field UCHAR SecondaryBus			
 	
### -field UCHAR SubordinateBus			
 	
### -field UCHAR SecondaryLatency			
 	
### -field UCHAR IOBase			
 	
### -field UCHAR IOLimit			
 	
### -field USHORT SecondaryStatus			
 	
### -field USHORT MemoryBase			
 	
### -field USHORT MemoryLimit			
 	
### -field USHORT PrefetchBase			
 	
### -field USHORT PrefetchLimit			
 	
### -field ULONG PrefetchBaseUpper32			
 	
### -field ULONG PrefetchLimitUpper32			
 	
### -field USHORT IOBaseUpper16			
 	
### -field USHORT IOLimitUpper16			
 	
### -field UCHAR CapabilitiesPtr			
 	
### -field UCHAR [3] Reserved1			
 	
### -field ULONG ROMBaseAddress			
 	
### -field UCHAR InterruptLine			
 	
### -field UCHAR InterruptPin			
 	
### -field USHORT BridgeControl			
 	
### -field struct __unnamed_struct_0cb3_187			
 	
### -field __unnamed_struct_0cb3_187 [PCI_TYPE2_ADDRESSES - 1] Range			
 	
### -field ULONG SocketRegistersBaseAddress			
 	
### -field UCHAR CapabilitiesPtr			
 	
### -field UCHAR Reserved			
 	
### -field USHORT SecondaryStatus			
 	
### -field UCHAR PrimaryBus			
 	
### -field UCHAR SecondaryBus			
 	
### -field UCHAR SubordinateBus			
 	
### -field UCHAR SecondaryLatency			
 	
### -field UCHAR InterruptLine			
 	
### -field UCHAR InterruptPin			
 	
### -field USHORT BridgeControl			
 	
## -remarks

## -see-also