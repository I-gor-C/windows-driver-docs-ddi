---
UID: NE.wdm._FILE_INFORMATION_CLASS
title: _FILE_INFORMATION_CLASS
author: windows-driver-content
description: A value that specifies which structure to use to query or set information for a file object.
old-location: ifsk\file_information_class.htm
old-project: ifsk
ms.assetid: aec0655b-7cc0-48b6-828c-b9d39c71e5b6
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: _FILE_INFORMATION_CLASS, FILE_INFORMATION_CLASS, *PFILE_INFORMATION_CLASS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: FltKernel.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows XP, Windows Server 2003, and later versions of the Windows operating system unless otherwise specified above.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FILE_INFORMATION_CLASS
req.alt-loc: ntifs.h,wdm.h
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
req.product: Windows 10 or later.
---

# _FILE_INFORMATION_CLASS enumeration



## -description
A value that specifies which structure to use to query or set information for a file object.


## -syntax

````
typedef enum _FILE_INFORMATION_CLASS { 
  FileDirectoryInformation                  = 1,
  FileFullDirectoryInformation,
  FileBothDirectoryInformation,
  FileBasicInformation,
  FileStandardInformation,
  FileInternalInformation,
  FileEaInformation,
  FileAccessInformation,
  FileNameInformation,
  FileRenameInformation,
  FileLinkInformation,
  FileNamesInformation,
  FileDispositionInformation,
  FilePositionInformation,
  FileFullEaInformation,
  FileModeInformation,
  FileAlignmentInformation,
  FileAllInformation,
  FileAllocationInformation,
  FileEndOfFileInformation,
  FileAlternateNameInformation,
  FileStreamInformation,
  FilePipeInformation,
  FilePipeLocalInformation,
  FilePipeRemoteInformation,
  FileMailslotQueryInformation,
  FileMailslotSetInformation,
  FileCompressionInformation,
  FileObjectIdInformation,
  FileCompletionInformation,
  FileMoveClusterInformation,
  FileQuotaInformation,
  FileReparsePointInformation,
  FileNetworkOpenInformation,
  FileAttributeTagInformation,
  FileTrackingInformation,
  FileIdBothDirectoryInformation,
  FileIdFullDirectoryInformation,
  FileValidDataLengthInformation,
  FileShortNameInformation,
  FileIoCompletionNotificationInformation,
  FileIoStatusBlockRangeInformation,
  FileIoPriorityHintInformation,
  FileSfioReserveInformation,
  FileSfioVolumeInformation,
  FileHardLinkInformation,
  FileProcessIdsUsingFileInformation,
  FileNormalizedNameInformation,
  FileNetworkPhysicalNameInformation,
  FileIdGlobalTxDirectoryInformation,
  FileIsRemoteDeviceInformation,
  FileUnusedInformation,
  FileNumaNodeInformation,
  FileStandardLinkInformation,
  FileRemoteProtocolInformation,
  FileRenameInformationBypassAccessCheck,
  FileLinkInformationBypassAccessCheck,
  FileVolumeNameInformation,
  FileIdInformation,
  FileIdExtdDirectoryInformation,
  FileReplaceCompletionInformation,
  FileHardLinkFullIdInformation,
      FileIdExtdBothDirectoryInformation,
      FileDispositionInformationEx,
  FileRenameInformationEx,
  FileRenameInformationExBypassAccessCheck,
  FileMaximumInformation
} FILE_INFORMATION_CLASS, *PFILE_INFORMATION_CLASS;
````


## -enum-fields

### -field FileDirectoryInformation

A <a href="ifsk.file_directory_information">FILE_DIRECTORY_INFORMATION</a> structure.  

### -field FileFullDirectoryInformation

A <a href="ifsk.file_full_dir_information">FILE_FULL_DIR_INFORMATION</a> structure.

### -field FileBothDirectoryInformation

A <a href="ifsk.file_both_dir_information">FILE_BOTH_DIR_INFORMATION</a> structure.

### -field FileBasicInformation

A <a href="kernel.file_basic_information">FILE_BASIC_INFORMATION</a> structure.

### -field FileStandardInformation

A <a href="kernel.file_standard_information">FILE_STANDARD_INFORMATION</a> structure.

### -field FileInternalInformation

A <a href="ifsk.file_internal_information">FILE_INTERNAL_INFORMATION</a> structure.

### -field FileEaInformation

A <a href="kernel.file_ea_information">FILE_EA_INFORMATION</a> structure.


### -field FileAccessInformation


A <a href="kernel.file_access_information">FILE_ACCESS_INFORMATION</a> structure.

### -field FileNameInformation


