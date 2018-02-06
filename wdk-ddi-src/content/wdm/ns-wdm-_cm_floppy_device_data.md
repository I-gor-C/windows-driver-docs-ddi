---
UID: NS:wdm._CM_FLOPPY_DEVICE_DATA
title: "_CM_FLOPPY_DEVICE_DATA"
author: windows-driver-content
description: The CM_FLOPPY_DEVICE_DATA structure defines a device-type-specific data record that is stored in the \\Registry\Machine\Hardware\Description tree for a floppy controller if the system can collect this information during the boot process.
old-location: kernel\cm_floppy_device_data.htm
old-project: kernel
ms.assetid: 0ef0d242-4ed6-4c48-85b8-0fc87d3fe39b
ms.author: windowsdriverdev
ms.date: 1/4/2018
ms.keywords: "*PCM_FLOPPY_DEVICE_DATA, kernel.cm_floppy_device_data, _CM_FLOPPY_DEVICE_DATA, wdm/CM_FLOPPY_DEVICE_DATA, wdm/PCM_FLOPPY_DEVICE_DATA, kstruct_a_7ec8badb-4d88-479e-b0dc-ce88660b8449.xml, CM_FLOPPY_DEVICE_DATA structure [Kernel-Mode Driver Architecture], PCM_FLOPPY_DEVICE_DATA structure pointer [Kernel-Mode Driver Architecture], CM_FLOPPY_DEVICE_DATA, PCM_FLOPPY_DEVICE_DATA"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
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
req.irql: PASSIVE_LEVEL (see Remarks section)
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	wdm.h
apiname:
-	CM_FLOPPY_DEVICE_DATA
product: Windows
targetos: Windows
req.typenames: "*PCM_FLOPPY_DEVICE_DATA, CM_FLOPPY_DEVICE_DATA"
req.product: Windows 10 or later.
---

# _CM_FLOPPY_DEVICE_DATA structure
The <b>CM_FLOPPY_DEVICE_DATA</b> structure defines a device-type-specific data record that is stored in the \\Registry\Machine\Hardware\Description tree for a floppy controller if the system can collect this information during the boot process.

## Syntax
````
typedef struct _CM_FLOPPY_DEVICE_DATA {
  USHORT Version;
  USHORT Revision;
  CHAR   Size[8];
  ULONG  MaxDensity;
  ULONG  MountDensity;
  UCHAR  StepRateHeadUnloadTime;
  UCHAR  HeadLoadTime;
  UCHAR  MotorOffTime;
  UCHAR  SectorLengthCode;
  UCHAR  SectorPerTrack;
  UCHAR  ReadWriteGapLength;
  UCHAR  DataTransferLength;
  UCHAR  FormatGapLength;
  UCHAR  FormatFillCharacter;
  UCHAR  HeadSettleTime;
  UCHAR  MotorSettleTime;
  UCHAR  MaximumTrackValue;
  UCHAR  DataTransferRate;
} CM_FLOPPY_DEVICE_DATA, *PCM_FLOPPY_DEVICE_DATA;
````

## Members


`DataTransferLength`

The data transfer length, in bytes, not including the synchronization field.

`DataTransferRate`

The value written to the Datarate register before accessing the media.

`FormatFillCharacter`

The format fill character.

`FormatGapLength`

The format gap length, in bytes.

`HeadLoadTime`

The head load time in milliseconds.

`HeadSettleTime`

The head settle time in milliseconds.

`MaxDensity`

The maximum density.

`MaximumTrackValue`

The maximum track number on the media. Track numbers are zero-based values.

`MotorOffTime`

The motor off time in seconds.

`MotorSettleTime`

The motor settle time in milliseconds.

`MountDensity`

The mount density.

`ReadWriteGapLength`

The read/write gap length, in bytes.

`Revision`

The revision of this structure.

`SectorLengthCode`

Indicates the sector size as an exponent in the formula ((2**<i>code</i>) * 128).

`SectorPerTrack`

The number of sectors per track.

`Size`

The floppy disk density size.

`StepRateHeadUnloadTime`

The step rate head unload time in milliseconds.

`Version`

The version number of this structure.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff549616">IoReportResourceUsage</a>

<a href="..\wdm\ns-wdm-_cm_partial_resource_descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff549453">IoQueryDeviceDescription</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20CM_FLOPPY_DEVICE_DATA structure%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>