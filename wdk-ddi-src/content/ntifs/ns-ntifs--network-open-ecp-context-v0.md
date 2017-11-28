---
UID: NS.ntifs._NETWORK_OPEN_ECP_CONTEXT_V0
title: NETWORK_OPEN_ECP_CONTEXT_V0
author: windows-driver-content
description: The NETWORK_OPEN_ECP_CONTEXT_V0 structure is used to interpret network ECP contexts on files.
old-location: ifsk\network_open_ecp_context_v0.htm
old-project: ifsk
ms.assetid: 447d623a-88cb-4d3d-8b05-4f5624c707ad
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: NETWORK_OPEN_ECP_CONTEXT_V0, NETWORK_OPEN_ECP_CONTEXT_V0, *PNETWORK_OPEN_ECP_CONTEXT_V0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: This structure is available starting with Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NETWORK_OPEN_ECP_CONTEXT_V0
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

# NETWORK_OPEN_ECP_CONTEXT_V0 structure



## -description
<p>The NETWORK_OPEN_ECP_CONTEXT_V0 structure is used to interpret network ECP contexts on files. </p>


## -syntax

````
typedef struct _NETWORK_OPEN_ECP_CONTEXT_V0 {
  USHORT Size;
  USHORT Reserved;
  struct {
    struct {
      NETWORK_OPEN_LOCATION_QUALIFIER  Location;
      NETWORK_OPEN_INTEGRITY_QUALIFIER Integrity;
    } in;
    struct {
      NETWORK_OPEN_LOCATION_QUALIFIER  Location;
      NETWORK_OPEN_INTEGRITY_QUALIFIER Integrity;
    } out;
  } DUMMYSTRUCTNAME;
} NETWORK_OPEN_ECP_CONTEXT_V0, *PNETWORK_OPEN_ECP_CONTEXT_V0;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure. </p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved. Must be set to zero. </p>
</dd>

### -field <b>DUMMYSTRUCTNAME</b>

<dd>
<p>A structure that contains restrictions to apply for opening the file and to apply to the file after it is opened.  </p>
<dl>

### -field <b>in</b>

<dd>
<p>A structure in the DUMMYSTRUCTNAME structure that contains restrictions for opening a file.</p>
<p></p>
<dl>

### -field <a id="Location"></a><a id="location"></a><a id="LOCATION"></a><b>Location</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff550908">NETWORK_OPEN_LOCATION_QUALIFIER</a>-typed value that specifies the location restriction to attach to the file. </p>
</dd>

### -field <a id="Integrity"></a><a id="integrity"></a><a id="INTEGRITY"></a><b>Integrity</b>

<dd>
<p>This member is currently not implemented and should be ignored. </p>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff550902">NETWORK_OPEN_INTEGRITY_QUALIFIER</a>-typed value that specifies the integrity restriction to attach to the file. </p>
</dd>
</dl>
</dd>

### -field <b>out</b>

<dd>
<p>A structure in the DUMMYSTRUCTNAME structure that contains information that a file provides after it is opened.</p>
<p></p>
<dl>

### -field <a id="Location"></a><a id="location"></a><a id="LOCATION"></a><b>Location</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff550908">NETWORK_OPEN_LOCATION_QUALIFIER</a>-typed value that specifies the location restriction to attach to the file. </p>
</dd>

### -field <a id="Integrity"></a><a id="integrity"></a><a id="INTEGRITY"></a><b>Integrity</b>

<dd>
<p>This member is currently not implemented and should be ignored. </p>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff550902">NETWORK_OPEN_INTEGRITY_QUALIFIER</a>-typed value that specifies the integrity restriction to attach to the file. </p>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>For information about how to use ECPs to associate extra information with a file when the file is created, see <a href="ifsk.using_extra_create_parameters_with_an_irp_mj_create_operation">Using Extra Create Parameters with an IRP_MJ_CREATE Operation</a>. </p>

<p>The NETWORK_OPEN_ECP_CONTEXT_V0 structure is read-only. You should use it to retrieve information about the network ECP context on a file only. For more information about this issue, see <a href="ifsk.system_defined_ecps">System-Defined ECPs</a>.</p>

<p>If a caller must verify that the file system acknowledged the NETWORK_OPEN_ECP_CONTEXT_V0 context structure, the caller should call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543321">FltIsEcpAcknowledged</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff546808">FsRtlIsEcpAcknowledged</a> routine on the ECP after the operation is complete.</p>

<p>In most cases, drivers that run on Windows Vista and later versions of Windows use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550896">NETWORK_OPEN_ECP_CONTEXT</a> structure to interpret network ECP contexts on files. However, drivers that run on Windows 7 and later versions of Windows and that must interpret network ECP contexts on files that reside on Windows Vista must use the NETWORK_OPEN_ECP_CONTEXT_V0 structure instead. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>This structure is available starting with Windows 7. </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550896">NETWORK_OPEN_ECP_CONTEXT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550902">NETWORK_OPEN_INTEGRITY_QUALIFIER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550908">NETWORK_OPEN_LOCATION_QUALIFIER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20NETWORK_OPEN_ECP_CONTEXT_V0 structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
