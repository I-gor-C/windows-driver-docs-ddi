---
UID: NS.ndis._NET_BUFFER_LIST_POOL_PARAMETERS
title: NET_BUFFER_LIST_POOL_PARAMETERS
author: windows-driver-content
description: The NET_BUFFER_LIST_POOL_PARAMETERS structure defines the parameters for a pool of NET_BUFFER_LIST structures.
old-location: netvista\net_buffer_list_pool_parameters.htm
old-project: netvista
ms.assetid: DBB172A0-957E-4FAC-9727-D72B060E3193
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NET_BUFFER_LIST_POOL_PARAMETERS, NET_BUFFER_LIST_POOL_PARAMETERS, *PNET_BUFFER_LIST_POOL_PARAMETERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NET_BUFFER_LIST_POOL_PARAMETERS
req.alt-loc: ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section
req.iface: 
---

# NET_BUFFER_LIST_POOL_PARAMETERS structure



## -description
<p>
<p>The <b>NET_BUFFER_LIST_POOL_PARAMETERS</b> structure defines the parameters for a pool of <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structures.</p>
</p>
<p>The <b>NET_BUFFER_LIST_POOL_PARAMETERS</b> structure defines the parameters for a pool of <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structures.</p>


## -syntax

````
typedef struct _NET_BUFFER_LIST_POOL_PARAMETERS {
  NDIS_OBJECT_HEADER Header;
  UCHAR              ProtocolId;
  BOOLEAN            fAllocateNetBuffer;
  USHORT             ContextSize;
  ULONG              PoolTag;
  ULONG              DataSize;
} NET_BUFFER_LIST_POOL_PARAMETERS, *PNET_BUFFER_LIST_POOL_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>NET_BUFFER_LIST_POOL_PARAMETERS</b> structure. This member is formatted as an <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The miniport driver must set the <b>Type</b> member of <b>Header</b> to NDIS_OBJECT_TYPE_DEFAULT. To specify the version of the <b>NET_BUFFER_LIST_POOL_PARAMETERS</b> structure, the driver must set the <b>Revision</b> member of <b>Header</b> to the following value: </p>
<p></p>
<dl>

### -field <a id="NET_BUFFER_LIST_POOL_PARAMETERS_REVISION_1"></a><a id="net_buffer_list_pool_parameters_revision_1"></a>NET_BUFFER_LIST_POOL_PARAMETERS_REVISION_1

<dd>
<p>Original version for NDIS 6.0.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_NET_BUFFER_LIST_POOL_PARAMETERS_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>ProtocolId</b>

<dd>
<p>The type of caller. Miniport, filter, and intermediate drivers set this field to zero
       (NDIS_PROTOCOL_ID_DEFAULT). Protocol drivers use one of the following values:
       </p>
<p></p>
<dl>

### -field <a id="NDIS_PROTOCOL_ID_DEFAULT"></a><a id="ndis_protocol_id_default"></a>NDIS_PROTOCOL_ID_DEFAULT

<dd>
<p>Specifies a default protocol driver identifier.</p>
</dd>

### -field <a id="NDIS_PROTOCOL_ID_TCP_IP"></a><a id="ndis_protocol_id_tcp_ip"></a>NDIS_PROTOCOL_ID_TCP_IP

<dd>
<p>Specifies the TCP/IP protocol.</p>
</dd>

### -field <a id="NDIS_PROTOCOL_ID_IPX"></a><a id="ndis_protocol_id_ipx"></a>NDIS_PROTOCOL_ID_IPX

<dd>
<p>Specifies the IPX protocol.</p>
</dd>

### -field <a id="NDIS_PROTOCOL_ID_NBF"></a><a id="ndis_protocol_id_nbf"></a>NDIS_PROTOCOL_ID_NBF

<dd>
<p>Specifies the NetBEUI protocol.</p>
</dd>
</dl>
</dd>

### -field <b>fAllocateNetBuffer</b>

<dd>
<p>If this member is set to TRUE, NDIS allocates a pool of <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structures. Each allocated <b>NET_BUFFER_LIST</b> structure is initialized with one 
       <a href="..\ndis\ns-ndis--net-buffer.md">NET_BUFFER</a> structure. </p>
<p>If this member is set to FALSE, NDIS allocates a pool of <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structures. Each allocated <b>NET_BUFFER_LIST</b> structure is not initialized  to contain any 
       <a href="..\ndis\ns-ndis--net-buffer.md">NET_BUFFER</a> structures.</p>
<p>For more information, see the Remarks section.</p>
</dd>

### -field <b>ContextSize</b>

<dd>
<p>The size, in bytes, of the preallocated 
       <a href="..\ndis\ns-ndis--net-buffer-list-context.md">NET_BUFFER_LIST_CONTEXT</a> structure
       data that NDIS should provide for the NET_BUFFER_LIST structures in this pool. The 
       <b>ContextSize</b> must be a multiple of the value that is defined by MEMORY_ALLOCATION_ALIGNMENT.</p>
</dd>

### -field <b>PoolTag</b>

<dd>
<p>A kernel pool tag that the caller uses when it allocates NET_BUFFER_LIST structures from this
       pool. The tag is a string, delimited by single quotation marks, with up to four characters, usually
       specified in reversed order. The kernel pool tag helps NDIS to identify the owner of the
       <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structures that are allocated from this pool.</p>
</dd>

### -field <b>DataSize</b>

<dd>
<p>The default data size, in bytes, for data buffers that are associated with this 
       <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> pool, if any. NDIS uses
       this value to set the size of any data buffers that it allocates for any associated 
       <a href="..\ndis\ns-ndis--net-buffer.md">NET_BUFFER</a> structures. 
       </p>
<p>For more information, see the Remarks section.</p>
</dd>
</dl>

## -remarks
<p>If 
       <b>fAllocateNetBuffer</b> is set to FALSE, NDIS will not allocate <a href="..\ndis\ns-ndis--net-buffer.md">NET_BUFFER</a> structures, and 
       <b>DataSize</b> should be set to zero.</p>

<p>If 
       <b>DataSize</b> is not zero, 
       <b>fAllocateNetBuffer</b> must be set to TRUE. This causes NDIS to allocate the <a href="..\ndis\ns-ndis--net-buffer.md">NET_BUFFER</a> structure with a data buffer
       of the specified size.</p>

<p>If 
       <b>DataSize</b> is zero and 
       <b>fAllocateNetBuffer</b> is <b>TRUE</b>, NDIS allocates the <a href="..\ndis\ns-ndis--net-buffer.md">NET_BUFFER</a> structure but not the data
       buffer.</p>

<p>The <i>Parameters</i> parameter of the <a href="..\ndis\nf-ndis-ndisallocatenetbufferlistpool.md">NdisAllocateNetBufferListPool</a> function contains a pointer to an <b>NET_BUFFER_LIST_POOL_PARAMETERS</b> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nf-ndis-ndisallocatenetbufferlistpool.md">NdisAllocateNetBufferListPool</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--net-buffer.md">NET_BUFFER</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--net-buffer-list-data.md">NET_BUFFER_LIST_DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NET_BUFFER_LIST_POOL_PARAMETERS structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
