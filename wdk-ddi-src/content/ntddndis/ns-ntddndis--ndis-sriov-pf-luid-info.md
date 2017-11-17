---
UID: NS.ntddndis._NDIS_SRIOV_PF_LUID_INFO
title: NDIS_SRIOV_PF_LUID_INFO
author: windows-driver-content
description: The NDIS_SRIOV_PF_LUID_INFO structure specifies the locally unique identifier (LUID) associated with the network adapter's PCI Express (PCIe) Physical Function (PF).
old-location: netvista\ndis_sriov_pf_luid_info.htm
ms.assetid: 03a83321-8396-4400-a15c-84a3b507702d
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_SRIOV_PF_LUID_INFO
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
req.irql: PASSIVE_LEVEL
ms.keywords: NDIS_SRIOV_PF_LUID_INFO, NDIS_SRIOV_PF_LUID_INFO, *PNDIS_SRIOV_PF_LUID_INFO
req.iface: 
---

# NDIS_SRIOV_PF_LUID_INFO structure



## -description
<p>The <b>NDIS_SRIOV_PF_LUID_INFO</b> structure specifies the locally unique identifier (LUID) associated with the network adapter's PCI Express (PCIe) Physical Function (PF).</p>


## -syntax

````
typedef struct _NDIS_SRIOV_PF_LUID_INFO {
  NDIS_OBJECT_HEADER Header;
  LUID               Luid;
} NDIS_SRIOV_PF_LUID_INFO, *PNDIS_SRIOV_PF_LUID_INFO;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>NDIS_SRIOV_PF_LUID_INFO</b> structure. This member is formatted as an <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The miniport driver must set the <b>Type</b> member of <b>Header</b> to NDIS_OBJECT_TYPE_DEFAULT. To specify the version of the <b>NDIS_SRIOV_PF_LUID_INFO</b> structure, the driver must set the <b>Revision</b> member of <b>Header</b> to the following value: </p>
<p></p>
<dl>

### -field <a id="NDIS_SRIOV_PF_LUID_INFO_REVISION_1"></a><a id="ndis_sriov_pf_luid_info_revision_1"></a>NDIS_SRIOV_PF_LUID_INFO_REVISION_1

<dd>
<p>Original version for NDIS 6.30 and later.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_SRIOV_PF_LUID_INFO_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>Luid</b>

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/ff557080">LUID</a> value that is associated with the PF network adapter. For more information, see the Remarks section.</p>
</dd>
</dl>

## -remarks
<p>NDIS generates an LUID for the PF  before NDIS calls the <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>
 function of the miniport driver for the PF. This LUID is valid until NDIS calls the PF miniport driver's <a href="https://msdn.microsoft.com/b8d452b4-bef3-4991-87cf-fac15bedfde4">MiniportHaltEx</a> function.</p>

<p>An overlying driver queries this LUID through OID query requests of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451864">OID_SRIOV_PF_LUID</a>. </p>

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
<dt>Ntddndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><b></b></dt>
<dt>
<a href="https://msdn.microsoft.com/b8d452b4-bef3-4991-87cf-fac15bedfde4">MiniportHaltEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565972">NDIS_MINIPORT_INIT_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451864">OID_SRIOV_PF_LUID</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SRIOV_PF_LUID_INFO structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