A <a href="kernel.file_name_information">FILE_NAME_INFORMATION</a> structure.

### -field FileRenameInformation


A <a href="ifsk.file_rename_information">FILE_RENAME_INFORMATION</a> structure.

### -field FileLinkInformation

A <a href="ifsk.file_link_information">FILE_LINK_INFORMATION</a> structure.

### -field FileNamesInformation

A <a href="ifsk.file_names_information">FILE_NAMES_INFORMATION</a> structure.


### -field FileDispositionInformation


A <a href="kernel.file_disposition_information">FILE_DISPOSITION_INFORMATION</a> structure.


### -field FilePositionInformation


A <a href="kernel.file_position_information">FILE_POSITION_INFORMATION</a> structure.


### -field FileFullEaInformation


A <a href="kernel.file_full_ea_information">FILE_FULL_EA_INFORMATION</a> structure.


### -field FileModeInformation


A <a href="kernel.file_mode_information">FILE_MODE_INFORMATION</a> structure.


### -field FileAlignmentInformation


A <a href="kernel.file_alignment_information">FILE_ALIGNMENT_INFORMATION</a> structure.

### -field FileAllInformation


A <a href="kernel.file_all_information">FILE_ALL_INFORMATION</a> structure.


### -field FileAllocationInformation


A <a href="ifsk.file_allocation_information">FILE_ALLOCATION_INFORMATION</a> structure.

### -field FileEndOfFileInformation


A <a href="kernel.file_end_of_file_information">FILE_END_OF_FILE_INFORMATION</a> structure.


### -field FileAlternateNameInformation


A <a href="kernel.file_name_information">FILE_NAME_INFORMATION</a> structure.


### -field FileStreamInformation


A message buffer that contains one or more <a href="ifsk.file_stream_information">FILE_STREAM_INFORMATION</a> structures.


### -field FilePipeInformation


A <a href="ifsk.file_pipe_information">FILE_PIPE_INFORMATION</a> structure.


### -field FilePipeLocalInformation


A <a href="ifsk.file_pipe_local_information">FILE_PIPE_LOCAL_INFORMATION</a> structure.


### -field FilePipeRemoteInformation


A <a href="ifsk.file_pipe_remote_information">FILE_PIPE_REMOTE_INFORMATION</a> structure.


### -field FileMailslotQueryInformation


A <a href="ifsk.file_mailslot_query_information">FILE_MAILSLOT_QUERY_INFORMATION</a> structure.


### -field FileMailslotSetInformation


A <a href="ifsk.file_mailslot_set_information">FILE_MAILSLOT_SET_INFORMATION</a> structure.


### -field FileCompressionInformation


A <a href="ifsk.file_compression_information">FILE_COMPRESSION_INFORMATION</a> structure.


### -field FileObjectIdInformation


A <a href="ifsk.file_objectid_information">FILE_OBJECTID_INFORMATION</a> structure.
 

### -field FileCompletionInformation

This value is reserved for system use.
 

### -field FileMoveClusterInformation

This value is reserved for system use.


### -field FileQuotaInformation

A <a href="ifsk.file_quota_information">FILE_QUOTA_INFORMATION</a> structure.  


### -field FileReparsePointInformation

A <a href="ifsk.file_reparse_point_information">FILE_REPARSE_POINT_INFORMATION</a> structure.


### -field FileNetworkOpenInformation

A <a href="kernel.file_network_open_information">FILE_NETWORK_OPEN_INFORMATION</a> structure.


### -field FileAttributeTagInformation

A <a href="kernel.file_attribute_tag_information">FILE_ATTRIBUTE_TAG_INFORMATION</a> structure.


### -field FileTrackingInformation

This value is reserved for system use.

### -field FileIdBothDirectoryInformation


A <a href="ifsk.file_id_both_dir_information">FILE_ID_BOTH_DIR_INFORMATION</a> structure.


### -field FileIdFullDirectoryInformation


A <a href="ifsk.file_id_full_dir_information">FILE_ID_FULL_DIR_INFORMATION</a> structure.

### -field FileValidDataLengthInformation


A <a href="kernel.file_valid_data_length_information">FILE_VALID_DATA_LENGTH_INFORMATION</a> structure.

### -field FileShortNameInformation


A <a href="kernel.file_name_information">FILE_NAME_INFORMATION</a> structure.


### -field FileIoCompletionNotificationInformation


This value is reserved for system use. This value is available starting with Windows Vista.


### -field FileIoStatusBlockRangeInformation

This value is reserved for system use. This value is available starting with Windows Vista.

### -field FileIoPriorityHintInformation

