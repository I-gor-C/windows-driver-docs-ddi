---
UID: NS:ntddstor._STORAGE_PHYSICAL_ADAPTER_DATA
title: "_STORAGE_PHYSICAL_ADAPTER_DATA"
author: windows-driver-content
description: Specifies the physical device data of a storage adapter.
old-location: storage\storage_physical_adapter_data.htm
old-project: storage
ms.assetid: 404A7AFC-291E-4056-9076-F9E62A07C9FB
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PSTORAGE_PHYSICAL_ADAPTER_DATA, PSTORAGE_PHYSICAL_ADAPTER_DATA, PSTORAGE_PHYSICAL_ADAPTER_DATA structure pointer [Storage Devices], STORAGE_PHYSICAL_ADAPTER_DATA, STORAGE_PHYSICAL_ADAPTER_DATA structure [Storage Devices], _STORAGE_PHYSICAL_ADAPTER_DATA, ntddstor/PSTORAGE_PHYSICAL_ADAPTER_DATA, ntddstor/STORAGE_PHYSICAL_ADAPTER_DATA, storage.storage_physical_adapter_data"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Ntddstor.h
api_name:
-	STORAGE_PHYSICAL_ADAPTER_DATA
product: Windows
targetos: Windows
req.typenames: STORAGE_PHYSICAL_ADAPTER_DATA, *PSTORAGE_PHYSICAL_ADAPTER_DATA
---

# _STORAGE_PHYSICAL_ADAPTER_DATA structure
Specifies the physical device data of a storage adapter.

## Syntax
```
typedef struct _STORAGE_PHYSICAL_ADAPTER_DATA {
  ULONG                           AdapterId;
  STORAGE_COMPONENT_HEALTH_STATUS HealthStatus;
  STORAGE_PROTOCOL_TYPE           CommandProtocol;
  STORAGE_SPEC_VERSION            SpecVersion;
  UCHAR                           Vendor[8];
  UCHAR                           Model[40];
  UCHAR                           FirmwareRevision[16];
  UCHAR                           PhysicalLocation[32];
  BOOLEAN                         ExpanderConnected;
  UCHAR                           Reserved0[3];
  ULONG                           Reserved1[3];
} *PSTORAGE_PHYSICAL_ADAPTER_DATA, STORAGE_PHYSICAL_ADAPTER_DATA;
```

## Members


`AdapterId`

The hardware ID of the storage adapter.

`HealthStatus`

Indicates the health status of a storage adapter, of type <a href="https://msdn.microsoft.com/library/windows/hardware/mt653957">STORAGE_COMPONENT_HEALTH_STATUS</a>.

`CommandProtocol`

Specifies the storage command protocols that are used between software and hardware, of type <a href="https://msdn.microsoft.com/library/windows/hardware/dn931818">STORAGE_PROTOCOL_TYPE</a>.

`SpecVersion`

Indicates the specification of the storage adapter, of type <a href="https://msdn.microsoft.com/library/windows/hardware/mt653963">STORAGE_SPEC_VERSION</a>.

`Vendor`



`Model`



`FirmwareRevision`



`PhysicalLocation`



`ExpanderConnected`



`Reserved0`



`Reserved1`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddstor.h (include Ntddstor.h) |