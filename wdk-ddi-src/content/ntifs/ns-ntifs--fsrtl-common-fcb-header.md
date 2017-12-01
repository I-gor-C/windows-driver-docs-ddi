---
UID: NS.ntifs._FSRTL_COMMON_FCB_HEADER
title: FSRTL_COMMON_FCB_HEADER
author: windows-driver-content
description: Do not use the FSRTL_COMMON_FCB_HEADER structure outside of the FSRTL_ADVANCED_FCB_HEADER structure.
old-location: ifsk\fsrtl_common_fcb_header.htm
old-project: ifsk
ms.assetid: b0b199ea-d72f-4de3-a6b1-bd22140d13cb
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FSRTL_COMMON_FCB_HEADER, FSRTL_COMMON_FCB_HEADER
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
req.alt-api: FSRTL_COMMON_FCB_HEADER
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

# FSRTL_COMMON_FCB_HEADER structure



## -description
<p>Do not use the FSRTL_COMMON_FCB_HEADER structure outside of the <a href="..\ntifs\ns-ntifs--fsrtl-advanced-fcb-header.md">FSRTL_ADVANCED_FCB_HEADER</a> structure.  The FSRTL_COMMON_FCB_HEADER structure contains context information that a file system maintains about a file, directory, volume, or alternate data stream.  </p>


## -syntax

````
typedef struct _FSRTL_COMMON_FCB_HEADER {
  CSHORT        NodeTypeCode;
  CSHORT        NodeByteSize;
  UCHAR         Flags;
  UCHAR         IsFastIoPossible;
  UCHAR         Flags2;
  UCHAR         Reserved  :4;
  UCHAR         Version  :4;
  PERESOURCE    Resource;
  PERESOURCE    PagingIoResource;
  LARGE_INTEGER AllocationSize;
  LARGE_INTEGER FileSize;
  LARGE_INTEGER ValidDataLength;
} FSRTL_COMMON_FCB_HEADER, *PFSRTL_COMMON_FCB_HEADER;
````


## -struct-fields
<dl>

### -field <b>NodeTypeCode</b>

<dd>
<p>Reserved for system use. </p>
</dd>

### -field <b>NodeByteSize</b>

<dd>
<p>Reserved for system use. </p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Bitmask of flags that indicate support for various features. This member must be a bitwise OR combination of one or more of the following values:</p>
<p></p>
<dl>

### -field <a id="FSRTL_FLAG_FILE_MODIFIED"></a><a id="fsrtl_flag_file_modified"></a>FSRTL_FLAG_FILE_MODIFIED

<dd>
<p>Reserved for system use. </p>
</dd>

### -field <a id="FSRTL_FLAG_FILE_LENGTH_CHANGED"></a><a id="fsrtl_flag_file_length_changed"></a>FSRTL_FLAG_FILE_LENGTH_CHANGED

<dd>
<p>Reserved for system use. </p>
</dd>

### -field <a id="FSRTL_FLAG_LIMIT_MODIFIED_PAGES"></a><a id="fsrtl_flag_limit_modified_pages"></a>FSRTL_FLAG_LIMIT_MODIFIED_PAGES

<dd>
<p>Reserved for system use.  File system drivers (except for filter drivers) that must set or clear a limit of modified data for a file should call <a href="..\ntifs\nf-ntifs-ccsetdirtypagethreshold.md">CcSetDirtyPageThreshold</a>.</p>
</dd>

### -field <a id="FSRTL_FLAG_ACQUIRE_MAIN_RSRC_EX"></a><a id="fsrtl_flag_acquire_main_rsrc_ex"></a>FSRTL_FLAG_ACQUIRE_MAIN_RSRC_EX

<dd>
<p>Reserved for system use. </p>
</dd>

### -field <a id="FSRTL_FLAG_ACQUIRE_MAIN_RSRC_SH"></a><a id="fsrtl_flag_acquire_main_rsrc_sh"></a>FSRTL_FLAG_ACQUIRE_MAIN_RSRC_SH

<dd>
<p>Reserved for system use. </p>
</dd>

