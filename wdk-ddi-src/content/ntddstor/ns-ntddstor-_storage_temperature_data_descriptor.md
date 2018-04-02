---
UID: NS:ntddstor._STORAGE_TEMPERATURE_DATA_DESCRIPTOR
title: "_STORAGE_TEMPERATURE_DATA_DESCRIPTOR"
author: windows-driver-content
description: This structure is used in conjunction with IOCTL_STORAGE_QUERY_PROPERTY to return temperature data from a storage device or adapter.
old-location: storage\storage_temperature_data_descriptor.htm
old-project: storage
ms.assetid: A6041B10-0296-4A96-B65C-C35B8DCB2B5D
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PSTORAGE_TEMPERATURE_DATA_DESCRIPTOR, PSTORAGE_TEMPERATURE_DATA_DESCRIPTOR, PSTORAGE_TEMPERATURE_DATA_DESCRIPTOR structure pointer [Storage Devices], STORAGE_TEMPERATURE_DATA_DESCRIPTOR, STORAGE_TEMPERATURE_DATA_DESCRIPTOR structure [Storage Devices], _STORAGE_TEMPERATURE_DATA_DESCRIPTOR, ntddstor/PSTORAGE_TEMPERATURE_DATA_DESCRIPTOR, ntddstor/STORAGE_TEMPERATURE_DATA_DESCRIPTOR, storage.storage_temperature_data_descriptor"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
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
-	ntddstor.h
api_name:
-	STORAGE_TEMPERATURE_DATA_DESCRIPTOR
product:
- Windows
targetos: Windows
req.typenames: STORAGE_TEMPERATURE_DATA_DESCRIPTOR, *PSTORAGE_TEMPERATURE_DATA_DESCRIPTOR
---

# _STORAGE_TEMPERATURE_DATA_DESCRIPTOR structure
This structure is used in conjunction with <a href="https://msdn.microsoft.com/library/windows/hardware/ff560590">IOCTL_STORAGE_QUERY_PROPERTY</a> to return temperature data from a storage device or adapter.

## Syntax
```
typedef struct _STORAGE_TEMPERATURE_DATA_DESCRIPTOR {
  ULONG                    Version;
  ULONG                    Size;
  SHORT                    CriticalTemperature;
  SHORT                    WarningTemperature;
  USHORT                   InfoCount;
  UCHAR                    Reserved0[2];
  ULONG                    Reserved1[2];
  STORAGE_TEMPERATURE_INFO TemperatureInfo[ANYSIZE_ARRAY];
} STORAGE_TEMPERATURE_DATA_DESCRIPTOR, *PSTORAGE_TEMPERATURE_DATA_DESCRIPTOR;
```

## Members


`Version`

Contains the size of this structure, in bytes. The value of this member will change as members are added to the structure.

`Size`

Specifies the total size of the data returned, in bytes. This may include data that follows this structure.

`CriticalTemperature`

Indicates the minimum temperature in degrees Celsius that may prevent normal operation. Exceeding this temperature may result in possible data loss, automatic device shutdown, extreme performance throttling, or permanent damage.

`WarningTemperature`

Indicates the maximum temperature in degrees Celsius at which the device is capable of operating continuously without degrading operation or reliability.

`InfoCount`

Specifies the number of <a href="https://msdn.microsoft.com/library/windows/hardware/mt651018">STORAGE_TEMPERATURE_INFO</a> structures reported in <b>TemperatureInfo</b>. More than one set of temperature data may be returned when there are multiple sensors in the drive.

`Reserved0`

Reserved for future use.

`Reserved1`

Reserved for future use.

`TemperatureInfo`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | ntddstor.h (include Ntddstor.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff560590">IOCTL_STORAGE_QUERY_PROPERTY</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff566996">STORAGE_PROPERTY_ID</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff566997">STORAGE_PROPERTY_QUERY</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt651018">STORAGE_TEMPERATURE_INFO</a>