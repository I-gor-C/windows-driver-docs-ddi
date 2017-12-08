---
UID: NF.wdfcompaniontarget.WdfCompanionTargetWdmGetCompanionProcess
title: WdfCompanionTargetWdmGetCompanionProcess function
author: windows-driver-content
description: For internal use only.
old-location: wdf\wdfcompaniontargetwdmgetcompanionprocess.htm
old-project: wdf
ms.assetid: 589c5076-e283-4cf4-bd9f-52a465794b06
ms.author: windowsdriverdev
ms.date: 11/30/2017
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
req.product: Windows 10 or later.
---

# WdfCompanionTargetWdmGetCompanionProcess function



## -description

			For internal use only.


## -syntax

````
PEPROCESS WdfCompanionTargetWdmGetCompanionProcess(
  _In_ WDFCOMPANIONTARGET CompanionTarget
);
````


## -parameters

### -param CompanionTarget [in]


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum KMDF version
</th>
<td width="70%">
1.23
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wdfcompaniontarget.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
&lt;= DISPATCH_LEVEL
</td>
</tr>
</table>