---
UID: NE.wdm._FILE_INFORMATION_CLASS
title: FILE_INFORMATION_CLASS
author: windows-driver-content
description: A value that specifies which structure to use to query or set information for a file object.
old-location: ifsk\file_information_class.htm
old-project: ifsk
ms.assetid: aec0655b-7cc0-48b6-828c-b9d39c71e5b6
ms.author: windowsdriverdev
ms.date: 11/14/2017
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
req.irql: <= APC_LEVEL
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

### -field <a id="FileDirectoryInformation"></a><a id="filedirectoryinformation"></a><a id="FILEDIRECTORYINFORMATION"></a><b>FileDirectoryInformation</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff540248">FILE_DIRECTORY_INFORMATION</a> structure.  </p>
</dd>

### -field <a id="FileFullDirectoryInformation"></a><a id="filefulldirectoryinformation"></a><a id="FILEFULLDIRECTORYINFORMATION"></a><b>FileFullDirectoryInformation</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff540289">FILE_FULL_DIR_INFORMATION</a> structure.</p>
</dd>

### -field <a id="FileBothDirectoryInformation"></a><a id="filebothdirectoryinformation"></a><a id="FILEBOTHDIRECTORYINFORMATION"></a><b>FileBothDirectoryInformation</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff540235">FILE_BOTH_DIR_INFORMATION</a> structure.</p>
</dd>

### -field <a id="FileBasicInformation"></a><a id="filebasicinformation"></a><a id="FILEBASICINFORMATION"></a><b>FileBasicInformation</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545762">FILE_BASIC_INFORMATION</a> structure.</p>
</dd>

### -field <a id="FileStandardInformation"></a><a id="filestandardinformation"></a><a id="FILESTANDARDINFORMATION"></a><b>FileStandardInformation</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545855">FILE_STANDARD_INFORMATION</a> structure.</p>
</dd>

### -field <a id="FileInternalInformation"></a><a id="fileinternalinformation"></a><a id="FILEINTERNALINFORMATION"></a><b>FileInternalInformation</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff540318">FILE_INTERNAL_INFORMATION</a> structure.</p>
</dd>

### -field <a id="FileEaInformation"></a><a id="fileeainformation"></a><a id="FILEEAINFORMATION"></a><b>FileEaInformation</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545773">FILE_EA_INFORMATION</a> structure.
</p>
</dd>

### -field <a id="FileAccessInformation"></a><a id="fileaccessinformation"></a><a id="FILEACCESSINFORMATION"></a><b>FileAccessInformation</b>

<dd>
<p>
A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545733">FILE_ACCESS_INFORMATION</a> structure.</p>
</dd>

### -field <a id="FileNameInformation"></a><a id="filenameinformation"></a><a id="FILENAMEINFORMATION"></a><b>FileNameInformation</b>

<dd>
<p>
A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545817">FILE_NAME_INFORMATION</a> structure.</p>
</dd>

### -field <a id="FileRenameInformation"></a><a id="filerenameinformation"></a><a id="FILERENAMEINFORMATION"></a><b>FileRenameInformation</b>

<dd>
<p>
A <a href="https://msdn.microsoft.com/library/windows/hardware/ff540344">FILE_RENAME_INFORMATION</a> structure.</p>
</dd>

### -field <a id="FileLinkInformation"></a><a id="filelinkinformation"></a><a id="FILELINKINFORMATION"></a><b>FileLinkInformation</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff540324">FILE_LINK_INFORMATION</a> structure.</p>
</dd>

### -field <a id="FileNamesInformation"></a><a id="filenamesinformation"></a><a id="FILENAMESINFORMATION"></a><b>FileNamesInformation</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff540329">FILE_NAMES_INFORMATION</a> structure.
</p>
</dd>

### -field <a id="FileDispositionInformation"></a><a id="filedispositioninformation"></a><a id="FILEDISPOSITIONINFORMATION"></a><b>FileDispositionInformation</b>

