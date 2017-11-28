---
UID: NF.wdfinterrupt.WdfInterruptEnable
title: WdfInterruptEnable
author: windows-driver-content
description: The WdfInterruptEnable method enables a specified device interrupt by calling the driver's EvtInterruptEnable callback function.
old-location: wdf\wdfinterruptenable.htm
old-project: wdf
ms.assetid: e2ffab7f-b6bf-4707-9a3d-9619330b2af1
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfInterruptEnable
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfinterrupt.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfInterruptEnable
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); 
WUDFx02000.dll (UMDF)
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfInterruptEnable function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfInterruptEnable</b> method enables a specified device interrupt by calling the driver's <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-enable.md">EvtInterruptEnable</a> callback function.</p>


## -syntax

````
VOID WdfInterruptEnable(
  _In_ WDFINTERRUPT Interrupt
);
````


## -parameters
<dl>

### -param <i>Interrupt</i> [in]

<dd>
<p>A handle to a framework interrupt object.</p>
</dd>
</dl>

## -returns
<p>None.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>Most framework-based drivers don't need to call <b>WdfInterruptEnable</b>, because the framework calls the driver's <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-enable.md">EvtInterruptEnable</a> callback function each time the device enters its working (D0) state.</p>

<p>For <a href="wdf.supporting_passive_level_interrupts">passive-level interrupt objects</a>, the framework calls <b>WdfInterruptEnable</b> at PASSIVE_LEVEL.</p>

<p>Do not call <b>WdfInterruptEnable</b> from an arbitrary thread context,  such as a <a href="wdf.request_handlers">request handler</a>.</p>

<p>For more information about handling interrupts in framework-based drivers, see <a href="wdf.handling_hardware_interrupts">Handling Hardware Interrupts</a>.</p>

<p>The following code example enables the device interrupt that is associated with a specified interrupt object.</p>

<p>Most framework-based drivers don't need to call <b>WdfInterruptEnable</b>, because the framework calls the driver's <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-enable.md">EvtInterruptEnable</a> callback function each time the device enters its working (D0) state.</p>

<p>For <a href="wdf.supporting_passive_level_interrupts">passive-level interrupt objects</a>, the framework calls <b>WdfInterruptEnable</b> at PASSIVE_LEVEL.</p>

<p>Do not call <b>WdfInterruptEnable</b> from an arbitrary thread context,  such as a <a href="wdf.request_handlers">request handler</a>.</p>

<p>For more information about handling interrupts in framework-based drivers, see <a href="wdf.handling_hardware_interrupts">Handling Hardware Interrupts</a>.</p>

<p>The following code example enables the device interrupt that is associated with a specified interrupt object.</p>

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
<dt>Wdfinterrupt.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
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
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547351">WdfInterruptDisable</a>
</dt>
<dt>
<a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-enable.md">EvtInterruptEnable</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfInterruptEnable method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
