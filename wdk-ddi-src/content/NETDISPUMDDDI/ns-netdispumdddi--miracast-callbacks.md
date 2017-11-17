---
UID: NS.netdispumdddi._MIRACAST_CALLBACKS
title: MIRACAST_CALLBACKS
author: windows-driver-content
description: Contains pointers to wireless display (Miracast) runtime callback functions that the Miracast user-mode driver can call.
old-location: display\miracast_callbacks.htm
ms.assetid: 2168a4d8-a33d-4534-b4e8-126a41e528f5
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
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
ms.keywords: MIRACAST_CALLBACKS, MIRACAST_CALLBACKS, *PMIRACAST_CALLBACKS
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

### -field <b>ReportSessionStatus</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/a3e44e55-5c6a-4a79-8caa-3a3b9db6b456">ReportSessionStatus</a>   function.</p>
</dd>

### -field <b>MiracastIoControl</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/df63ec18-79e0-40a6-a412-46071eb8a7fe">MiracastIoControl</a>   function.</p>
</dd>

### -field <b>ReportStatistic</b>

<dd>
<p>A pointer to the    <a href="https://msdn.microsoft.com/13e1afa2-5552-468f-ac6b-3458dedd9b76">ReportStatistic</a> function.</p>
</dd>

### -field <b>GetNextChunkData</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/24b1d89a-4200-41ec-aa73-15b37e4cca6d">GetNextChunkData</a>    function.</p>
</dd>

### -field <b>RegisterForDataRateNotifications</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/81500bb9-27f1-4688-b244-37dfd766f3c8">RegisterForDataRateNotifications</a>    function.</p>
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