<dd>
<p>
A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545765">FILE_DISPOSITION_INFORMATION</a> structure.
</p>
</dd>

### -field <a id="FilePositionInformation"></a><a id="filepositioninformation"></a><a id="FILEPOSITIONINFORMATION"></a><b>FilePositionInformation</b>

<dd>
<p>
A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545848">FILE_POSITION_INFORMATION</a> structure.
</p>
</dd>

### -field <a id="FileFullEaInformation"></a><a id="filefulleainformation"></a><a id="FILEFULLEAINFORMATION"></a><b>FileFullEaInformation</b>

<dd>
<p>
A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545793">FILE_FULL_EA_INFORMATION</a> structure.
</p>
</dd>

### -field <a id="FileModeInformation"></a><a id="filemodeinformation"></a><a id="FILEMODEINFORMATION"></a><b>FileModeInformation</b>

<dd>
<p>
A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545809">FILE_MODE_INFORMATION</a> structure.
</p>
</dd>

### -field <a id="FileAlignmentInformation"></a><a id="filealignmentinformation"></a><a id="FILEALIGNMENTINFORMATION"></a><b>FileAlignmentInformation</b>

<dd>
<p>
A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545740">FILE_ALIGNMENT_INFORMATION</a> structure.</p>
</dd>

### -field <a id="FileAllInformation"></a><a id="fileallinformation"></a><a id="FILEALLINFORMATION"></a><b>FileAllInformation</b>

<dd>
<p>
A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545743">FILE_ALL_INFORMATION</a> structure.
</p>
</dd>

### -field <a id="FileAllocationInformation"></a><a id="fileallocationinformation"></a><a id="FILEALLOCATIONINFORMATION"></a><b>FileAllocationInformation</b>

<dd>
<p>
A <a href="https://msdn.microsoft.com/library/windows/hardware/ff540232">FILE_ALLOCATION_INFORMATION</a> structure.</p>
</dd>

### -field <a id="FileEndOfFileInformation"></a><a id="fileendoffileinformation"></a><a id="FILEENDOFFILEINFORMATION"></a><b>FileEndOfFileInformation</b>

<dd>
<p>
A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545780">FILE_END_OF_FILE_INFORMATION</a> structure.
</p>
</dd>

### -field <a id="FileAlternateNameInformation"></a><a id="filealternatenameinformation"></a><a id="FILEALTERNATENAMEINFORMATION"></a><b>FileAlternateNameInformation</b>

<dd>
<p>
A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545817">FILE_NAME_INFORMATION</a> structure.
</p>
</dd>

### -field <a id="FileStreamInformation"></a><a id="filestreaminformation"></a><a id="FILESTREAMINFORMATION"></a><b>FileStreamInformation</b>

<dd>
<p>
A message buffer that contains one or more <a href="https://msdn.microsoft.com/library/windows/hardware/ff540364">FILE_STREAM_INFORMATION</a> structures.
</p>
</dd>

### -field <a id="FilePipeInformation"></a><a id="filepipeinformation"></a><a id="FILEPIPEINFORMATION"></a><b>FilePipeInformation</b>

<dd>
<p>
A <a href="https://msdn.microsoft.com/library/windows/hardware/ff728845">FILE_PIPE_INFORMATION</a> structure.
</p>
</dd>

### -field <a id="FilePipeLocalInformation"></a><a id="filepipelocalinformation"></a><a id="FILEPIPELOCALINFORMATION"></a><b>FilePipeLocalInformation</b>

<dd>
<p>
A <a href="https://msdn.microsoft.com/library/windows/hardware/ff728846">FILE_PIPE_LOCAL_INFORMATION</a> structure.
</p>
</dd>

### -field <a id="FilePipeRemoteInformation"></a><a id="filepiperemoteinformation"></a><a id="FILEPIPEREMOTEINFORMATION"></a><b>FilePipeRemoteInformation</b>

