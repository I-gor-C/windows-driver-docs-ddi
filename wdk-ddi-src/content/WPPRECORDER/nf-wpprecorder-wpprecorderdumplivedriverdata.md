---
UID: NF.wpprecorder.WppRecorderDumpLiveDriverData
title: WppRecorderDumpLiveDriverData
author: windows-driver-content
description: The WppRecorderDumpLiveDriverData method gets the buffer associated with the specified Inflight Trace Recorder log.
old-location: devtest\wpprecorderdumplivedriverdata.htm
ms.assetid: FE3DE2A8-8EE5-4F34-BEE6-731987E5F5BD
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: devtest
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
ms.keywords: WppRecorderDumpLiveDriverData
req.iface: 
req.product: Windows 10 or later.
---

# WppRecorderDumpLiveDriverData function



## -description
<p>The <b>WppRecorderDumpLiveDriverData</b> method gets the buffer associated with the specified Inflight Trace Recorder log.</p>


## -syntax

````
NTSTATUS WppRecorderDumpLiveDriverData(
  [in]  RECORDER_LOG RecorderLog,
  [out] PVOID        *OutBuffer,
  [out] PULONG       OutBufferLength,
  [out] LPGUID       Guid
);
````


## -parameters
<dl>

### -param <i>RecorderLog</i> [in]

<dd>
<p>A recorder log handle returned in a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/dn914615">WppRecorderLogCreate</a>.</p>
</dd>

### -param <i>OutBuffer</i> [out]

<dd>
<p>Pointer to the buffer that was allocated by <a href="https://msdn.microsoft.com/library/windows/hardware/dn914615">WppRecorderLogCreate</a>.</p>
</dd>

### -param <i>OutBufferLength</i> [out]

<dd>
<p>Pointer to a ULONG that contains the size of the output buffer pointed to by <i>OutBuffer.</i></p>
</dd>

### -param <i>Guid</i> [out]

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