---
UID: NS.fwpsk._NDIS_SWITCH_NIC_ARRAY
title: NDIS_SWITCH_NIC_ARRAY
author: windows-driver-content
description: The NDIS_SWITCH_NIC_ARRAY structure specifies an array of network adapter configuration parameters.
old-location: netvista\ndis_switch_nic_array.htm
old-project: netvista
ms.assetid: 3509a177-d974-45fb-9387-21780483cbe7
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_SWITCH_NIC_ARRAY,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: fwpsk.h
req.include-header: Ndis.h, Fwpsk.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_SWITCH_NIC_ARRAY
req.alt-loc: Ntddndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# NDIS_SWITCH_NIC_ARRAY structure



## -description
<p>
<p>The <b>NDIS_SWITCH_NIC_ARRAY</b> structure specifies an array of  network adapter configuration parameters. Each element in the array specifies the parameters for a  network adapter that is connected to a port on a Hyper-V extensible switch. Each element is formatted as an <a href="https://msdn.microsoft.com/library/windows/hardware/hh598215">NDIS_SWITCH_NIC_PARAMETERS</a> structure.</p>
</p>
<p>The <b>NDIS_SWITCH_NIC_ARRAY</b> structure specifies an array of  network adapter configuration parameters. Each element in the array specifies the parameters for a  network adapter that is connected to a port on a Hyper-V extensible switch. Each element is formatted as an <a href="https://msdn.microsoft.com/library/windows/hardware/hh598215">NDIS_SWITCH_NIC_PARAMETERS</a> structure.</p>


## -syntax

````
typedef struct _NDIS_SWITCH_NIC_ARRAY {
  NDIS_OBJECT_HEADER Header;
  ULONG              Flags;
  USHORT             FirstElementOffset;
  ULONG              NumElements;
  ULONG              ElementSize;
} NDIS_SWITCH_NIC_ARRAY, *PNDIS_SWITCH_NIC_ARRAY;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>NDIS_SWITCH_NIC_ARRAY</b> structure. This member is formatted as an <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The <b>Type</b> member of <b>Header</b> must be set to NDIS_OBJECT_TYPE_DEFAULT. To specify the version of the <b>NDIS_SWITCH_NIC_ARRAY</b> structure, the <b>Revision</b> member of <b>Header</b> must be set to the following value: </p>
<p></p>
<dl>

### -field <a id="NDIS_SWITCH_NIC_ARRAY_REVISION_1"></a><a id="ndis_switch_nic_array_revision_1"></a>NDIS_SWITCH_NIC_ARRAY_REVISION_1

<dd>
<p>Original version for NDIS 6.30 and later.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_NDIS_SWITCH_NIC_ARRAY_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>Flags</b>

<dd>
<p>A ULONG value that contains a bitwise <b>OR</b> of flags. This member is reserved for NDIS.

</p>
</dd>

### -field <b>FirstElementOffset</b>

<dd>
<p>A USHORT value that specifies the offset, in bytes, to the first element in an array of elements that follow this structure. The offset is measured from the start of the <b>NDIS_SWITCH_NIC_ARRAY</b> structure up to the beginning of the first element. Each element in the array is an <a href="https://msdn.microsoft.com/library/windows/hardware/hh598215">NDIS_SWITCH_NIC_PARAMETERS</a> structure.

</p>
<div class="alert"><b>Note</b>  If <b>NumElements</b> is set to zero, this member is ignored.  </div>
<div> </div>
</dd>

### -field <b>NumElements</b>

<dd>
<p>A ULONG value that specifies the number of <a href="https://msdn.microsoft.com/library/windows/hardware/hh598215">NDIS_SWITCH_NIC_PARAMETERS</a> elements that follow the <b>NDIS_SWITCH_NIC_ARRAY</b> structure. </p>
</dd>

### -field <b>ElementSize</b>

<dd>
<p>A ULONG value that specifies the size, in bytes, of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh598215">NDIS_SWITCH_NIC_PARAMETERS</a> elements that follows the <b>NDIS_SWITCH_NIC_ARRAY</b> structure. </p>
</dd>
</dl>

## -remarks
<p>The <b>NDIS_SWITCH_NIC_ARRAY</b> structure is returned in OID query requests of <a href="https://msdn.microsoft.com/library/windows/hardware/hh598261">OID_SWITCH_NIC_ARRAY</a>. An array of <a href="https://msdn.microsoft.com/library/windows/hardware/hh598215">NDIS_SWITCH_NIC_PARAMETERS</a> structures follows the <b>NDIS_SWITCH_NIC_ARRAY</b> structure in the information buffer that is associated with the OID query request. The <b>InformationBuffer</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710">NDIS_OID_REQUEST</a> structure contains a pointer to this information buffer.</p>

<p>Extensible switch extensions can access individual <a href="https://msdn.microsoft.com/library/windows/hardware/hh598215">NDIS_SWITCH_NIC_PARAMETERS</a> structures inside an <b>NDIS_SWITCH_NIC_ARRAY</b> structure by using the <a href="https://msdn.microsoft.com/library/windows/hardware/hh598213">NDIS_SWITCH_NIC_AT_ARRAY_INDEX</a> macro.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.30 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddndis.h (include Ndis.h or Fwpsk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><b></b></dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598215">NDIS_SWITCH_NIC_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598213">NDIS_SWITCH_NIC_AT_ARRAY_INDEX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598261">OID_SWITCH_NIC_ARRAY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_NIC_ARRAY structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
