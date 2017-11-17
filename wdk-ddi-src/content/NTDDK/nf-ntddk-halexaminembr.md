---
UID: NF.ntddk.HalExamineMBR
title: HalExamineMBR
author: windows-driver-content
description: The HalExamineMBR routine reads the master boot record (MBR) of a disk and returns data from the MBR if the MBR is of the type specified by the caller.
old-location: kernel\halexaminembr.htm
ms.assetid: 6db72f2c-af24-4807-b90b-65dc2b309dc7
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HalExamineMBR
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
ms.keywords: HalExamineMBR
req.iface: 
---

# HalExamineMBR function



## -description
<p>The <b>HalExamineMBR</b> routine reads the master boot record (MBR) of a disk and returns data from the MBR if the MBR is of the type specified by the caller.</p>


## -syntax

````
VOID HalExamineMBR(
  _In_  PDEVICE_OBJECT DeviceObject,
  _In_  ULONG          SectorSize,
  _In_  ULONG          MBRTypeIdentifier,
  _Out_ PVOID          *Buffer
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>A pointer to the device object for the device being examined.</p>
</dd>

### -param <i>SectorSize</i> [in]

<dd>
<p>The minimum number of bytes that an I/O operation can fetch from the device being examined. If this value is less than 512, <b>HalExamineMBR</b> reads 512 bytes to ensure that it reads an entire partition table.</p>
</dd>

### -param <i>MBRTypeIdentifier</i> [in]

<dd>
<p>MBR partition type identifier. This parameter specifies the type of MBR that may be on the disk. For more information, see Remarks.</p>
</dd>

### -param <i>Buffer</i> [out]

<dd>
<p>A pointer to a location to which <b>HalExamineMBR</b> writes a pointer to a buffer that contains data from the MBR. The layout of the buffer depends on the MBR partition type. <b>HalExamineMBR</b> allocates the storage for this buffer. The caller must deallocate this buffer as soon as possible by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544590">ExFreePool</a> routine.</p>
<p><b>HalExamineMBR</b> sets *<i>Buffer</i> = <b>NULL</b> if the MBR partition type of the disk does not match that specified by <i>MBRTypeIdentifier</i> or if there is an error.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>For a list of system-defined MBR partition type identifiers, see the table in <a href="https://msdn.microsoft.com/library/windows/hardware/ff563751">PARTITION_INFORMATION</a>. These identifiers are defined in the Ntdddisk.h header file.</p>

<p>For a list of system-defined MBR partition type identifiers, see the table in <a href="https://msdn.microsoft.com/library/windows/hardware/ff563751">PARTITION_INFORMATION</a>. These identifiers are defined in the Ntdddisk.h header file.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows XP.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975204">PowerIrpDDis</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544590">ExFreePool</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563751">PARTITION_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20HalExamineMBR routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
