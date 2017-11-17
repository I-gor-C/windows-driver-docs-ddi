---
UID: NS.mrx._LOWIO_CONTEXT
title: LOWIO_CONTEXT
author: windows-driver-content
description: 
ms.assetid: 485ad0c6-0de8-4a9f-9e29-c88a01d8434a
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: LOWIO_CONTEXT, LOWIO_CONTEXT
req.header: mrx.h
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

# LOWIO_CONTEXT structure

## -description



## -struct-fields

### -field union ParamsFor			
 	
### -field __unnamed_union_0c08_2 __unnamed_union_0c08_2			
 	
### -field USHORT Operation			
 	
### -field USHORT Flags			
 	
### -field PLOWIO_COMPLETION_ROUTINE CompletionRoutine			
 	
### -field PERESOURCE Resource			
 	
### -field ERESOURCE_THREAD ResourceThreadId			
 	
### -field ULONG Flags			
 	
### -field PMDL Buffer			
 	
### -field RXVBO ByteOffset			
 	
### -field ULONG ByteCount			
 	
### -field ULONG Key			
 	
### -field PNON_PAGED_FCB NonPagedFcb			
 	
### -field union __unnamed_union_0c08_5			
 	
### -field ULONG Flags			
 	
### -field RXVBO ByteOffset			
 	
### -field ULONG Key			
 	
### -field PLOWIO_LOCK_LIST LockList			
 	
### -field LONGLONG Length			
 	
### -field BOOLEAN WatchTree			
 	
### -field ULONG CompletionFilter			
 	
### -field ULONG NotificationBufferLength			
 	
### -field PVOID pNotificationBuffer			
 	
### -field XXCTL_LOWIO_COMPONENT FsCtl			
 	
### -field XXCTL_LOWIO_COMPONENT IoCtl			
 	
## -remarks

## -see-also