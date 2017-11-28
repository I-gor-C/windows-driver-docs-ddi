---
UID: NF.wdfchildlist.WdfChildListRetrieveNextDevice
title: WdfChildListRetrieveNextDevice
author: windows-driver-content
description: The WdfChildListRetrieveNextDevice method traverses a specified child list and retrieves the next child device that matches specified criteria.
old-location: wdf\wdfchildlistretrievenextdevice.htm
old-project: wdf
ms.assetid: 925807ff-e445-4ccf-ace6-fd913439799b
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfChildListRetrieveNextDevice
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfchildlist.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfChildListRetrieveNextDevice
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
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfChildListRetrieveNextDevice function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfChildListRetrieveNextDevice</b> method traverses a specified child list and retrieves the next child device that matches specified criteria.</p>


## -syntax

````
NTSTATUS WdfChildListRetrieveNextDevice(
  _In_    WDFCHILDLIST             ChildList,
  _In_    PWDF_CHILD_LIST_ITERATOR Iterator,
  _Out_   WDFDEVICE                *Device,
  _Inout_ PWDF_CHILD_RETRIEVE_INFO Info
);
````


## -parameters
<dl>

### -param <i>ChildList</i> [in]

<dd>
<p>A handle to a framework child-list object.</p>
</dd>

### -param <i>Iterator</i> [in]

<dd>
<p>A pointer to the same caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff551230">WDF_CHILD_LIST_ITERATOR</a> structure that the driver previously supplied to <a href="https://msdn.microsoft.com/library/windows/hardware/ff545601">WdfChildListBeginIteration</a>.</p>
</dd>

### -param <i>Device</i> [out]

<dd>
<p>A pointer to a location that receives a handle to a framework device object. The received value is <b>NULL</b> if the <i>Iterator</i> parameter specifies the <a href="..\wdfchildlist\ne-wdfchildlist--wdf-retrieve-child-flags.md">WdfRetrievePendingChildren</a> flag.</p>
</dd>

### -param <i>Info</i> [in, out]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff551234">WDF_CHILD_RETRIEVE_INFO</a> structure. This pointer is optional and can be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p><b>WdfChildListRetrieveNextDevice</b> returns STATUS_SUCCESS, or another status value for which <a href="https://msdn.microsoft.com/fe823930-e3ff-4c95-a640-bb6470c95d1d">NT_SUCCESS(status)</a> equals <b>TRUE</b>, if the operation succeeds. Otherwise, this method might return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An input parameter was invalid.</p><dl>
<dt><b>STATUS_INFO_LENGTH_MISMATCH</b></dt>
</dl><p>The size of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551230">WDF_CHILD_LIST_ITERATOR</a> structure that <i>Iterator</i> specified was incorrect</p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>An address description was specified but the child list did not contain address descriptions.</p><dl>
<dt><b>STATUS_NO_MORE_ENTRIES</b></dt>
</dl><p>The framework reached the end of the child list.</p><dl>
<dt><b>STATUS_INVALID_DEVICE_STATE</b></dt>
</dl><p>The driver has not called <a href="https://msdn.microsoft.com/library/windows/hardware/ff545601">WdfChildListBeginIteration</a>.</p>

<p> </p>

<p>This method might also return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.

</p>

<p>A system bug check occurs if the driver supplies an invalid object handle.
</p>

## -remarks
<p>Before calling <b>WdfChildListRetrieveNextDevice</b>, your driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545601">WdfChildListBeginIteration</a>. After the driver has finished traversing the child list, it must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545618">WdfChildListEndIteration</a>. The framework then informs the Plug and Play (PnP) manager of any changes that were made to the child list.</p>

<p>Each time the driver calls <b>WdfChildListRetrieveNextDevice</b>, the method retrieves the next child that matches the following search criteria:</p>

<p>The child's type must correspond to <a href="https://msdn.microsoft.com/library/windows/hardware/ff552507">WDF_RETRIEVE_CHILD_FLAGS</a>-typed flags in the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff551230">WDF_CHILD_LIST_ITERATOR</a> structure.</p>

<p>If the driver provides a pointer to an <a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-identification-description-compare.md">EvtChildListIdentificationDescriptionCompare</a> callback function in its <a href="https://msdn.microsoft.com/library/windows/hardware/ff551234">WDF_CHILD_RETRIEVE_INFO</a> structure, the callback function must return <b>TRUE</b>.</p>

