---
UID: NE.wditypes._WDI_IHV_TASK_PRIORITY
title: WDI_IHV_TASK_PRIORITY
author: windows-driver-content
description: The WDI_IHV_TASK_PRIORITY enumeration defines IHV task priorities.
old-location: netvista\wdi_ihv_task_priority.htm
old-project: netvista
ms.assetid: 606CF45C-5398-4157-92A7-382B6162D806
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDF_WORKITEM_CONFIG, WDF_WORKITEM_CONFIG, *PWDF_WORKITEM_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wditypes.hpp
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_IHV_TASK_PRIORITY
req.alt-loc: wditypes.hpp
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
req.product: Windows 10 or later.
---

# WDI_IHV_TASK_PRIORITY enumeration



## -description
<p>The WDI_IHV_TASK_PRIORITY enumeration defines IHV task priorities.</p>


## -syntax

````
typedef enum _WDI_IHV_TASK_PRIORITY { 
  WDI_IHV_TASK_PRIORITY_HIGH    = 1,
  WDI_IHV_TASK_PRIORITY_MEDIUM  = 2,
  WDI_IHV_TASK_PRIORITY_LOW     = 3
} WDI_IHV_TASK_PRIORITY;
````


## -enum-fields
<dl>

### -field <a id="WDI_IHV_TASK_PRIORITY_HIGH"></a><a id="wdi_ihv_task_priority_high"></a><b>WDI_IHV_TASK_PRIORITY_HIGH</b>

<dd>
<p>High priority.</p>
</dd>

### -field <a id="WDI_IHV_TASK_PRIORITY_MEDIUM"></a><a id="wdi_ihv_task_priority_medium"></a><b>WDI_IHV_TASK_PRIORITY_MEDIUM</b>

<dd>
<p>Medium priority.</p>
</dd>

### -field <a id="WDI_IHV_TASK_PRIORITY_LOW"></a><a id="wdi_ihv_task_priority_low"></a><b>WDI_IHV_TASK_PRIORITY_LOW</b>

<dd>
<p>Low priority.</p>
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
<dt>Wditypes.hpp</dt>
</dl>
</td>
</tr>
</table>