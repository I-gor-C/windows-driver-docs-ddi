---
UID: NF.wpprecorder.WppRecorderLogCreate
title: WppRecorderLogCreate
author: windows-driver-content
description: The WppRecorderLogCreate method creates a buffer to contain the recorder log.
old-location: devtest\wpprecorderlogcreate.htm
old-project: devtest
ms.assetid: 103796C6-989F-4FE3-A8E6-4B8F5648E521
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: WppRecorderLogCreate
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
req.alt-api: WppRecorderLogCreate
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

# WppRecorderLogCreate function



## -description
<p>The <a href="..\wpprecorder\nf-wpprecorder-wpprecorderlogcreate.md">WppRecorderLogCreate</a> method creates a buffer to contain the recorder log.</p>


## -syntax

````
NTSTATUS WppRecorderLogCreate(
   NULL CreateParams,
   NULL RecorderLog
);
````


## -parameters
<dl>

### -param <i>CreateParams</i> 

<dd>
<p>A pointer to a RECORDER_LOG_CREATE_PARAMS structure.</p>
</dd>

### -param <i>RecorderLog</i> 

<dd>
<p>A handle for the recorder log.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if the operation succeeds. Otherwise, one of appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> values</p>

## -remarks
<p>Before calling <a href="..\wpprecorder\nf-wpprecorder-wpprecorderlogcreate.md">WppRecorderLogCreate</a>, allocate a <a href="..\wpprecorder\ns-wpprecorder--recorder-log-create-params.md">RECORDER_LOG_CREATE_PARAMS</a> structure and initialize by calling <a href="..\wpprecorder\nf-wpprecorder-recorder-log-create-params-init.md">RECORDER_LOG_CREATE_PARAMS_INIT</a>.</p>

<p>You must first call <a href="devtest.wpp_init_tracing">WPP_INIT_TRACING</a> before calling <a href="..\wpprecorder\nf-wpprecorder-wpprecorderlogcreate.md">WppRecorderLogCreate</a>. Default values are used unless the members of <i>CreateParams</i> are modified before calling <b>WppRecorderLogCreate</b>.</p>

<p>If a successful NTSTATUS is returned, the driver can use the <i>RecorderLog</i> handle for logging. </p>

<p>If a successful NTSTATUS is not returned, the driver must use a <b>RECORDER_LOG</b> handle to the default log. Also, the driver must not attempt to log to or delete the handle pointed to by <i>RecorderLog</i>.</p>

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