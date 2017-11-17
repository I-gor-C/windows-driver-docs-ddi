---
UID: NS.ucxendpoint._ENDPOINTS_CONFIGURE
title: ENDPOINTS_CONFIGURE
author: windows-driver-content
description: 
ms.assetid: 3e84a9ca-faf6-47b3-87ef-d92bc3b4ff9e
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: ENDPOINTS_CONFIGURE, ENDPOINTS_CONFIGURE, *PENDPOINTS_CONFIGURE
req.header: ucxendpoint.h
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

# ENDPOINTS_CONFIGURE structure

## -description



## -struct-fields

### -field USBDEVICE_MGMT_HEADER Header			
 	
### -field ULONG EndpointsToEnableCount			
 	
### -field UCXENDPOINT * EndpointsToEnable			
 	
### -field ULONG EndpointsToDisableCount			
 	
### -field UCXENDPOINT * EndpointsToDisable			
 	
### -field ULONG EndpointsEnabledAndUnchangedCount			
 	
### -field UCXENDPOINT * EndpointsEnabledAndUnchanged			
 	
### -field ENDPOINTS_CONFIGURE_FAILURE_FLAGS FailureFlags			
 	
### -field ULONG ExitLatencyDelta			
 	
### -field UCHAR ConfigurationValue			
 	
### -field UCHAR InterfaceNumber			
 	
### -field UCHAR AlternateSetting			
 	
### -field ULONG Reserved1			
 	
### -field PVOID Reserved2			
 	
## -remarks

## -see-also