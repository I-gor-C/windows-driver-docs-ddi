---
UID: NF.wdfchildlist.WdfChildListAddOrUpdateChildDescriptionAsPresent
title: WdfChildListAddOrUpdateChildDescriptionAsPresent function
author: windows-driver-content
description: The WdfChildListAddOrUpdateChildDescriptionAsPresent method adds a new child description to a list of children or updates an existing child description.
old-location: wdf\wdfchildlistaddorupdatechilddescriptionaspresent.htm
old-project: wdf
ms.assetid: 10d169bc-4476-4d7f-8eeb-49941c12a7a0
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfChildListAddOrUpdateChildDescriptionAsPresent
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
req.alt-api: WdfChildListAddOrUpdateChildDescriptionAsPresent
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
req.product: Windows 10 or later.
---

# WdfChildListAddOrUpdateChildDescriptionAsPresent function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfChildListAddOrUpdateChildDescriptionAsPresent</b> method adds a new child description to a list of children or updates an existing child description.



## -syntax

````
NTSTATUS WdfChildListAddOrUpdateChildDescriptionAsPresent(
  _In_     WDFCHILDLIST                                 ChildList,
  _In_     PWDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER IdentificationDescription,
  _In_opt_ PWDF_CHILD_ADDRESS_DESCRIPTION_HEADER        AddressDescription
);
````


## -parameters

### -param ChildList [in]

A handle to a framework child list object.


### -param IdentificationDescription [in]

A pointer to a <a href="wdf.wdf_child_identification_description_header">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER</a> structure that identifies a child <a href="wdf.dynamic_enumeration#dynamic_child_descriptions#dynamic_child_descriptions">identification description</a>.


### -param AddressDescription [in, optional]

A pointer to a <a href="wdf.wdf_child_address_description_header">WDF_CHILD_ADDRESS_DESCRIPTION_HEADER</a> structure that identifies a child <a href="wdf.dynamic_enumeration#dynamic_child_descriptions#dynamic_child_descriptions">address description</a>. If an address description is not needed, this parameter can be <b>NULL</b>.


## -returns
<b>WdfChildListAddOrUpdateChildDescriptionAsPresent</b> returns STATUS_SUCCESS, or another NTSTATUS-typed status value for which <a href="https://msdn.microsoft.com/fe823930-e3ff-4c95-a640-bb6470c95d1d">NT_SUCCESS(status)</a> equals <b>TRUE</b>, if the operation succeeds. Otherwise, this method might return one of the following values:
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>An input parameter was invalid.
<dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl>The size of the identification description or address description was incorrect.
<dl>
<dt><b>STATUS_OBJECT_NAME_EXISTS</b></dt>
</dl>A child with the supplied identification description already exists. In this case, the framework copies the supplied address description to the existing child.
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>A child description could be allocated.

 

This method might also return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.



A system bug check occurs if the driver supplies an invalid object handle.



## -remarks
The <b>WdfChildListAddOrUpdateChildDescriptionAsPresent</b> method searches the specified child list for a child that matches the supplied identification description. If a match is found, the framework updates the child's address description, if supplied, and returns STATUS_OBJECT_NAME_EXISTS. If no match is found, the framework creates a new child by using the supplied identification and address descriptions.

A driver can call <b>WdfChildListAddOrUpdateChildDescriptionAsPresent</b> to add or update a single child description. The framework immediately updates the child list and informs the Plug and Play (PnP) manager that changes have been made.

Alternatively, the driver can do the following:

Call <a href="wdf.wdfchildlistbeginscan">WdfChildListBeginScan</a> to prepare the child list for updating.

Call <b>WdfChildListAddOrUpdateChildDescriptionAsPresent</b> multiple times to add or update the child descriptions for all of the parent device's children.

Call <a href="wdf.wdfchildlistendscan">WdfChildListEndScan</a> to process changes to the child list.

If the driver uses this alternative procedure, the framework waits until the driver calls <a href="wdf.wdfchildlistendscan">WdfChildListEndScan</a> before updating the child list and informing the PnP manager that changes have been made. When your driver calls <a href="wdf.wdfchildlistbeginscan">WdfChildListBeginScan</a>, the framework marks all previously reported devices as no longer being present. Therefore, the driver must call <b>WdfChildListAddOrUpdateChildDescriptionAsPresent</b> for all children, not just newly discovered children. 

At some time after a driver calls <b>WdfChildListAddOrUpdateChildDescriptionAsPresent</b>, the framework calls the driver's <a href="..\wdfchildlist\nc-wdfchildlist-evt_wdf_child_list_create_device.md">EvtChildListCreateDevice</a> callback function so that the driver can create a device object by calling <a href="wdf.wdfdevicecreate">WdfDeviceCreate</a>.

For more information about child lists, see <a href="wdf.dynamic_enumeration">Dynamic Enumeration</a>.

The following code example is based on code that the <a href="http://go.microsoft.com/fwlink/p/?linkid=256131">kmdf_fx2</a> sample contains. The example adds child descriptions to a device's default child list. It retrieves switch settings that the driver previously stored in a device object's context space and then calls <b>WdfChildListAddOrUpdateChildDescriptionAsPresent</b> for each switch that is set.


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
Header

</th>
<td width="70%">
<dl>
<dt>Wdfchildlist.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= DISPATCH_LEVEL

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
<a href="..\wdfchildlist\nc-wdfchildlist-evt_wdf_child_list_create_device.md">EvtChildListCreateDevice</a>
</dt>
<dt>
<a href="wdf.wdf_child_identification_description_header">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER</a>
</dt>
<dt>
<a href="wdf.wdf_child_identification_description_header_init">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER_INIT</a>
</dt>
<dt>
<a href="wdf.wdfchildlistbeginscan">WdfChildListBeginScan</a>
</dt>
<dt>
<a href="wdf.wdfchildlistendscan">WdfChildListEndScan</a>
</dt>
<dt>
<a href="wdf.wdfdevicecreate">WdfDeviceCreate</a>
</dt>
<dt>
<a href="wdf.wdffdogetdefaultchildlist">WdfFdoGetDefaultChildList</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfChildListAddOrUpdateChildDescriptionAsPresent method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

