---
UID: NS.ntddscsi._STORAGE_FIRMWARE_INFO_V2
title: STORAGE_FIRMWARE_INFO_V2
author: windows-driver-content
description: 
ms.assetid: 310b26a7-62dc-4d09-872b-8b6baf549012
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: STORAGE_FIRMWARE_INFO_V2, STORAGE_FIRMWARE_INFO_V2, *PSTORAGE_FIRMWARE_INFO_V2
req.header: ntddscsi.h
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

# STORAGE_FIRMWARE_INFO_V2 structure

## -description



## -struct-fields

### -field ULONG Version			
 	
### -field ULONG Size			
 	
### -field BOOLEAN UpgradeSupport			
 	
### -field UCHAR SlotCount			
 	
### -field UCHAR ActiveSlot			
 	
### -field UCHAR PendingActivateSlot			
 	
### -field BOOLEAN FirmwareShared			
 	
### -field UCHAR [3] Reserved			
 	
### -field ULONG ImagePayloadAlignment			
 	
### -field ULONG ImagePayloadMaxSize			
 	
### -field STORAGE_FIRMWARE_SLOT_INFO_V2 [0] Slot			
 	
## -remarks

## -see-also