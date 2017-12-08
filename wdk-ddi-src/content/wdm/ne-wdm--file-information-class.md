---
UID: NE.wdm._FILE_INFORMATION_CLASS
title: FILE_INFORMATION_CLASS
author: windows-driver-content
description: A value that specifies which structure to use to query or set information for a file object.
old-location: ifsk\file_information_class.htm
old-project: ifsk
ms.assetid: aec0655b-7cc0-48b6-828c-b9d39c71e5b6
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
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
req.iface: 
req.product: Windows 10 or later.
---

# FILE_INFORMATION_CLASS enumeration



## -description
<p>A value that specifies which structure to use to query or set information for a file object.</p>


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
<dl>

### -field FileDirectoryInformation

<dd>
<p>A <a href="..\ntifs\ns-ntifs--file-directory-information.md">FILE_DIRECTORY_INFORMATION</a> structure.  </p>
</dd>

### -field FileFullDirectoryInformation

<dd>
<p>A <a href="..\ntifs\ns-ntifs--file-full-dir-information.md">FILE_FULL_DIR_INFORMATION</a> structure.</p>
</dd>

### -field FileBothDirectoryInformation

<dd>
<p>A <a href="..\ntifs\ns-ntifs--file-both-dir-information.md">FILE_BOTH_DIR_INFORMATION</a> structure.</p>
</dd>

### -field FileBasicInformation

<dd>
<p>A <a href="..\wdm\ns-wdm--file-basic-information.md">FILE_BASIC_INFORMATION</a> structure.</p>
</dd>

### -field FileStandardInformation

<dd>
<p>A <a href="..\wdm\ns-wdm--file-standard-information.md">FILE_STANDARD_INFORMATION</a> structure.</p>
</dd>

### -field FileInternalInformation

<dd>
<p>A <a href="..\ntifs\ns-ntifs--file-internal-information.md">FILE_INTERNAL_INFORMATION</a> structure.</p>
</dd>

### -field FileEaInformation

<dd>
<p>A <a href="..\ntifs\ns-ntifs--file-ea-information.md">FILE_EA_INFORMATION</a> structure.
</p>
</dd>

### -field FileAccessInformation

<dd>
<p>
A <a href="..\ntifs\ns-ntifs--file-access-information.md">FILE_ACCESS_INFORMATION</a> structure.</p>
</dd>

### -field FileNameInformation

<dd>
<p>
A <a href="..\ntddk\ns-ntddk--file-name-information.md">FILE_NAME_INFORMATION</a> structure.</p>
</dd>

### -field FileRenameInformation

<dd>
<p>
A <a href="..\ntifs\ns-ntifs--file-rename-information.md">FILE_RENAME_INFORMATION</a> structure.</p>
</dd>

### -field FileLinkInformation

<dd>
<p>A <a href="..\ntifs\ns-ntifs--file-link-information.md">FILE_LINK_INFORMATION</a> structure.</p>
</dd>

### -field FileNamesInformation

<dd>
<p>A <a href="..\ntifs\ns-ntifs--file-names-information.md">FILE_NAMES_INFORMATION</a> structure.
</p>
</dd>

### -field FileDispositionInformation

<dd>
<p>
A <a href="..\ntddk\ns-ntddk--file-disposition-information.md">FILE_DISPOSITION_INFORMATION</a> structure.
</p>
</dd>

### -field FilePositionInformation

<dd>
<p>
A <a href="..\wdm\ns-wdm--file-position-information.md">FILE_POSITION_INFORMATION</a> structure.
</p>
</dd>

### -field FileFullEaInformation

<dd>
<p>
A <a href="..\wdm\ns-wdm--file-full-ea-information.md">FILE_FULL_EA_INFORMATION</a> structure.
</p>
</dd>

### -field FileModeInformation

<dd>
<p>
A <a href="..\ntifs\ns-ntifs--file-mode-information.md">FILE_MODE_INFORMATION</a> structure.
</p>
</dd>

### -field FileAlignmentInformation

<dd>
<p>
A <a href="..\ntddk\ns-ntddk--file-alignment-information.md">FILE_ALIGNMENT_INFORMATION</a> structure.</p>
</dd>

### -field FileAllInformation

<dd>
<p>
A <a href="..\ntifs\ns-ntifs--file-all-information.md">FILE_ALL_INFORMATION</a> structure.
</p>
</dd>

### -field FileAllocationInformation

<dd>
<p>
A <a href="..\ntifs\ns-ntifs--file-allocation-information.md">FILE_ALLOCATION_INFORMATION</a> structure.</p>
</dd>

### -field FileEndOfFileInformation

<dd>
<p>
A <a href="..\ntddk\ns-ntddk--file-end-of-file-information.md">FILE_END_OF_FILE_INFORMATION</a> structure.
</p>
</dd>

### -field FileAlternateNameInformation

<dd>
<p>
A <a href="..\ntddk\ns-ntddk--file-name-information.md">FILE_NAME_INFORMATION</a> structure.
</p>
</dd>

### -field FileStreamInformation

<dd>
<p>
A message buffer that contains one or more <a href="..\ntifs\ns-ntifs--file-stream-information.md">FILE_STREAM_INFORMATION</a> structures.
</p>
</dd>