### -field <a id="FSRTL_FLAG_USER_MAPPED_FILE"></a><a id="fsrtl_flag_user_mapped_file"></a>FSRTL_FLAG_USER_MAPPED_FILE

<dd>
<p>The Cache Manager sets this flag to indicate that a view is mapped to a file. </p>
</dd>

### -field <a id="FSRTL_FLAG_ADVANCED_HEADER"></a><a id="fsrtl_flag_advanced_header"></a>FSRTL_FLAG_ADVANCED_HEADER

<dd>
<p>This flag indicates that the file system is using <a href="..\ntifs\ns-ntifs--fsrtl-advanced-fcb-header.md">FSRTL_ADVANCED_FCB_HEADER</a> instead of FSRTL_COMMON_FCB_HEADER in its file control block (FCB) structures. This flag is required because use of the FSRTL_COMMON_FCB_HEADER structure outside of the FSRTL_ADVANCED_FCB_HEADER structure is deprecated.</p>
</dd>

### -field <a id="FSRTL_FLAG_EOF_ADVANCE_ACTIVE"></a><a id="fsrtl_flag_eof_advance_active"></a>FSRTL_FLAG_EOF_ADVANCE_ACTIVE

<dd>
<p>Reserved for system use. </p>
</dd>
</dl>
</dd>

### -field <b>IsFastIoPossible</b>

<dd>
<p>This member must be one of the following values: </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p><b>FastIoIsPossible</b></p>
</td>
<td>
<p>Fast I/O is possible. </p>
</td>
</tr>
<tr>
<td>
<p><b>FastIoIsQuestionable</b></p>
</td>
<td>
<p>An exclusive byte range lock exists for the file. The caller should call the file system's <b>FastIoCheckIfPossible</b> routine. </p>
</td>
</tr>
<tr>
<td>
<p><b>FastIoIsNotPossible</b></p>
</td>
<td>
<p>The FCB for the file is bad, or an opportunistic lock (also called  "oplock") exists for the file. </p>
</td>
</tr>
</table>
<p> </p>
<p>For more information about these values, see the reference entries for <a href="..\ntifs\nf-ntifs-fsrtlaretherecurrentfilelocks.md">FsRtlAreThereCurrentFileLocks</a>, <a href="ifsk.fsrtlcopyread">FsRtlCopyRead</a>, and <a href="ifsk.fsrtlcopywrite">FsRtlCopyWrite</a>. </p>
</dd>

### -field <b>Flags2</b>

<dd>
<p>Bitmask of flags that the file system sets to indicate support for various features. This member must be one or more of the following values: </p>
<p></p>
<dl>

### -field <a id="FSRTL_FLAG2_DO_MODIFIED_WRITE"></a><a id="fsrtl_flag2_do_modified_write"></a>FSRTL_FLAG2_DO_MODIFIED_WRITE

<dd>
<p>This flag is used together with the <b>FsContext2</b> member of the file object for the file stream as follows: </p>
<ul>
<li>If the <b>FsContext2</b> member of the file object is non-<b>NULL</b>, the file stream represents an open instance of a file or a directory, and the value of this flag is ignored by the operating system.</li>
<li>If the <b>FsContext2</b> member of the file object is <b>NULL</b>, and this flag is not set, the file object is a stream file object, and the stream is a modified-no-write (MNW) stream.</li>
<li>If the <b>FsContext2</b> member of the file object is <b>NULL</b>, and this flag is set, the file object is a stream file object, and the stream is writable.</li>
</ul>
</dd>

### -field <a id="FSRTL_FLAG2_PURGE_WHEN_MAPPED"></a><a id="fsrtl_flag2_purge_when_mapped"></a>FSRTL_FLAG2_PURGE_WHEN_MAPPED

<dd>
<p>If this flag is set, the Cache Manager will flush and purge the cache map when a user first maps a file. </p>
</dd>

### -field <a id="FSRTL_FLAG2_SUPPORTS_FILTER_CONTEXTS"></a><a id="fsrtl_flag2_supports_filter_contexts"></a>FSRTL_FLAG2_SUPPORTS_FILTER_CONTEXTS

