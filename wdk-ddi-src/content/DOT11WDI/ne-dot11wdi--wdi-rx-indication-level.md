---
UID: NE.dot11wdi._WDI_RX_INDICATION_LEVEL
title: WDI_RX_INDICATION_LEVEL
author: windows-driver-content
description: The WDI_RX_INDICATION_LEVEL enumeration defines the RX indication levels.
old-location: netvista\wdi_rx_indication_level.htm
ms.assetid: 73ad8d04-c245-4a3c-92ff-4729737ede92
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: dot11wdi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_RX_INDICATION_LEVEL
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
req.irql: 
ms.keywords: SYNTHVOICEPRIORITY_INSTANCE, SYNTHVOICEPRIORITY_INSTANCE, *PSYNTHVOICEPRIORITY_INSTANCE
req.iface: ISynthSinkDMus
---

# WDI_RX_INDICATION_LEVEL enumeration



## -description
<p>The WDI_RX_INDICATION_LEVEL enumeration defines the RX indication levels.</p>


## -syntax

````
typedef enum _WDI_RX_INDICATION_LEVEL { 
  WDI_RX_INDICATION_DISPATCH_GENERAL                           = 0,
  WDI_RX_INDICATION_DISPATCH_FIRST_OF_DPC                      = 1,
  WDI_RX_INDICATION_FROM_RX_RESUME_FRAMES                      = 2,
  WDI_RX_INDICATION_PASSIVE                                    = 3,
  WDI_RX_INDICATION_FLAG_RESOURCES                             = 0x80000000,
  WDI_RX_INDICATION_DISPATCH_GENERAL_WITH_LOW_RESOURCES        = WDI_RX_INDICATION_FLAG_RESOURCES | WDI_RX_INDICATION_DISPATCH_GENERAL,
  WDI_RX_INDICATION_DISPATCH_FIRST_OF_DPC_WITH_LOW_RESSOURCES  = WDI_RX_INDICATION_FLAG_RESOURCES | WDI_RX_INDICATION_DISPATCH_FIRST_OF_DPC,
  WDI_RX_INDICATION_FROM_RX_RESUME_FRAMES_WITH_LOW_RESOURCES   = WDI_RX_INDICATION_FLAG_RESOURCES | WDI_RX_INDICATION_FROM_RX_RESUME_FRAMES,
  WDI_RX_INDICATION_PASSIVE_WITH_LOW_RESOURCES                 = WDI_RX_INDICATION_FLAG_RESOURCES | WDI_RX_INDICATION_PASSIVE
} WDI_RX_INDICATION_LEVEL;
````


## -enum-fields
<dl>

### -field <a id="WDI_RX_INDICATION_DISPATCH_GENERAL"></a><a id="wdi_rx_indication_dispatch_general"></a><b>WDI_RX_INDICATION_DISPATCH_GENERAL</b>

<dd>
<p>Used for subsequent data indications in a DPC. <b>WDI_RX_INDICATION_DISPATCH_FIRST_OF_DPC</b> is used for the first data indication of a DPC.</p>
</dd>

### -field <a id="WDI_RX_INDICATION_DISPATCH_FIRST_OF_DPC"></a><a id="wdi_rx_indication_dispatch_first_of_dpc"></a><b>WDI_RX_INDICATION_DISPATCH_FIRST_OF_DPC</b>

<dd>
<p>Used for the first data indication (<a href="https://msdn.microsoft.com/F2F92DAE-6C13-4EE6-9DE7-B77F5FAFAE60">NdisWdiRxInorderDataIndication</a>) of a DPC.</p>
</dd>

### -field <a id="WDI_RX_INDICATION_FROM_RX_RESUME_FRAMES"></a><a id="wdi_rx_indication_from_rx_resume_frames"></a><b>WDI_RX_INDICATION_FROM_RX_RESUME_FRAMES</b>

<dd>
<p>Used when making data indications in the context of <a href="https://msdn.microsoft.com/483C59C3-8F9C-48A5-B5E4-34A60BAE1B1A">MiniportWdiRxResume</a>.</p>
</dd>

### -field <a id="WDI_RX_INDICATION_PASSIVE"></a><a id="wdi_rx_indication_passive"></a><b>WDI_RX_INDICATION_PASSIVE</b>

<dd>
<p>Used when making data indications at passive level.</p>
</dd>

### -field <a id="WDI_RX_INDICATION_FLAG_RESOURCES"></a><a id="wdi_rx_indication_flag_resources"></a><b>WDI_RX_INDICATION_FLAG_RESOURCES</b>

<dd>
<p>Bitwise OR’d with other enum values to cause RxMgr to set <b>NDIS_RECEIVE_FLAG_RESOURCES</b>.</p>
</dd>

### -field <a id="WDI_RX_INDICATION_DISPATCH_GENERAL_WITH_LOW_RESOURCES"></a><a id="wdi_rx_indication_dispatch_general_with_low_resources"></a><b>WDI_RX_INDICATION_DISPATCH_GENERAL_WITH_LOW_RESOURCES</b>

<dd>
<p>Bitwise OR of <b>WDI_RX_INDICATION_FLAG_RESOURCES</b> and <b>WDI_RX_INDICATION_DISPATCH_GENERAL</b>.</p>
</dd>

### -field <a id="WDI_RX_INDICATION_DISPATCH_FIRST_OF_DPC_WITH_LOW_RESSOURCES"></a><a id="wdi_rx_indication_dispatch_first_of_dpc_with_low_ressources"></a><b>WDI_RX_INDICATION_DISPATCH_FIRST_OF_DPC_WITH_LOW_RESSOURCES</b>

<dd>
<p>Bitwise OR of <b>WDI_RX_INDICATION_FLAG_RESOURCES</b> and <b>WDI_RX_INDICATION_DISPATCH_FIRST_OF_DPC</b>.</p>
</dd>

### -field <a id="WDI_RX_INDICATION_FROM_RX_RESUME_FRAMES_WITH_LOW_RESOURCES"></a><a id="wdi_rx_indication_from_rx_resume_frames_with_low_resources"></a><b>WDI_RX_INDICATION_FROM_RX_RESUME_FRAMES_WITH_LOW_RESOURCES</b>

<dd>
<p>Bitwise OR of <b>WDI_RX_INDICATION_FLAG_RESOURCES</b> and <b>WDI_RX_INDICATION_FROM_RX_RESUME_FRAMES</b>.</p>
</dd>

### -field <a id="WDI_RX_INDICATION_PASSIVE_WITH_LOW_RESOURCES"></a><a id="wdi_rx_indication_passive_with_low_resources"></a><b>WDI_RX_INDICATION_PASSIVE_WITH_LOW_RESOURCES</b>

<dd>
<p>Bitwise OR of <b>WDI_RX_INDICATION_FLAG_RESOURCES</b> and <b>WDI_RX_INDICATION_PASSIVE</b>.</p>
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