<dd>
<p>
A <a href="https://msdn.microsoft.com/library/windows/hardware/ff728847">FILE_PIPE_REMOTE_INFORMATION</a> structure.
</p>
</dd>

### -field <a id="FileMailslotQueryInformation"></a><a id="filemailslotqueryinformation"></a><a id="FILEMAILSLOTQUERYINFORMATION"></a><b>FileMailslotQueryInformation</b>

<dd>
<p>
A <a href="https://msdn.microsoft.com/library/windows/hardware/ff728843">FILE_MAILSLOT_QUERY_INFORMATION</a> structure.
</p>
</dd>

### -field <a id="FileMailslotSetInformation"></a><a id="filemailslotsetinformation"></a><a id="FILEMAILSLOTSETINFORMATION"></a><b>FileMailslotSetInformation</b>

<dd>
<p>
A <a href="https://msdn.microsoft.com/library/windows/hardware/ff728844">FILE_MAILSLOT_SET_INFORMATION</a> structure.
</p>
</dd>

### -field <a id="FileCompressionInformation"></a><a id="filecompressioninformation"></a><a id="FILECOMPRESSIONINFORMATION"></a><b>FileCompressionInformation</b>

<dd>
<p>
A <a href="https://msdn.microsoft.com/library/windows/hardware/ff540239">FILE_COMPRESSION_INFORMATION</a> structure.
</p>
</dd>

### -field <a id="FileObjectIdInformation"></a><a id="fileobjectidinformation"></a><a id="FILEOBJECTIDINFORMATION"></a><b>FileObjectIdInformation</b>

<dd>
<p>
A <a href="https://msdn.microsoft.com/library/windows/hardware/ff540335">FILE_OBJECTID_INFORMATION</a> structure.
 </p>
</dd>

### -field <a id="FileCompletionInformation"></a><a id="filecompletioninformation"></a><a id="FILECOMPLETIONINFORMATION"></a><b>FileCompletionInformation</b>

<dd>
<p>This value is reserved for system use.
 </p>
</dd>

### -field <a id="FileMoveClusterInformation"></a><a id="filemoveclusterinformation"></a><a id="FILEMOVECLUSTERINFORMATION"></a><b>FileMoveClusterInformation</b>

<dd>
<p>This value is reserved for system use.
</p>
</dd>

### -field <a id="FileQuotaInformation"></a><a id="filequotainformation"></a><a id="FILEQUOTAINFORMATION"></a><b>FileQuotaInformation</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff540342">FILE_QUOTA_INFORMATION</a> structure.  
</p>
</dd>

### -field <a id="FileReparsePointInformation"></a><a id="filereparsepointinformation"></a><a id="FILEREPARSEPOINTINFORMATION"></a><b>FileReparsePointInformation</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff540354">FILE_REPARSE_POINT_INFORMATION</a> structure.
</p>
</dd>

### -field <a id="FileNetworkOpenInformation"></a><a id="filenetworkopeninformation"></a><a id="FILENETWORKOPENINFORMATION"></a><b>FileNetworkOpenInformation</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545822">FILE_NETWORK_OPEN_INFORMATION</a> structure.
</p>
</dd>

### -field <a id="FileAttributeTagInformation"></a><a id="fileattributetaginformation"></a><a id="FILEATTRIBUTETAGINFORMATION"></a><b>FileAttributeTagInformation</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545750">FILE_ATTRIBUTE_TAG_INFORMATION</a> structure.
</p>
</dd>

### -field <a id="FileTrackingInformation"></a><a id="filetrackinginformation"></a><a id="FILETRACKINGINFORMATION"></a><b>FileTrackingInformation</b>

<dd>
<p>This value is reserved for system use.</p>
</dd>

### -field <a id="FileIdBothDirectoryInformation"></a><a id="fileidbothdirectoryinformation"></a><a id="FILEIDBOTHDIRECTORYINFORMATION"></a><b>FileIdBothDirectoryInformation</b>

