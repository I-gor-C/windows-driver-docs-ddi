---
UID: NC.wdfchildlist.EVT_WDF_CHILD_LIST_IDENTIFICATION_DESCRIPTION_DUPLICATE
title: EVT_WDF_CHILD_LIST_IDENTIFICATION_DESCRIPTION_DUPLICATE
author: windows-driver-content
description: A driver's EvtChildListIdentificationDescriptionDuplicate event callback function duplicates a child identification description.
old-location: wdf\evtchildlistidentificationdescriptionduplicate.htm
ms.assetid: 5c2ec27c-2d88-4e0c-8f11-4f58d720df46
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfchildlist.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: EvtChildListIdentificationDescriptionDuplicate
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
ms.keywords: WDBGEXTS_THREAD_OS_INFO, WDBGEXTS_THREAD_OS_INFO, *PWDBGEXTS_THREAD_OS_INFO
req.iface: 
req.product: Windows 10 or later.
---

# EVT_WDF_CHILD_LIST_IDENTIFICATION_DESCRIPTION_DUPLICATE callback



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>A driver's <i>EvtChildListIdentificationDescriptionDuplicate</i> event callback function duplicates a child identification description.</p>


## -prototype

````
EVT_WDF_CHILD_LIST_IDENTIFICATION_DESCRIPTION_DUPLICATE EvtChildListIdentificationDescriptionDuplicate;

NTSTATUS EvtChildListIdentificationDescriptionDuplicate(
  _In_  WDFCHILDLIST                                 ChildList,
  _In_  PWDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER SourceIdentificationDescription,
  _Out_ PWDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER DestinationIdentificationDescription
)
{ ... }
````


## -parameters
<dl>

### -param <i>ChildList</i> [in]

<dd>
<p>A handle to a framework child-list object.</p>
</dd>

### -param <i>SourceIdentificationDescription</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551223">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER</a> structure that identifies the source location of the child identification description.</p>
</dd>

### -param <i>DestinationIdentificationDescription</i> [out]

<dd>
<p>A pointer to a WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER structure that identifies the destination location of the duplicate child identification description.</p>
</dd>
</dl>

## -returns
<p>The <i>EvtChildListIdentificationDescriptionDuplicate</i> callback function must return STATUS_SUCCESS, or another status value for which <a href="https://msdn.microsoft.com/fe823930-e3ff-4c95-a640-bb6470c95d1d">NT_SUCCESS</a>(<i>status</i>) equals <b>TRUE</b>, if the operation succeeds. Otherwise, this callback function must return a status value for which NT_SUCCESS(<i>status</i>) equals <b>FALSE</b>. </p>

## -remarks
<p>If a bus driver is using <a href="wdf.dynamic_enumeration">dynamic enumeration</a>, it can register an <i>EvtChildListIdentificationDescriptionDuplicate</i> callback function by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff547258">WdfFdoInitSetDefaultChildListConfig</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff545615">WdfChildListCreate</a>.</p>

<p>The framework duplicates driver-supplied identification descriptions so that it can have internal copies of the descriptions.</p>

<p>The <i>EvtChildListIdentificationDescriptionDuplicate</i> callback function must create a duplicate copy of an identification description. A driver must supply this callback function if the framework cannot call <a href="https://msdn.microsoft.com/library/windows/hardware/ff561808">RtlCopyMemory</a> to duplicate the identification description. (The framework cannot call <b>RtlCopyMemory</b> if the description contains pointers to additional memory.)</p>

<p>If your driver does not provide an <i>EvtChildListIdentificationDescriptionDuplicate</i> callback function, the framework duplicates identification descriptions by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff561808">RtlCopyMemory</a>.</p>

<p>The following steps describe a typical scenario:</p>

<p>The driver determines that a child device exists.</p>

<p>The driver creates an identification description by filling in a driver-defined structure that contains a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551223">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER</a> structure and possibly by dynamically allocating addition memory to store identification information that has a device-specific size. </p>

<p>The driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545591">WdfChildListAddOrUpdateChildDescriptionAsPresent</a> to report a child device, supplying a pointer to the identification description. </p>

<p>The framework calls the <i>EvtChildListIdentificationDescriptionDuplicate</i> callback function (if it exists) or <a href="https://msdn.microsoft.com/library/windows/hardware/ff561808">RtlCopyMemory</a> to duplicate the identification description so that it can have an internal copy of the description.</p>

