---
UID: NF.wdfdpc.WdfDpcCancel
title: WdfDpcCancel
author: windows-driver-content
description: The WdfDpcCancel method attempts to cancel the execution of a DPC object's scheduled EvtDpcFunc callback function.
old-location: wdf\wdfdpccancel.htm
old-project: wdf
ms.assetid: 6eb56c5b-d198-4542-a239-c54b49561196
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfDpcCancel
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdpc.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfDpcCancel
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: See Remarks section.
req.iface: 
req.product: Windows 10 or later.
---

# WdfDpcCancel function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfDpcCancel</b> method attempts to cancel the execution of a DPC object's scheduled <a href="wdf.evtdpcfunc">EvtDpcFunc</a> callback function.</p>


## -syntax

````
BOOLEAN WdfDpcCancel(
  _In_ WDFDPC  Dpc,
  _In_ BOOLEAN Wait
);
````


## -parameters
<dl>

### -param <i>Dpc</i> [in]

<dd>
<p>A handle to a framework DPC object.</p>
</dd>

### -param <i>Wait</i> [in]

<dd>
<p>A Boolean value that, if <b>TRUE</b>, indicates that the <b>WdfDpcCancel</b> method will not return until the DPC object's <a href="wdf.evtdpcfunc">EvtDpcFunc</a> callback function is either canceled or finishes executing. If <b>FALSE</b>, the <b>WdfDpcCancel</b> method returns immediately.</p>
</dd>
</dl>

## -returns
<p><b>WdfDpcCancel</b> returns <b>TRUE</b> if the specified DPC object's <a href="wdf.evtdpcfunc">EvtDpcFunc</a> callback function was in the system's DPC queue. The method returns <b>FALSE</b> if the callback function was not in the DPC queue, either because the callback function was executing or because it had finished executing.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>If the specified DPC object's <a href="wdf.evtdpcfunc">EvtDpcFunc</a> callback function is in the system's DPC queue, it is removed from the queue. If the <i>EvtDpcFunc</i> function is not in the queue, it is either executing or has finished executing. </p>

<p>If the <i>Wait</i> parameter is <b>TRUE</b>, <b>WdfDpcCancel</b> must be called at IRQL = PASSIVE_LEVEL. If the <i>Wait</i> parameter is <b>FALSE</b>, <b>WdfDpcCancel</b> can be called at any IRQL.</p>

<p>The following code example cancels the execution of the callback function that is associated with the DPC object that the code example in the <a href="..\wdfdpc\nf-wdfdpc-wdfdpccreate.md">WdfDpcCreate</a> topic created.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdpc.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>See Remarks section.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.evtdpcfunc">EvtDpcFunc</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDpcCancel method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