<dd>
<p>
A <a href="https://msdn.microsoft.com/library/windows/hardware/ff540303">FILE_ID_BOTH_DIR_INFORMATION</a> structure.
</p>
</dd>

### -field <a id="FileIdFullDirectoryInformation"></a><a id="fileidfulldirectoryinformation"></a><a id="FILEIDFULLDIRECTORYINFORMATION"></a><b>FileIdFullDirectoryInformation</b>

<dd>
<p>
A <a href="https://msdn.microsoft.com/library/windows/hardware/ff540310">FILE_ID_FULL_DIR_INFORMATION</a> structure.</p>
</dd>

### -field <a id="FileValidDataLengthInformation"></a><a id="filevaliddatalengthinformation"></a><a id="FILEVALIDDATALENGTHINFORMATION"></a><b>FileValidDataLengthInformation</b>

<dd>
<p>
A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545873">FILE_VALID_DATA_LENGTH_INFORMATION</a> structure.</p>
</dd>

### -field <a id="FileShortNameInformation"></a><a id="fileshortnameinformation"></a><a id="FILESHORTNAMEINFORMATION"></a><b>FileShortNameInformation</b>

<dd>
<p>
A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545817">FILE_NAME_INFORMATION</a> structure.
</p>
</dd>

### -field <a id="FileIoCompletionNotificationInformation"></a><a id="fileiocompletionnotificationinformation"></a><a id="FILEIOCOMPLETIONNOTIFICATIONINFORMATION"></a><b>FileIoCompletionNotificationInformation</b>

<dd>
<p>
This value is reserved for system use. This value is available starting with Windows Vista.
</p>
</dd>

### -field <a id="FileIoStatusBlockRangeInformation"></a><a id="fileiostatusblockrangeinformation"></a><a id="FILEIOSTATUSBLOCKRANGEINFORMATION"></a><b>FileIoStatusBlockRangeInformation</b>

<dd>
<p>This value is reserved for system use. This value is available starting with Windows Vista.</p>
</dd>

### -field <a id="FileIoPriorityHintInformation"></a><a id="fileiopriorityhintinformation"></a><a id="FILEIOPRIORITYHINTINFORMATION"></a><b>FileIoPriorityHintInformation</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545802">FILE_IO_PRIORITY_HINT_INFORMATION</a> structure. This value is available starting with Windows Vista.</p>
</dd>

### -field <a id="FileSfioReserveInformation"></a><a id="filesfioreserveinformation"></a><a id="FILESFIORESERVEINFORMATION"></a><b>FileSfioReserveInformation</b>

<dd>
<p>This value is reserved for system use. This value is available starting with Windows Vista.
</p>
</dd>

### -field <a id="FileSfioVolumeInformation"></a><a id="filesfiovolumeinformation"></a><a id="FILESFIOVOLUMEINFORMATION"></a><b>FileSfioVolumeInformation</b>

<dd>
<p>This value is reserved for system use. This value is available starting with Windows Vista.
</p>
</dd>

### -field <a id="FileHardLinkInformation"></a><a id="filehardlinkinformation"></a><a id="FILEHARDLINKINFORMATION"></a><b>FileHardLinkInformation</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff728841">FILE_LINKS_INFORMATION</a> structure. This value is available starting with Windows Vista.</p>
</dd>

### -field <a id="FileProcessIdsUsingFileInformation"></a><a id="fileprocessidsusingfileinformation"></a><a id="FILEPROCESSIDSUSINGFILEINFORMATION"></a><b>FileProcessIdsUsingFileInformation</b>

<dd>
<p>
A <b>FILE_PROCESS_IDS_USING_FILE_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows Vista.</p>
</dd>

