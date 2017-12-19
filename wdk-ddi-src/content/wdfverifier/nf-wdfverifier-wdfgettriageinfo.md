---
UID: NF.wdfverifier.WdfGetTriageInfo
title: WdfGetTriageInfo function
author: windows-driver-content
description: The WdfGetTriageInfo method is reserved for internal use only.
old-location: wdf\wdfgettriageinfo.htm
old-project: wdf
ms.assetid: F6B1DC49-B691-45E4-8DE9-ADCD73D90ADE
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfGetTriageInfo
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfverifier.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 2.0
req.alt-api: WdfGetTriageInfo
req.alt-loc: Wdfverifier.h
req.ddi-compliance: DriverCreate
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.product: Windows 10 or later.
---

# WdfGetTriageInfo function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfGetTriageInfo</b> method is reserved for internal use only.



## -syntax

````
PVOID WdfGetTriageInfo(void);
````


## -parameters


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.11

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
2.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfverifier.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>
</td>
</tr>
</table>