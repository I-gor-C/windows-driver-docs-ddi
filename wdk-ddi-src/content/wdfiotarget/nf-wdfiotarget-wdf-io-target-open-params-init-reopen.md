---
UID: NF.wdfiotarget.WDF_IO_TARGET_OPEN_PARAMS_INIT_REOPEN
title: WDF_IO_TARGET_OPEN_PARAMS_INIT_REOPEN
author: windows-driver-content
description: The WDF_IO_TARGET_OPEN_PARAMS_INIT_REOPEN function initializes a driver's WDF_IO_TARGET_OPEN_PARAMS structure so the driver can reopen a remote I/O target.
old-location: wdf\wdf_io_target_open_params_init_reopen.htm
ms.assetid: 00f1e870-4c74-44d3-9ee9-c8b9e63e5f3b
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfiotarget.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_IO_TARGET_OPEN_PARAMS_INIT_REOPEN
req.alt-loc: wdfiotarget.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level
ms.keywords: WDF_IO_TARGET_OPEN_PARAMS_INIT_REOPEN
req.iface: 
req.product: Windows 10 or later.
---

# WDF_IO_TARGET_OPEN_PARAMS_INIT_REOPEN function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_IO_TARGET_OPEN_PARAMS_INIT_REOPEN</b> function initializes a driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552377">WDF_IO_TARGET_OPEN_PARAMS</a> structure so the driver can reopen a remote I/O target. </p>


## -syntax

````
VOID WDF_IO_TARGET_OPEN_PARAMS_INIT_REOPEN(
  _Out_ PWDF_IO_TARGET_OPEN_PARAMS Params
);
````


## -parameters
<dl>

### -param <i>Params</i> [out]

<dd>
<p>A pointer to a driver-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff552377">WDF_IO_TARGET_OPEN_PARAMS</a> structure, which the function initializes.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff552377">WDF_IO_TARGET_OPEN_PARAMS</a> structure is used as input to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548634">WdfIoTargetOpen</a> method. Your driver should call <b>WDF_IO_TARGET_OPEN_PARAMS_INIT_REOPEN</b> to initialize a <b>WDF_IO_TARGET_OPEN_PARAMS</b> structure if the driver is calling <b>WdfIoTargetOpen</b> from within an <a href="https://msdn.microsoft.com/9f275a2c-6f40-461d-bd2c-767b2494ad1c">EvtIoTargetRemoveCanceled</a> callback function.</p>

<p>The <b>WDF_IO_TARGET_OPEN_PARAMS_INIT_REOPEN</b> function zeros the specified <a href="https://msdn.microsoft.com/library/windows/hardware/ff552377">WDF_IO_TARGET_OPEN_PARAMS</a> structure and sets the structure's <b>Size</b> member. Then, the function sets the <b>Type</b> member to <a href="https://msdn.microsoft.com/27aa5d78-03ce-4fc9-b1c8-d02a760e2787">WdfIoTargetOpenReopen</a>.</p>

<p>For more information about I/O targets, see <a href="wdf.using_i_o_targets">Using I/O Targets</a>.</p>

<p>The following code example is a segment of an <a href="https://msdn.microsoft.com/9f275a2c-6f40-461d-bd2c-767b2494ad1c">EvtIoTargetRemoveCanceled</a> callback function that reopens a remote I/O target.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff552377">WDF_IO_TARGET_OPEN_PARAMS</a> structure is used as input to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548634">WdfIoTargetOpen</a> method. Your driver should call <b>WDF_IO_TARGET_OPEN_PARAMS_INIT_REOPEN</b> to initialize a <b>WDF_IO_TARGET_OPEN_PARAMS</b> structure if the driver is calling <b>WdfIoTargetOpen</b> from within an <a href="https://msdn.microsoft.com/9f275a2c-6f40-461d-bd2c-767b2494ad1c">EvtIoTargetRemoveCanceled</a> callback function.</p>

<p>The <b>WDF_IO_TARGET_OPEN_PARAMS_INIT_REOPEN</b> function zeros the specified <a href="https://msdn.microsoft.com/library/windows/hardware/ff552377">WDF_IO_TARGET_OPEN_PARAMS</a> structure and sets the structure's <b>Size</b> member. Then, the function sets the <b>Type</b> member to <a href="https://msdn.microsoft.com/27aa5d78-03ce-4fc9-b1c8-d02a760e2787">WdfIoTargetOpenReopen</a>.</p>

<p>For more information about I/O targets, see <a href="wdf.using_i_o_targets">Using I/O Targets</a>.</p>

<p>The following code example is a segment of an <a href="https://msdn.microsoft.com/9f275a2c-6f40-461d-bd2c-767b2494ad1c">EvtIoTargetRemoveCanceled</a> callback function that reopens a remote I/O target.</p>

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
<dt>Wdfiotarget.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/9f275a2c-6f40-461d-bd2c-767b2494ad1c">EvtIoTargetRemoveCanceled</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552377">WDF_IO_TARGET_OPEN_PARAMS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548634">WdfIoTargetOpen</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/27aa5d78-03ce-4fc9-b1c8-d02a760e2787">WdfIoTargetOpenReopen</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_IO_TARGET_OPEN_PARAMS_INIT_REOPEN function%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
