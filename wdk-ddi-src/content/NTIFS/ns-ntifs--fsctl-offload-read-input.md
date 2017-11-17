---
UID: NS.ntifs._FSCTL_OFFLOAD_READ_INPUT
title: FSCTL_OFFLOAD_READ_INPUT
author: windows-driver-content
description: The FSCTL_OFFLOAD_READ_INPUT structure contains the input for the FSCTL_OFFLOAD_READ control code request.
old-location: ifsk\fsctl_offload_read_input.htm
ms.assetid: 11F9FFC6-D2F6-4CCA-9459-CF2639AE652D
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h, Fltkernel.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FSCTL_OFFLOAD_READ_INPUT
req.alt-loc: ntifs.h
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
ms.keywords: FSCTL_OFFLOAD_READ_INPUT, FSCTL_OFFLOAD_READ_INPUT, *PFSCTL_OFFLOAD_READ_INPUT
req.iface: 
---

# FSCTL_OFFLOAD_READ_INPUT structure



## -description
<p>The <b>FSCTL_OFFLOAD_READ_INPUT</b> structure contains the input for the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451101">FSCTL_OFFLOAD_READ</a> control code request.</p>


## -syntax

````
typedef struct _FSCTL_OFFLOAD_READ_INPUT {
  ULONG     Size;
  ULONG     Flags;
  ULONG     TokenTimeToLive;
  ULONG     Reserved;
  ULONGLONG FileOffset;
  ULONGLONG Length;
} FSCTL_OFFLOAD_READ_INPUT, *PFSCTL_OFFLOAD_READ_INPUT;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size of this structure. Set this member to <b>sizeof</b>(FSCTL_OFFLOAD_READ_INPUT).</p>
</dd>

### -field <b>Flags</b>

<dd>
<p> This member is not used. Set to 0.</p>
</dd>

### -field <b>TokenTimeToLive</b>

<dd>
<p>The time, in milliseconds, for which the read operation remains valid. The default time-to-live is 0. The recommended value for time-to-live is also 0.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p> Reserved.</p>
</dd>

### -field <b>FileOffset</b>

<dd>
<p> The position in the file to start reading from. The offset value must be aligned to a logical sector boundary on the volume.</p>
</dd>

### -field <b>Length</b>

<dd>
<p> The length, in bytes, of data to read, starting at <b>FileOffset</b>. The length  value must align to a logical sector boundary on the volume, except when the length matches end-of-file.</p>
</dd>
</dl>

## -remarks
<p>The  storage device's copy provider retains the data read for the duration in <b>TokenTimeToLive</b>. Multiple writes with the same token can be performed until the time in <b>TokenTimeToLive</b> expires.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h or Fltkernel.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451101">FSCTL_OFFLOAD_READ</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451109">FSCTL_OFFLOAD_READ_OUTPUT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FSCTL_OFFLOAD_READ_INPUT structure%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