<p>The framework can use <a href="https://msdn.microsoft.com/library/windows/hardware/ff561808">RtlCopyMemory</a> to duplicate an identification description, if the description consists of a single structure with a predetermined size that is specified by the <b>IdentificationDescriptionSize</b> member of the WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER structure. However, sometimes the description must also contain additional information that is stored in dynamically allocated memory. In this case, you will typically define a description structure so that a member points to the dynamically allocated memory, and your driver must provide an <i>EvtChildListIdentificationDescriptionDuplicate</i> callback function. The callback function must do the following:</p>

<p>Allocate additional memory, typically by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff544501">ExAllocatePool</a>.</p>

<p>Store the allocated memory's address in the driver-defined address description structure (that is, the callback function's <i>DestinationIdentificationDescription</i> structure).</p>

<p>Copy other structure members from the callback function's <i>SourceIdentificationDescription</i> structure to the callback function's <i>DestinationIdentificationDescription</i> structure.</p>

<p>The only <a href="https://msdn.microsoft.com/BFD91F00-5D35-4AF8-A6B6-F27DF64605D8">framework child-list object method</a> that a driver's <i>EvtChildListIdentificationDescriptionDuplicate</i> callback function can call is <a href="https://msdn.microsoft.com/library/windows/hardware/ff545636">WdfChildListGetDevice</a>.</p>

<p>The framework acquires an internal child-list object lock before calling the <i>EvtChildListIdentificationDescriptionDuplicate</i> callback function. This callback function must only perform operations that are related to the uplication operation, such as calling framework memory object methods and accessing object context space. It must not call methods that access other drivers.</p>

<p>If your driver supplies an <i>EvtChildListIdentificationDescriptionDuplicate</i> callback function, it might also need <a href="https://msdn.microsoft.com/c44d6a2f-c7ef-486d-973e-aada068ddc06">EvtChildListIdentificationDescriptionCopy</a>, <a href="https://msdn.microsoft.com/b807f9f8-588f-4303-be97-a9fd4cff2bbd">EvtChildListIdentificationDescriptionCompare</a>, and <a href="https://msdn.microsoft.com/4874f03e-b4e7-4fae-8737-7630462cd7e5">EvtChildListIdentificationDescriptionCleanup</a> callback functions.</p>

<p>For more information about dynamic enumeration, see <a href="wdf.enumerating_the_devices_on_a_bus">Enumerating the Devices on a Bus</a>.</p>

<p>To define an <i>EvtChildListIdentificationDescriptionDuplicate</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtChildListIdentificationDescriptionDuplicate</i> callback function that is named <i>MyChildListIdentificationDescriptionDuplicate</i>, use the <b>EVT_WDF_CHILD_LIST_IDENTIFICATION_DESCRIPTION_DUPLICATE</b> type as shown in this code example:</p>

<p>To define an <i>EvtChildListIdentificationDescriptionDuplicate</i> callback function that is named <b>MyChildListIdentificationDescriptionDuplicate</b>, you must first provide a function declaration that SDV and other verification tools require, as follows:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_WDF_CHILD_LIST_IDENTIFICATION_DESCRIPTION_DUPLICATE</b> function type is defined in the WdfChildlist.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_CHILD_LIST_IDENTIFICATION_DESCRIPTION_DUPLICATE</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

<p>If a bus driver is using <a href="wdf.dynamic_enumeration">dynamic enumeration</a>, it can register an <i>EvtChildListIdentificationDescriptionDuplicate</i> callback function by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff547258">WdfFdoInitSetDefaultChildListConfig</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff545615">WdfChildListCreate</a>.</p>

<p>The framework duplicates driver-supplied identification descriptions so that it can have internal copies of the descriptions.</p>

<p>The <i>EvtChildListIdentificationDescriptionDuplicate</i> callback function must create a duplicate copy of an identification description. A driver must supply this callback function if the framework cannot call <a href="https://msdn.microsoft.com/library/windows/hardware/ff561808">RtlCopyMemory</a> to duplicate the identification description. (The framework cannot call <b>RtlCopyMemory</b> if the description contains pointers to additional memory.)</p>

<p>If your driver does not provide an <i>EvtChildListIdentificationDescriptionDuplicate</i> callback function, the framework duplicates identification descriptions by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff561808">RtlCopyMemory</a>.</p>

<p>The following steps describe a typical scenario:</p>

<p>The driver determines that a child device exists.</p>

<p>The driver creates an identification description by filling in a driver-defined structure that contains a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551223">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER</a> structure and possibly by dynamically allocating addition memory to store identification information that has a device-specific size. </p>

