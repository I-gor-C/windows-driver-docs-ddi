---
UID : NS:mpiodisk._MPIO_DSM_Path_V2
title : _MPIO_DSM_Path_V2
author : windows-driver-content
description : The MPIO_DSM_Path_V2 structure is used to represent the DSM's definition of a path. It is a superset of the previously existing MPIO_DSM_Path class.
old-location : storage\mpio_dsm_path_v2.htm
old-project : storage
ms.assetid : 8ebbb4c0-c761-42a5-a41a-9d661a6126d9
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : MPIO_DSM_Path_V2 structure [Storage Devices], *PMPIO_DSM_Path_V2, structs-scsibus_e1d340a8-aa6a-4219-8bd4-c11fc3520f5d.xml, mpiodisk/MPIO_DSM_Path_V2, _MPIO_DSM_Path_V2, MPIO_DSM_Path_V2, PMPIO_DSM_Path_V2 structure pointer [Storage Devices], mpiodisk/PMPIO_DSM_Path_V2, PMPIO_DSM_Path_V2, storage.mpio_dsm_path_v2
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : mpiodisk.h
req.include-header : Mpiowmi.h
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
req.typenames : "*PMPIO_DSM_Path_V2, MPIO_DSM_Path_V2"
---

# _MPIO_DSM_Path_V2 structure
The MPIO_DSM_Path_V2 structure is used to represent the DSM's definition of a path. It is a superset of the previously existing MPIO_DSM_Path class.

## Syntax
````
typedef struct _MPIO_DSM_Path_V2 {
  ULONGLONG DsmPathId;
  ULONGLONG Reserved;
  ULONG     PathWeight;
  ULONG     PrimaryPath;
  ULONG     OptimizedPath;
  ULONG     PreferredPath;
  ULONG     FailedPath;
  ULONG     TargetPortGroup_State;
  ULONG     ALUASupport;
  UCHAR     SymmetricLUA;
  UCHAR     TargetPortGroup_Preferred;
  USHORT    TargetPortGroup_Identifier;
  ULONG     TargetPort_Identifier;
  ULONG     Reserved32;
  ULONGLONG Reserved64;
} MPIO_DSM_Path_V2, *PMPIO_DSM_Path_V2;
````

## Members


`ALUASupport`

An unsigned 32-bitfield that returns the Asymmetrical Logical Unit Access (ALUA) state transition support that is indicated by the LUN.

`DsmPathId`

An unsigned 64-bitfield that is used as a unique identifier to distinguish paths known to the DSM.

`FailedPath`

A 32-bit unsigned field that is used as a flag to indicate if the path has failed.

`OptimizedPath`

An unsigned 32-bitfield that is used in conjunction with <i>PrimaryPath</i> to indicate the path state for accessing a LUN.

`PathWeight`

An unsigned 32-bitfield that holds the weight associated with the given path.

`PreferredPath`

An unsigned 32-bitfield that is used as a flag to indicate whether this is the preferred path for accessing the LUN.

`PrimaryPath`

An unsigned 32-bitfield that is used as a flag to indicate the path state when accessing a particular LUN.

`Reserved`

Should be zero.

`Reserved32`

Should be zero.

`Reserved64`

Should be zero.

`SymmetricLUA`

An unsigned 8-bitfield that is used as a flag to indicate to the application if logical unit access is symmetric.

`TargetPort_Identifier`

An unsigned 32-bitfield that contains the identifier of the target port that corresponds to this path through which the LUN has been exposed.

`TargetPortGroup_Identifier`

An unsigned 16-bitfield that contains the identifier of the LUN's target port group that corresponds to this path.

`TargetPortGroup_Preferred`

An unsigned 8-bitfield that is used as a flag. This field indicates if the LUN's target port group that corresponds to this path is preferred for the LUN access.

`TargetPortGroup_State`

An unsigned 32-bitfield that is used to indicate the access state of the target port group to which this instance of the LUN belongs.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | mpiodisk.h (include Mpiowmi.h) |