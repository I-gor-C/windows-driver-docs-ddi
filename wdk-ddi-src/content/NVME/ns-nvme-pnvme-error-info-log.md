---
UID: NS.nvme.PNVME_ERROR_INFO_LOG
title: PNVME_ERROR_INFO_LOG
author: windows-driver-content
description: 
ms.assetid: 18980f00-c02d-42aa-8551-cdd2f1ea2509
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: PNVME_ERROR_INFO_LOG, NVME_ERROR_INFO_LOG, *PNVME_ERROR_INFO_LOG
req.header: nvme.h
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

# PNVME_ERROR_INFO_LOG structure

## -description



## -struct-fields

### -field struct ParameterErrorLocation			
 	
### -field __unnamed_struct_0b31_143 __unnamed_struct_0b31_143			
 	
### -field ULONGLONG ErrorCount			
 	
### -field USHORT SQID			
 	
### -field USHORT CMDID			
 	
### -field NVME_COMMAND_STATUS Status			
 	
### -field ULONGLONG Lba			
 	
### -field ULONG NameSpace			
 	
### -field UCHAR VendorInfoAvailable			
 	
### -field UCHAR [3] Reserved0			
 	
### -field ULONGLONG CommandSpecificInfo			
 	
### -field UCHAR [24] Reserved1			
 	
## -remarks

## -see-also