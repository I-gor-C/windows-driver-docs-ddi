---
UID: NF.wpprecorder.WppRecorderDumpLiveDriverData
title: WppRecorderDumpLiveDriverData
author: windows-driver-content
description: The WppRecorderDumpLiveDriverData method gets the buffer associated with the specified Inflight Trace Recorder log.
old-location: devtest\wpprecorderdumplivedriverdata.htm
old-project: devtest
ms.assetid: FE3DE2A8-8EE5-4F34-BEE6-731987E5F5BD
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: WppRecorderDumpLiveDriverData
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wpprecorder.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WppRecorderDumpLiveDriverData
req.alt-loc: Wpprecorder.h
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

# WppRecorderDumpLiveDriverData function



## -description
<p>The <a href="..\wpprecorder\nf-wpprecorder-wpprecorderdumplivedriverdata.md">WppRecorderDumpLiveDriverData</a> method gets the buffer associated with the specified Inflight Trace Recorder log.</p>


## -syntax

````
NTSTATUS WppRecorderDumpLiveDriverData(
   NULL OutBuffer,
   NULL OutBufferLength,
   NULL Guid
);
````


## -parameters
<dl>

### -param <i>OutBuffer</i> 

<dd>
<p>Pointer to the buffer that was allocated by WppRecorderLogCreate.</p>
</dd>

### -param <i>OutBufferLength</i> 

<dd>
<p>Pointer to a ULONG that contains the size of the output buffer pointed to by OutBuffer.</p>
</dd>

### -param <i>Guid</i> 

<dd>
<p>Pointer to the WPP controller GUID that identifies the driver data.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if the operation succeeds. Otherwise, one of appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> values</p>

## -remarks


## -requirements
<table>
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