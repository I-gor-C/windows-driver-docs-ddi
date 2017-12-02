---
UID: NF.wpprecorder.WppRecorderGetTriageInfo
title: WppRecorderGetTriageInfo
author: windows-driver-content
description: The WppRecorderGetTriageInfo.
old-location: devtest\wpprecordergettriageinfo.htm
old-project: devtest
ms.assetid: D2790496-1F86-4EF0-8AFE-77AC0C89EE05
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: WppRecorderGetTriageInfo
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wpprecorder.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WppRecorderGetTriageInfo
req.alt-loc: wpprecorder.h
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
req.product: Windows 10 or later.
---

# WppRecorderGetTriageInfo function



## -description
<p>The <b>WppRecorderGetTriageInfo</b> method </p>


## -syntax

````
NTSTATUS WppRecorderGetTriageInfo(
  _Out_ PWPP_TRIAGE_INFO WppTriageInfo
);
````


## -parameters
<dl>

### -param WppTriageInfo [out]

<dd>
<p>Pointer to a <a href="..\wpprecorder\ns-wpprecorder--wpp-triage-info.md">WPP_TRIAGE_INFO</a> structure.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if the operation succeeds. Otherwise, one of appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> values</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wpprecorder.h</dt>
</dl>
</td>
</tr>
</table>