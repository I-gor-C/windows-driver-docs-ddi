---
UID: NS.DOT11WDI._WDI_RX_METADATA
title: _WDI_RX_METADATA
author: windows-driver-content
description: The WDI_RX_METADATA structure defines the RX metadata.
old-location: netvista\wdi_rx_metadata.htm
old-project: NetVista
ms.assetid: da1ac5d6-fb17-4034-8448-d582bafda870
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _WDI_RX_METADATA, PWDI_RX_METADATA, *PWDI_RX_METADATA, WDI_RX_METADATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dot11wdi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_RX_METADATA
req.alt-loc: dot11wdi.h
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
---

# _WDI_RX_METADATA structure



## -description
The 
  WDI_RX_METADATA structure defines the RX metadata.

The RX Engine specifies this metadata in the <b>rxMetadata</b> section of the <a href="netvista.wdi_frame_metadata">WDI_FRAME_METADATA</a> buffer attached to each <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> (in MiniportReserved[0]). Each NET_BUFFER_LIST represents an MPDU.  The IHV miniport driver must not allocate a <a href="..\windot11\ns-windot11-dot11_extsta_recv_context.md">DOT11_EXTSTA_RECV_CONTEXT</a> structure as this is handled by WDI.



## -syntax

````
typedef struct _WDI_RX_METADATA {
  WDI_FRAME_PAYLOAD_TYPE PayloadType;
} WDI_RX_METADATA, *PWDI_RX_METADATA;
````


## -struct-fields

### -field PayloadType

The payload type, specified for each MPDU.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 10

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2016

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Dot11wdi.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.net_buffer_list">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="netvista.wdi_frame_metadata">WDI_FRAME_METADATA</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20WDI_RX_METADATA structure%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

