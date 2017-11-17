---
UID: NS.ndis._NDIS_PD_PROVIDER_DISPATCH
title: NDIS_PD_PROVIDER_DISPATCH
author: windows-driver-content
description: This structure is used as input for the OID_PD_OPEN_PROVIDER and serves as a container for all the provider's driver routines.
old-location: netvista\ndis_pd_provider_dispatch.htm
ms.assetid: E93B8A07-7C06-470B-9B26-8D59C2685D2C
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_PD_PROVIDER_DISPATCH
req.alt-loc: Ndis.h
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
ms.keywords: NDIS_PD_PROVIDER_DISPATCH, NDIS_PD_PROVIDER_DISPATCH
req.iface: 
---

# NDIS_PD_PROVIDER_DISPATCH structure



## -description
<p>This structure is used as input for the <a href="https://msdn.microsoft.com/library/windows/hardware/dn931852">OID_PD_OPEN_PROVIDER</a> and serves as a container for all the provider's driver routines.</p>


## -syntax

````
typedef struct _NDIS_PD_PROVIDER_DISPATCH {
  NDIS_OBJECT_HEADER                     Header;
  ULONG                                  Flags;
  NDIS_PD_ALLOCATE_QUEUE_HANDLER         NdisPDAllocateQueue;
  NDIS_PD_FREE_QUEUE_HANDLER             NdisPDFreeQueue;
  NDIS_PD_ON_RSS_RECEIVE_QUEUES_HANDLER  NdisPDOnRssReceiveQueues;
  NDIS_PD_OFF_RSS_RECEIVE_QUEUES_HANDLER NdisPDOffRssReceiveQueues;
  NDIS_PD_ALLOCATE_COUNTER_HANDLER       NdisPDAllocateCounter;
  NDIS_PD_FREE_COUNTER_HANDLER           NdisPDFreeCounter;
  NDIS_PD_QUERY_COUNTER_HANDLER          NdisPDQueryCounter;
  NDIS_PD_SET_RECEIVE_FILTER_HANDLER     NdisPDSetReceiveFilter;
  NDIS_PD_CLEAR_RECEIVE_FILTER_HANDLER   NdisPDClearReceiveFilter;
} NDIS_PD_PROVIDER_DISPATCH, *PNDIS_PD_PROVIDER_DISPATCH;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the <b>NDIS_PD_PROVIDER_DISPATCH</b> structure. Set the members of this structure as follows:</p>
<ul>
<li><b>Type</b> = <b>NDIS_OBJECT_TYPE_DEFAULT</b></li>
<li><b>Revision</b> = <b>NDIS_PD_PROVIDER_DISPATCH_REVISION_1</b></li>
<li><b>Size</b> = <b>NDIS_SIZEOF_PD_PROVIDER_DISPATCH_REVISION_1</b></li>
</ul>
</dd>

### -field <b>Flags</b>

<dd>
<p>This member is reserved and must be set to 0 by the provider.</p>
</dd>

### -field <b>NdisPDAllocateQueue</b>

<dd>
<p>See <a href="https://msdn.microsoft.com/E9091C69-0E21-40CC-B3D3-1F770ABA0D47">NdisPDAllocateQueue</a>.</p>
</dd>

### -field <b>NdisPDFreeQueue</b>

<dd>
<p>See <a href="https://msdn.microsoft.com/1DE8582C-AF11-4CBA-8F4C-159266A7F3BA">NdisPDFreeQueue</a>.</p>
</dd>

### -field <b>NdisPDOnRssReceiveQueues</b>

<dd>
<p>See <a href="https://msdn.microsoft.com/26A78067-74F2-49C4-897E-44A0A24793DE">NdisPDOnRssReceiveQueues</a>.</p>
</dd>

### -field <b>NdisPDOffRssReceiveQueues</b>

<dd>
<p>See <a href="https://msdn.microsoft.com/A12D59BF-600F-4F76-946D-5531C139B0F8">NdisPDOffRssReceiveQueues</a>.</p>
</dd>

### -field <b>NdisPDAllocateCounter</b>

<dd>
<p>See <a href="https://msdn.microsoft.com/86AA537D-952F-4A7A-ACA4-24B8C1AE932A">NdisPDAllocateCounter</a>.</p>
</dd>

### -field <b>NdisPDFreeCounter</b>

<dd>
<p>See <a href="https://msdn.microsoft.com/60C47437-A999-4F82-B144-6F77410E5C07">NdisPDFreeCounter</a>.</p>
</dd>

### -field <b>NdisPDQueryCounter</b>

<dd>
<p>See <a href="https://msdn.microsoft.com/C4860A43-2C53-4967-81A8-41FFF5CD2A5E">NdisPDQueryCounter</a>.</p>
</dd>

### -field <b>NdisPDSetReceiveFilter</b>

<dd>
<p>See <a href="https://msdn.microsoft.com/49587142-9C84-4F73-BE0C-D256A8E6BF4B">NdisPDSetReceiveFilter</a>.</p>
</dd>

### -field <b>NdisPDClearReceiveFilter</b>

<dd>
<p>See <a href="https://msdn.microsoft.com/C91F2E5D-C37F-48A9-9AE0-F5A8C5D8F54D">NdisPDClearReceiveFilter</a>.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
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
<dt>Ndis.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PD_PROVIDER_DISPATCH structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
