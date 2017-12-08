---
UID: NS.ntifs._NETWORK_OPEN_ECP_CONTEXT~r1
title: NETWORK_OPEN_ECP_CONTEXT
author: windows-driver-content
description: The NETWORK_OPEN_ECP_CONTEXT structure is used to interpret network ECP contexts on files.
old-location: ifsk\network_open_ecp_context.htm
old-project: ifsk
ms.assetid: 583fe92d-ce81-47b4-bd75-5566a5379790
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NETWORK_OPEN_ECP_CONTEXT, NETWORK_OPEN_ECP_CONTEXT, *PNETWORK_OPEN_ECP_CONTEXT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: This structure is available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NETWORK_OPEN_ECP_CONTEXT
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

# NETWORK_OPEN_ECP_CONTEXT structure



## -description
<p>The <b>NETWORK_OPEN_ECP_CONTEXT</b> structure is used to interpret network ECP contexts on files. </p>


## -syntax

````
typedef struct _NETWORK_OPEN_ECP_CONTEXT {
  USHORT Size;
  USHORT Reserved;
  struct {
    struct {
      NETWORK_OPEN_LOCATION_QUALIFIER  Location;
      NETWORK_OPEN_INTEGRITY_QUALIFIER Integrity;
      ULONG                            Flags;
    } in;
    struct {
      NETWORK_OPEN_LOCATION_QUALIFIER  Location;
      NETWORK_OPEN_INTEGRITY_QUALIFIER Integrity;
      ULONG                            Flags;
    } out;
  };
} NETWORK_OPEN_ECP_CONTEXT, *PNETWORK_OPEN_ECP_CONTEXT;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>The size, in bytes, of this structure. </p>
</dd>

### -field Reserved

<dd>
<p>Reserved. Must be set to zero. </p>
</dd>

### -field ( unnamed struct )

<dd>
<p>A structure that contains restrictions for opening the file and to apply to the file after it is opened. </p>
<dl>

### -field in

<dd>
<p>A structure in the DUMMYSTRUCTNAME structure that contains restrictions for opening a file.</p>
<p></p>
<dl>

### -field Location

<dd>
<p>A <a href="..\ntifs\ne-ntifs-network-open-location-qualifier.md">NETWORK_OPEN_LOCATION_QUALIFIER</a>-typed value that specifies the location restriction to attach to the file. </p>
</dd>

### -field Integrity

<dd>
<p>This member is currently not implemented and should be ignored. </p>
<p>A <a href="..\ntifs\ne-ntifs-network-open-integrity-qualifier.md">NETWORK_OPEN_INTEGRITY_QUALIFIER</a>-typed value that specifies the integrity restriction to attach to the file. </p>
</dd>

### -field Flags

<dd>
<p>Supported starting with Windows 7.</p>
<p>A value that specifies attributes for the file. This member is a bitwise OR of any of the flags in the following table.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>NETWORK_OPEN_ECP_IN_FLAG_DISABLE_HANDLE_COLLAPSING</p>
<p>(0x1)</p>
</td>
<td>
<p>This flag indicates to the SMB or SMB2 redirector that the incoming open request must not be piggybacked and collapsed onto an existing open handle to the same file.</p>
</td>
</tr>
<tr>
<td>
<p>NETWORK_OPEN_ECP_IN_FLAG_DISABLE_HANDLE_DURABILITY</p>
<p>(0x2)</p>
</td>
<td>
<p>This flag causes the SMB2 redirector to disable durability on this open handle. For more information about opening a file for durable operation, see <a href="http://go.microsoft.com/fwlink/p/?linkid=160861">Application Requests Creating a File Opened for Durable Operation</a>.</p>
</td>
</tr>
<tr>
<td>
<p>NETWORK_OPEN_ECP_IN_FLAG_DISABLE_OPLOCKS</p>
<p>(0x4)</p>
</td>
<td>
<p>This flag indicates to the SMB or SMB2 redirector not to grant oplocks for the  incoming open request.</p>
<p>This flag is available starting with Windows 8.</p>
</td>
</tr>
<tr>
<td>
<p>NETWORK_OPEN_ECP_IN_FLAG_FORCE_BUFFERED_SYNCHRONOUS_IO_HACK </p>
<p>(0x80000000)</p>
</td>
<td>
<p>This flag is reserved for internal use and must not be used by applications.</p>
<p>This flag forces the redirector to use synchronous I/O even though the handle was opened for asynchronous I/O.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>
</dd>

