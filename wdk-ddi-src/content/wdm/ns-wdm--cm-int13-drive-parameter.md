---
UID: NS.wdm._CM_INT13_DRIVE_PARAMETER
title: CM_INT13_DRIVE_PARAMETER
author: windows-driver-content
description: The CM_INT13_DRIVE_PARAMETER structure defines a device-type-specific data record that is stored in the \\Registry\Machine\Hardware\Description tree for a disk controller if the system can collect this information during the boot process.
old-location: kernel\cm_int13_drive_parameter.htm
old-project: kernel
ms.assetid: eee1070f-c821-42bd-a0c9-d429fac6305b
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: CM_INT13_DRIVE_PARAMETER, CM_INT13_DRIVE_PARAMETER, *PCM_INT13_DRIVE_PARAMETER
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
req.alt-api: CM_INT13_DRIVE_PARAMETER
req.alt-loc: wdm.h
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
req.iface: 
req.product: Windows 10 or later.
---

# CM_INT13_DRIVE_PARAMETER structure



## -description
<p>The <b>CM_INT13_DRIVE_PARAMETER</b> structure defines a device-type-specific data record that is stored in the \\Registry\Machine\Hardware\Description tree for a disk controller if the system can collect this information during the boot process.</p>


## -syntax

````
typedef struct _CM_INT13_DRIVE_PARAMETER {
  USHORT DriveSelect;
  ULONG  MaxCylinders;
  USHORT SectorsPerTrack;
  USHORT MaxHeads;
  USHORT NumberDrives;
} CM_INT13_DRIVE_PARAMETER, *PCM_INT13_DRIVE_PARAMETER;
````


## -struct-fields
<dl>

### -field DriveSelect

<dd>
<p>The drive selected value.</p>
</dd>

### -field MaxCylinders

<dd>
<p>The maximum number of cylinders.</p>
</dd>

### -field SectorsPerTrack

<dd>
<p>The number of sectors per track.</p>
</dd>

### -field MaxHeads

<dd>
<p>The maximum number of heads.</p>
</dd>

### -field NumberDrives

<dd>
<p>The number of drives. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549453">IoQueryDeviceDescription</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549616">IoReportResourceUsage</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20CM_INT13_DRIVE_PARAMETER structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
