---
UID: NF.wpprecorder.RECORDER_LOG_CREATE_PARAMS_INIT_APPEND_POINTER
title: RECORDER_LOG_CREATE_PARAMS_INIT_APPEND_POINTER
author: windows-driver-content
description: The RECORDER_LOG_CREATE_PARAMS_INIT_APPEND_POINTER method initializes the RECORDER_LOG_CREATE_PARAMS with the pointer to link logs.
old-location: devtest\recorder_log_create_params_init_append_pointer.htm
ms.assetid: EC94E27C-C863-49F0-B13C-B661E96991B7
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
req.alt-api: RECORDER_LOG_CREATE_PARAMS_INIT_APPEND_POINTER
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
ms.keywords: RECORDER_LOG_CREATE_PARAMS_INIT_APPEND_POINTER
req.iface: 
req.product: Windows 10 or later.
---

# RECORDER_LOG_CREATE_PARAMS_INIT_APPEND_POINTER function



## -description
<p>The <b>RECORDER_LOG_CREATE_PARAMS_INIT_APPEND_POINTER</b> method initializes the <a href="https://msdn.microsoft.com/library/windows/hardware/dn914608">RECORDER_LOG_CREATE_PARAMS</a> with the pointer to link logs.</p>


## -syntax

````
FORCEINLINE void RECORDER_LOG_CREATE_PARAMS_INIT_APPEND_POINTER(
  _Out_    PRECORDER_LOG_CREATE_PARAMS Params,
  _In_opt_ PSTR                        LogIdentifier,
  _In_     PVOID                       LogIdentifierAppendPointer
);
````


## -parameters
<dl>

### -param <i>Params</i> [out]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/dn914608">RECORDER_LOG_CREATE_PARAMS</a> structure.</p>
</dd>

### -param <i>LogIdentifier</i> [in, optional]

<dd>
<p>String identifier for the log.</p>
</dd>

### -param <i>LogIdentifierAppendPointer</i> [in]

<dd>
<p>A pointer from each debug message to its IFR’s metadata structure.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

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