### -field FilePipeInformation

<dd>
<p>
A <a href="..\ntifs\ns-ntifs--file-pipe-information.md">FILE_PIPE_INFORMATION</a> structure.
</p>
</dd>

### -field FilePipeLocalInformation

<dd>
<p>
A <a href="..\ntifs\ns-ntifs--file-pipe-local-information.md">FILE_PIPE_LOCAL_INFORMATION</a> structure.
</p>
</dd>

### -field FilePipeRemoteInformation

<dd>
<p>
A <a href="..\ntifs\ns-ntifs--file-pipe-remote-information.md">FILE_PIPE_REMOTE_INFORMATION</a> structure.
</p>
</dd>

### -field FileMailslotQueryInformation

<dd>
<p>
A <a href="..\ntifs\ns-ntifs--file-mailslot-query-information.md">FILE_MAILSLOT_QUERY_INFORMATION</a> structure.
</p>
</dd>

### -field FileMailslotSetInformation

<dd>
<p>
A <a href="..\ntifs\ns-ntifs--file-mailslot-set-information.md">FILE_MAILSLOT_SET_INFORMATION</a> structure.
</p>
</dd>

### -field FileCompressionInformation

<dd>
<p>
A <a href="..\ntifs\ns-ntifs--file-compression-information.md">FILE_COMPRESSION_INFORMATION</a> structure.
</p>
</dd>

### -field FileObjectIdInformation

<dd>
<p>
A <a href="..\ntifs\ns-ntifs--file-objectid-information.md">FILE_OBJECTID_INFORMATION</a> structure.
 </p>
</dd>

### -field FileCompletionInformation

<dd>
<p>This value is reserved for system use.
 </p>
</dd>

### -field FileMoveClusterInformation

<dd>
<p>This value is reserved for system use.
</p>
</dd>

### -field FileQuotaInformation

<dd>
<p>A <a href="..\ntifs\ns-ntifs--file-quota-information.md">FILE_QUOTA_INFORMATION</a> structure.  
</p>
</dd>

### -field FileReparsePointInformation

<dd>
<p>A <a href="..\ntifs\ns-ntifs--file-reparse-point-information.md">FILE_REPARSE_POINT_INFORMATION</a> structure.
</p>
</dd>

### -field FileNetworkOpenInformation

<dd>
<p>A <a href="..\wdm\ns-wdm--file-network-open-information.md">FILE_NETWORK_OPEN_INFORMATION</a> structure.
</p>
</dd>

### -field FileAttributeTagInformation

<dd>
<p>A <a href="..\ntddk\ns-ntddk--file-attribute-tag-information.md">FILE_ATTRIBUTE_TAG_INFORMATION</a> structure.
</p>
</dd>

### -field FileTrackingInformation

<dd>
<p>This value is reserved for system use.</p>
</dd>

### -field FileIdBothDirectoryInformation

<dd>
<p>
A <a href="..\ntifs\ns-ntifs--file-id-both-dir-information.md">FILE_ID_BOTH_DIR_INFORMATION</a> structure.
</p>
</dd>

### -field FileIdFullDirectoryInformation

<dd>
<p>
A <a href="..\ntifs\ns-ntifs--file-id-full-dir-information.md">FILE_ID_FULL_DIR_INFORMATION</a> structure.</p>
</dd>

### -field FileValidDataLengthInformation

<dd>
<p>
A <a href="..\ntddk\ns-ntddk--file-valid-data-length-information.md">FILE_VALID_DATA_LENGTH_INFORMATION</a> structure.</p>
</dd>

### -field FileShortNameInformation

<dd>
<p>
A <a href="..\ntddk\ns-ntddk--file-name-information.md">FILE_NAME_INFORMATION</a> structure.
</p>
</dd>

### -field FileIoCompletionNotificationInformation

<dd>
<p>
This value is reserved for system use. This value is available starting with Windows Vista.
</p>
</dd>

### -field FileIoStatusBlockRangeInformation

<dd>
<p>This value is reserved for system use. This value is available starting with Windows Vista.</p>
</dd>

### -field FileIoPriorityHintInformation

<dd>
<p>A <a href="..\wdm\ns-wdm--file-io-priority-hint-information.md">FILE_IO_PRIORITY_HINT_INFORMATION</a> structure. This value is available starting with Windows Vista.</p>
</dd>

### -field FileSfioReserveInformation

<dd>
<p>This value is reserved for system use. This value is available starting with Windows Vista.
</p>
</dd>

### -field FileSfioVolumeInformation

<dd>
<p>This value is reserved for system use. This value is available starting with Windows Vista.
</p>
</dd>

### -field FileHardLinkInformation

<dd>
<p>A <a href="..\ntifs\ns-ntifs--file-links-information.md">FILE_LINKS_INFORMATION</a> structure. This value is available starting with Windows Vista.</p>
</dd>

### -field FileProcessIdsUsingFileInformation

<dd>
<p>
A <b>FILE_PROCESS_IDS_USING_FILE_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows Vista.</p>
</dd>

### -field FileNormalizedNameInformation

