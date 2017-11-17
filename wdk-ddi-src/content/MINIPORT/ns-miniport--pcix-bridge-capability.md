---
UID: NS.miniport._PCIX_BRIDGE_CAPABILITY
title: PCIX_BRIDGE_CAPABILITY
author: windows-driver-content
description: 
ms.assetid: 4b009443-183e-4129-bd5b-55bb30e23fbb
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: PCIX_BRIDGE_CAPABILITY, PCIX_BRIDGE_CAPABILITY, *PPCIX_BRIDGE_CAPABILITY
req.header: miniport.h
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

# PCIX_BRIDGE_CAPABILITY structure

## -description



## -struct-fields

### -field union SecondaryStatus			
 	
### -field __unnamed_union_0c02_25 __unnamed_union_0c02_25			
 	
### -field union BridgeStatus			
 	
### -field __unnamed_union_0c02_27 __unnamed_union_0c02_27			
 	
### -field union EccControlStatus			
 	
### -field __unnamed_union_0c02_29 __unnamed_union_0c02_29			
 	
### -field PCI_CAPABILITIES_HEADER Header			
 	
### -field USHORT UpstreamSplitTransactionCapacity			
 	
### -field USHORT UpstreamSplitTransactionLimit			
 	
### -field USHORT DownstreamSplitTransactionCapacity			
 	
### -field USHORT DownstreamSplitTransactionLimit			
 	
### -field ULONG EccFirstAddress			
 	
### -field ULONG EccSecondAddress			
 	
### -field ULONG EccAttribute			
 	
### -field USHORT  : 1 Bus64Bit			
 	
### -field USHORT  : 1 Bus133MHzCapable			
 	
### -field USHORT  : 1 SplitCompletionDiscarded			
 	
### -field USHORT  : 1 UnexpectedSplitCompletion			
 	
### -field USHORT  : 1 SplitCompletionOverrun			
 	
### -field USHORT  : 1 SplitRequestDelayed			
 	
### -field USHORT  : 4 BusModeFrequency			
 	
### -field USHORT  : 2 Rsvd			
 	
### -field USHORT  : 2 Version			
 	
### -field USHORT  : 1 Bus266MHzCapable			
 	
### -field USHORT  : 1 Bus533MHzCapable			
 	
### -field USHORT AsUSHORT			
 	
### -field ULONG  : 3 FunctionNumber			
 	
### -field ULONG  : 5 DeviceNumber			
 	
### -field ULONG  : 8 BusNumber			
 	
### -field ULONG  : 1 Device64Bit			
 	
### -field ULONG  : 1 Device133MHzCapable			
 	
### -field ULONG  : 1 SplitCompletionDiscarded			
 	
### -field ULONG  : 1 UnexpectedSplitCompletion			
 	
### -field ULONG  : 1 SplitCompletionOverrun			
 	
### -field ULONG  : 1 SplitRequestDelayed			
 	
### -field ULONG  : 7 Rsvd			
 	
### -field ULONG  : 1 DIMCapable			
 	
### -field ULONG  : 1 Device266MHzCapable			
 	
### -field ULONG  : 1 Device533MHzCapable			
 	
### -field ULONG AsULONG			
 	
### -field ULONG  : 1 SelectSecondaryRegisters			
 	
### -field ULONG  : 1 ErrorPresentInOtherBank			
 	
### -field ULONG  : 1 AdditionalCorrectableError			
 	
### -field ULONG  : 1 AdditionalUncorrectableError			
 	
### -field ULONG  : 3 ErrorPhase			
 	
### -field ULONG  : 1 ErrorCorrected			
 	
### -field ULONG  : 8 Syndrome			
 	
### -field ULONG  : 4 ErrorFirstCommand			
 	
### -field ULONG  : 4 ErrorSecondCommand			
 	
### -field ULONG  : 4 ErrorUpperAttributes			
 	
### -field ULONG  : 1 ControlUpdateEnable			
 	
### -field ULONG  : 1 Rsvd			
 	
### -field ULONG  : 1 DisableSingleBitCorrection			
 	
### -field ULONG  : 1 EccMode			
 	
### -field ULONG AsULONG			
 	
## -remarks

## -see-also