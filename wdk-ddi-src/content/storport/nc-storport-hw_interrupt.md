---
UID: NC.storport.HW_INTERRUPT
title: HW_INTERRUPT
author: windows-driver-content
description: The Storport driver calls the HwStorInterrupt routine after the HBA generates an interrupt request.
old-location: storage\hwstorinterrupt.htm
old-project: storage
ms.assetid: 3c61d947-3e05-4750-a50c-be9b2dc573f0
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: _STORAGE_DEVICE_UNIQUE_IDENTIFIER, STORAGE_DEVICE_UNIQUE_IDENTIFIER, *PSTORAGE_DEVICE_UNIQUE_IDENTIFIER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HwStorInterrupt
req.alt-loc: Storport.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: DIRQL
req.product: Windows 10 or later.
---

# HW_INTERRUPT callback



## -description
The Storport driver calls the <b>HwStorInterrupt</b> routine after the HBA generates an interrupt request.


## -prototype

````
HW_INTERRUPT HwStorInterrupt;

BOOLEAN HwStorInterrupt(
   IN PVOID DeviceExtension
)
{ ... }
````


## -parameters

### -param DeviceExtension 

A pointer to the miniport driver's per HBA storage area. 

## -returns
If the miniport driver finds that its HBA did not generate the interrupt, <b>HwStorInterrupt</b> should return <b>FALSE</b> as soon as possible. The <b>HwStorInterrupt</b> routine should return within 50 microseconds.

## -remarks
The name <b>HwStorInterrupt</b> is just a placeholder. The actual prototype of this routine is defined in <i>Storport.h</i> as follows:

The <b>HwStorInterrupt</b> routine should return within 50 microseconds, ideally as short a time as possible. Therefore, all activity does not have to occur at high IRQL should be deferred to the <a href="storage.hwstordpcroutine">HwStorDpcRoutine</a> that is defined in the miniport driver and issued by using <a href="storage.storportissuedpc">StorPortIssueDpc</a>.  The latency of the DPC is very low, and it will be called immediately after the return from high IRQL.

The port driver calls the <b>HwStorInterrupt</b> routine at DIRQL.

To define an <b>HwStorInterrupt</b> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="https://msdn.microsoft.com/2F3549EF-B50F-455A-BDC7-1F67782B8DCA">Code Analysis for Drivers</a>, <a href="https://msdn.microsoft.com/74feeb16-387c-4796-987a-aff3fb79b556">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.

 For example, to define a <b>HwStorInterrupt</b> callback routine that is named <i>MyHwInterrupt</i>, use the <b>HW_INTERRUPT</b> type as shown in this code example:

Then, implement your callback routine as follows:

The <b>HW_INTERRUPT</b> function type is defined in the Storport.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>HW_INTERRUPT</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/40BD11CD-A559-4F90-BF39-4ED2FB800392">Declaring Functions Using Function Role Types for Storport Drivers</a>. For information about _Use_decl_annotations_, see <a href="c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.

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
Header
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
DIRQL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.hwstordpcroutine">HwStorDpcRoutine</a>
</dt>
<dt>
<a href="storage.storportissuedpc">StorPortIssueDpc</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20HwStorInterrupt routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
