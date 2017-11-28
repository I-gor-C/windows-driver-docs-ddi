---
UID: NF.wdfchildlist.WdfChildListUpdateChildDescriptionAsMissing
title: WdfChildListUpdateChildDescriptionAsMissing
author: windows-driver-content
description: The WdfChildListUpdateChildDescriptionAsMissing method informs the framework that a specified child device is currently unplugged or otherwise unavailable.
old-location: wdf\wdfchildlistupdatechilddescriptionasmissing.htm
old-project: wdf
ms.assetid: 21932a96-285c-490d-a1fb-a137aed57bbb
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfChildListUpdateChildDescriptionAsMissing
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
req.alt-api: WdfChildListUpdateChildDescriptionAsMissing
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

# WdfChildListUpdateChildDescriptionAsMissing function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfChildListUpdateChildDescriptionAsMissing</b> method informs the framework that a specified child device is currently unplugged or otherwise unavailable.</p>


## -syntax

````
NTSTATUS WdfChildListUpdateChildDescriptionAsMissing(
  _In_ WDFCHILDLIST                                 ChildList,
  _In_ PWDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER IdentificationDescription
);
````


## -parameters
<dl>

### -param <i>ChildList</i> [in]

<dd>
<p>A handle to a child list object.</p>
</dd>

### -param <i>IdentificationDescription</i> [in]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff551223">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER</a> structure that identifies a driver-supplied child <a href="wdf.dynamic_enumeration#dynamic_child_descriptions#dynamic_child_descriptions">identification description</a>.</p>
</dd>
</dl>

## -returns
<p><b>WdfChildListUpdateChildDescriptionAsMissing</b> returns STATUS_SUCCESS, or another status value for which <a href="https://msdn.microsoft.com/fe823930-e3ff-4c95-a640-bb6470c95d1d">NT_SUCCESS(status)</a> equals <b>TRUE</b>, if the operation succeeds. Otherwise, this method might return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An input parameter was invalid.</p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>The size of the structure that <i>IdentificationDescription</i> points to was incorrect.</p><dl>
<dt><b>STATUS_NO_SUCH_DEVICE</b></dt>
</dl><p>The specified device was not found in the child list.</p>

<p> </p>

<p>This method might also return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.

</p>

<p>A system bug check occurs if the driver supplies an invalid object handle.
</p>

## -remarks
<p>Your driver can report that a device is unavailable even if the driver never called <a href="https://msdn.microsoft.com/library/windows/hardware/ff545591">WdfChildListAddOrUpdateChildDescriptionAsPresent</a> to report that the device was present. In this case, the <b>WdfChildListUpdateChildDescriptionAsMissing</b> method just returns STATUS_NO_SUCH_DEVICE.</p>

<p>If you want to report that all devices in a child list are unavailable, your driver can simply call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545608">WdfChildListBeginScan</a>, followed immediately by <a href="https://msdn.microsoft.com/library/windows/hardware/ff545626">WdfChildListEndScan</a>, instead of calling <b>WdfChildListUpdateChildDescriptionAsMissing</b> for each device.</p>

<p>For more information about child devices and child lists, see <a href="wdf.dynamic_enumeration">Dynamic Enumeration</a>.</p>

<p>The following code example informs the framework that a child device with a specified serial number is unavailable.</p>

<p>Your driver can report that a device is unavailable even if the driver never called <a href="https://msdn.microsoft.com/library/windows/hardware/ff545591">WdfChildListAddOrUpdateChildDescriptionAsPresent</a> to report that the device was present. In this case, the <b>WdfChildListUpdateChildDescriptionAsMissing</b> method just returns STATUS_NO_SUCH_DEVICE.</p>

<p>If you want to report that all devices in a child list are unavailable, your driver can simply call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545608">WdfChildListBeginScan</a>, followed immediately by <a href="https://msdn.microsoft.com/library/windows/hardware/ff545626">WdfChildListEndScan</a>, instead of calling <b>WdfChildListUpdateChildDescriptionAsMissing</b> for each device.</p>

<p>For more information about child devices and child lists, see <a href="wdf.dynamic_enumeration">Dynamic Enumeration</a>.</p>

<p>The following code example informs the framework that a child device with a specified serial number is unavailable.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551223">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551225">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545591">WdfChildListAddOrUpdateChildDescriptionAsPresent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfChildListUpdateChildDescriptionAsMissing method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
