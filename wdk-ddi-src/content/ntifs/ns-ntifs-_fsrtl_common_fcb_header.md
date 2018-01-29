---
UID : NS:ntifs._FSRTL_COMMON_FCB_HEADER
title : _FSRTL_COMMON_FCB_HEADER
author : windows-driver-content
description : Do not use the FSRTL_COMMON_FCB_HEADER structure outside of the FSRTL_ADVANCED_FCB_HEADER structure.
old-location : ifsk\fsrtl_common_fcb_header.htm
old-project : ifsk
ms.assetid : b0b199ea-d72f-4de3-a6b1-bd22140d13cb
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : ntifs/FSRTL_COMMON_FCB_HEADER, contextstructures_775f0b4a-8043-4125-85b4-530a79ed76ba.xml, FSRTL_COMMON_FCB_HEADER structure [Installable File System Drivers], PFSRTL_COMMON_FCB_HEADER, FSRTL_COMMON_FCB_HEADER, _FSRTL_COMMON_FCB_HEADER, ntifs/PFSRTL_COMMON_FCB_HEADER, *PFSRTL_COMMON_FCB_HEADER, PFSRTL_COMMON_FCB_HEADER structure pointer [Installable File System Drivers], ifsk.fsrtl_common_fcb_header
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntifs.h
req.include-header : Ntifs.h, Fltkernel.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : FSRTL_COMMON_FCB_HEADER
---

# _FSRTL_COMMON_FCB_HEADER structure
Do not use the FSRTL_COMMON_FCB_HEADER structure outside of the <a href="..\ntifs\ns-ntifs-_fsrtl_advanced_fcb_header.md">FSRTL_ADVANCED_FCB_HEADER</a> structure.  The FSRTL_COMMON_FCB_HEADER structure contains context information that a file system maintains about a file, directory, volume, or alternate data stream.

## Syntax
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

## Members


`AllocationSize`

Allocation size for the file stream. 

For more information about the <b>AllocationSize</b>, <b>FileSize</b>, and <b>ValidDataLength</b> members, see <a href="..\ntifs\nf-ntifs-ccinitializecachemap.md">CcInitializeCacheMap</a>.

`FileSize`

File size of the file stream.

`Flags`

Bitmask of flags that indicate support for various features. This member must be a bitwise OR combination of one or more of the following values:

`Flags2`

Bitmask of flags that the file system sets to indicate support for various features. This member must be one or more of the following values:

`IsFastIoPossible`

This member must be one of the following values: 
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<b>FastIoIsPossible</b>

</td>
<td>
Fast I/O is possible. 

</td>
</tr>
<tr>
<td>
<b>FastIoIsQuestionable</b>

</td>
<td>
An exclusive byte range lock exists for the file. The caller should call the file system's <b>FastIoCheckIfPossible</b> routine. 

</td>
</tr>
<tr>
<td>
<b>FastIoIsNotPossible</b>

</td>
<td>
The FCB for the file is bad, or an opportunistic lock (also called  "oplock") exists for the file. 

</td>
</tr>
</table> 

For more information about these values, see the reference entries for <a href="..\ntifs\nf-ntifs-fsrtlaretherecurrentfilelocks.md">FsRtlAreThereCurrentFileLocks</a>, <a href="..\ntifs\nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlcopyread~r7.md">FsRtlCopyRead</a>, and <a href="..\ntifs\nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlcopywrite~r7.md">FsRtlCopyWrite</a>.

`NodeByteSize`

Reserved for system use.

`NodeTypeCode`

Reserved for system use.

`PagingIoResource`

Pointer to an additional resource variable, for which the file system supplies the storage that will be used to synchronize paging I/O access to the FCB. The resource variable must be allocated from nonpaged pool. 

Filter drivers should treat this member as opaque.

`Reserved`

Reserved for system use. Drivers must set this bit-field to zero.

`Resource`

Pointer to an initialized resource variable, for which the file system supplies the storage that will be used to synchronize I/O access to the FCB. The resource variable must be allocated from nonpaged pool. 

Filter drivers should treat this member as opaque.

`ValidDataLength`

Valid data length of the file stream.

`Version`

Reserved for system use.  This bit-field is set by the <a href="..\ntifs\nf-ntifs-fsrtlsetupadvancedheader.md">FsRtlSetupAdvancedHeader</a> or <a href="..\ntifs\nf-ntifs-fsrtlsetupadvancedheaderex.md">FsRtlSetupAdvancedHeaderEx</a> macro.  Starting with Windows Vista, the value of this bit-field is FSRTL_FCB_HEADER_V1 or greater; otherwise, the value is FSRTL_FCB_HEADER_V0.  See <a href="..\ntifs\ns-ntifs-_fsrtl_advanced_fcb_header.md">FSRTL_ADVANCED_FCB_HEADER</a> for more information.

## Remarks
File systems must set the <b>FsContext</b> member of every file object to point to an <a href="..\ntifs\ns-ntifs-_fsrtl_advanced_fcb_header.md">FSRTL_ADVANCED_FCB_HEADER</a> structure.  This structure can be embedded inside of a file-system-specific stream context object structure (the remainder of this structure is file-system-specific). Usually, the FSRTL_ADVANCED_FCB_HEADER  structure is a file control block (FCB). However, on some file systems that support multiple data streams, such as NTFS, it is a stream control block (SCB).
<div class="alert"><b>Note</b>   To support filter manager and filter contexts, file systems must use the FSRTL_ADVANCED_FCB_HEADER structure in their stream context objects. All Microsoft file systems use this structure, and all third-party file system developers must do so as well.  FCBs and SCBs for all classes of open requests, including volume open requests, must include this structure.</div><div> </div>If the file is used as a paging file, the FSRTL_ADVANCED_FCB_HEADER structure must be allocated from nonpaged pool. Otherwise, it can be allocated from paged or nonpaged pool.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntifs.h (include Ntifs.h, Fltkernel.h) |

## See Also

<a href="..\ntifs\nf-ntifs-fsrtlaretherecurrentfilelocks.md">FsRtlAreThereCurrentFileLocks</a>

<a href="..\ntifs\nf-ntifs-fsrtlsetupadvancedheader.md">FsRtlSetupAdvancedHeader</a>

<a href="..\ntifs\ns-ntifs-_fsrtl_advanced_fcb_header.md">FSRTL_ADVANCED_FCB_HEADER</a>

<a href="..\ntifs\ns-ntifs-_fsrtl_per_stream_context.md">FSRTL_PER_STREAM_CONTEXT</a>

<a href="..\ntifs\nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlcopywrite~r7.md">FsRtlCopyWrite</a>

<a href="..\ntifs\nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlcopyread~r7.md">FsRtlCopyRead</a>

<a href="..\ntifs\nf-ntifs-ccinitializecachemap.md">CcInitializeCacheMap</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FSRTL_COMMON_FCB_HEADER structure%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>