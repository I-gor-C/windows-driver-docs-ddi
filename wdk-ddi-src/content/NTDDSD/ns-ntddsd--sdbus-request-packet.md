---
UID: NS.ntddsd._SDBUS_REQUEST_PACKET
title: SDBUS_REQUEST_PACKET
author: windows-driver-content
description: 
ms.assetid: 20af7d8b-679a-46a4-a0da-19ff678df91b
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: SDBUS_REQUEST_PACKET, SDBUS_REQUEST_PACKET, *PSDBUS_REQUEST_PACKET
req.header: ntddsd.h
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

# SDBUS_REQUEST_PACKET structure

## -description



## -struct-fields

### -field union ResponseData			
 	
### -field __unnamed_union_0c2d_6 __unnamed_union_0c2d_6			
 	
### -field union Parameters			
 	
### -field __unnamed_union_0c2d_7 __unnamed_union_0c2d_7			
 	
### -field SD_REQUEST_FUNCTION RequestFunction			
 	
### -field PVOID [3] UserContext			
 	
### -field ULONG_PTR Information			
 	
### -field UCHAR ResponseLength			
 	
### -field UCHAR Reserved			
 	
### -field USHORT Flags			
 	
### -field UCHAR [16] AsUCHAR			
 	
### -field ULONG [4] AsULONG			
 	
### -field SDRESP_TYPE3 Type3			
 	
### -field SDBUS_PROPERTY Property			
 	
### -field PVOID Buffer			
 	
### -field ULONG Length			
 	
### -field SDCMD_DESCRIPTOR CmdDesc			
 	
### -field ULONG Argument			
 	
### -field PMDL Mdl			
 	
### -field ULONG Length			
 	
### -field SDBUS_ERASE_TYPE EraseType			
 	
### -field ULONG StartBlock			
 	
### -field ULONG EndBlock			
 	
### -field ULONG Frequency			
 	
### -field PIRP IrpToHpi			
 	
## -remarks

## -see-also