<dd>
<p>This flag indicates that the file system is using <a href="..\ntifs\ns-ntifs--fsrtl-advanced-fcb-header.md">FSRTL_ADVANCED_FCB_HEADER</a> instead of FSRTL_COMMON_FCB_HEADER in its FCB structures. This flag is required because use of the FSRTL_COMMON_FCB_HEADER structure outside of the FSRTL_ADVANCED_FCB_HEADER structure is deprecated.</p>
</dd>

### -field <a id="FSRTL_FLAG2_IS_PAGING_FILE_"></a><a id="fsrtl_flag2_is_paging_file_"></a>FSRTL_FLAG2_IS_PAGING_FILE 

<dd>
<p>If set, this FCB header is associated with a page file.</p>
</dd>
</dl>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use. Drivers must set this bit-field to zero. </p>
</dd>

### -field <b>Version</b>

<dd>
<p>Reserved for system use.  This bit-field is set by the <a href="..\ntifs\nf-ntifs-fsrtlsetupadvancedheader.md">FsRtlSetupAdvancedHeader</a> or <a href="..\ntifs\nf-ntifs-fsrtlsetupadvancedheaderex.md">FsRtlSetupAdvancedHeaderEx</a> macro.  Starting with Windows Vista, the value of this bit-field is FSRTL_FCB_HEADER_V1 or greater; otherwise, the value is FSRTL_FCB_HEADER_V0.  See <a href="..\ntifs\ns-ntifs--fsrtl-advanced-fcb-header.md">FSRTL_ADVANCED_FCB_HEADER</a> for more information.</p>
</dd>

### -field <b>Resource</b>

<dd>
<p>Pointer to an initialized resource variable, for which the file system supplies the storage that will be used to synchronize I/O access to the FCB. The resource variable must be allocated from nonpaged pool. </p>
<p>Filter drivers should treat this member as opaque. </p>
</dd>

### -field <b>PagingIoResource</b>

<dd>
<p>Pointer to an additional resource variable, for which the file system supplies the storage that will be used to synchronize paging I/O access to the FCB. The resource variable must be allocated from nonpaged pool. </p>
<p>Filter drivers should treat this member as opaque. </p>
</dd>

### -field <b>AllocationSize</b>

<dd>
<p>Allocation size for the file stream. </p>
<p>For more information about the <b>AllocationSize</b>, <b>FileSize</b>, and <b>ValidDataLength</b> members, see <a href="..\ntifs\nf-ntifs-ccinitializecachemap.md">CcInitializeCacheMap</a>.</p>
</dd>

### -field <b>FileSize</b>

<dd>
<p>File size of the file stream. </p>
</dd>

### -field <b>ValidDataLength</b>

<dd>
<p>Valid data length of the file stream. </p>
</dd>
</dl>

## -remarks
<p>File systems must set the <b>FsContext</b> member of every file object to point to an <a href="..\ntifs\ns-ntifs--fsrtl-advanced-fcb-header.md">FSRTL_ADVANCED_FCB_HEADER</a> structure.  This structure can be embedded inside of a file-system-specific stream context object structure (the remainder of this structure is file-system-specific). Usually, the FSRTL_ADVANCED_FCB_HEADER  structure is a file control block (FCB). However, on some file systems that support multiple data streams, such as NTFS, it is a stream control block (SCB).</p>

<p>If the file is used as a paging file, the FSRTL_ADVANCED_FCB_HEADER structure must be allocated from nonpaged pool. Otherwise, it can be allocated from paged or nonpaged pool.</p>

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
<a href="..\ntifs\nf-ntifs-ccinitializecachemap.md">CcInitializeCacheMap</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--fsrtl-advanced-fcb-header.md">FSRTL_ADVANCED_FCB_HEADER</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--fsrtl-per-stream-context.md">FSRTL_PER_STREAM_CONTEXT</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtlaretherecurrentfilelocks.md">FsRtlAreThereCurrentFileLocks</a>
</dt>
<dt>
<a href="ifsk.fsrtlcopyread">FsRtlCopyRead</a>
</dt>
<dt>
<a href="ifsk.fsrtlcopywrite">FsRtlCopyWrite</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtlsetupadvancedheader.md">FsRtlSetupAdvancedHeader</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FSRTL_COMMON_FCB_HEADER structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
