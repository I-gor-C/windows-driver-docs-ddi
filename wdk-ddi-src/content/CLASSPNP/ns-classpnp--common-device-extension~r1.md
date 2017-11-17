---
UID: NS.classpnp._COMMON_DEVICE_EXTENSION~r1
title: COMMON_DEVICE_EXTENSION
author: windows-driver-content
description: 
ms.assetid: ed3b51c8-c39a-4dab-8e4c-8b3147d1d779
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: COMMON_DEVICE_EXTENSION, COMMON_DEVICE_EXTENSION, *PCOMMON_DEVICE_EXTENSION
req.header: classpnp.h
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

# COMMON_DEVICE_EXTENSION structure

## -description



## -struct-fields

### -field struct __unnamed_struct_0b7c_3			
 	
### -field ULONG Version			
 	
### -field PDEVICE_OBJECT DeviceObject			
 	
### -field PDEVICE_OBJECT LowerDeviceObject			
 	
### -field PFUNCTIONAL_DEVICE_EXTENSION PartitionZeroExtension			
 	
### -field PCLASS_DRIVER_EXTENSION DriverExtension			
 	
### -field LONG RemoveLock			
 	
### -field KEVENT RemoveEvent			
 	
### -field KSPIN_LOCK RemoveTrackingSpinlock			
 	
### -field PVOID RemoveTrackingList			
 	
### -field LONG RemoveTrackingUntrackedCount			
 	
### -field PVOID DriverData			
 	
### -field UCHAR PreviousState			
 	
### -field UCHAR CurrentState			
 	
### -field ULONG IsRemoved			
 	
### -field UNICODE_STRING DeviceName			
 	
### -field PPHYSICAL_DEVICE_EXTENSION ChildList			
 	
### -field ULONG PartitionNumber			
 	
### -field LARGE_INTEGER PartitionLength			
 	
### -field LARGE_INTEGER StartingOffset			
 	
### -field PCLASS_DEV_INFO DevInfo			
 	
### -field ULONG PagingPathCount			
 	
### -field ULONG DumpPathCount			
 	
### -field ULONG HibernationPathCount			
 	
### -field KEVENT PathCountEvent			
 	
### -field NPAGED_LOOKASIDE_LIST SrbLookasideList			
 	
### -field UNICODE_STRING MountedDeviceInterfaceName			
 	
### -field ULONG GuidCount			
 	
### -field PGUIDREGINFO GuidRegInfo			
 	
### -field DICTIONARY FileObjectDictionary			
 	
### -field PCLASS_PRIVATE_COMMON_DATA PrivateCommonData			
 	
### -field ULONG_PTR Reserved1			
 	
### -field PDRIVER_DISPATCH * DispatchTable			
 	
### -field ULONG_PTR Reserved2			
 	
### -field ULONG_PTR Reserved3			
 	
### -field ULONG_PTR Reserved4			
 	
## -remarks

## -see-also