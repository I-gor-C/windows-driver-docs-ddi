---
UID: NF.stiusd.IStiDeviceControl.WriteToErrorLog
title: IStiDeviceControl::WriteToErrorLog
author: windows-driver-content
description: The IStiDeviceControl::WriteToErrorLog method allows a user-mode still image minidriver to write a message into the still image error log.
old-location: image\istidevicecontrol_writetoerrorlog.htm
old-project: image
ms.assetid: 22f9688e-1e61-46a6-a9f6-0244d7dd47ce
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IStiDeviceControl, WriteToErrorLog, IStiDeviceControl::WriteToErrorLog
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: stiusd.h
req.include-header: Stiusd.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IStiDeviceControl.WriteToErrorLog
req.alt-loc: stiusd.h
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
req.iface: IStiDeviceControl
req.product: Windows 10 or later.
---

# IStiDeviceControl::WriteToErrorLog method



## -description
<p>The <b>IStiDeviceControl::WriteToErrorLog</b> method allows a user-mode still image minidriver to write a message into the still image error log.</p>


## -syntax

````
HRESULT WriteToErrorLog(
   DWORD   dwMessageType,
   LPCWSTR pszMessage,
   DWORD   dwErrorCode
);
````


## -parameters
<dl>

### -param <i>dwMessageType</i> 

<dd>
<p>Caller-supplied constant value representing the message type. The following values are defined in <i>Sti.h</i>:</p>
<p>STI_TRACE_INFORMATION</p>
<p>STI_TRACE_WARNING</p>
<p>STI_TRACE_ERROR</p>
</dd>

### -param <i>pszMessage</i> 

<dd>
<p>Caller-supplied pointer to a message string to be written to the log file.</p>
</dd>

### -param <i>dwErrorCode</i> 

<dd>
<p><i>Not used</i>.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the method returns S_OK. Otherwise, it returns one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.</p>

## -remarks
<p>The still image error log file is named <i>sti_trace.log</i> and is located in the Windows directory. Control Panel allows a user to select which still image error types (informational, warning, or error) are written to the error log (see <a href="image.registry_entries_for_still_image_devices#ddk_non_modifiable_registry_entries_si#ddk_non_modifiable_registry_entries_si">Nonmodifiable Registry Entries</a>).</p>

<p>Error messages should be reserved for critical error conditions, such as device hardware failures. Informational messages can be used for your own debugging purposes. Logged messages aren't visible to users, but they might be used by a support engineer to help debug a user's problems.</p>

<p>A still image minidriver receives an <b>IStiDeviceControl</b> interface pointer as input to its <a href="image.istiusd_initialize">IStiUSD::Initialize</a> method.</p>

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
<dt>Stiusd.h (include Stiusd.h)</dt>
</dl>
</td>
</tr>
</table>