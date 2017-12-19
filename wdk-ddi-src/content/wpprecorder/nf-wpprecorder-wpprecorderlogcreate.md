---
UID: NF.wpprecorder.WppRecorderLogCreate
title: WppRecorderLogCreate macro
author: windows-driver-content
description: The WppRecorderLogCreate method creates a buffer to contain the recorder log.
old-location: devtest\wpprecorderlogcreate.htm
old-project: devtest
ms.assetid: 103796C6-989F-4FE3-A8E6-4B8F5648E521
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: WppRecorderLogCreate
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
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
req.product: Windows 10 or later.
---

# WppRecorderLogCreate macro



## -description
The <a href="devtest.wpprecorderlogcreate">WppRecorderLogCreate</a> method creates a buffer to contain the recorder log.



## -syntax

````
NTSTATUS WppRecorderLogCreate(
   NULL CreateParams,
   NULL RecorderLog
);
````


## -parameters

### -param CreateParams 

A pointer to a RECORDER_LOG_CREATE_PARAMS structure.


### -param RecorderLog 

A handle for the recorder log.


## -remarks
Before calling <a href="devtest.wpprecorderlogcreate">WppRecorderLogCreate</a>, allocate a <a href="devtest.recorder_log_create_params">RECORDER_LOG_CREATE_PARAMS</a> structure and initialize by calling <a href="devtest.recorder_log_create_params_init">RECORDER_LOG_CREATE_PARAMS_INIT</a>.

You must first call <a href="devtest.wpp_init_tracing">WPP_INIT_TRACING</a> before calling <a href="devtest.wpprecorderlogcreate">WppRecorderLogCreate</a>. Default values are used unless the members of <i>CreateParams</i> are modified before calling <b>WppRecorderLogCreate</b>.

If a successful NTSTATUS is returned, the driver can use the <i>RecorderLog</i> handle for logging. 

If a successful NTSTATUS is not returned, the driver must use a <b>RECORDER_LOG</b> handle to the default log. Also, the driver must not attempt to log to or delete the handle pointed to by <i>RecorderLog</i>.


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wpprecorder.h</dt>
</dl>
</td>
</tr>
</table>