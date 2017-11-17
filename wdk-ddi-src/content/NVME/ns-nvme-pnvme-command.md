---
UID: NS.nvme.PNVME_COMMAND
title: PNVME_COMMAND
author: windows-driver-content
description: 
ms.assetid: c2e7c9c0-5653-4179-b21d-e34df7683c65
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: PNVME_COMMAND, NVME_COMMAND, *PNVME_COMMAND
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

# PNVME_COMMAND structure

## -description



## -struct-fields

### -field union u			
 	
### -field __unnamed_union_0b31_217 __unnamed_union_0b31_217			
 	
### -field NVME_COMMAND_DWORD0 CDW0			
 	
### -field ULONG NSID			
 	
### -field ULONG [2] Reserved0			
 	
### -field ULONGLONG MPTR			
 	
### -field ULONGLONG PRP1			
 	
### -field ULONGLONG PRP2			
 	
### -field ULONG CDW10			
 	
### -field ULONG CDW11			
 	
### -field ULONG CDW12			
 	
### -field ULONG CDW13			
 	
### -field ULONG CDW14			
 	
### -field ULONG CDW15			
 	
### -field NVME_CDW10_IDENTIFY CDW10			
 	
### -field ULONG CDW11			
 	
### -field ULONG CDW12			
 	
### -field ULONG CDW13			
 	
### -field ULONG CDW14			
 	
### -field ULONG CDW15			
 	
### -field NVME_CDW10_GET_FEATURES CDW10			
 	
### -field NVME_CDW11_FEATURES CDW11			
 	
### -field ULONG CDW12			
 	
### -field ULONG CDW13			
 	
### -field ULONG CDW14			
 	
### -field ULONG CDW15			
 	
### -field NVME_CDW10_SET_FEATURES CDW10			
 	
### -field NVME_CDW11_FEATURES CDW11			
 	
### -field NVME_CDW12_FEATURES CDW12			
 	
### -field NVME_CDW13_FEATURES CDW13			
 	
### -field NVME_CDW14_FEATURES CDW14			
 	
### -field NVME_CDW15_FEATURES CDW15			
 	
### -field NVME_CDW10_GET_LOG_PAGE CDW10			
 	
### -field ULONG CDW11			
 	
### -field ULONG CDW12			
 	
### -field ULONG CDW13			
 	
### -field ULONG CDW14			
 	
### -field ULONG CDW15			
 	
### -field NVME_CDW10_CREATE_IO_QUEUE CDW10			
 	
### -field NVME_CDW11_CREATE_IO_CQ CDW11			
 	
### -field ULONG CDW12			
 	
### -field ULONG CDW13			
 	
### -field ULONG CDW14			
 	
### -field ULONG CDW15			
 	
### -field NVME_CDW10_CREATE_IO_QUEUE CDW10			
 	
### -field NVME_CDW11_CREATE_IO_SQ CDW11			
 	
### -field ULONG CDW12			
 	
### -field ULONG CDW13			
 	
### -field ULONG CDW14			
 	
### -field ULONG CDW15			
 	
### -field NVME_CDW10_DATASET_MANAGEMENT CDW10			
 	
### -field NVME_CDW11_DATASET_MANAGEMENT CDW11			
 	
### -field ULONG CDW12			
 	
### -field ULONG CDW13			
 	
### -field ULONG CDW14			
 	
### -field ULONG CDW15			
 	
### -field NVME_CDW10_SECURITY_SEND_RECEIVE CDW10			
 	
### -field NVME_CDW11_SECURITY_SEND CDW11			
 	
### -field ULONG CDW12			
 	
### -field ULONG CDW13			
 	
### -field ULONG CDW14			
 	
### -field ULONG CDW15			
 	
### -field NVME_CDW10_SECURITY_SEND_RECEIVE CDW10			
 	
### -field NVME_CDW11_SECURITY_RECEIVE CDW11			
 	
### -field ULONG CDW12			
 	
### -field ULONG CDW13			
 	
### -field ULONG CDW14			
 	
### -field ULONG CDW15			
 	
### -field NVME_CDW10_FIRMWARE_DOWNLOAD CDW10			
 	
### -field NVME_CDW11_FIRMWARE_DOWNLOAD CDW11			
 	
### -field ULONG CDW12			
 	
### -field ULONG CDW13			
 	
### -field ULONG CDW14			
 	
### -field ULONG CDW15			
 	
### -field NVME_CDW10_FIRMWARE_ACTIVATE CDW10			
 	
### -field ULONG CDW11			
 	
### -field ULONG CDW12			
 	
### -field ULONG CDW13			
 	
### -field ULONG CDW14			
 	
### -field ULONG CDW15			
 	
### -field NVME_CDW10_FORMAT_NVM CDW10			
 	
### -field ULONG CDW11			
 	
### -field ULONG CDW12			
 	
### -field ULONG CDW13			
 	
### -field ULONG CDW14			
 	
### -field ULONG CDW15			
 	
### -field NVME_CDW10_DIRECTIVE_RECEIVE CDW10			
 	
### -field NVME_CDW11_DIRECTIVE_RECEIVE CDW11			
 	
### -field NVME_CDW12_DIRECTIVE_RECEIVE CDW12			
 	
### -field ULONG CDW13			
 	
### -field ULONG CDW14			
 	
### -field ULONG CDW15			
 	
### -field NVME_CDW10_DIRECTIVE_SEND CDW10			
 	
### -field NVME_CDW11_DIRECTIVE_SEND CDW11			
 	
### -field NVME_CDW12_DIRECTIVE_SEND CDW12			
 	
### -field ULONG CDW13			
 	
### -field ULONG CDW14			
 	
### -field ULONG CDW15			
 	
### -field ULONG LBALOW			
 	
### -field ULONG LBAHIGH			
 	
### -field NVME_CDW12_READ_WRITE CDW12			
 	
### -field NVME_CDW13_READ_WRITE CDW13			
 	
### -field ULONG CDW14			
 	
### -field NVME_CDW15_READ_WRITE CDW15			
 	
## -remarks

## -see-also