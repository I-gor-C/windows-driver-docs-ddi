---
UID: NS.netdma._NET_DMA_PNP_NOTIFICATION
title: NET_DMA_PNP_NOTIFICATION
author: windows-driver-content
description: The NET_DMA_PNP_NOTIFICATION structure specifies a power management notification in the NetDMA interface.
old-location: netvista\net_dma_pnp_notification.htm
old-project: netvista
ms.assetid: 8a505077-dec6-47cc-8730-d68e19309d3b
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NET_DMA_PNP_NOTIFICATION, NET_DMA_PNP_NOTIFICATION, *PNET_DMA_PNP_NOTIFICATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: netdma.h
req.include-header: Netdma.h
req.target-type: Windows
req.target-min-winverclnt: Supported for NetDMA 2.0 and NetDMA 1.1 drivers in Windows Server 2008.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NET_DMA_PNP_NOTIFICATION
req.alt-loc: netdma.h
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

# NET_DMA_PNP_NOTIFICATION structure



## -description

## -syntax

````
typedef struct _NET_DMA_PNP_NOTIFICATION {
  ULONG                         StructureRevision;
  ULONG                         StructureSize;
  NET_DMA_PNP_NOTIFICATION_CODE NotificationCode;
  PVOID                         Buffer;
  ULONG                         BufferLength;
} NET_DMA_PNP_NOTIFICATION, *PNET_DMA_PNP_NOTIFICATION;
````


## -struct-fields
<dl>

### -field <b>StructureRevision</b>

<dd>
<p>The revision for this structure. The NetDMA provider driver must set this member to
     NET_DMA_PNP_NOTIFICATION_REVISION_1.</p>
</dd>

### -field <b>StructureSize</b>

<dd>
<p>The size, in bytes, of the notification structure. This size does not include the size of the
     notification specific data at 
     <b>Buffer</b>, if any. A NetDMA provider driver must set this member to 
     sizeof(NET_DMA_PNP_NOTIFICATION).</p>
</dd>

### -field <b>NotificationCode</b>

<dd>
<p>A value that identifies the DMA provider event. This value must be one of the values from the 
     <a href="..\netdma\ne-netdma--net-dma-pnp-notification-code.md">
     NET_DMA_PNP_NOTIFICATION_CODE</a> enumeration.</p>
</dd>

### -field <b>Buffer</b>

<dd>
<p>A pointer to notification-specific data, if any. NetDMA provider drivers set this member to <b>NULL</b>
     for 
     <b>NetDmaNotificationProviderPowerDown</b> and 
     <b>NetDmaNotificationProviderPowerUp</b> notifications.</p>
</dd>

### -field <b>BufferLength</b>

<dd>
<p>The length, in bytes, of the notification-specific data at the 
     <b>Buffer</b> member. NetDMA provider drivers set this member to zero for 
     <b>NetDmaNotificationProviderPowerDown</b> and 
     <b>NetDmaNotificationProviderPowerUp</b> notifications.</p>
</dd>
</dl>

## -remarks
<p>To send a power management notification to the NetDMA interface, NetDMA provider drivers call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568332">NetDmaPnPEventNotify</a> function and
    provide a pointer to a NET_DMA_PNP_NOTIFICATION structure at the 
    <i>PnPEvent</i> parameter.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported for NetDMA 2.0 and NetDMA 1.1 drivers in Windows Server 2008.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Netdma.h (include Netdma.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568736">NET_DMA_PNP_NOTIFICATION_CODE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568332">NetDmaPnPEventNotify</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NET_DMA_PNP_NOTIFICATION structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
