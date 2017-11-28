---
UID: NF.wpprecorder.WppRecorderConfigure
title: WppRecorderConfigure
author: windows-driver-content
description: The WppRecorderConfigure method enables or disables the default log to which WPP prints.
old-location: devtest\wpprecorderconfigure.htm
old-project: devtest
ms.assetid: 995E4606-F987-46A7-8310-28E8E9C7682C
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: WppRecorderConfigure
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
req.alt-api: WppRecorderConfigure
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

# WppRecorderConfigure function



## -description
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/dn914611">WppRecorderConfigure</a> method enables or disables the default log to which WPP prints.</p>


## -syntax

````
NTSTATUS WppRecorderConfigure(
   PRECORDER_CONFIGURE_PARAMS ConfigureParams
);
````


## -parameters
<dl>

### -param <i>ConfigureParams</i> 

<dd>
<p>Pointer to a caller-allocated RECORDER_CONFIGURE_PARAMS structure.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if completed successfully.</p>

## -remarks
<p>Before calling <a href="https://msdn.microsoft.com/library/windows/hardware/dn914611">WppRecorderConfigure</a>, allocate a <a href="https://msdn.microsoft.com/library/windows/hardware/dn914606">RECORDER_CONFIGURE_PARAMS</a> structure and initialize by calling <a href="https://msdn.microsoft.com/library/windows/hardware/dn914607">RECORDER_CONFIGURE_PARAMS_INIT</a>. </p>

<p>This method only configures the default log. By default that log is enabled. If you have a custom log, you must disable the default log by setting the <b>CreateDefaultLog</b> to FALSE.</p>

<p>Before calling <a href="https://msdn.microsoft.com/library/windows/hardware/dn914611">WppRecorderConfigure</a>, allocate a <a href="https://msdn.microsoft.com/library/windows/hardware/dn914606">RECORDER_CONFIGURE_PARAMS</a> structure and initialize by calling <a href="https://msdn.microsoft.com/library/windows/hardware/dn914607">RECORDER_CONFIGURE_PARAMS_INIT</a>. </p>

<p>This method only configures the default log. By default that log is enabled. If you have a custom log, you must disable the default log by setting the <b>CreateDefaultLog</b> to FALSE.</p>

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