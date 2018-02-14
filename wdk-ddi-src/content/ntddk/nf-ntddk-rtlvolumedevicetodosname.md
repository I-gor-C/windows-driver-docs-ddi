---
UID: NF:ntddk.RtlVolumeDeviceToDosName
title: RtlVolumeDeviceToDosName function
author: windows-driver-content
description: The RtlVolumeDeviceToDosName routine is obsolete for Windows XP and later versions of Windows. Use IoVolumeDeviceToDosName instead.RtlVolumeDeviceToDosName returns the MS-DOS path for a specified device object that represents a file system volume.
old-location: kernel\rtlvolumedevicetodosname.htm
old-project: kernel
ms.assetid: e25db70f-04bf-4fb1-8ff5-2beb4c825797
ms.author: windowsdriverdev
ms.date: 1/4/2018
ms.keywords: RtlVolumeDeviceToDosName routine [Kernel-Mode Driver Architecture], RtlVolumeDeviceToDosName, k109_a95aea8c-1156-4852-b4eb-38d2f141fcca.xml, kernel.rtlvolumedevicetodosname, ntddk/RtlVolumeDeviceToDosName
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Obsolete for Microsoft Windows XP and later versions of Windows. Use IoVolumeDeviceToDosName instead.
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
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	DllExport
apilocation:
-	NtosKrnl.exe
apiname:
-	RtlVolumeDeviceToDosName
product: Windows
targetos: Windows
req.typenames: "*PWHEA_RAW_DATA_FORMAT, WHEA_RAW_DATA_FORMAT"
---


# RtlVolumeDeviceToDosName function
The <b>RtlVolumeDeviceToDosName</b> routine is <u>obsolete</u> for Windows XP and later versions of Windows. Use <a href="..\ntddk\nf-ntddk-iovolumedevicetodosname.md">IoVolumeDeviceToDosName</a> instead.

<b>RtlVolumeDeviceToDosName</b> returns the MS-DOS path for a specified device object that represents a file system volume.

## Syntax

````
NTSTATUS RtlVolumeDeviceToDosName(
  _In_  PVOID           VolumeDeviceObject,
  _Out_ PUNICODE_STRING DosName
);
````

## Parameters

`VolumeDeviceObject`

Pointer to a device object that represents a volume device object created by a storage class driver.

`DosName`

Pointer to a Unicode string containing the MS-DOS path of the volume device object specified by <i>VolumeDeviceObject</i>.


## Return Value

<b>RtlVolumeDeviceToDosName</b> returns STATUS_SUCCESS or an appropriate error status.

## Remarks

The behavior of this routine is identical to that of <a href="..\ntddk\nf-ntddk-iovolumedevicetodosname.md">IoVolumeDeviceToDosName</a>. For more information about how to use this routine, see <b>IoVolumeDeviceToDosName</b>.

Drivers that must work on older NT-based operating systems may use this routine. Drivers written for Windows XP and later must use <b>IoVolumeDeviceToDosName</b> instead.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Obsolete for Microsoft Windows XP and later versions of Windows. Use IoVolumeDeviceToDosName instead. Obsolete for Microsoft Windows XP and later versions of Windows. Use IoVolumeDeviceToDosName instead. |
| **Target Platform** | Universal |
| **Header** | ntddk.h (include Ntddk.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |