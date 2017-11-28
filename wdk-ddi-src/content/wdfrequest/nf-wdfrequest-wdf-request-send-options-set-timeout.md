---
UID: NF.wdfrequest.WDF_REQUEST_SEND_OPTIONS_SET_TIMEOUT
title: WDF_REQUEST_SEND_OPTIONS_SET_TIMEOUT
author: windows-driver-content
description: The WDF_REQUEST_SEND_OPTIONS_SET_TIMEOUT function sets a time-out value in a driver's WDF_REQUEST_SEND_OPTIONS structure.
old-location: wdf\wdf_request_send_options_set_timeout.htm
old-project: wdf
ms.assetid: 729bd44f-9ac7-4b3d-905d-a78b10fba2a7
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_REQUEST_SEND_OPTIONS_SET_TIMEOUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfrequest.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_REQUEST_SEND_OPTIONS_SET_TIMEOUT
req.alt-loc: wdfrequest.h
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

# WDF_REQUEST_SEND_OPTIONS_SET_TIMEOUT function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_REQUEST_SEND_OPTIONS_SET_TIMEOUT</b> function sets a time-out value in a driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552491">WDF_REQUEST_SEND_OPTIONS</a> structure.</p>


## -syntax

````
VOID WDF_REQUEST_SEND_OPTIONS_SET_TIMEOUT(
  _Inout_ PWDF_REQUEST_SEND_OPTIONS Options,
  _In_    LONGLONG                  Timeout
);
````


## -parameters
<dl>

### -param <i>Options</i> [in, out]

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552491">WDF_REQUEST_SEND_OPTIONS</a> structure.</p>
</dd>

### -param <i>Timeout</i> [in]

<dd>
<p>An absolute or relative time-out value. For more information, see the <b>Timeout</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552491">WDF_REQUEST_SEND_OPTIONS</a> structure.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>To set a time-out value, your driver must call <b>WDF_REQUEST_SEND_OPTIONS_SET_TIMEOUT</b> after it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff552497">WDF_REQUEST_SEND_OPTIONS_INIT</a>.</p>

<p>The <b>WDF_REQUEST_SEND_OPTIONS_SET_TIMEOUT</b> function stores the specified timeout value in the specified <a href="https://msdn.microsoft.com/library/windows/hardware/ff552491">WDF_REQUEST_SEND_OPTIONS</a> structure's <b>Timeout</b> member. It also sets the <b>WDF_REQUEST_SEND_OPTION_TIMEOUT</b> flag in the structure's <b>Flags</b> member.</p>

<p>The following code example initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552491">WDF_REQUEST_SEND_OPTIONS</a> structure and sets a time-out value for the structure. (The example calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff552449">WDF_REL_TIMEOUT_IN_SEC</a> to specify a relative time-out value of 10 seconds.) The example then uses the <b>WDF_REQUEST_SEND_OPTIONS</b> structure as input to <a href="https://msdn.microsoft.com/library/windows/hardware/ff551163">WdfUsbTargetPipeWriteSynchronously</a>.</p>

<p>To set a time-out value, your driver must call <b>WDF_REQUEST_SEND_OPTIONS_SET_TIMEOUT</b> after it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff552497">WDF_REQUEST_SEND_OPTIONS_INIT</a>.</p>

<p>The <b>WDF_REQUEST_SEND_OPTIONS_SET_TIMEOUT</b> function stores the specified timeout value in the specified <a href="https://msdn.microsoft.com/library/windows/hardware/ff552491">WDF_REQUEST_SEND_OPTIONS</a> structure's <b>Timeout</b> member. It also sets the <b>WDF_REQUEST_SEND_OPTION_TIMEOUT</b> flag in the structure's <b>Flags</b> member.</p>

<p>The following code example initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552491">WDF_REQUEST_SEND_OPTIONS</a> structure and sets a time-out value for the structure. (The example calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff552449">WDF_REL_TIMEOUT_IN_SEC</a> to specify a relative time-out value of 10 seconds.) The example then uses the <b>WDF_REQUEST_SEND_OPTIONS</b> structure as input to <a href="https://msdn.microsoft.com/library/windows/hardware/ff551163">WdfUsbTargetPipeWriteSynchronously</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfrequest.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552491">WDF_REQUEST_SEND_OPTIONS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552497">WDF_REQUEST_SEND_OPTIONS_INIT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_REQUEST_SEND_OPTIONS_SET_TIMEOUT function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
