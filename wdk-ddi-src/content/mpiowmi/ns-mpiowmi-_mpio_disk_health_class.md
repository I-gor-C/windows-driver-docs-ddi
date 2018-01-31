---
UID : NS:mpiowmi._MPIO_DISK_HEALTH_CLASS
title : "_MPIO_DISK_HEALTH_CLASS"
author : windows-driver-content
description : The MPIO_DISK_HEALTH_CLASS structure contains the health information for a multi-path disk.
old-location : storage\mpio_disk_health_class.htm
old-project : storage
ms.assetid : 07b04bad-9d52-4a32-8834-48cd5803844c
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : storage.mpio_disk_health_class, MPIO_DISK_HEALTH_CLASS, mpiowmi/MPIO_DISK_HEALTH_CLASS, PMPIO_DISK_HEALTH_CLASS structure pointer [Storage Devices], PMPIO_DISK_HEALTH_CLASS, *PMPIO_DISK_HEALTH_CLASS, MPIO_DISK_HEALTH_CLASS structure [Storage Devices], structs-scsibus_b3dfb95d-08eb-4eb6-80bb-3437282a65d6.xml, mpiowmi/PMPIO_DISK_HEALTH_CLASS, _MPIO_DISK_HEALTH_CLASS
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
req.typenames : "*PMPIO_DISK_HEALTH_CLASS, MPIO_DISK_HEALTH_CLASS"
---

# _MPIO_DISK_HEALTH_CLASS structure
The MPIO_DISK_HEALTH_CLASS structure contains the health information for a multi-path disk.

## Syntax
````
typedef struct _MPIO_DISK_HEALTH_CLASS {
  WCHAR     Name[63 + 1];
  ULONGLONG NumberReads;
  ULONGLONG NumberWrites;
  ULONGLONG NumberBytesRead;
  ULONGLONG NumberBytesWritten;
  ULONGLONG NumberRetries;
  ULONGLONG NumberIoErrors;
  ULONGLONG CreateTime;
  ULONGLONG PathFailures;
  ULONGLONG FailTime;
  BOOLEAN   DeviceOffline;
  UCHAR     NumberReadsWrap;
  UCHAR     NumberWritesWrap;
  UCHAR     NumberBytesReadWrap;
  UCHAR     NumberBytesWrittenWrap;
  UCHAR     Pad[3];
} MPIO_DISK_HEALTH_CLASS, *PMPIO_DISK_HEALTH_CLASS;
````

## Members


`CreateTime`

A 64-bit integer that specifies the system time when the health packet was created for this multi-path disk.

`DeviceOffline`

A Boolean field that indicates whether the multi-path disk is offline or has failed.

`FailTime`

A 64-bit integer that specifies the system time when this multi-path disk went offline or failed.

`Name`

The name of this multi-path disk.

`NumberBytesRead`

An unsigned 64-bitfield that specifies the total number of bytes that are read from this multi-path disk.

`NumberBytesReadWrap`

An unsigned character field that specifies the total number of times that the <i>NumberBytesRead</i> parameter has rolled around to zero.

`NumberBytesWritten`

An unsigned 64-bitfield that specifies the total number of bytes that are written to this multi-path disk.

`NumberBytesWrittenWrap`

An unsigned character field that specifies the total number of times that the <i>NumberBytesWritten</i> parameter has rolled around to zero.

`NumberIoErrors`

An unsigned 64-bitfield that specifies the total number of I/O errors that are encountered by this multi-path disk.

`NumberReads`

An unsigned 64-bitfield that specifies the number of read requests that are serviced by this multi-path disk.

`NumberReadsWrap`

An unsigned character field that specifies the total number of times that the <i>NumberReads</i> parameter has rolled around to zero.

`NumberRetries`

An unsigned 64-bitfield that specifies the total number of retries for this multi-path disk.

`NumberWrites`

An unsigned 64-bitfield that specifies the number of write requests that are serviced by this multi-path disk.

`NumberWritesWrap`

An unsigned character field that specifies the total number of times the <i>NumberWrites</i> parameter has rolled around to zero.

`Pad`

Should be zero.

`PathFailures`

A 64-bit integer that specifies the total number of path failures for this multi-path disk.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | mpiowmi.h (include Mpiowmi.h) |