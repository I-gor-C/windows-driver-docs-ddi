---
UID: NS.netdispumdddi._MIRACAST_CALLBACKS
title: MIRACAST_CALLBACKS
author: windows-driver-content
description: Contains pointers to wireless display (Miracast) runtime callback functions that the Miracast user-mode driver can call.
old-location: display\miracast_callbacks.htm
old-project: display
ms.assetid: 2168a4d8-a33d-4534-b4e8-126a41e528f5
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: MIRACAST_CALLBACKS, MIRACAST_CALLBACKS, *PMIRACAST_CALLBACKS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: netdispumdddi.h
req.include-header: Netdispumdddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MIRACAST_CALLBACKS
req.alt-loc: Netdispumdddi.h
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

# MIRACAST_CALLBACKS structure



## -description
<p>Contains pointers to wireless display (Miracast) runtime callback functions that the Miracast user-mode driver can call.</p>


## -syntax

````
typedef struct _MIRACAST_CALLBACKS {
  PFN_REPORT_SESSION_STATUS           ReportSessionStatus;
  PFN_MIRACAST_IO_CONTROL             MiracastIoControl;
  PFN_REPORT_STATISTIC                ReportStatistic;
  PFN_GET_NEXT_CHUNK_DATA             GetNextChunkData;
  PFN_REGISTER_DATARATE_NOTIFICATIONS RegisterForDataRateNotifications;
} MIRACAST_CALLBACKS, *PMIRACAST_CALLBACKS;
````


## -struct-fields
<dl>

### -field ReportSessionStatus

<dd>
<p>A pointer to the <a href="..\netdispumdddi\nc-netdispumdddi-pfn-report-session-status.md">ReportSessionStatus</a>   function.</p>
</dd>

### -field MiracastIoControl

<dd>
<p>A pointer to the <a href="..\netdispumdddi\nc-netdispumdddi-pfn-miracast-io-control.md">MiracastIoControl</a>   function.</p>
</dd>

### -field ReportStatistic

<dd>
<p>A pointer to the    <a href="..\netdispumdddi\nc-netdispumdddi-pfn-report-statistic.md">ReportStatistic</a> function.</p>
</dd>

### -field GetNextChunkData

<dd>
<p>A pointer to the <a href="..\netdispumdddi\nc-netdispumdddi-pfn-get-next-chunk-data.md">GetNextChunkData</a>    function.</p>
</dd>

### -field RegisterForDataRateNotifications

<dd>
<p>A pointer to the <a href="..\netdispumdddi\nc-netdispumdddi-pfn-register-datarate-notifications.md">RegisterForDataRateNotifications</a>    function.</p>
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
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Netdispumdddi.h (include Netdispumdddi.h)</dt>
</dl>
</td>
</tr>
</table>