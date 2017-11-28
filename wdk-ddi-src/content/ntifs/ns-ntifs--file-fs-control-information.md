---
UID: NS.ntifs._FILE_FS_CONTROL_INFORMATION
title: FILE_FS_CONTROL_INFORMATION
author: windows-driver-content
description: The FILE_FS_CONTROL_INFORMATION structure is used to query or set control information for the files in a directory.
old-location: ifsk\file_fs_control_information.htm
old-project: ifsk
ms.assetid: 8a7e136a-fc87-481c-bb35-270408cb5071
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FILE_FS_CONTROL_INFORMATION, FILE_FS_CONTROL_INFORMATION, *PFILE_FS_CONTROL_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: Ntifs.h, Fltkernel.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FILE_FS_CONTROL_INFORMATION
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
req.iface: 
---

# FILE_FS_CONTROL_INFORMATION structure



## -description
<p>The FILE_FS_CONTROL_INFORMATION structure is used to query or set control information for the files in a directory. </p>


## -syntax

````
typedef struct _FILE_FS_CONTROL_INFORMATION {
  LARGE_INTEGER FreeSpaceStartFiltering;
  LARGE_INTEGER FreeSpaceThreshold;
  LARGE_INTEGER FreeSpaceStopFiltering;
  LARGE_INTEGER DefaultQuotaThreshold;
  LARGE_INTEGER DefaultQuotaLimit;
  ULONG         FileSystemControlFlags;
} FILE_FS_CONTROL_INFORMATION, *PFILE_FS_CONTROL_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>FreeSpaceStartFiltering</b>

<dd>
<p>Minimum amount of free disk space, in bytes, that is required for the Content-Indexing daemon to begin document filtering. </p>
</dd>

### -field <b>FreeSpaceThreshold</b>

<dd>
<p>Minimum amount of free disk space, in bytes, required for the Indexing Service to continue to filter documents and merge word lists. If the amount of free disk space falls below this threshold, a warning message is written to the Microsoft Windows application event log. Filtering and merging are halted until space is freed. </p>
</dd>

### -field <b>FreeSpaceStopFiltering</b>

<dd>
<p>Minimum amount of free disk space, in bytes, that is required for the Content-Indexing daemon to continue document filtering. If the amount of free disk space falls below this threshold, document filtering is halted. </p>
</dd>

### -field <b>DefaultQuotaThreshold</b>

<dd>
<p>Default per-user disk quota warning threshold for the volume. </p>
</dd>

### -field <b>DefaultQuotaLimit</b>

<dd>
<p>Default per-user disk quota limit for the volume. </p>
</dd>

### -field <b>FileSystemControlFlags</b>

<dd>
<p>Bitmask of flags that control quota enforcement and logging of user-related quota events on the volume. Logging makes an entry in the Windows application event log. Compatible combination of one or more of the following: </p>
<table>
<tr>
<th>File System Control Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>FILE_VC_CONTENT_INDEX_DISABLED</p>
</td>
<td>
<p>If set, content indexing is disabled. </p>
</td>
</tr>
<tr>
<td>
<p>FILE_VC_LOG_QUOTA_LIMIT</p>
</td>
<td>
<p>If set, an event log entry will be created when the user exceeds his or her assigned disk quota limit. </p>
</td>
</tr>
<tr>
<td>
<p>FILE_VC_LOG_QUOTA_THRESHOLD</p>
</td>
<td>
<p>If set, an event log entry will be created when the user exceeds his or her assigned quota warning threshold. </p>
</td>
</tr>
<tr>
<td>
<p>FILE_VC_LOG_VOLUME_LIMIT</p>
</td>
<td>
<p>If set, an event log entry will be created when the volume's free space limit is exceeded. </p>
</td>
</tr>
<tr>
<td>
<p>FILE_VC_LOG_VOLUME_THRESHOLD</p>
</td>
<td>
<p>If set, an event log entry will be created when the volume's free space threshold is exceeded. </p>
</td>
</tr>
<tr>
<td>
<p>FILE_VC_QUOTA_ENFORCE</p>
</td>
<td>
<p>If set, quotas are enforced on the volume. </p>
</td>
</tr>
<tr>
<td>
<p>FILE_VC_QUOTA_TRACK</p>
</td>
<td>
<p>If set, quotas are tracked on the volume. </p>
</td>
</tr>
<tr>
<td>
<p>FILE_VC_QUOTAS_INCOMPLETE</p>
</td>
<td>
<p>If set, the quota information for the volume is incomplete. </p>
</td>
</tr>
<tr>
<td>
<p>FILE_VC_QUOTAS_REBUILDING</p>
</td>
<td>
<p>If set, the file system is rebuilding the quota information for the volume. </p>
</td>
</tr>
</table>
<p> </p>
<p>In addition, the following flag masks are defined. These are useful for testing flag values. </p>
<table>
<tr>
<th>Mask</th>
<th>Value</th>
</tr>
<tr>
<td>
<p>FILE_VC_QUOTA_MASK</p>
</td>
<td>
<p>FILE_VC_QUOTA_ENFORCE | FILE_VC_QUOTA_TRACK</p>
</td>
</tr>
<tr>
<td>
<p>FILE_VC_QUOTA_NONE</p>
</td>
<td>
<p>~FILE_VC_QUOTA_ENFORCE &amp; ~FILE_VC_QUOTA_TRACK</p>
</td>
</tr>
<tr>
<td>
<p>FILE_VC_VALID_MASK</p>
</td>
<td>
<p>ORed combination of all flags in the above table. </p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks
<p>This information can be queried in either of the following ways: </p>

<p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543443">FltQueryVolumeInformation</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff567070">ZwQueryVolumeInformationFile</a>, passing FileFsControlInformation as the value of <i>FileInformationClass</i> and passing a caller-allocated, FILE_FS_CONTROL_INFORMATION-structured buffer as the value of <i>FileInformation</i>. </p>

<p>Create an IRP with major function code IRP_MJ_QUERY_VOLUME_INFORMATION. </p>

<p>FILE_READ_DATA access to the volume is required to query this information. </p>

<p>This information can be set in either of the following ways: </p>

<p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544564">FltSetVolumeInformation</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff567112">ZwSetVolumeInformationFile</a>, passing FileFsControlInformation as the value of <i>FileInformationClass</i> and passing a caller-allocated, FILE_FS_CONTROL_INFORMATION-structured buffer as the value of <i>FileInformation</i>. </p>

<p>Create an IRP with major function code IRP_MJ_SET_VOLUME_INFORMATION. </p>

<p>FILE_WRITE_DATA access to the volume is required to set this information. </p>

<p>The size of the buffer passed in the <i>FileInformation</i> parameter to <a href="https://msdn.microsoft.com/library/windows/hardware/ff543443">FltQueryVolumeInformation</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544564">FltSetVolumeInformation</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff567070">ZwQueryVolumeInformationFile</a>, or <b>ZwSetVolumeInformationFile</b> must be at least <b>sizeof</b> (FILE_FS_CONTROL_INFORMATION). </p>

<p>This structure must be aligned on a LONGLONG (8-byte) boundary. </p>

## -requirements
<table>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543443">FltQueryVolumeInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544564">FltSetVolumeInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549318">IRP_MJ_QUERY_VOLUME_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549415">IRP_MJ_SET_VOLUME_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567070">ZwQueryVolumeInformationFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567112">ZwSetVolumeInformationFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FILE_FS_CONTROL_INFORMATION structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