### -field <a id="FileNormalizedNameInformation"></a><a id="filenormalizednameinformation"></a><a id="FILENORMALIZEDNAMEINFORMATION"></a><b>FileNormalizedNameInformation</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545817">FILE_NAME_INFORMATION</a> structure. This value is defined starting with Windows Vista. It is supported starting with Windows 8.
</p>
</dd>

### -field <a id="FileNetworkPhysicalNameInformation"></a><a id="filenetworkphysicalnameinformation"></a><a id="FILENETWORKPHYSICALNAMEINFORMATION"></a><b>FileNetworkPhysicalNameInformation</b>

<dd>
<p>
A <a href="https://msdn.microsoft.com/library/windows/hardware/dn602488">FILE_NETWORK_PHYSICAL_NAME_INFORMATION</a> structure. This value is available starting with Windows Vista.</p>
</dd>

### -field <a id="FileIdGlobalTxDirectoryInformation"></a><a id="fileidglobaltxdirectoryinformation"></a><a id="FILEIDGLOBALTXDIRECTORYINFORMATION"></a><b>FileIdGlobalTxDirectoryInformation</b>

<dd>
<p>
A <a href="https://msdn.microsoft.com/library/windows/hardware/ff728839">FILE_ID_GLOBAL_TX_DIR_INFORMATION</a> structure. This value is available starting with Windows 7.
</p>
</dd>

### -field <a id="FileIsRemoteDeviceInformation"></a><a id="fileisremotedeviceinformation"></a><a id="FILEISREMOTEDEVICEINFORMATION"></a><b>FileIsRemoteDeviceInformation</b>

<dd>
<p>A <b>FILE_IS_REMOTE_DEVICE_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows 7.
</p>
</dd>

### -field <a id="FileUnusedInformation"></a><a id="fileunusedinformation"></a><a id="FILEUNUSEDINFORMATION"></a><b>FileUnusedInformation</b>

<dd>
<p>This value is reserved for system use. This value is available starting with Windows 7.
</p>
</dd>

### -field <a id="FileNumaNodeInformation"></a><a id="filenumanodeinformation"></a><a id="FILENUMANODEINFORMATION"></a><b>FileNumaNodeInformation</b>

<dd>
<p>A <b>FILE_NUMA_NODE_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows 7.</p>
</dd>

### -field <a id="FileStandardLinkInformation"></a><a id="filestandardlinkinformation"></a><a id="FILESTANDARDLINKINFORMATION"></a><b>FileStandardLinkInformation</b>

<dd>
<p>A <b>FILE_STANDARD_LINK_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows 7.
</p>
</dd>

### -field <a id="FileRemoteProtocolInformation"></a><a id="fileremoteprotocolinformation"></a><a id="FILEREMOTEPROTOCOLINFORMATION"></a><b>FileRemoteProtocolInformation</b>

<dd>
<p>A <b>FILE_REMOTE_PROTOCOL_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows 7.</p>
</dd>

### -field <a id="FileRenameInformationBypassAccessCheck"></a><a id="filerenameinformationbypassaccesscheck"></a><a id="FILERENAMEINFORMATIONBYPASSACCESSCHECK"></a><b>FileRenameInformationBypassAccessCheck</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff540344">FILE_RENAME_INFORMATION</a> structure. This value is available starting with Windows 10. </p>
<p>This is a special version of the <b>FileRenameInformation</b> operation that is used by kernel-mode drivers only in order to bypass security
        access checks.  This operation
        is only recognized by the <i>IOManager</i> and a file system should never
        receive it.
</p>
</dd>

### -field <a id="FileLinkInformationBypassAccessCheck"></a><a id="filelinkinformationbypassaccesscheck"></a><a id="FILELINKINFORMATIONBYPASSACCESSCHECK"></a><b>FileLinkInformationBypassAccessCheck</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff540324">FILE_LINK_INFORMATION</a> structure. This value is available starting with Windows 10.</p>
<p>This is a special version of the <b>FileLinkInformation</b> operation that is used by kernel-mode drivers only in order to bypass security
        access checks.  This operation
        is only recognized by the <i>IOManager</i> and a file system should never
        receive it.
