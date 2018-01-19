---
UID : NS:mpiowmi._SCSI_ADDR
title : _SCSI_ADDR
author : windows-driver-content
description : The SCSI_ADDR structure represents a SCSI address.
old-location : storage\scsi_addr.htm
old-project : storage
ms.assetid : d53e0b05-8761-4b88-a7d5-081244b3dc93
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : _SCSI_ADDR, SCSI_ADDR, *PSCSI_ADDR
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : mpiowmi.h
req.include-header : Mpiowmi.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : SCSI_ADDR
req.alt-loc : mpiowmi.h
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
req.typenames : SCSI_ADDR, *PSCSI_ADDR
---

# _SCSI_ADDR structure
The SCSI_ADDR structure represents a SCSI address.

## Syntax
````
typedef struct _SCSI_ADDR {
  UCHAR PortNumber;
  UCHAR ScsiPathId;
  UCHAR TargetId;
  UCHAR Lun;
} SCSI_ADDR, *PSCSI_ADDR;
````

## Members

        
            `Lun`

            An unsigned 8-bitfield that represents the Lun as defined by the SCSI_ADDRESS structure in <i>Ntddscsi.h</i>.
        
            `PortNumber`

            An unsigned 8-bitfield that represents the PortNumber as defined by the SCSI_ADDRESS structure in <i>Ntddscsi.h</i>.
        
            `ScsiPathId`

            An unsigned 8-bitfield that represents the PathId as defined by the SCSI_ADDRESS structure in <i>Ntddscsi.h</i>.
        
            `TargetId`

            An unsigned 8-bitfield that represents the TargetId as defined by the SCSI_ADDRESS structure in <i>Ntddscsi.h</i>.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | mpiowmi.h (include Mpiowmi.h) |