<p>The driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545591">WdfChildListAddOrUpdateChildDescriptionAsPresent</a> to report a child device, supplying a pointer to the identification description. </p>

<p>The framework calls the <i>EvtChildListIdentificationDescriptionDuplicate</i> callback function (if it exists) or <a href="https://msdn.microsoft.com/library/windows/hardware/ff561808">RtlCopyMemory</a> to duplicate the identification description so that it can have an internal copy of the description.</p>

<p>The framework can use <a href="https://msdn.microsoft.com/library/windows/hardware/ff561808">RtlCopyMemory</a> to duplicate an identification description, if the description consists of a single structure with a predetermined size that is specified by the <b>IdentificationDescriptionSize</b> member of the WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER structure. However, sometimes the description must also contain additional information that is stored in dynamically allocated memory. In this case, you will typically define a description structure so that a member points to the dynamically allocated memory, and your driver must provide an <i>EvtChildListIdentificationDescriptionDuplicate</i> callback function. The callback function must do the following:</p>

<p>Allocate additional memory, typically by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff544501">ExAllocatePool</a>.</p>

<p>Store the allocated memory's address in the driver-defined address description structure (that is, the callback function's <i>DestinationIdentificationDescription</i> structure).</p>

<p>Copy other structure members from the callback function's <i>SourceIdentificationDescription</i> structure to the callback function's <i>DestinationIdentificationDescription</i> structure.</p>

<p>The only <a href="https://msdn.microsoft.com/BFD91F00-5D35-4AF8-A6B6-F27DF64605D8">framework child-list object method</a> that a driver's <i>EvtChildListIdentificationDescriptionDuplicate</i> callback function can call is <a href="https://msdn.microsoft.com/library/windows/hardware/ff545636">WdfChildListGetDevice</a>.</p>

<p>The framework acquires an internal child-list object lock before calling the <i>EvtChildListIdentificationDescriptionDuplicate</i> callback function. This callback function must only perform operations that are related to the uplication operation, such as calling framework memory object methods and accessing object context space. It must not call methods that access other drivers.</p>

<p>If your driver supplies an <i>EvtChildListIdentificationDescriptionDuplicate</i> callback function, it might also need <a href="https://msdn.microsoft.com/c44d6a2f-c7ef-486d-973e-aada068ddc06">EvtChildListIdentificationDescriptionCopy</a>, <a href="https://msdn.microsoft.com/b807f9f8-588f-4303-be97-a9fd4cff2bbd">EvtChildListIdentificationDescriptionCompare</a>, and <a href="https://msdn.microsoft.com/4874f03e-b4e7-4fae-8737-7630462cd7e5">EvtChildListIdentificationDescriptionCleanup</a> callback functions.</p>

<p>For more information about dynamic enumeration, see <a href="wdf.enumerating_the_devices_on_a_bus">Enumerating the Devices on a Bus</a>.</p>

<p>To define an <i>EvtChildListIdentificationDescriptionDuplicate</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtChildListIdentificationDescriptionDuplicate</i> callback function that is named <i>MyChildListIdentificationDescriptionDuplicate</i>, use the <b>EVT_WDF_CHILD_LIST_IDENTIFICATION_DESCRIPTION_DUPLICATE</b> type as shown in this code example:</p>

<p>To define an <i>EvtChildListIdentificationDescriptionDuplicate</i> callback function that is named <b>MyChildListIdentificationDescriptionDuplicate</b>, you must first provide a function declaration that SDV and other verification tools require, as follows:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_WDF_CHILD_LIST_IDENTIFICATION_DESCRIPTION_DUPLICATE</b> function type is defined in the WdfChildlist.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_CHILD_LIST_IDENTIFICATION_DESCRIPTION_DUPLICATE</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

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
<a href="https://msdn.microsoft.com/4874f03e-b4e7-4fae-8737-7630462cd7e5">EvtChildListIdentificationDescriptionCleanup</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b807f9f8-588f-4303-be97-a9fd4cff2bbd">EvtChildListIdentificationDescriptionCompare</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/c44d6a2f-c7ef-486d-973e-aada068ddc06">EvtChildListIdentificationDescriptionCopy</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544501">ExAllocatePool</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561808">RtlCopyMemory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551223">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545591">WdfChildListAddOrUpdateChildDescriptionAsPresent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545615">WdfChildListCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545636">WdfChildListGetDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547258">WdfFdoInitSetDefaultChildListConfig</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20EVT_WDF_CHILD_LIST_IDENTIFICATION_DESCRIPTION_DUPLICATE callback function%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
