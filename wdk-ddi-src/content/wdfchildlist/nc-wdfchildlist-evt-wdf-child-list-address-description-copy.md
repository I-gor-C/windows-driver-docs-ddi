---
UID: NC.wdfchildlist.EVT_WDF_CHILD_LIST_ADDRESS_DESCRIPTION_COPY
title: EVT_WDF_CHILD_LIST_ADDRESS_DESCRIPTION_COPY
author: windows-driver-content
description: A driver's EvtChildListAddressDescriptionCopy event callback function copies a child address description from one specified location to another.
old-location: wdf\evtchildlistaddressdescriptioncopy.htm
old-project: wdf
ms.assetid: b73ec39c-8d93-4992-8791-5070a088701a
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
req.alt-api: EvtChildListAddressDescriptionCopy
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

# EVT_WDF_CHILD_LIST_ADDRESS_DESCRIPTION_COPY callback



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>A driver's <i>EvtChildListAddressDescriptionCopy</i> event callback function copies a child address description from one specified location to another.</p>


## -prototype

````
EVT_WDF_CHILD_LIST_ADDRESS_DESCRIPTION_COPY EvtChildListAddressDescriptionCopy;

VOID EvtChildListAddressDescriptionCopy(
  _In_  WDFCHILDLIST                          ChildList,
  _In_  PWDF_CHILD_ADDRESS_DESCRIPTION_HEADER SourceAddressDescription,
  _Out_ PWDF_CHILD_ADDRESS_DESCRIPTION_HEADER DestinationAddressDescription
)
{ ... }
````


## -parameters
<dl>

### -param <i>ChildList</i> [in]

<dd>
<p>A handle to a framework child-list object.</p>
</dd>

### -param <i>SourceAddressDescription</i> [in]

<dd>
<p>A pointer to a <a href="..\wdfchildlist\ns-wdfchildlist--wdf-child-address-description-header.md">WDF_CHILD_ADDRESS_DESCRIPTION_HEADER</a> structure that identifies the source location of the child address description.</p>
</dd>

### -param <i>DestinationAddressDescription</i> [out]

<dd>
<p>A pointer to a WDF_CHILD_ADDRESS_DESCRIPTION_HEADER structure that identifies the destination location of the child address description.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>If a bus driver is using <a href="wdf.dynamic_enumeration">dynamic enumeration</a>, it can register an  <i>EvtChildListAddressDescriptionCopy</i> callback function by calling <a href="..\wdffdo\nf-wdffdo-wdffdoinitsetdefaultchildlistconfig.md">WdfFdoInitSetDefaultChildListConfig</a> or <a href="..\wdfchildlist\nf-wdfchildlist-wdfchildlistcreate.md">WdfChildListCreate</a>.</p>

<p>The framework copies information from one driver-supplied address description to another when it needs to update an existing description with new information, or when it needs to pass the contents of an address description to the driver.</p>

<p>The <i>EvtChildListAddressDescriptionCopy</i> callback function must copy the contents of a source description to a destination description. A driver must supply this callback function if its child devices require an address description, and if the framework cannot call <a href="..\wdm\nf-wdm-rtlcopymemory.md">RtlCopyMemory</a> to copy the address description. (The framework cannot call <b>RtlCopyMemory</b> if the description contains pointers to additional memory.)</p>

<p>If your driver provides address descriptions but does not provide a <i>EvtChildListAddressDescriptionCopy</i> callback function, the framework copies address descriptions by calling <a href="..\wdm\nf-wdm-rtlcopymemory.md">RtlCopyMemory</a>.</p>

<p>The following steps describe a typical scenario:</p>

<p>The driver determines that a child device exists.</p>

<p>The driver creates an address description by filling in a driver-defined structure that contains a <a href="..\wdfchildlist\ns-wdfchildlist--wdf-child-address-description-header.md">WDF_CHILD_ADDRESS_DESCRIPTION_HEADER</a> structure and possibly by dynamically allocating additional memory to store address information that has a device-specific size. </p>

<p>The driver calls <a href="..\wdfchildlist\nf-wdfchildlist-wdfchildlistaddorupdatechilddescriptionaspresent.md">WdfChildListAddOrUpdateChildDescriptionAsPresent</a> to report a child device, supplying a pointer to the address description. </p>

