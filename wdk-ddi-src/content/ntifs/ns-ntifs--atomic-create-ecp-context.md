---
UID: NS.ntifs._ATOMIC_CREATE_ECP_CONTEXT
title: ATOMIC_CREATE_ECP_CONTEXT
author: windows-driver-content
description: This structure allows supplemental operations to be performed on a file atomically during create.
old-location: ifsk\atomic_create_ecp_context.htm
old-project: ifsk
ms.assetid: CFA879CC-6124-4E1C-B440-358455A5E6EF
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: ATOMIC_CREATE_ECP_CONTEXT, ATOMIC_CREATE_ECP_CONTEXT, *PATOMIC_CREATE_ECP_CONTEXT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1607
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ATOMIC_CREATE_ECP_CONTEXT
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

# ATOMIC_CREATE_ECP_CONTEXT structure



## -description
<p>This structure allows supplemental
operations to be performed on a file atomically during create. Use the </p>


## -syntax

````
typedef struct _ATOMIC_CREATE_ECP_CONTEXT {
  USHORT                                                           Size;
  USHORT                                                           InFlags;
  USHORT                                                           OutFlags;
  USHORT                                                           ReparseBufferLength;
  _Field_size_bytes_opt_(ReparseBufferLength) PREPARSE_DATA_BUFFER ReparseBuffer;
  LONGLONG                                                         FileSize;
  LONGLONG                                                         ValidDataLength;
#if (NTDDI_VERSION >= NTDDI_WIN10_RS2)
  PFILE_TIMESTAMPS                                                 FileTimestamps;
#endif 
#if (NTDDI_VERSION >= NTDDI_WIN10_RS3)
  ULONG                                                            FileAttributes;
  ULONG                                                            UsnSourceInfo;
  USN                                                              Usn;
#endif 
} ATOMIC_CREATE_ECP_CONTEXT, *PATOMIC_CREATE_ECP_CONTEXT;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size of the context structure.</p>
</dd>

### -field <b>InFlags</b>

<dd>
<p>Flags that indicate the requested supplemental operation(s) to be performed with the create operation.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="ATOMIC_CREATE_ECP_IN_FLAG_SPARSE_SPECIFIED"></a><a id="atomic_create_ecp_in_flag_sparse_specified"></a><dl>

### -field <b>ATOMIC_CREATE_ECP_IN_FLAG_SPARSE_SPECIFIED</b>


### -field 0x0001

</dl>
</td>
<td width="60%">
<p>Requests that the sparse flag be set on the file.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="ATOMIC_CREATE_ECP_IN_FLAG_REPARSE_POINT_SPECIFIED"></a><a id="atomic_create_ecp_in_flag_reparse_point_specified"></a><dl>

### -field <b>ATOMIC_CREATE_ECP_IN_FLAG_REPARSE_POINT_SPECIFIED</b>


### -field 0x0002

</dl>
</td>
<td width="60%">
<p>Requests that a reparse point be set on the file.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="ATOMIC_CREATE_ECP_IN_FLAG_EOF_SPECIFIED"></a><a id="atomic_create_ecp_in_flag_eof_specified"></a><dl>

### -field <b>ATOMIC_CREATE_ECP_IN_FLAG_EOF_SPECIFIED</b>


### -field 0x0004

</dl>
</td>
<td width="60%">
<p>Requests that a file size be set on the file.  This also implies
that on-disk allocation will occur to support the requested file size.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="ATOMIC_CREATE_ECP_IN_FLAG_VDL_SPECIFIED"></a><a id="atomic_create_ecp_in_flag_vdl_specified"></a><dl>

### -field <b>ATOMIC_CREATE_ECP_IN_FLAG_VDL_SPECIFIED</b>


### -field 0x0008

</dl>
</td>
<td width="60%">
<p>Requests that a valid data length be set on the file.  This also
implies that the file size be set to at least the requested valid data
length.  </p>
<div class="alert"><b>Note</b>  This is considered a privileged operation if it could potentially
expose uninitialized data.</div>
<div> </div>
</td>
</tr>
<tr>
<td width="40%"><a id="ATOMIC_CREATE_ECP_IN_FLAG_OPERATION_MASK"></a><a id="atomic_create_ecp_in_flag_operation_mask"></a><dl>

### -field <b>ATOMIC_CREATE_ECP_IN_FLAG_OPERATION_MASK</b>


### -field 0x00ff

</dl>
</td>
<td width="60%">
<p>Use this flag as a mask to specify the other <b>InFlags</b> flag values.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="ATOMIC_CREATE_ECP_IN_FLAG_BEST_EFFORT"></a><a id="atomic_create_ecp_in_flag_best_effort"></a><dl>

