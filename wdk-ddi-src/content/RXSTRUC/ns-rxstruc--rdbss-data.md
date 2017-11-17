---
UID: NS.rxstruc._RDBSS_DATA
title: RDBSS_DATA
author: windows-driver-content
description: 
ms.assetid: b26dc450-14c5-4837-9b28-657933c61511
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: RDBSS_DATA, RDBSS_DATA
req.header: rxstruc.h
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

# RDBSS_DATA structure

## -description



## -struct-fields

### -field NODE_TYPE_CODE NodeTypeCode			
 	
### -field NODE_BYTE_SIZE NodeByteSize			
 	
### -field PDRIVER_OBJECT DriverObject			
 	
### -field __volatile LONG NumberOfMinirdrsStarted			
 	
### -field FAST_MUTEX MinirdrRegistrationMutex			
 	
### -field LIST_ENTRY RegisteredMiniRdrs			
 	
### -field LONG NumberOfMinirdrsRegistered			
 	
### -field PEPROCESS OurProcess			
 	
### -field CACHE_MANAGER_CALLBACKS CacheManagerCallbacks			
 	
### -field ERESOURCE Resource			
 	
## -remarks

## -see-also