</p>
</dd>

### -field <a id="FileVolumeNameInformation"></a><a id="filevolumenameinformation"></a><a id="FILEVOLUMENAMEINFORMATION"></a><b>FileVolumeNameInformation</b>

<dd>
<p>A <b>FILE_VOLUME_NAME_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows 10.</p>
</dd>

### -field <a id="FileIdInformation"></a><a id="fileidinformation"></a><a id="FILEIDINFORMATION"></a><b>FileIdInformation</b>

<dd>
<p>A <b>FILE_ID_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows 10.</p>
</dd>

### -field <a id="FileIdExtdDirectoryInformation"></a><a id="fileidextddirectoryinformation"></a><a id="FILEIDEXTDDIRECTORYINFORMATION"></a><b>FileIdExtdDirectoryInformation</b>

<dd>
<p>A <b>FILE_ID_EXTD_DIR_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows 10.</p>
</dd>

### -field <a id="FileReplaceCompletionInformation"></a><a id="filereplacecompletioninformation"></a><a id="FILEREPLACECOMPLETIONINFORMATION"></a><b>FileReplaceCompletionInformation</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/dn369252">FILE_COMPLETION_INFORMATION</a> structure to change or remove the completion port associated with a file handle. This value is available starting with Windows 8.1.</p>
</dd>

### -field <a id="FileHardLinkFullIdInformation"></a><a id="filehardlinkfullidinformation"></a><a id="FILEHARDLINKFULLIDINFORMATION"></a><b>FileHardLinkFullIdInformation</b>

<dd>
<p>A <b>FILE_LINK_ENTRY_FULL_ID_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows 10.</p>
</dd>

### -field <a id="____FileIdExtdBothDirectoryInformation"></a><a id="____fileidextdbothdirectoryinformation"></a><a id="____FILEIDEXTDBOTHDIRECTORYINFORMATION"></a><b>    FileIdExtdBothDirectoryInformation</b>

<dd>
<p>A <b>FILE_ID_EXTD_BOTH_DIR_INFORMATION</b> structure. This value is reserved for system use. This value is available starting with Windows 10.</p>
</dd>

### -field <a id="____FileDispositionInformationEx"></a><a id="____filedispositioninformationex"></a><a id="____FILEDISPOSITIONINFORMATIONEX"></a><b>    FileDispositionInformationEx</b>

<dd>
<p>A <a href="..\ntddk\ns-ntddk--file-disposition-information-ex.md">FILE_DISPOSITION_INFORMATION_EX</a> structure that indicates how the operating system should delete a file. This value is available starting with Windows 10, version 1709.</p>
</dd>

### -field <a id="FileRenameInformationEx"></a><a id="filerenameinformationex"></a><a id="FILERENAMEINFORMATIONEX"></a><b>FileRenameInformationEx</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff540344">FILE_RENAME_INFORMATION</a> structure which contains additional flags. This value is available starting with Windows 10, version 1709. </p>
<p></p>
</dd>

### -field <a id="FileRenameInformationExBypassAccessCheck"></a><a id="filerenameinformationexbypassaccesscheck"></a><a id="FILERENAMEINFORMATIONEXBYPASSACCESSCHECK"></a><b>FileRenameInformationExBypassAccessCheck</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff540344">FILE_RENAME_INFORMATION</a> structure which contains additional flags. This value is available starting with Windows 10, version 1709. </p>
<p>This is a special version of the <b>FileRenameInformation</b> operation that is used by kernel-mode drivers only in order to bypass security
        access checks.  This operation
        is only recognized by the <i>IOManager</i> and a file system should never
        receive it.
</p>
</dd>

### -field <a id="FileMaximumInformation"></a><a id="filemaximuminformation"></a><a id="FILEMAXIMUMINFORMATION"></a><b>FileMaximumInformation</b>

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