---
UID: NF.wdfrequest.WdfRequestGetEffectiveIoType
title: WdfRequestGetEffectiveIoType
author: windows-driver-content
description: The WdfRequestGetEffectiveIoType method returns the buffer access method that UMDF is using for the data buffers of the specified I/O request.
old-location: wdf\wdfrequestgeteffectiveiotype.htm
old-project: wdf
ms.assetid: ED63E47F-B91F-49DC-9CE9-8CFE8F670B16
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfRequestGetEffectiveIoType
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfrequest.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 2.0
req.alt-api: WdfRequestGetEffectiveIoType
req.alt-loc: WUDFx02000.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: WUDFx02000.lib
req.dll: WUDFx02000.dll; 
TBD
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfRequestGetEffectiveIoType function



## -description
<p class="CCE_Message">[Applies to UMDF only]</p>
<p>The <b>WdfRequestGetEffectiveIoType</b> method returns the buffer access method that UMDF is using for the data buffers of the specified I/O request.</p>


## -syntax

````
WDF_DEVICE_IO_TYPE WdfRequestGetEffectiveIoType(
  _In_ WDFREQUEST Request
);
````


## -parameters
<dl>

### -param <i>Request</i> [in]

<dd>
<p>A handle to a framework request object.</p>
</dd>
</dl>

## -returns
<p><b>WdfRequestGetEffectiveIoType</b> returns a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551255">WDF_DEVICE_IO_TYPE</a>-typed value that identifies the buffer access method that UMDF is using for the I/O request's data buffers. </p>

## -remarks
<p>For more information, see <a href="wdf.managing_buffer_access_methods_in_umdf_drivers">Managing Buffer Access Methods in UMDF Drivers</a>.</p>

<p>The following code example shows how an <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-write.md">EvtIoWrite</a> callback function can determine the buffer access method for the specified write request.</p>

<p>For more information, see <a href="wdf.managing_buffer_access_methods_in_umdf_drivers">Managing Buffer Access Methods in UMDF Drivers</a>.</p>

<p>The following code example shows how an <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-write.md">EvtIoWrite</a> callback function can determine the buffer access method for the specified write request.</p>

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
<p>Minimum support</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx02000.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx02000.dll; </dt>
<dt>TBD</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551255">WDF_DEVICE_IO_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRequestGetEffectiveIoType method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