<dd>
<p>A <a href="..\fltkernel\ns-fltkernel--flt-file-name-information.md">FILE_NAME_INFORMATION</a> structure. This value is defined starting with Windows Vista. It is supported starting with Windows 8.
</p>
</dd>

### -field FileNetworkPhysicalNameInformation

<dd>
<p>
A <a href="..\ntifs\ns-ntifs--file-network-physical-name-information.md">FILE_NETWORK_PHYSICAL_NAME_INFORMATION</a> structure. This value is available starting with Windows Vista.</p>
</dd>

### -field FileIdGlobalTxDirectoryInformation

<dd>
<p>
A <a href="..\ntifs\ns-ntifs--file-id-global-tx-dir-information.md">FILE_ID_GLOBAL_TX_DIR_INFORMATION</a> structure. This value is available starting with Windows 7.
</p>
</dd>

### -field FileIsRemoteDeviceInformation

<dd>
<p>A <b>FILE_IS_REMOTE_DEVICE_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows 7.
</p>
</dd>

### -field FileUnusedInformation

<dd>
<p>This value is reserved for system use. This value is available starting with Windows 7.
</p>
</dd>

### -field FileNumaNodeInformation

<dd>
<p>A <b>FILE_NUMA_NODE_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows 7.</p>
</dd>

### -field FileStandardLinkInformation

<dd>
<p>A <b>FILE_STANDARD_LINK_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows 7.
</p>
</dd>

### -field FileRemoteProtocolInformation

<dd>
<p>A <b>FILE_REMOTE_PROTOCOL_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows 7.</p>
</dd>

### -field FileRenameInformationBypassAccessCheck

<dd>
<p>A <a href="..\ntifs\ns-ntifs--file-rename-information.md">FILE_RENAME_INFORMATION</a> structure. This value is available starting with Windows 10. </p>
<p>This is a special version of the <b>FileRenameInformation</b> operation that is used by kernel-mode drivers only in order to bypass security
        access checks.  This operation
        is only recognized by the <i>IOManager</i> and a file system should never
        receive it.
</p>
</dd>

### -field FileLinkInformationBypassAccessCheck

<dd>
<p>A <a href="..\ntifs\ns-ntifs--file-link-information.md">FILE_LINK_INFORMATION</a> structure. This value is available starting with Windows 10.</p>
<p>This is a special version of the <b>FileLinkInformation</b> operation that is used by kernel-mode drivers only in order to bypass security
        access checks.  This operation
        is only recognized by the <i>IOManager</i> and a file system should never
        receive it.
</p>
</dd>

### -field FileVolumeNameInformation

<dd>
<p>A <b>FILE_VOLUME_NAME_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows 10.</p>
</dd>

### -field FileIdInformation

<dd>
<p>A <b>FILE_ID_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows 10.</p>
</dd>

### -field FileIdExtdDirectoryInformation

<dd>
<p>A <b>FILE_ID_EXTD_DIR_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows 10.</p>
</dd>

### -field FileReplaceCompletionInformation

<dd>
<p>A <a href="..\ntifs\ns-ntifs--file-completion-information.md">FILE_COMPLETION_INFORMATION</a> structure to change or remove the completion port associated with a file handle. This value is available starting with Windows 8.1.</p>
</dd>

### -field FileHardLinkFullIdInformation

<dd>
<p>A <b>FILE_LINK_ENTRY_FULL_ID_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows 10.</p>
</dd>

### -field     FileIdExtdBothDirectoryInformation

<dd>
<p>A <b>FILE_ID_EXTD_BOTH_DIR_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows 10.</p>
</dd>

### -field     FileDispositionInformationEx

<dd>
<p>A <a href="..\ntddk\ns-ntddk--file-disposition-information-ex.md">FILE_DISPOSITION_INFORMATION_EX</a> structure that indicates how the operating system should delete a file. This value is available starting with Windows 10, version 1709.</p>
</dd>

### -field FileRenameInformationEx

<dd>
<p>A <a href="..\ntifs\ns-ntifs--file-rename-information.md">FILE_RENAME_INFORMATION</a> structure which contains additional flags. This value is available starting with Windows 10, version 1709. </p>
<p></p>
</dd>

### -field FileRenameInformationExBypassAccessCheck

<dd>
<p>A <a href="..\ntifs\ns-ntifs--file-rename-information.md">FILE_RENAME_INFORMATION</a> structure which contains additional flags. This value is available starting with Windows 10, version 1709. </p>
<p>This is a special version of the <b>FileRenameInformation</b> operation that is used by kernel-mode drivers only in order to bypass security
        access checks.  This operation
        is only recognized by the <i>IOManager</i> and a file system should never
        receive it.
</p>
</dd>

### -field FileMaximumInformation

<dd>
<p>
This value is reserved for system use. This value is available starting with Windows 7.
</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows XP, Windows Server 2003, and later versions of the Windows operating system unless otherwise specified above.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include FltKernel.h or Ntifs.h); </dt>
<dt>Wdm.h (include Wdm.h for use in kernel-mode driver projects)</dt>
</dl>
</td>
</tr>
</table>