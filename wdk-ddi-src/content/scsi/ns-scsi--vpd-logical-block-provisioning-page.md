---
UID: NS.scsi._VPD_LOGICAL_BLOCK_PROVISIONING_PAGE
title: VPD_LOGICAL_BLOCK_PROVISIONING_PAGE
author: windows-driver-content
description: 
ms.assetid: 6a95c04f-30b2-4ddb-8246-13a74269f797
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: VPD_LOGICAL_BLOCK_PROVISIONING_PAGE, VPD_LOGICAL_BLOCK_PROVISIONING_PAGE, *PVPD_LOGICAL_BLOCK_PROVISIONING_PAGE
req.header: scsi.h
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

# VPD_LOGICAL_BLOCK_PROVISIONING_PAGE structure

## -description



## -struct-fields

### -field UCHAR  : 5 DeviceType			
 	
### -field UCHAR  : 3 DeviceTypeQualifier			
 	
### -field UCHAR PageCode			
 	
### -field UCHAR [2] PageLength			
 	
### -field UCHAR ThresholdExponent			
 	
### -field UCHAR  : 1 DP			
 	
### -field UCHAR  : 1 ANC_SUP			
 	
### -field UCHAR  : 1 LBPRZ			
 	
### -field UCHAR  : 2 Reserved0			
 	
### -field UCHAR  : 1 LBPWS10			
 	
### -field UCHAR  : 1 LBPWS			
 	
### -field UCHAR  : 1 LBPU			
 	
### -field UCHAR  : 3 ProvisioningType			
 	
### -field UCHAR  : 5 Reserved1			
 	
### -field UCHAR Reserved2			
 	
### -field UCHAR [0] ProvisioningGroupDescr			
 	
## -remarks

## -see-also