---
UID: NF.wpprecorder.WppRecorderConfigure
title: WppRecorderConfigure macro
author: windows-driver-content
description: The WppRecorderConfigure method enables or disables the default log to which WPP prints.
old-location: devtest\wpprecorderconfigure.htm
old-project: devtest
ms.assetid: 995E4606-F987-46A7-8310-28E8E9C7682C
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: WppRecorderConfigure
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
req.product: Windows 10 or later.
---

# WppRecorderConfigure macro



## -description
The <a href="devtest.wpprecorderconfigure">WppRecorderConfigure</a> method enables or disables the default log to which WPP prints.



## -syntax

````
NTSTATUS WppRecorderConfigure(
   PRECORDER_CONFIGURE_PARAMS ConfigureParams
);
````


## -parameters

### -param ConfigureParams 

Pointer to a caller-allocated RECORDER_CONFIGURE_PARAMS structure.


## -remarks
Before calling <a href="devtest.wpprecorderconfigure">WppRecorderConfigure</a>, allocate a <a href="devtest.recorder_configure_params">RECORDER_CONFIGURE_PARAMS</a> structure and initialize by calling <a href="devtest.recorder_configure_params_init">RECORDER_CONFIGURE_PARAMS_INIT</a>. 

This method only configures the default log. By default that log is enabled. If you have a custom log, you must disable the default log by setting the <b>CreateDefaultLog</b> to FALSE.


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