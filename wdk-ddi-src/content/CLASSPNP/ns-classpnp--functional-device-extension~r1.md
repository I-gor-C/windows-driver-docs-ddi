---
UID: NS.classpnp._FUNCTIONAL_DEVICE_EXTENSION~r1
title: FUNCTIONAL_DEVICE_EXTENSION
author: windows-driver-content
description: 
ms.assetid: a5d8263c-7ea0-4b12-81a3-4adb4961430d
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: FUNCTIONAL_DEVICE_EXTENSION, FUNCTIONAL_DEVICE_EXTENSION, *PFUNCTIONAL_DEVICE_EXTENSION
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

# FUNCTIONAL_DEVICE_EXTENSION structure

## -description



## -struct-fields

### -field union __unnamed_union_0b7c_14			
 	
### -field PDEVICE_OBJECT LowerPdo			
 	
### -field PSTORAGE_DEVICE_DESCRIPTOR DeviceDescriptor			
 	
### -field PSTORAGE_ADAPTER_DESCRIPTOR AdapterDescriptor			
 	
### -field DEVICE_POWER_STATE DevicePowerState			
 	
### -field ULONG DMByteSkew			
 	
### -field ULONG DMSkew			
 	
### -field BOOLEAN DMActive			
 	
### -field UCHAR SenseDataLength			
 	
### -field UCHAR Reserved			
 	
### -field UCHAR [2] Reserved0			
 	
### -field DISK_GEOMETRY DiskGeometry			
 	
### -field PSENSE_DATA SenseData			
 	
### -field ULONG TimeOutValue			
 	
### -field ULONG DeviceNumber			
 	
### -field ULONG SrbFlags			
 	
### -field ULONG ErrorCount			
 	
### -field LONG LockCount			
 	
### -field LONG ProtectedLockCount			
 	
### -field LONG InternalLockCount			
 	
### -field KEVENT EjectSynchronizationEvent			
 	
### -field USHORT DeviceFlags			
 	
### -field UCHAR SectorShift			
 	
### -field UCHAR CdbForceUnitAccess			
 	
### -field UCHAR ReservedByte			
 	
### -field PMEDIA_CHANGE_DETECTION_INFO MediaChangeDetectionInfo			
 	
### -field PKEVENT Unused1			
 	
### -field HANDLE Unused2			
 	
### -field FILE_OBJECT_EXTENSION KernelModeMcnContext			
 	
### -field ULONG MediaChangeCount			
 	
### -field HANDLE DeviceDirectory			
 	
### -field KSPIN_LOCK ReleaseQueueSpinLock			
 	
### -field PIRP ReleaseQueueIrp			
 	
### -field SCSI_REQUEST_BLOCK ReleaseQueueSrb			
 	
### -field BOOLEAN ReleaseQueueNeeded			
 	
### -field BOOLEAN ReleaseQueueInProgress			
 	
### -field BOOLEAN ReleaseQueueIrpFromPool			
 	
### -field BOOLEAN FailurePredicted			
 	
### -field ULONG FailureReason			
 	
### -field PFAILURE_PREDICTION_INFO FailurePredictionInfo			
 	
### -field BOOLEAN PowerDownInProgress			
 	
### -field ULONG EnumerationInterlock			
 	
### -field KEVENT ChildLock			
 	
### -field PKTHREAD ChildLockOwner			
 	
### -field ULONG ChildLockAcquisitionCount			
 	
### -field ULONG ScanForSpecialFlags			
 	
### -field KDPC PowerRetryDpc			
 	
### -field KTIMER PowerRetryTimer			
 	
### -field CLASS_POWER_CONTEXT PowerContext			
 	
### -field ULONG_PTR Reserved1			
 	
### -field ULONG_PTR Reserved2			
 	
### -field ULONG_PTR Reserved3			
 	
### -field ULONG_PTR Reserved4			
 	
### -field ULONG CompletionSuccessCount			
 	
### -field ULONG SavedSrbFlags			
 	
### -field ULONG SavedErrorCount			
 	
### -field ULONG_PTR Reserved1			
 	
### -field PCLASS_PRIVATE_FDO_DATA PrivateFdoData			
 	
### -field PCLASS_FUNCTION_SUPPORT_INFO FunctionSupportInfo			
 	
### -field PSTORAGE_MINIPORT_DESCRIPTOR MiniportDescriptor			
 	
### -field ULONG_PTR Reserved2			
 	
### -field ULONG_PTR Reserved3			
 	
### -field PADDITIONAL_FDO_DATA AdditionalFdoData			
 	
### -field ULONG_PTR Reserved4			
 	
### -field ULONG Version			
 	
### -field PDEVICE_OBJECT DeviceObject			
 	
### -field COMMON_DEVICE_EXTENSION CommonExtension			
 	
## -remarks

## -see-also