<p>If the driver provides an <a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-identification-description-compare.md">EvtChildListIdentificationDescriptionCompare</a> callback function, it must also provide an <a href="wdf.dynamic_enumeration#dynamic_child_descriptions#dynamic_child_descriptions">identification description</a> in the WDF_CHILD_RETRIEVE_INFO structure. The framework uses the callback function to compare the passed-in identification descriptor with a child's description in the child list, if the WDF_RETRIEVE_CHILD_FLAGS-typed flags indicate that the child is a match candidate. If the callback function returns <b>TRUE</b>, the match is successful. If the callback function returns <b>FALSE</b>, the framework looks for another candidate.</p>

<p>When <b>WdfChildListRetrieveNextDevice</b> finds a match, it copies the child's identification description and address description into the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff551234">WDF_CHILD_RETRIEVE_INFO</a> structure, if the pointer that the <i>Info</i> parameter specifies is not <b>NULL</b>. (Note that this operation overwrites the driver's input identification description.) The method also places a handle to the child's device object in the location that the <i>Device</i> parameter identifies.</p>

<p>For more information about child lists, see <a href="wdf.dynamic_enumeration">Dynamic Enumeration</a>.</p>

<p>The following code example informs the framework that all of a parent device's children are being ejected. The example obtains a device's default child list and walks through the list. It obtains each child's identification descriptor, and it passes each identification descriptor to <a href="https://msdn.microsoft.com/library/windows/hardware/ff545641">WdfChildListRequestChildEject</a>.</p>

<p>Before calling <b>WdfChildListRetrieveNextDevice</b>, your driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545601">WdfChildListBeginIteration</a>. After the driver has finished traversing the child list, it must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545618">WdfChildListEndIteration</a>. The framework then informs the Plug and Play (PnP) manager of any changes that were made to the child list.</p>

<p>Each time the driver calls <b>WdfChildListRetrieveNextDevice</b>, the method retrieves the next child that matches the following search criteria:</p>

<p>The child's type must correspond to <a href="https://msdn.microsoft.com/library/windows/hardware/ff552507">WDF_RETRIEVE_CHILD_FLAGS</a>-typed flags in the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff551230">WDF_CHILD_LIST_ITERATOR</a> structure.</p>

<p>If the driver provides a pointer to an <a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-identification-description-compare.md">EvtChildListIdentificationDescriptionCompare</a> callback function in its <a href="https://msdn.microsoft.com/library/windows/hardware/ff551234">WDF_CHILD_RETRIEVE_INFO</a> structure, the callback function must return <b>TRUE</b>.</p>

<p>If the driver provides an <a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-identification-description-compare.md">EvtChildListIdentificationDescriptionCompare</a> callback function, it must also provide an <a href="wdf.dynamic_enumeration#dynamic_child_descriptions#dynamic_child_descriptions">identification description</a> in the WDF_CHILD_RETRIEVE_INFO structure. The framework uses the callback function to compare the passed-in identification descriptor with a child's description in the child list, if the WDF_RETRIEVE_CHILD_FLAGS-typed flags indicate that the child is a match candidate. If the callback function returns <b>TRUE</b>, the match is successful. If the callback function returns <b>FALSE</b>, the framework looks for another candidate.</p>

<p>When <b>WdfChildListRetrieveNextDevice</b> finds a match, it copies the child's identification description and address description into the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff551234">WDF_CHILD_RETRIEVE_INFO</a> structure, if the pointer that the <i>Info</i> parameter specifies is not <b>NULL</b>. (Note that this operation overwrites the driver's input identification description.) The method also places a handle to the child's device object in the location that the <i>Device</i> parameter identifies.</p>

<p>For more information about child lists, see <a href="wdf.dynamic_enumeration">Dynamic Enumeration</a>.</p>

<p>The following code example informs the framework that all of a parent device's children are being ejected. The example obtains a device's default child list and walks through the list. It obtains each child's identification descriptor, and it passes each identification descriptor to <a href="https://msdn.microsoft.com/library/windows/hardware/ff545641">WdfChildListRequestChildEject</a>.</p>

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
<dt>Wdfchildlist.h (include Wdf.h)</dt>
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
<p>&lt;= DISPATCH_LEVEL</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551230">WDF_CHILD_LIST_ITERATOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551232">WDF_CHILD_LIST_ITERATOR_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551225">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551234">WDF_CHILD_RETRIEVE_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552507">WDF_RETRIEVE_CHILD_FLAGS</a>
</dt>
<dt>
<a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-identification-description-compare.md">EvtChildListIdentificationDescriptionCompare</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545608">WdfChildListBeginScan</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545641">WdfChildListRequestChildEject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545655">WdfChildListRetrieveNextDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545601">WdfChildListBeginIteration</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545618">WdfChildListEndIteration</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfChildListRetrieveNextDevice method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