A <a href="kernel.file_io_priority_hint_information">FILE_IO_PRIORITY_HINT_INFORMATION</a> structure. This value is available starting with Windows Vista.

### -field FileSfioReserveInformation

This value is reserved for system use. This value is available starting with Windows Vista.


### -field FileSfioVolumeInformation

This value is reserved for system use. This value is available starting with Windows Vista.


### -field FileHardLinkInformation

A <a href="ifsk.file_links_information">FILE_LINKS_INFORMATION</a> structure. This value is available starting with Windows Vista.

### -field FileProcessIdsUsingFileInformation


A <b>FILE_PROCESS_IDS_USING_FILE_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows Vista.

### -field FileNormalizedNameInformation

A <a href="ifsk.flt_file_name_information">FILE_NAME_INFORMATION</a> structure. This value is defined starting with Windows Vista. It is supported starting with Windows 8.


### -field FileNetworkPhysicalNameInformation


A <a href="ifsk.file_network_physical_name_information">FILE_NETWORK_PHYSICAL_NAME_INFORMATION</a> structure. This value is available starting with Windows Vista.

### -field FileIdGlobalTxDirectoryInformation


A <a href="ifsk.file_id_global_tx_dir_information">FILE_ID_GLOBAL_TX_DIR_INFORMATION</a> structure. This value is available starting with Windows 7.


### -field FileIsRemoteDeviceInformation

A <b>FILE_IS_REMOTE_DEVICE_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows 7.


### -field FileUnusedInformation

This value is reserved for system use. This value is available starting with Windows 7.


### -field FileNumaNodeInformation

A <b>FILE_NUMA_NODE_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows 7.

### -field FileStandardLinkInformation

A <b>FILE_STANDARD_LINK_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows 7.


### -field FileRemoteProtocolInformation

A <b>FILE_REMOTE_PROTOCOL_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows 7.

### -field FileRenameInformationBypassAccessCheck

A <a href="ifsk.file_rename_information">FILE_RENAME_INFORMATION</a> structure. This value is available starting with Windows 10. 
This is a special version of the <b>FileRenameInformation</b> operation that is used by kernel-mode drivers only in order to bypass security
        access checks.  This operation
        is only recognized by the <i>IOManager</i> and a file system should never
        receive it.


### -field FileLinkInformationBypassAccessCheck

A <a href="ifsk.file_link_information">FILE_LINK_INFORMATION</a> structure. This value is available starting with Windows 10.
This is a special version of the <b>FileLinkInformation</b> operation that is used by kernel-mode drivers only in order to bypass security
        access checks.  This operation
        is only recognized by the <i>IOManager</i> and a file system should never
        receive it.


### -field FileVolumeNameInformation

A <b>FILE_VOLUME_NAME_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows 10.

### -field FileIdInformation

A <b>FILE_ID_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows 10.

### -field FileIdExtdDirectoryInformation

A <b>FILE_ID_EXTD_DIR_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows 10.

### -field FileReplaceCompletionInformation

A <a href="ifsk.file_completion_information">FILE_COMPLETION_INFORMATION</a> structure to change or remove the completion port associated with a file handle. This value is available starting with Windows 8.1.

### -field FileHardLinkFullIdInformation

A <b>FILE_LINK_ENTRY_FULL_ID_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows 10.

### -field     FileIdExtdBothDirectoryInformation

A <b>FILE_ID_EXTD_BOTH_DIR_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows 10.

### -field     FileDispositionInformationEx

A <a href="ifsk.file_disposition_information_ex">FILE_DISPOSITION_INFORMATION_EX</a> structure that indicates how the operating system should delete a file. This value is available starting with Windows 10, version 1709.

### -field FileRenameInformationEx

A <a href="ifsk.file_rename_information">FILE_RENAME_INFORMATION</a> structure which contains additional flags. This value is available starting with Windows 10, version 1709. 


### -field FileRenameInformationExBypassAccessCheck

A <a href="ifsk.file_rename_information">FILE_RENAME_INFORMATION</a> structure which contains additional flags. This value is available starting with Windows 10, version 1709. 
This is a special version of the <b>FileRenameInformation</b> operation that is used by kernel-mode drivers only in order to bypass security
        access checks.  This operation
        is only recognized by the <i>IOManager</i> and a file system should never
        receive it.


### -field FileMaximumInformation


This value is reserved for system use. This value is available starting with Windows 7.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available in Windows XP, Windows Server 2003, and later versions of the Windows operating system unless otherwise specified above.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include FltKernel.h or Ntifs.h); </dt>
<dt>Wdm.h (include Wdm.h for use in kernel-mode driver projects)</dt>
</dl>
</td>
</tr>
</table>