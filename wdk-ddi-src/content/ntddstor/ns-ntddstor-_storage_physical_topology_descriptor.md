---
UID : NS:ntddstor._STORAGE_PHYSICAL_TOPOLOGY_DESCRIPTOR
title : _STORAGE_PHYSICAL_TOPOLOGY_DESCRIPTOR
author : windows-driver-content
description : Describes the physical topology of storage in a system.
old-location : storage\storage_physical_topology_descriptor.htm
old-project : storage
ms.assetid : FD5714DF-9D34-4396-86BC-40054C199A0E
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : STORAGE_PHYSICAL_TOPOLOGY_DESCRIPTOR structure [Storage Devices], STORAGE_PHYSICAL_TOPOLOGY_DESCRIPTOR, ntddstor/PSTORAGE_PHYSICAL_TOPOLOGY_DESCRIPTOR, _STORAGE_PHYSICAL_TOPOLOGY_DESCRIPTOR, PSTORAGE_PHYSICAL_TOPOLOGY_DESCRIPTOR, storage.storage_physical_topology_descriptor, *PSTORAGE_PHYSICAL_TOPOLOGY_DESCRIPTOR, PSTORAGE_PHYSICAL_TOPOLOGY_DESCRIPTOR structure pointer [Storage Devices], ntddstor/STORAGE_PHYSICAL_TOPOLOGY_DESCRIPTOR
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntddstor.h
req.include-header : Ntddstor.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : STORAGE_PHYSICAL_TOPOLOGY_DESCRIPTOR, *PSTORAGE_PHYSICAL_TOPOLOGY_DESCRIPTOR
---

# _STORAGE_PHYSICAL_TOPOLOGY_DESCRIPTOR structure
Describes the physical topology of storage in a system.

## Syntax
````
typedef struct _STORAGE_PHYSICAL_TOPOLOGY_DESCRIPTOR {
  ULONG                      Version;
  ULONG                      Size;
  ULONG                      NodeCount;
  ULONG                      Reserved;
  STORAGE_PHYSICAL_NODE_DATA Node[ANYSIZE_ARRAY];
} STORAGE_PHYSICAL_TOPOLOGY_DESCRIPTOR, *PSTORAGE_PHYSICAL_TOPOLOGY_DESCRIPTOR;
````

## Members


`Node`



`NodeCount`

The total number of storage nodes in the system.

`Reserved`

Indicates if storage in the system is reserved.

`Size`

The total size of data in the system.

`Version`

The version of the physical topology.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddstor.h (include Ntddstor.h) |