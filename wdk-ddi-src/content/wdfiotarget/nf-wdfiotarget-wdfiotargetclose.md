---
UID: NF.wdfiotarget.WdfIoTargetClose
title: WdfIoTargetClose function
author: windows-driver-content
description: The WdfIoTargetClose method closes a specified remote I/O target.
old-location: wdf\wdfiotargetclose.htm
old-project: wdf
ms.assetid: 7de1ce11-a2b3-4d68-b279-4652b822297b
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: WdfIoTargetClose
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfiotarget.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfIoTargetClose
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# WdfIoTargetClose function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfIoTargetClose</b> method closes a specified remote I/O target.



## -syntax

````
VOID WdfIoTargetClose(
  _In_ WDFIOTARGET IoTarget
);
````


## -parameters

### -param IoTarget [in]

A handle to an I/O target object that was obtained from a previous call to <a href="wdf.wdfiotargetcreate">WdfIoTargetCreate</a>.


## -returns
None.

A bug check occurs if the driver supplies an invalid object handle.




## -remarks
After a driver has called <b>WdfIoTargetClose</b>, it can call <a href="wdf.wdfiotargetopen">WdfIoTargetOpen</a> to reopen the remote I/O target.

Drivers that supply an <a href="..\wdfiotarget\nc-wdfiotarget-evt_wdf_io_target_remove_complete.md">EvtIoTargetRemoveComplete</a> callback function must call <b>WdfIoTargetClose</b> from within that callback function.

Before the <b>WdfIoTargetClose</b> method returns, the framework <a href="wdf.canceling_i_o_requests">cancels</a> all of the target queue's I/O requests. 

If a driver has finished using a remote I/O target and will not use the target again, and the target has no child request objects that are still pending, the driver can call <a href="wdf.wdfobjectdelete">WdfObjectDelete</a> without first calling <b>WdfIoTargetClose</b>. The call to <b>WdfObjectDelete</b> will close the remote I/O target, cancel all of the target queue's I/O requests, and delete the I/O target object. (Note that if the remote I/O target's parent object is a device object, the framework closes the target and deletes the target object when it deletes the parent object.) If the target has any child request objects that are still pending, the driver must call <b>WdfIoTargetClose</b> before it can safely call <b>WdfObjectDelete</b>.

For more information about <b>WdfIoTargetClose</b>, see <a href="wdf.controlling_a_general_i_o_target_s_state">Controlling a General I/O Target's State</a>. 

For more information about I/O targets, see <a href="wdf.using_i_o_targets">Using I/O Targets</a>.

The following code example is an <a href="..\wdfiotarget\nc-wdfiotarget-evt_wdf_io_target_remove_complete.md">EvtIoTargetRemoveComplete</a> callback function that removes a specified I/O target from a driver's collection of I/O targets and then closes the I/O target.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.0

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
2.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfiotarget.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

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
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfiotarget\nc-wdfiotarget-evt_wdf_io_target_remove_complete.md">EvtIoTargetRemoveComplete</a>
</dt>
<dt>
<a href="wdf.wdfiotargetcreate">WdfIoTargetCreate</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfIoTargetClose method%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

