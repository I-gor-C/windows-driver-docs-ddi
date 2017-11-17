---
UID: NS.ntddstor._DEVICEDUMP_SECTION_HEADER
title: DEVICEDUMP_SECTION_HEADER
author: windows-driver-content
description: 
ms.assetid: 31c857b5-8fed-4079-b7b2-eba4a5d533ba
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DEVICEDUMP_SECTION_HEADER, DEVICEDUMP_SECTION_HEADER, *PDEVICEDUMP_SECTION_HEADER
req.header: ntddstor.h
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

# DEVICEDUMP_SECTION_HEADER structure

## -description



## -struct-fields

### -field GUID guidDeviceDataId			
 	
### -field UCHAR [16] sOrganizationID			
 	
### -field ULONG dwFirmwareRevision			
 	
### -field UCHAR [DEVICEDUMP_MAX_IDSTRING] sModelNumber			
 	
### -field UCHAR [DEVICEDUMP_MAX_IDSTRING] szDeviceManufacturingID			
 	
### -field ULONG dwFlags			
 	
### -field ULONG bRestrictedPrivateDataVersion			
 	
### -field ULONG dwFirmwareIssueId			
 	
### -field UCHAR [MAX_FW_BUCKET_ID_LENGTH] szIssueDescriptionString			
 	
## -remarks

## -see-also