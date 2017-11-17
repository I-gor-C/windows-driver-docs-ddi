---
UID: NS.wdfrequest._WDF_REQUEST_SEND_OPTIONS
title: WDF_REQUEST_SEND_OPTIONS
author: windows-driver-content
description: The WDF_REQUEST_SEND_OPTIONS structure specifies options that are associated with sending an I/O request to an I/O target.
old-location: wdf\wdf_request_send_options.htm
ms.assetid: 0d561e0f-ca7e-44ed-9025-1a6513e4cd28
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfrequest.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_REQUEST_SEND_OPTIONS
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
req.irql: <=DISPATCH_LEVEL
ms.keywords: WDF_REQUEST_SEND_OPTIONS, WDF_REQUEST_SEND_OPTIONS, *PWDF_REQUEST_SEND_OPTIONS
req.iface: 
req.product: Windows 10 or later.
---

# WDF_REQUEST_SEND_OPTIONS structure



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_REQUEST_SEND_OPTIONS</b> structure specifies options that are associated with sending an I/O request to an I/O target.</p>


## -syntax

````
typedef struct _WDF_REQUEST_SEND_OPTIONS {
  ULONG    Size;
  ULONG    Flags;
  LONGLONG Timeout;
} WDF_REQUEST_SEND_OPTIONS, *PWDF_REQUEST_SEND_OPTIONS;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A bitwise OR of <a href="https://msdn.microsoft.com/library/windows/hardware/ff552493">WDF_REQUEST_SEND_OPTIONS_FLAGS</a>-typed flags.</p>
</dd>

### -field <b>Timeout</b>

<dd>
<p>A time-out value, in system time units (100-nanosecond intervals). If the driver has set the WDF_REQUEST_SEND_OPTION_TIMEOUT flag, the framework cancels the associated I/O request if it is not completed within the specified time-out period. The time-out value can be negative, positive, or zero, as follows:</p>
<ul>
<li>
<p>If the value is negative, the expiration time is relative to the current system time.</p>
</li>
<li>
<p>If the value is positive, the expiration time is specified as an absolute time (which is actually relative to January 1, 1601). </p>
</li>
<li>
<p>If the value is zero, the framework does not time out the request.</p>
</li>
</ul>
<p>Relative expiration times are not affected by any changes to the system time that might occur within the specified time-out period. Absolute expiration times do reflect system time changes.</p>
<p>The framework provides <a href="https://msdn.microsoft.com/E7D5564D-7BAA-412E-959F-3655B963B4C1">time conversion functions</a> that convert time values into system time units.</p>
<p>If the framework cancels an I/O request because the specified time-out period has elapsed, the framework provides a completion status of STATUS_IO_TIMEOUT for the I/O request. However, after the time-out period elapses, the I/O target might complete the I/O request before the framework is able to cancel it. In that case, the I/O request's completion status will not be STATUS_IO_TIMEOUT.

</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_REQUEST_SEND_OPTIONS</b> structure is passed to object methods that send an I/O request to an I/O target, such as the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550027">WdfRequestSend</a> method. The structure must be initialized by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552497">WDF_REQUEST_SEND_OPTIONS_INIT</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff552498">WDF_REQUEST_SEND_OPTIONS_SET_TIMEOUT</a> functions.</p>

<p>If the driver is sending the request synchronously, we recommend that the driver set a time-out value and the time-out flag in the <b>Flags</b> member of this structure.</p>

## -requirements
<table>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550027">WdfRequestSend</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552497">WDF_REQUEST_SEND_OPTIONS_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552498">WDF_REQUEST_SEND_OPTIONS_SET_TIMEOUT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552493">WDF_REQUEST_SEND_OPTIONS_FLAGS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_REQUEST_SEND_OPTIONS structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