<p>The framework determines that the driver had previously reported the device, so the framework can update the device's old address description with new information. </p>

<p>The framework calls the <i>EvtChildListAddressDescriptionCopy</i> callback function (if it exists) or <a href="..\wdm\nf-wdm-rtlcopymemory.md">RtlCopyMemory</a> to copy the new address description information into the existing address description.</p>

<p>The framework can use <a href="..\wdm\nf-wdm-rtlcopymemory.md">RtlCopyMemory</a> to copy an address description, if the description consists of a single structure with a predetermined size that is specified by the <b>AddressDescriptionSize</b> member of the <a href="..\wdfchildlist\ns-wdfchildlist--wdf-child-address-description-header.md">WDF_CHILD_ADDRESS_DESCRIPTION_HEADER</a> structure. However, sometimes the description must also contain additional information that is stored in dynamically allocated memory. In this case, you will typically define a description structure so that a member points to the dynamically allocated memory, and your driver must provide an <i>EvtChildListAddressDescriptionCopy</i> callback function. The callback function must do the following:</p>

<p>In the callback function's <i>SourceAddressDescription</i> and <i>DestinationAddressDescription</i> structures, find the pointers to dynamically allocated memory.</p>

<p>Copy the dynamically allocated memory from the source to the destination, using the pointers.</p>

<p>Copy other structure members from the callback function's <i>SourceAddressDescription</i> structure to the callback function's <i>DestinationAddressDescription</i> structure.</p>

<p>The only <a href="wdf.wdf_child-list_object_reference">framework child-list object method</a> that a driver's <i>EvtChildListAddressDescriptionCopy</i> callback function can call is <a href="..\wdfchildlist\nf-wdfchildlist-wdfchildlistgetdevice.md">WdfChildListGetDevice</a>.</p>

<p>The framework acquires an internal child-list object lock before calling the <i>EvtChildListAddressDescriptionCopy</i> callback function. The callback function must only perform operations that are related to the described copy operation, such as calling framework memory object methods and accessing object context space. It must not call methods that access other drivers.</p>

<p>If your driver supplies an <i>EvtChildListAddressDescriptionCopy</i> callback function, it might also need <a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-address-description-duplicate.md">EvtChildListAddressDescriptionDuplicate</a> and <a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-address-description-cleanup.md">EvtChildListAddressDescriptionCleanup</a> callback functions.</p>

<p>For more information about dynamic enumeration, see <a href="wdf.enumerating_the_devices_on_a_bus">Enumerating the Devices on a Bus</a><u>.</u></p>

<p>To define an <i>EvtChildListAddressDescriptionCopy</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtChildListAddressDescriptionCopy</i> callback function that is named <i>MyChildListAddressDescriptionCopy</i>, use the <b>EVT_WDF_CHILD_LIST_ADDRESS_DESCRIPTION</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_WDF_CHILD_LIST_ADDRESS_DESCRIPTION</b> function type is defined in the WdfChildlist.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_CHILD_LIST_ADDRESS_DESCRIPTION</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

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
<a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-address-description-cleanup.md">EvtChildListAddressDescriptionCleanup</a>
</dt>
<dt>
<a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-address-description-duplicate.md">EvtChildListAddressDescriptionDuplicate</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-rtlcopymemory.md">RtlCopyMemory</a>
</dt>
<dt>
<a href="..\wdfchildlist\ns-wdfchildlist--wdf-child-address-description-header.md">WDF_CHILD_ADDRESS_DESCRIPTION_HEADER</a>
</dt>
<dt>
<a href="..\wdfchildlist\nf-wdfchildlist-wdfchildlistaddorupdatechilddescriptionaspresent.md">WdfChildListAddOrUpdateChildDescriptionAsPresent</a>
</dt>
<dt>
<a href="..\wdfchildlist\nf-wdfchildlist-wdfchildlistcreate.md">WdfChildListCreate</a>
</dt>
<dt>
<a href="..\wdfchildlist\nf-wdfchildlist-wdfchildlistgetdevice.md">WdfChildListGetDevice</a>
</dt>
<dt>
<a href="..\wdffdo\nf-wdffdo-wdffdoinitsetdefaultchildlistconfig.md">WdfFdoInitSetDefaultChildListConfig</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20EVT_WDF_CHILD_LIST_ADDRESS_DESCRIPTION_COPY callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
