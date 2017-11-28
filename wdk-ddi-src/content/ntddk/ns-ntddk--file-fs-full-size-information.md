---
UID: NS.ntddk._FILE_FS_FULL_SIZE_INFORMATION
title: FILE_FS_FULL_SIZE_INFORMATION
author: windows-driver-content
description: The FILE_FS_FULL_SIZE_INFORMATION structure is used to query sector size information for a file system volume.
old-location: ifsk\file_fs_full_size_information.htm
old-project: ifsk
ms.assetid: 4a37bfed-cf8e-4c97-a9fe-a44d910bed92
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FILE_FS_FULL_SIZE_INFORMATION, FILE_FS_FULL_SIZE_INFORMATION, *PFILE_FS_FULL_SIZE_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: Ntddk.h, Ntifs.h, Fltkernel.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FILE_FS_FULL_SIZE_INFORMATION
req.alt-loc: ntddk.h
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
req.iface: 
---

# FILE_FS_FULL_SIZE_INFORMATION structure



## -description
<p>The FILE_FS_FULL_SIZE_INFORMATION structure is used to query sector size information for a file system volume. </p>


## -syntax

````
typedef struct _FILE_FS_FULL_SIZE_INFORMATION {
  LARGE_INTEGER TotalAllocationUnits;
  LARGE_INTEGER CallerAvailableAllocationUnits;
  LARGE_INTEGER ActualAvailableAllocationUnits;
  ULONG         SectorsPerAllocationUnit;
  ULONG         BytesPerSector;
} FILE_FS_FULL_SIZE_INFORMATION, *PFILE_FS_FULL_SIZE_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>TotalAllocationUnits</b>

<dd>
<p>Total number of allocation units on the volume that are available to the user associated with the calling thread. </p>
<p><b>Microsoft Windows 2000 and later:</b> If per-user quotas are in use, this value may be less than the total number of allocation units on the disk. </p>
</dd>

### -field <b>CallerAvailableAllocationUnits</b>

<dd>
<p>Total number of free allocation units on the volume that are available to the user associated with the calling thread. </p>
<p><b>Windows 2000 and later:</b> If per-user quotas are in use, this value may be less than the total number of free allocation units on the disk. </p>
</dd>

### -field <b>ActualAvailableAllocationUnits</b>

<dd>
<p>Total number of free allocation units on the volume. </p>
</dd>

### -field <b>SectorsPerAllocationUnit</b>

<dd>
<p>Number of sectors in each allocation unit. </p>
</dd>

### -field <b>BytesPerSector</b>

<dd>
<p>Number of bytes in each sector. </p>
</dd>
</dl>

## -remarks
<p>This information can be queried in either of the following ways: </p>

<p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543443">FltQueryVolumeInformation</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff567070">ZwQueryVolumeInformationFile</a>, passing FileFsFullSizeInformation as the value of <i>FileInformationClass</i> and passing a caller-allocated, FILE_FS_FULL_SIZE_INFORMATION-structured buffer as the value of <i>FileInformation</i>. </p>

<p>Create an IRP with major function code IRP_MJ_QUERY_VOLUME_INFORMATION. </p>

<p>No specific access rights are required to query this information. Thus this information is available as long as the volume is accessed through an open handle to the volume itself, or to a file or directory on the volume. </p>

<p>The size of the buffer passed in the <i>FileInformation</i> parameter to <a href="https://msdn.microsoft.com/library/windows/hardware/ff543443">FltQueryVolumeInformation</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff567070">ZwQueryVolumeInformationFile</a> must be at least <b>sizeof</b> (FILE_FS_FULL_SIZE_INFORMATION). </p>

<p>This structure must be aligned on a LONGLONG (8-byte) boundary. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h, Ntifs.h, or Fltkernel.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543443">FltQueryVolumeInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549318">IRP_MJ_QUERY_VOLUME_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567070">ZwQueryVolumeInformationFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FILE_FS_FULL_SIZE_INFORMATION structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
