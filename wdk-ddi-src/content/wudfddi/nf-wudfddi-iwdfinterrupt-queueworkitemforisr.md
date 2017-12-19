---
UID: NF.wudfddi.IWDFInterrupt.QueueWorkItemForIsr
title: IWDFInterrupt::QueueWorkItemForIsr method
author: windows-driver-content
description: The QueueWorkItemForIsr method queues a work item to process interrupt-related work outside of the interrupt service routine.
old-location: wdf\iwdfinterrupt_queueworkitemforisr.htm
old-project: wdf
ms.assetid: 5C6DC011-4032-4DB6-AE17-88E510DF9A3A
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: IWDFInterrupt, IWDFInterrupt::QueueWorkItemForIsr, QueueWorkItemForIsr
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
req.alt-api: IWDFInterrupt.QueueWorkItemForIsr
req.alt-loc: WUDFx.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: 
req.product: Windows 10 or later.
---

# IWDFInterrupt::QueueWorkItemForIsr method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>QueueWorkItemForIsr</b> method queues a work item to process interrupt-related work outside of the interrupt service routine.



## -syntax

````
BOOLEAN QueueWorkItemForIsr();
````


## -parameters


## -returns
The method returns TRUE if a work item was successfully queued. If a work item is already in the queue, the method returns FALSE.

The method returns TRUE if a work item was successfully queued. If a work item is already in the queue, the method returns FALSE.

The method returns TRUE if a work item was successfully queued. If a work item is already in the queue, the method returns FALSE.


## -remarks
The driver provides a pointer to its <a href="..\wudfinterrupt\nc-wudfinterrupt-wudf_interrupt_workitem.md">OnInterruptWorkItem</a> callback function when it calls  <a href="wdf.iwdfdevice3_createinterrupt">IWDFDevice3::CreateInterrupt</a> to create the interrupt object.

For more information about handling interrupts in UMDF drivers, see <a href="wdf.accessing_hardware_and_handling_interrupts">Accessing Hardware and Handling Interrupts</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
End of support

</th>
<td width="70%">
Unavailable in UMDF 2.0 and later.

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
1.11

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wudfddi.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wudfinterrupt\nc-wudfinterrupt-wudf_interrupt_workitem.md">OnInterruptWorkItem</a>
</dt>
<dt>
<a href="..\wudfddi\nn-wudfddi-iwdfinterrupt.md">IWDFInterrupt</a>
</dt>
<dt>
<a href="wdf.iwdfdevice3_createworkitem">IWDFDevice3::CreateWorkItem</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFInterrupt::QueueWorkItemForIsr method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

