---
UID: NS.wpprecorder._RECORDER_CONFIGURE_PARAMS
title: RECORDER_CONFIGURE_PARAMS
author: windows-driver-content
description: The RECORDER_CONFIGURE_PARAMS structure is an input parameter to the WppRecorderConfigure method to enable or disable the default log to which WPP prints.
old-location: devtest\recorder_configure_params.htm
old-project: devtest
ms.assetid: 9D2AB7D0-CD75-4539-9CB8-8CBA33EFE299
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: RECORDER_CONFIGURE_PARAMS, RECORDER_CONFIGURE_PARAMS, *PRECORDER_CONFIGURE_PARAMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wpprecorder.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RECORDER_CONFIGURE_PARAMS
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

# RECORDER_CONFIGURE_PARAMS structure



## -description
<p>The <b>RECORDER_CONFIGURE_PARAMS</b> structure is an input parameter to the <a href="..\wpprecorder\nf-wpprecorder-wpprecorderconfigure.md">WppRecorderConfigure</a> method to enable or disable the default log to which WPP prints.</p>


## -syntax

````
typedef struct _RECORDER_CONFIGURE_PARAMS {
  ULONG   Size;
  BOOLEAN CreateDefaultLog;
} RECORDER_CONFIGURE_PARAMS, *PRECORDER_CONFIGURE_PARAMS;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Size of this structure.</p>
</dd>

### -field <b>CreateDefaultLog</b>

<dd>
<p>Indicates whether WPP should use the default log for trace messages. TRUE (default), use the default log; FALSE disable the default log.</p>
</dd>
</dl>

## -remarks
<p>To initialize this structure, the caller must call <a href="..\wpprecorder\nf-wpprecorder-recorder-configure-params-init.md">RECORDER_CONFIGURE_PARAMS_INIT</a>.</p>

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