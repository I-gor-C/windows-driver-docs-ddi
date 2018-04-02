---
UID: NS:fltuserstructures._INSTANCE_AGGREGATE_STANDARD_INFORMATION
title: "_INSTANCE_AGGREGATE_STANDARD_INFORMATION"
author: windows-driver-content
description: The caller-allocated INSTANCE_AGGREGATE_STANDARD_INFORMATION structure contains information for either a minifilter driver instance or a legacy filter driver.
old-location: ifsk\instance_aggregate_standard_information.htm
old-project: ifsk
ms.assetid: 35311ee7-d023-4b04-b510-a949ab9a40ca
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PINSTANCE_AGGREGATE_STANDARD_INFORMATION, FltSystemStructures_b1c8bf6f-d693-4f15-ad58-9e31d593464b.xml, INSTANCE_AGGREGATE_STANDARD_INFORMATION, INSTANCE_AGGREGATE_STANDARD_INFORMATION structure [Installable File System Drivers], PINSTANCE_AGGREGATE_STANDARD_INFORMATION, PINSTANCE_AGGREGATE_STANDARD_INFORMATION structure pointer [Installable File System Drivers], SUPPORTED_FS_FEATURES_OFFLOAD_READ, SUPPORTED_FS_FEATURES_OFFLOAD_WRITE, _INSTANCE_AGGREGATE_STANDARD_INFORMATION, fltuserstructures/INSTANCE_AGGREGATE_STANDARD_INFORMATION, fltuserstructures/PINSTANCE_AGGREGATE_STANDARD_INFORMATION, ifsk.instance_aggregate_standard_information"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: fltuserstructures.h
req.include-header: FltUser.h, FltKernel.h
req.target-type: Windows
req.target-min-winverclnt: This structure is available starting with Windows Vista.
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	fltuserstructures.h
api_name:
-	INSTANCE_AGGREGATE_STANDARD_INFORMATION
product: Windows
targetos: Windows
req.typenames: INSTANCE_AGGREGATE_STANDARD_INFORMATION, *PINSTANCE_AGGREGATE_STANDARD_INFORMATION
---

# _INSTANCE_AGGREGATE_STANDARD_INFORMATION structure
The caller-allocated INSTANCE_AGGREGATE_STANDARD_INFORMATION structure contains information for either a minifilter driver instance or a legacy filter driver.

## Syntax
```
typedef struct _INSTANCE_AGGREGATE_STANDARD_INFORMATION {
  ULONG NextEntryOffset;
  ULONG Flags;
  union {
    struct {
      ULONG               Flags;
      ULONG               FrameID;
      FLT_FILESYSTEM_TYPE VolumeFileSystemType;
      USHORT              InstanceNameLength;
      USHORT              InstanceNameBufferOffset;
      USHORT              AltitudeLength;
      USHORT              AltitudeBufferOffset;
      USHORT              VolumeNameLength;
      USHORT              VolumeNameBufferOffset;
      USHORT              FilterNameLength;
      USHORT              FilterNameBufferOffset;
      ULONG               SupportedFeatures;
    } MiniFilter;
    struct {
      ULONG  Flags;
      USHORT AltitudeLength;
      USHORT AltitudeBufferOffset;
      USHORT VolumeNameLength;
      USHORT VolumeNameBufferOffset;
      USHORT FilterNameLength;
      USHORT FilterNameBufferOffset;
      ULONG  SupportedFeatures;
    } LegacyFilter;
  } Type;
} INSTANCE_AGGREGATE_STANDARD_INFORMATION, *PINSTANCE_AGGREGATE_STANDARD_INFORMATION;
```

## Members


`NextEntryOffset`

Byte offset of the next INSTANCE_AGGREGATE_STANDARD_INFORMATION structure if multiple structures are present in a buffer. This member is zero if no other structures follow this one.

`Flags`

Indicates whether the filter driver is a legacy filter driver or a minifilter driver.  This member must contain one of the following flags.

<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
FLTFL_IASI_IS_MINIFILTER

</td>
<td>
The filter driver is a minifilter driver - use the <b>MiniFilter</b> portion of the union.

</td>
</tr>
<tr>
<td>
FLTFL_IASI_IS_LEGACYFILTER

</td>
<td>
The filter driver is a legacy filter driver - use the <b>LegacyFilter</b> portion of the union.

</td>
</tr>
</table>

`Type`



## Remarks
A structure of type INSTANCE_AGGREGATE_STANDARD_INFORMATION can be allocated from paged or nonpaged pool.  This structure is passed as a parameter to routines such as the following:

<ul>
<li>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff540541">FilterInstanceFindFirst</a>


</li>
<li>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff541493">FilterInstanceFindNext</a>


</li>
<li>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff541499">FilterInstanceGetInformation</a>


</li>
<li>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff541541">FilterVolumeInstanceFindFirst</a>


</li>
<li>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff541551">FilterVolumeInstanceFindNext</a>


</li>
<li>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff542071">FltEnumerateInstanceInformationByFilter</a>


</li>
<li>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff542082">FltEnumerateInstanceInformationByVolume</a>


</li>
<li>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff543062">FltGetInstanceInformation</a>


</li>
</ul>
The INSTANCE_AGGREGATE_STANDARD_INFORMATION structure must be aligned on a LONGLONG (8-byte) boundary. If a buffer contains two or more of these structures, the <b>NextEntryOffset</b> value in each entry falls on an 8-byte boundary.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | This structure is available starting with Windows Vista. This structure is available starting with Windows Vista. |
| **Header** | fltuserstructures.h (include FltUser.h, FltKernel.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff540541">FilterInstanceFindFirst</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541493">FilterInstanceFindNext</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541499">FilterInstanceGetInformation</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541541">FilterVolumeInstanceFindFirst</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541551">FilterVolumeInstanceFindNext</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542071">FltEnumerateInstanceInformationByFilter</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542082">FltEnumerateInstanceInformationByVolume</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff543062">FltGetInstanceInformation</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548176">INSTANCE_BASIC_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548185">INSTANCE_FULL_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548190">INSTANCE_PARTIAL_INFORMATION</a>