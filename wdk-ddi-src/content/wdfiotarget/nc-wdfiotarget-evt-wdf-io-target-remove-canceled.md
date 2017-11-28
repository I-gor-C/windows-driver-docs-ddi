---
UID: NC.wdfiotarget.EVT_WDF_IO_TARGET_REMOVE_CANCELED
title: EVT_WDF_IO_TARGET_REMOVE_CANCELED
author: windows-driver-content
description: A driver's EvtIoTargetRemoveCanceled event callback function performs operations when the removal of a specified remote I/O target is canceled.
old-location: wdf\evtiotargetremovecanceled.htm
old-project: wdf
ms.assetid: 9f275a2c-6f40-461d-bd2c-767b2494ad1c
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY, WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY, *PWDF_IO_QUEUE_FORWARD_PROGRESS_POLICY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdfiotarget.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: EvtIoTargetRemoveCanceled
req.alt-loc: WdfIoTarget.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# EVT_WDF_IO_TARGET_REMOVE_CANCELED callback



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>A driver's <i>EvtIoTargetRemoveCanceled</i> event callback function performs operations when the removal of a specified remote I/O target is canceled.</p>


## -prototype

````
EVT_WDF_IO_TARGET_REMOVE_CANCELED EvtIoTargetRemoveCanceled;

VOID EvtIoTargetRemoveCanceled(
  _In_ WDFIOTARGET IoTarget
)
{ ... }
````


## -parameters
<dl>

### -param <i>IoTarget</i> [in]

<dd>
<p>A handle to an I/O target object. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>To register an <i>EvtIoTargetRemoveCanceled</i> callback function, place the callback function's address in the I/O target's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552377">WDF_IO_TARGET_OPEN_PARAMS</a> structure. </p>

<p>If the driver's <a href="..\wdfiotarget\nc-wdfiotarget-evt-wdf-io-target-query-remove.md">EvtIoTargetQueryRemove</a> callback function called <a href="https://msdn.microsoft.com/library/windows/hardware/ff548589">WdfIoTargetCloseForQueryRemove</a>, the driver's <i>EvtIoTargetRemoveCanceled</i> callback function must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548634">WdfIoTargetOpen</a> to re-enable sending I/O requests to the I/O target. When the driver calls <b>WdfIoTargetOpen</b>, it can specify <b>WdfIoTargetOpenReopen</b> for the <b>Type</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552377">WDF_IO_TARGET_OPEN_PARAMS</a> structure.</p>

<p>If the driver did not provide an <a href="..\wdfiotarget\nc-wdfiotarget-evt-wdf-io-target-query-remove.md">EvtIoTargetQueryRemove</a> callback function, the driver's <i>EvtIoTargetRemoveCanceled</i> callback function can optionally call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548634">WdfIoTargetOpen</a> and specify <b>WdfIoTargetOpenReopen</b>.</p>

<p>The optional <i>EvtIoTargetRemoveCanceled</i> callback function should perform any additional operations that might be necessary before the driver resumes sending I/O requests to the I/O target.</p>

<p>For more information about the <i>EvtIoTargetRemoveCanceled</i> callback function, see <a href="wdf.controlling_a_general_i_o_target_s_state">Controlling a General I/O Target's State</a>.</p>

<p>To define an <i>EvtIoTargetRemoveCanceled</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtIoTargetRemoveCanceled</i> callback function that is named <i>MyIoTargetRemoveCanceled</i>, use the <b>EVT_WDF_IO_TARGET_REMOVE_CANCELED</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_WDF_IO_TARGET_REMOVE_CANCELED</b> function type is defined in the WdfIoTarget.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_IO_TARGET_REMOVE_CANCELED</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

<p>To register an <i>EvtIoTargetRemoveCanceled</i> callback function, place the callback function's address in the I/O target's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552377">WDF_IO_TARGET_OPEN_PARAMS</a> structure. </p>

<p>If the driver's <a href="..\wdfiotarget\nc-wdfiotarget-evt-wdf-io-target-query-remove.md">EvtIoTargetQueryRemove</a> callback function called <a href="https://msdn.microsoft.com/library/windows/hardware/ff548589">WdfIoTargetCloseForQueryRemove</a>, the driver's <i>EvtIoTargetRemoveCanceled</i> callback function must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548634">WdfIoTargetOpen</a> to re-enable sending I/O requests to the I/O target. When the driver calls <b>WdfIoTargetOpen</b>, it can specify <b>WdfIoTargetOpenReopen</b> for the <b>Type</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552377">WDF_IO_TARGET_OPEN_PARAMS</a> structure.</p>

<p>If the driver did not provide an <a href="..\wdfiotarget\nc-wdfiotarget-evt-wdf-io-target-query-remove.md">EvtIoTargetQueryRemove</a> callback function, the driver's <i>EvtIoTargetRemoveCanceled</i> callback function can optionally call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548634">WdfIoTargetOpen</a> and specify <b>WdfIoTargetOpenReopen</b>.</p>

<p>The optional <i>EvtIoTargetRemoveCanceled</i> callback function should perform any additional operations that might be necessary before the driver resumes sending I/O requests to the I/O target.</p>

<p>For more information about the <i>EvtIoTargetRemoveCanceled</i> callback function, see <a href="wdf.controlling_a_general_i_o_target_s_state">Controlling a General I/O Target's State</a>.</p>

<p>To define an <i>EvtIoTargetRemoveCanceled</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtIoTargetRemoveCanceled</i> callback function that is named <i>MyIoTargetRemoveCanceled</i>, use the <b>EVT_WDF_IO_TARGET_REMOVE_CANCELED</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_WDF_IO_TARGET_REMOVE_CANCELED</b> function type is defined in the WdfIoTarget.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_IO_TARGET_REMOVE_CANCELED</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

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
<dt>WdfIoTarget.h (include Wdf.h)</dt>
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
<a href="..\wdfiotarget\nc-wdfiotarget-evt-wdf-io-target-remove-complete.md">EvtIoTargetRemoveComplete</a>
</dt>
<dt>
<a href="..\wdfiotarget\nc-wdfiotarget-evt-wdf-io-target-query-remove.md">EvtIoTargetQueryRemove</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552377">WDF_IO_TARGET_OPEN_PARAMS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548589">WdfIoTargetCloseForQueryRemove</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548634">WdfIoTargetOpen</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20EVT_WDF_IO_TARGET_REMOVE_CANCELED callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
