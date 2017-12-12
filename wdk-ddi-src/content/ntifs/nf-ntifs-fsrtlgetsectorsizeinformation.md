---
UID: NF.ntifs.FsRtlGetSectorSizeInformation
title: FsRtlGetSectorSizeInformation function
author: windows-driver-content
description: The FsRtlGetSectorSizeInformation routine retrieves the physical and logical sector size information for a storage volume.
old-location: ifsk\fsrtlgetsectorsizeinformation.htm
old-project: ifsk
ms.assetid: 337E5450-8C90-48B7-B344-FB9420498D4F
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlGetSectorSizeInformation
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlGetSectorSizeInformation
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
---

# FsRtlGetSectorSizeInformation function



## -description
The <b>FsRtlGetSectorSizeInformation</b> routine retrieves the physical and logical sector size information for a storage volume.



## -syntax

````
NTSTATUS FsRtlGetSectorSizeInformation(
  _In_  PDEVICE_OBJECT                   RealDevice,
  _Out_ PFILE_FS_SECTOR_SIZE_INFORMATION SectorSizeInfo
);
````


## -parameters

### -param RealDevice [in]

The target device object for a storage device.


### -param SectorSizeInfo [out]

A pointer to a caller supplied <a href="ifsk.file_fs_sector_size_information">FILE_FS_SECTOR_SIZE_INFORMATION</a> structure.


## -returns
<b>FsRtlGetSectorSizeInformation</b> returns <b>STATUS_SUCCESS</b> if the sector size information is returned in <i>SectorSizeInfo</i>. Otherwise, another appropriate <b>NTSTATUS</b> value is returned such as the following.
<dl>
<dt><b>STATUS_BAD_DEVICE_TYPE</b></dt>
</dl>The storage device reported an invalid sector size.

 


## -remarks
This routine is used by file system drivers to retrieve sector size information from the storage device containing the volume. A file system driver typically maintains the device object sent in <i>RealDevice</i> in its  volume parameter block (VPD) for the storage volume.

Drivers other than file system drivers, can query sector size information using the <a href="ifsk.fltqueryvolumeinformation">FltQueryVolumeInformation</a> or  <a href="kernel.zwqueryvolumeinformationfile">ZwQueryVolumeInformationFile</a> routines, or by sending an <a href="ifsk.irp_mj_query_volume_information">IRP_MJ_QUERY_VOLUME_INFORMATION</a> request and specifying <b>FileFsSectorSizeInformation</b> as the file system information class.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in starting with Windows 8.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.fltqueryvolumeinformation">FltQueryVolumeInformation</a>
</dt>
<dt>
<a href="kernel.zwqueryvolumeinformationfile">ZwQueryVolumeInformationFile</a>
</dt>
<dt>
<a href="ifsk.file_fs_sector_size_information">FILE_FS_SECTOR_SIZE_INFORMATION</a>
</dt>
<dt>
<a href="ifsk.irp_mj_query_volume_information">IRP_MJ_QUERY_VOLUME_INFORMATION</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlGetSectorSizeInformation routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

