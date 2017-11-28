---
UID: NF.wdfcompaniontarget.WdfCompanionTargetWdmGetCompanionProcess
title: WdfCompanionTargetWdmGetCompanionProcess
author: windows-driver-content
description: For internal use only.
old-location: wdf\wdfcompaniontargetwdmgetcompanionprocess.htm
old-project: wdf
ms.assetid: 589c5076-e283-4cf4-bd9f-52a465794b06
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfCompanionTargetWdmGetCompanionProcess
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfcompaniontarget.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.23
req.umdf-ver: 
req.alt-api: WdfCompanionTargetWdmGetCompanionProcess
req.alt-loc: wdfcompaniontarget.h
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

# WdfCompanionTargetWdmGetCompanionProcess function



## -description
<p>
			For internal use only.</p>


## -syntax

````
PEPROCESS WdfCompanionTargetWdmGetCompanionProcess(
  _In_ WDFCOMPANIONTARGET CompanionTarget
);
````


## -parameters
<dl>

### -param <i>CompanionTarget</i> [in]

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.23</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfcompaniontarget.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>