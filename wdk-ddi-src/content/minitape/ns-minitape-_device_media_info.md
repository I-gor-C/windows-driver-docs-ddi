---
UID: NS:minitape._DEVICE_MEDIA_INFO
title: "_DEVICE_MEDIA_INFO"
author: windows-driver-content
description: A storage class driver returns an array of DEVICE_MEDIA_INFO structures, embedded in a GET_MEDIA_TYPES structure, in response to an IOCTL_STORAGE_GET_MEDIA_TYPES_EX device-control request.
old-location: storage\device_media_info.htm
old-project: storage
ms.assetid: 87906511-7bcb-4f4d-9383-44b0501536e3
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PDEVICE_MEDIA_INFO, DEVICE_MEDIA_INFO, DEVICE_MEDIA_INFO structure [Storage Devices], MEDIA_CURRENTLY_MOUNTED, MEDIA_ERASEABLE, MEDIA_READ_ONLY, MEDIA_READ_WRITE, MEDIA_WRITE_ONCE, MEDIA_WRITE_PROTECTED, PDEVICE_MEDIA_INFO, PDEVICE_MEDIA_INFO structure pointer [Storage Devices], _DEVICE_MEDIA_INFO, ntddstor/DEVICE_MEDIA_INFO, ntddstor/PDEVICE_MEDIA_INFO, storage.device_media_info, structs-general_e2c363ff-f053-45be-a807-f90480c0ae1f.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: minitape.h
req.include-header: Ntddstor.h, Minitape.h
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
-	ntddstor.h
api_name:
-	DEVICE_MEDIA_INFO
product: Windows
targetos: Windows
req.typenames: DEVICE_MEDIA_INFO, *PDEVICE_MEDIA_INFO
---

# _DEVICE_MEDIA_INFO structure
A storage class driver returns an array of <b>DEVICE_MEDIA_INFO</b> structures, embedded in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff554987">GET_MEDIA_TYPES</a> structure, in response to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff560563">IOCTL_STORAGE_GET_MEDIA_TYPES_EX</a> device-control request.

## Syntax
```
typedef struct _DEVICE_MEDIA_INFO {
  union {
    struct {
      LARGE_INTEGER      Cylinders;
      STORAGE_MEDIA_TYPE MediaType;
      ULONG              TracksPerCylinder;
      ULONG              SectorsPerTrack;
      ULONG              BytesPerSector;
      ULONG              NumberMediaSides;
      ULONG              MediaCharacteristics;
    } DiskInfo;
    struct {
      LARGE_INTEGER      Cylinders;
      STORAGE_MEDIA_TYPE MediaType;
      ULONG              TracksPerCylinder;
      ULONG              SectorsPerTrack;
      ULONG              BytesPerSector;
      ULONG              NumberMediaSides;
      ULONG              MediaCharacteristics;
    } RemovableDiskInfo;
    struct {
      STORAGE_MEDIA_TYPE MediaType;
      ULONG              MediaCharacteristics;
      ULONG              CurrentBlockSize;
      STORAGE_BUS_TYPE   BusType;
      union {
        struct {
          UCHAR MediumType;
          UCHAR DensityCode;
        } ScsiInformation;
      } BusSpecificData;
    } TapeInfo;
  } DeviceSpecific;
} *PDEVICE_MEDIA_INFO, DEVICE_MEDIA_INFO;
```

## Members


`DeviceSpecific`



## Remarks
This structure is used by a storage driver to indicate the types of media supported by a device and which type is currently mounted, if any. A driver must provide this information if it might control drives in a media library or changer or if its device might be accessed by the Removable Storage Manager (RSM). 

The driver fills in an array of <b>DEVICE_MEDIA_INFO</b> structures, one for each medium type supported by the device, embedded in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff554987">GET_MEDIA_TYPES</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | minitape.h (include Ntddstor.h, Minitape.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff566992">STORAGE_MEDIA_TYPE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff567939">TapeMiniGetMediaTypes</a>