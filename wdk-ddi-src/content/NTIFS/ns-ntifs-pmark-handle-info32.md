---
UID: NS.ntifs.PMARK_HANDLE_INFO32
title: PMARK_HANDLE_INFO32
author: windows-driver-content
description: Contains information that is used to mark a specified file or directory, and its update sequence number (USN) change journal record with data about changes.
old-location: ifsk\mark_handle_info32.htm
ms.assetid: BAC97D72-23C4-49A6-A13D-0F011113DB32
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Fltkernel.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MARK_HANDLE_INFO32
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
ms.keywords: PMARK_HANDLE_INFO32, MARK_HANDLE_INFO32, *PMARK_HANDLE_INFO32
req.iface: 
---

# PMARK_HANDLE_INFO32 structure



## -description
<p>Contains information that is used to mark a specified file or directory, and its update sequence 
    number (USN) change journal record with data about changes. This is only defined for 64-bit code and is used to 
    interpret input data formatted as a <a href="fs.mark_handle_info_str">MARK_HANDLE_INFO</a> structure sent from 32-bit 
    code. It is used with the <a href="fs.fsctl_mark_handle">FSCTL_MARK_HANDLE</a> 
    control code.</p>


## -syntax

````
typedef struct {
#if (_WIN32_WINNT >= 0x0602)
  union {
    ULONG UsnSourceInfo;
    ULONG CopyNumber;
  };
#else 
  ULONG  UsnSourceInfo;
#endif 
  UINT32 VolumeHandle;
  ULONG  HandleInfo;
} MARK_HANDLE_INFO32, *PMARK_HANDLE_INFO32;
````


## -struct-fields
<dl>

### -field <b>UsnSourceInfo</b>

<dd>
<p>The type of changes being made.</p>
<p>The operation does not modify the file or directory externally from the point of view of the application that 
       created it.</p>
<p>When a thread writes a new USN record, the source information flags in the prior record continues to be 
       present only if the thread also sets those flags. Therefore, the source information structure allows 
       applications to filter out USN records that are set only by a known source, such as an antivirus filter.</p>
<p>The following values are defined.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="USN_SOURCE_DATA_MANAGEMENT"></a><a id="usn_source_data_management"></a><dl>

### -field <b>USN_SOURCE_DATA_MANAGEMENT</b>


### -field 0x00000001

</dl>
</td>
<td width="60%">
<p>The operation provides information about a change to the file or directory made by the operating system.</p>
<p>A typical use is when Remote Storage moves data from external to local storage. Remote Storage is the 
         hierarchical storage management software. Such a move usually at a minimum adds the 
         <b>USN_REASON_DATA_OVERWRITE</b> flag to a USN record. However, the data has not changed 
         from the user point of view. By noting <b>USN_SOURCE_DATA_MANAGEMENT</b> in the 
         <b>SourceInfo</b> member of the 
         <a href="fs.usn_record_str">USN_RECORD</a> structure that holds the record, you can 
         determine that although a write operation is performed on the item, data has not changed.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="USN_SOURCE_AUXILIARY_DATA"></a><a id="usn_source_auxiliary_data"></a><dl>

### -field <b>USN_SOURCE_AUXILIARY_DATA</b>


### -field 0x00000002

</dl>
</td>
<td width="60%">
<p>The operation adds a private data stream to a file or directory.</p>
<p>An example might be a virus detector adding checksum information. As the virus detector modifies the item, 
         the system generates USN records. <b>USN_SOURCE_AUXILIARY_DATA</b> indicates that the 
         modifications did not change the application data.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="USN_SOURCE_REPLICATION_MANAGEMENT"></a><a id="usn_source_replication_management"></a><dl>

### -field <b>USN_SOURCE_REPLICATION_MANAGEMENT</b>


### -field 0x00000004

</dl>
</td>
<td width="60%">
<p>The operation creates or updates the contents of a replicated file.</p>
<p>For example, the file replication service sets this flag when it creates or updates a file in a replicated 
         directory.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>CopyNumber</b>

<dd>
<p>The zero-based copy number to use for subsequent reads. This is for use on  on Storage Spaces and Streams on 
        NTFS and ReFS and non-integrity streams on ReFS (streams with integrity on ReFS handle this automatically.)</p>
<p><b>Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:  </b>This member is not supported before Windows 8 and Windows Server 2012.</p>
</dd>

### -field <b>UsnSourceInfo</b>

<dd>
<p>The type of changes being made.</p>
<p>The operation does not modify the file or directory externally from the point of view of the application that 
       created it.</p>
<p>When a thread writes a new USN record, the source information flags in the prior record continues to be 
       present only if the thread also sets those flags. Therefore, the source information structure allows 
       applications to filter out USN records that are set only by a known source, such as an antivirus filter.</p>
<p>The following values are defined.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="USN_SOURCE_DATA_MANAGEMENT"></a><a id="usn_source_data_management"></a><dl>

### -field <b>USN_SOURCE_DATA_MANAGEMENT</b>


### -field 0x00000001

