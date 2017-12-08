---
UID: NS.dot11wdi._WDI_RX_METADATA
title: WDI_RX_METADATA
author: windows-driver-content
description: The WDI_RX_METADATA structure defines the RX metadata.
old-location: netvista\wdi_rx_metadata.htm
old-project: netvista
ms.assetid: da1ac5d6-fb17-4034-8448-d582bafda870
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WDI_RX_METADATA, WDI_RX_METADATA, *PWDI_RX_METADATA
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
req.iface: 
---

# WDI_RX_METADATA structure



## -description
<p>The 
  WDI_RX_METADATA structure defines the RX metadata.</p>
<p>The RX Engine specifies this metadata in the <b>rxMetadata</b> section of the <a href="..\dot11wdi\ns-dot11wdi--wdi-frame-metadata.md">WDI_FRAME_METADATA</a> buffer attached to each <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> (in MiniportReserved[0]). Each NET_BUFFER_LIST represents an MPDU.  The IHV miniport driver must not allocate a <a href="..\windot11\ns-windot11-dot11-extsta-recv-context.md">DOT11_EXTSTA_RECV_CONTEXT</a> structure as this is handled by WDI.</p>


## -syntax

````
typedef struct _WDI_RX_METADATA {
  WDI_FRAME_PAYLOAD_TYPE PayloadType;
} WDI_RX_METADATA, *PWDI_RX_METADATA;
````


## -struct-fields
<dl>

### -field PayloadType

<dd>
<p>The payload type, specified for each MPDU.</p>
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
<dt>Dot11wdi.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="..\dot11wdi\ns-dot11wdi--wdi-frame-metadata.md">WDI_FRAME_METADATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WDI_RX_METADATA structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
