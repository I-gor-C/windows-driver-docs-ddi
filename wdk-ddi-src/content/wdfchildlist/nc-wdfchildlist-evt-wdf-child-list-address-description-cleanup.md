---
UID: NC.wdfchildlist.EVT_WDF_CHILD_LIST_ADDRESS_DESCRIPTION_CLEANUP
title: EVT_WDF_CHILD_LIST_ADDRESS_DESCRIPTION_CLEANUP
author: windows-driver-content
description: A driver's EvtChildListAddressDescriptionCleanup event callback function frees any memory allocations for an address description that the driver's EvtChildListAddressDescriptionDuplicate callback function allocated.
old-location: wdf\evtchildlistaddressdescriptioncleanup.htm
old-project: wdf
ms.assetid: 845c8c96-7d34-4273-963e-b7f644884f26
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDBGEXTS_THREAD_OS_INFO, WDBGEXTS_THREAD_OS_INFO, *PWDBGEXTS_THREAD_OS_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdfchildlist.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: EvtChildListAddressDescriptionCleanup
req.alt-loc: WdfChildlist.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# EVT_WDF_CHILD_LIST_ADDRESS_DESCRIPTION_CLEANUP callback



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>A driver's <i>EvtChildListAddressDescriptionCleanup</i> event callback function frees any memory allocations for an <a href="wdf.dynamic_enumeration">address description</a> that the driver's <a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-address-description-duplicate.md">EvtChildListAddressDescriptionDuplicate</a> callback function allocated.</p>


## -prototype

````
EVT_WDF_CHILD_LIST_ADDRESS_DESCRIPTION_CLEANUP EvtChildListAddressDescriptionCleanup;

VOID EvtChildListAddressDescriptionCleanup(
  _In_    WDFCHILDLIST                          ChildList,
  _Inout_ PWDF_CHILD_ADDRESS_DESCRIPTION_HEADER AddressDescription
)
{ ... }
````


## -parameters
<dl>

### -param <i>ChildList</i> [in]

<dd>
<p>A handle to a framework child-list object.</p>
</dd>

### -param <i>AddressDescription</i> [in, out]

<dd>
<p>A pointer to a <a href="..\wdfchildlist\ns-wdfchildlist--wdf-child-address-description-header.md">WDF_CHILD_ADDRESS_DESCRIPTION_HEADER</a> structure that identifies an address description.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>If a bus driver is using <a href="wdf.dynamic_enumeration">dynamic enumeration</a>, it can register an <i>EvtChildListAddressDescriptionCleanup</i> callback function by calling <a href="..\wdffdo\nf-wdffdo-wdffdoinitsetdefaultchildlistconfig.md">WdfFdoInitSetDefaultChildListConfig</a> or <a href="..\wdfchildlist\nf-wdfchildlist-wdfchildlistcreate.md">WdfChildListCreate</a>.</p>

<p>If an address description points to additional information that is stored in dynamically allocated memory, and if that memory is allocated by an <a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-address-description-duplicate.md">EvtChildListAddressDescriptionDuplicate</a> callback function, the driver must provide an <i>EvtChildListAddressDescriptionCleanup</i> callback function. </p>

<p>Typically, the <a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-address-description-duplicate.md">EvtChildListAddressDescriptionDuplicate</a> callback function allocates memory by calling <a href="..\wdm\nf-wdm-exallocatepool.md">ExAllocatePool</a>. The <i>EvtChildListAddressDescriptionCleanup</i> callback function must deallocate that memory by calling <a href="..\ntddk\nf-ntddk-exfreepool.md">ExFreePool</a>. This callback function must not attempt to deallocate the rest of the address description. In other words, the callback function must not deallocate the address description structure that the <i>AddressDescription</i> parameter points to; it must deallocate only additional memory allocations that the description structure points to.</p>

<p>For more information about dynamic enumeration, see <a href="wdf.enumerating_the_devices_on_a_bus">Enumerating the Devices on a Bus</a><u>.</u></p>

<p>To define an <i>EvtChildListAddressDescriptionCleanup</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtChildListAddressDescriptionCleanup</i> callback function that is named <i>MyChildListAddressDescriptionCleanup</i>, use the <b>EVT_WDF_CHILD_LIST_ADDRESS_DESCRIPTION_CLEANUP</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_WDF_CHILD_LIST_ADDRESS_DESCRIPTION_CLEANUP</b> function type is defined in the WdfChildlist.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_CHILD_LIST_ADDRESS_DESCRIPTION_CLEANUP</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

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
<dt>WdfChildlist.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-address-description-duplicate.md">EvtChildListAddressDescriptionDuplicate</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-exallocatepool.md">ExAllocatePool</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-exfreepool.md">ExFreePool</a>
</dt>
<dt>
<a href="..\wdfchildlist\ns-wdfchildlist--wdf-child-address-description-header.md">WDF_CHILD_ADDRESS_DESCRIPTION_HEADER</a>
</dt>
<dt>
<a href="..\wdfchildlist\nf-wdfchildlist-wdfchildlistcreate.md">WdfChildListCreate</a>
</dt>
<dt>
<a href="..\wdffdo\nf-wdffdo-wdffdoinitsetdefaultchildlistconfig.md">WdfFdoInitSetDefaultChildListConfig</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20EVT_WDF_CHILD_LIST_ADDRESS_DESCRIPTION_CLEANUP callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