</dl>
</td>
<td width="60%">
<p>The operation provides information about a change to the file or directory made by the operating system.</p>
<p>A typical use is when Remote Storage moves data from external to local storage. Remote Storage is the 
         hierarchical storage management software. Such a move usually at a minimum adds the 
         <b>USN_REASON_DATA_OVERWRITE</b> flag to a USN record. However, the data has not changed 
         from the user point of view. By noting <b>USN_SOURCE_DATA_MANAGEMENT</b> in the 
         <b>SourceInfo</b> member of the 
         <a href="fs.usn_record_str">USN_RECORD</a> structure that holds the record, you can 
         determine that although a write operation is performed on the item, data has not changed.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="USN_SOURCE_AUXILIARY_DATA"></a><a id="usn_source_auxiliary_data"></a><dl>

### -field <b>USN_SOURCE_AUXILIARY_DATA</b>


### -field 0x00000002

</dl>
</td>
<td width="60%">
<p>The operation adds a private data stream to a file or directory.</p>
<p>An example might be a virus detector adding checksum information. As the virus detector modifies the item, 
         the system generates USN records. <b>USN_SOURCE_AUXILIARY_DATA</b> indicates that the 
         modifications did not change the application data.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="USN_SOURCE_REPLICATION_MANAGEMENT"></a><a id="usn_source_replication_management"></a><dl>

### -field <b>USN_SOURCE_REPLICATION_MANAGEMENT</b>


### -field 0x00000004

</dl>
</td>
<td width="60%">
<p>The operation creates or updates the contents of a replicated file.</p>
<p>For example, the file replication service sets this flag when it creates or updates a file in a replicated 
         directory.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>VolumeHandle</b>

<dd>
<p>The volume handle to the volume where the file or directory resides. For more information on obtaining a 
        volume handle, see the Remarks section.</p>
<p>This handle is required to check the privileges for this operation.</p>
<p>The caller must have the <b>SE_MANAGE_VOLUME_NAME</b> privilege. For more information, 
        see <a href="https://msdn.microsoft.com/library/windows/hardware/ff559863">Privileges</a>.</p>
</dd>

### -field <b>HandleInfo</b>

<dd>
<p>The flag that specifies additional information about the file or directory identified by the handle value 
       in the <b>VolumeHandle</b> member.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="MARK_HANDLE_PROTECT_CLUSTERS"></a><a id="mark_handle_protect_clusters"></a><dl>

### -field <b>MARK_HANDLE_PROTECT_CLUSTERS</b>


### -field 0x00000001

</dl>
</td>
<td width="60%">
<p>The file is marked as unable to be defragmented until the handle is closed.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="MARK_HANDLE_TXF_SYSTEM_LOG"></a><a id="mark_handle_txf_system_log"></a><dl>

### -field <b>MARK_HANDLE_TXF_SYSTEM_LOG</b>


### -field 0x00000004

</dl>
</td>
<td width="60%">
<p>The file is marked as unable to be defragmented until the handle is closed.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="MARK_HANDLE_NOT_TXF_SYSTEM_LOG"></a><a id="mark_handle_not_txf_system_log"></a><dl>

### -field <b>MARK_HANDLE_NOT_TXF_SYSTEM_LOG</b>


### -field 0x00000008

</dl>
</td>
<td width="60%">
<p>The file is marked as unable to be defragmented until the handle is closed.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="MARK_HANDLE_REALTIME"></a><a id="mark_handle_realtime"></a><dl>

### -field <b>MARK_HANDLE_REALTIME</b>


### -field 0x00000020

</dl>
</td>
<td width="60%">
<p>The file is marked for real-time read behavior regardless of the actual file type. Files marked with 
         this flag must be opened for <a href="fs.file_buffering">unbuffered I/O</a>.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="MARK_HANDLE_NOT_REALTIME"></a><a id="mark_handle_not_realtime"></a><dl>

### -field <b>MARK_HANDLE_NOT_REALTIME</b>


### -field 0x00000040

</dl>
</td>
<td width="60%">
<p>The file previously marked for real-time read behavior using the 
         <b>MARK_HANDLE_REALTIME</b> flag can be unmarked using this flag, removing the real-time 
         behavior. Files marked with this flag must be opened for 
         <a href="fs.file_buffering">unbuffered I/O</a>.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks
<p>When running on a 64-bit system, file system minifilters must interpret the input data sent by a 32-bit process in the system buffer for the <a href="fs.fsctl_mark_handle">FSCTL_MARK_HANDLE</a> control code as a <b>MARK_HANDLE_INFO32</b> structure. A minifilter may check the process word length by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff543308">FltIs32bitProcess</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows XP.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Fltkernel.h or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543308">FltIs32bitProcess</a>
</dt>
<dt>
<a href="fs.fsctl_mark_handle">FSCTL_MARK_HANDLE</a>
</dt>
<dt>
<a href="fs.mark_handle_info_str">MARK_HANDLE_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20MARK_HANDLE_INFO32 structure%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
