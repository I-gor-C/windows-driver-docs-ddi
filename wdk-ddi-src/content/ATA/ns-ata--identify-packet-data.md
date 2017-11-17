---
UID: NS.ata._IDENTIFY_PACKET_DATA
title: IDENTIFY_PACKET_DATA
author: windows-driver-content
description: 
ms.assetid: d224f4cc-bd80-42d9-a94e-2d1ed83ef850
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IDENTIFY_PACKET_DATA, IDENTIFY_PACKET_DATA, *PIDENTIFY_PACKET_DATA
req.header: ata.h
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

# IDENTIFY_PACKET_DATA structure

## -description



## -struct-fields

### -field struct GeneralConfiguration			
 	
### -field __unnamed_struct_0b6d_23 __unnamed_struct_0b6d_23			
 	
### -field struct Capabilities			
 	
### -field __unnamed_struct_0b6d_24 __unnamed_struct_0b6d_24			
 	
### -field struct DMADIR			
 	
### -field __unnamed_struct_0b6d_25 __unnamed_struct_0b6d_25			
 	
### -field struct SerialAtaCapabilities			
 	
### -field __unnamed_struct_0b6d_26 __unnamed_struct_0b6d_26			
 	
### -field struct SerialAtaFeaturesSupported			
 	
### -field __unnamed_struct_0b6d_27 __unnamed_struct_0b6d_27			
 	
### -field struct SerialAtaFeaturesEnabled			
 	
### -field __unnamed_struct_0b6d_28 __unnamed_struct_0b6d_28			
 	
### -field struct CommandSetSupport			
 	
### -field __unnamed_struct_0b6d_29 __unnamed_struct_0b6d_29			
 	
### -field struct CommandSetSupportExt			
 	
### -field __unnamed_struct_0b6d_30 __unnamed_struct_0b6d_30			
 	
### -field struct CommandSetActive			
 	
### -field __unnamed_struct_0b6d_31 __unnamed_struct_0b6d_31			
 	
### -field struct CommandSetActiveExt			
 	
### -field __unnamed_struct_0b6d_32 __unnamed_struct_0b6d_32			
 	
### -field struct TransportMajorVersion			
 	
### -field __unnamed_struct_0b6d_33 __unnamed_struct_0b6d_33			
 	
### -field USHORT ResevedWord1			
 	
### -field USHORT UniqueConfiguration			
 	
### -field USHORT [7] ReservedWords3			
 	
### -field UCHAR [20] SerialNumber			
 	
### -field USHORT [3] ReservedWords20			
 	
### -field UCHAR [8] FirmwareRevision			
 	
### -field UCHAR [40] ModelNumber			
 	
### -field USHORT [2] ReservedWords47			
 	
### -field USHORT [2] ObsoleteWords51			
 	
### -field USHORT  : 3 TranslationFieldsValid			
 	
### -field USHORT  : 13 Reserved3			
 	
### -field USHORT [8] ReservedWords54			
 	
### -field USHORT  : 8 MultiWordDMASupport			
 	
### -field USHORT  : 8 MultiWordDMAActive			
 	
### -field USHORT  : 8 AdvancedPIOModes			
 	
### -field USHORT  : 8 ReservedByte64			
 	
### -field USHORT MinimumMWXferCycleTime			
 	
### -field USHORT RecommendedMWXferCycleTime			
 	
### -field USHORT MinimumPIOCycleTime			
 	
### -field USHORT MinimumPIOCycleTimeIORDY			
 	
### -field USHORT [2] ReservedWords69			
 	
### -field USHORT BusReleaseDelay			
 	
### -field USHORT ServiceCommandDelay			
 	
### -field USHORT [2] ReservedWords73			
 	
### -field USHORT  : 5 QueueDepth			
 	
### -field USHORT  : 11 ReservedWord75			
 	
### -field USHORT MajorRevision			
 	
### -field USHORT MinorRevision			
 	
### -field USHORT  : 8 UltraDMASupport			
 	
### -field USHORT  : 8 UltraDMAActive			
 	
### -field USHORT TimeRequiredForNormalEraseModeSecurityEraseUnit			
 	
### -field USHORT TimeRequiredForEnhancedEraseModeSecurityEraseUnit			
 	
### -field USHORT CurrentAPMLevel			
 	
### -field USHORT MasterPasswordID			
 	
### -field USHORT HardwareResetResult			
 	
### -field USHORT [14] ReservedWords94			
 	
### -field USHORT [4] WorldWideName			
 	
### -field USHORT [13] ReservedWords112			
 	
### -field USHORT AtapiZeroByteCount			
 	
### -field USHORT ReservedWord126			
 	
### -field USHORT  : 2 MsnSupport			
 	
### -field USHORT  : 14 ReservedWord127			
 	
### -field USHORT SecurityStatus			
 	
### -field USHORT [31] VendorSpecific			
 	
### -field USHORT [16] ReservedWord160			
 	
### -field USHORT [46] ReservedWord176			
 	
### -field USHORT TransportMinorVersion			
 	
### -field USHORT [31] ReservedWord224			
 	
### -field USHORT  : 8 Signature			
 	
### -field USHORT  : 8 CheckSum			
 	
## -remarks

## -see-also