### -field out

<dd>
<p>A structure in the DUMMYSTRUCTNAME structure that contains information that a file provides after it is opened.</p>
<p></p>
<dl>

### -field Location

<dd>
<p>A <a href="..\ntifs\ne-ntifs-network-open-location-qualifier.md">NETWORK_OPEN_LOCATION_QUALIFIER</a>-typed value that specifies the location restriction to attach to the file. </p>
</dd>

### -field Integrity

<dd>
<p>This member is currently not implemented and should be ignored. </p>
<p>A <a href="..\ntifs\ne-ntifs-network-open-integrity-qualifier.md">NETWORK_OPEN_INTEGRITY_QUALIFIER</a>-typed value that specifies the integrity restriction to attach to the file. </p>
</dd>

### -field Flags

<dd>
<p>Supported starting with Windows 7.</p>
<p>A value that specifies attributes for the file. This member is a bitwise OR of any of the flags in the following table.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>NETWORK_OPEN_ECP_IN_FLAG_DISABLE_HANDLE_COLLAPSING </p>
<p>(0x1)</p>
</td>
<td>
<p>This flag indicates to the SMB or SMB2 redirector that the incoming open request must not be piggybacked and collapsed onto an existing open handle to the same file.</p>
</td>
</tr>
<tr>
<td>
<p>NETWORK_OPEN_ECP_IN_FLAG_DISABLE_HANDLE_DURABILITY </p>
<p>(0x2)</p>
</td>
<td>
<p>This flag causes the SMB2 redirector to disable durability on this open handle. For more information about opening a file for durable operation, see <a href="http://go.microsoft.com/fwlink/p/?linkid=160861">Application Requests Creating a File Opened for Durable Operation</a>.</p>
</td>
</tr>
<tr>
<td>
<p>NETWORK_OPEN_ECP_IN_FLAG_FORCE_BUFFERED_SYNCHRONOUS_IO_HACK </p>
<p>(0x80000000)</p>
</td>
<td>
<p>This flag is reserved for internal use and must not be used by applications.</p>
<p>This flag forces the redirector to use synchronous I/O even though the handle was opened for asynchronous I/O.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>For information about how to use ECPs to associate extra information with a file when the file is created, see <a href="ifsk.using_extra_create_parameters_with_an_irp_mj_create_operation">Using Extra Create Parameters with an IRP_MJ_CREATE Operation</a>. </p>

<p>The NETWORK_OPEN_ECP_CONTEXT structure is read-only. You should use it to retrieve information about the network ECP context on a file only. For more information about this issue, see <a href="ifsk.system_defined_ecps">System-Defined ECPs</a>.</p>

<p>If a caller must verify that the file system acknowledged the <b>NETWORK_OPEN_ECP_CONTEXT</b> context structure, the caller should call the <a href="..\fltkernel\nf-fltkernel-fltisecpacknowledged.md">FltIsEcpAcknowledged</a> or <a href="..\ntifs\nf-ntifs-fsrtlisecpacknowledged.md">FsRtlIsEcpAcknowledged</a> routine on the ECP after the operation is complete.</p>

<p>Drivers that run on Windows 7 and later versions of Windows and that must interpret network ECP contexts on files that reside on Windows Vista must use the <a href="..\ntifs\ns-ntifs--network-open-ecp-context-v0.md">NETWORK_OPEN_ECP_CONTEXT_V0</a> structure instead. Drivers that run on Windows Vista and later versions of Windows use the <b>NETWORK_OPEN_ECP_CONTEXT</b> structure to interpret network ECP contexts on files. However, the <b>DUMMYSTRUCTNAME.in.Flags</b> and <b>DUMMYSTRUCTNAME.out.Flags</b> members are only supported starting with Windows 7. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>This structure is available starting with Windows Vista.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntifs\ns-ntifs--network-open-ecp-context-v0.md">NETWORK_OPEN_ECP_CONTEXT_V0</a>
</dt>
<dt>
<a href="..\ntifs\ne-ntifs-network-open-integrity-qualifier.md">NETWORK_OPEN_INTEGRITY_QUALIFIER</a>
</dt>
<dt>
<a href="..\ntifs\ne-ntifs-network-open-location-qualifier.md">NETWORK_OPEN_LOCATION_QUALIFIER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20NETWORK_OPEN_ECP_CONTEXT structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
