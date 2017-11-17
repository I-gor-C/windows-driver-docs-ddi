---
UID: NS.mrxfcb._MRX_NET_ROOT_
title: MRX_NET_ROOT_
author: windows-driver-content
description: 
ms.assetid: f5684f81-b9ad-4c2a-9010-19d2ad5bbd73
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: MRX_NET_ROOT_, MRX_NET_ROOT, *PMRX_NET_ROOT
req.header: mrxfcb.h
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

# MRX_NET_ROOT_ structure

## -description



## -struct-fields

### -field union __unnamed_union_0c09_1			
 	
### -field PMRX_SRV_CALL pSrvCall			
 	
### -field PVOID Context			
 	
### -field PVOID Context2			
 	
### -field ULONG Flags			
 	
### -field __volatile ULONG NumberOfFcbs			
 	
### -field __volatile ULONG NumberOfSrvOpens			
 	
### -field MRX_NET_ROOT_STATE MRxNetRootState			
 	
### -field NET_ROOT_TYPE Type			
 	
### -field MRX_PURGE_RELATIONSHIP PurgeRelationship			
 	
### -field MRX_PURGE_SYNCLOCATION PurgeSyncLocation			
 	
### -field DEVICE_TYPE DeviceType			
 	
### -field PUNICODE_STRING pNetRootName			
 	
### -field UNICODE_STRING InnerNamePrefix			
 	
### -field ULONG ParameterValidationStamp			
 	
### -field ULONG DataCollectionSize			
 	
### -field NETROOT_THROTTLING_PARAMETERS PipeReadThrottlingParameters			
 	
### -field ULONG ClusterSize			
 	
### -field ULONG ReadAheadGranularity			
 	
### -field NETROOT_THROTTLING_PARAMETERS LockThrottlingParameters			
 	
### -field ULONG RenameInfoOverallocationSize			
 	
### -field GUID VolumeId			
 	
## -remarks

## -see-also