### -field <b>ATOMIC_CREATE_ECP_IN_FLAG_BEST_EFFORT</b>


### -field 0x0100

</dl>
</td>
<td width="60%">
<p>Indicates that the  file system should perform the create operation even if some of the requested supplemental operations could not be
performed or are not supported by the file system. The caller may check
the <b>OutFlags</b> to see which operations were performed.  If this flag is not specified, the file system should fail the create operation if it cannot successfully
perform all of the requested supplemental operations.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>OutFlags</b>

<dd>
<p>Flags that indicate the actual supplemental operation(s) performed with a successful create operation.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="ATOMIC_CREATE_ECP_OUT_FLAG_SPARSE_SET"></a><a id="atomic_create_ecp_out_flag_sparse_set"></a><dl>

### -field <b>ATOMIC_CREATE_ECP_OUT_FLAG_SPARSE_SET</b>


### -field 0x0001

</dl>
</td>
<td width="60%">
<p>Indicates that the sparse flag was set on the file.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="ATOMIC_CREATE_ECP_OUT_FLAG_REPARSE_POINT_SET"></a><a id="atomic_create_ecp_out_flag_reparse_point_set"></a><dl>

### -field <b>ATOMIC_CREATE_ECP_OUT_FLAG_REPARSE_POINT_SET</b>


### -field 0x0002

</dl>
</td>
<td width="60%">
<p>Indicates that a reparse point was set on the file.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="ATOMIC_CREATE_ECP_OUT_FLAG_EOF_SET"></a><a id="atomic_create_ecp_out_flag_eof_set"></a><dl>

### -field <b>ATOMIC_CREATE_ECP_OUT_FLAG_EOF_SET</b>


### -field 0x0004

</dl>
</td>
<td width="60%">
<p>Indicates that a file size was set on the file, and that on-disk allocation occurred to support the requested file size.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="ATOMIC_CREATE_ECP_OUT_FLAG_VDL_SET"></a><a id="atomic_create_ecp_out_flag_vdl_set"></a><dl>

### -field <b>ATOMIC_CREATE_ECP_OUT_FLAG_VDL_SET</b>


### -field 0x0008

</dl>
</td>
<td width="60%">
<p>Indicates that a valid data length was set on the file, and that the file size was set to at least the requested valid data
length.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="ATOMIC_CREATE_ECP_OUT_FLAG_OPERATION_MASK"></a><a id="atomic_create_ecp_out_flag_operation_mask"></a><dl>

### -field <b>ATOMIC_CREATE_ECP_OUT_FLAG_OPERATION_MASK</b>


### -field 0x00ff

</dl>
</td>
<td width="60%">
<p>Use this flag value as a mask to determine the supplemental operations that were performed with the create operation.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>ReparseBufferLength</b>

<dd>
<p>The length of the <b>ReparseBuffer</b> member. This value can't exceed the <b>MAXIMUM_REPARSE_DATA_BUFFER_SIZE</b> (16K).</p>
</dd>

### -field <b>ReparseBuffer</b>

<dd>
<p>The optional value that indicates the type of buffer used in the create operation. Possible values are <b>REPARSE_DATA_BUFFER</b> or <b>REPARSE_GUID_DATA_BUFFER</b>.</p>
</dd>

### -field <b>FileSize</b>

<dd>
<p>The optional value that is used with <b>ATOMIC_CREATE_ECP_IN_FLAG_EOF_SPECIFIED</b> to indicate the requested file size to be set on the file.</p>
</dd>

### -field <b>ValidDataLength</b>

<dd>
<p>The optional value that is used with <b>ATOMIC_CREATE_ECP_IN_FLAG_VDL_SPECIFIED</b> to indicate the requested valid data length to be set on the file.</p>
</dd>

### -field <b>FileTimestamps</b>

<dd>
<p>Pointer to an optional <a href="..\ntifs\ns-ntifs--file-timestamps.md">FILE_TIMESTAMPS</a> structure which contains  the last recorded instance of specific actions on a file.</p>
</dd>

### -field <b>FileAttributes</b>

<dd>
<p>Specifies the attributes of a file.</p>
</dd>

### -field <b>UsnSourceInfo</b>

<dd>
<p>Specifies optional Update Sequence Number (USN) source info flags.</p>
</dd>

### -field <b>Usn</b>

<dd>
<p>Specifies the Update Sequence Number (USN). This value is filled at the end of <b>GUID_ECP_ATOMIC_CREATE</b> .</p>
</dd>
</dl>

## -remarks
<p>The GUID used for this structure is the <b>GUID_ECP_ATOMIC_CREATE</b> (<code>4720bd83-52ac-4104-a130-d1ec6a8cc8e5</code>).</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1607</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h</dt>
</dl>
</td>
</tr>
</table>