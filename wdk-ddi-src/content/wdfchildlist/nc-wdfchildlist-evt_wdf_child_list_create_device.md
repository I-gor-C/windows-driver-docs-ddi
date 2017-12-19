---
UID: NC.wdfchildlist.EVT_WDF_CHILD_LIST_CREATE_DEVICE
title: EVT_WDF_CHILD_LIST_CREATE_DEVICE
author: windows-driver-content
description: A bus driver'sEvtChildListCreateDevice event callback function creates a framework device object for a new device that has been dynamically enumerated.
old-location: wdf\evtchildlistcreatedevice.htm
old-project: wdf
ms.assetid: 296fbe06-1680-43a8-b5c3-1a1faa19c6c3
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _WDBGEXTS_THREAD_OS_INFO, PWDBGEXTS_THREAD_OS_INFO, WDBGEXTS_THREAD_OS_INFO, *PWDBGEXTS_THREAD_OS_INFO
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
req.alt-api: EvtChildListCreateDevice
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
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# EVT_WDF_CHILD_LIST_CREATE_DEVICE callback



## -description
<p class="CCE_Message">[Applies to KMDF only]

A bus driver's<i>EvtChildListCreateDevice</i> event callback function creates a framework device object for a new device that has been dynamically enumerated.



## -prototype

````
EVT_WDF_CHILD_LIST_CREATE_DEVICE EvtChildListCreateDevice;

NTSTATUS EvtChildListCreateDevice(
  _In_ WDFCHILDLIST                                 ChildList,
  _In_ PWDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER IdentificationDescription,
  _In_ PWDFDEVICE_INIT                              ChildInit
)
{ ... }
````


## -parameters

### -param ChildList [in]

A handle to the framework child-list object that the driver specified when it called <a href="wdf.wdfchildlistaddorupdatechilddescriptionaspresent">WdfChildListAddOrUpdateChildDescriptionAsPresent</a>.


### -param IdentificationDescription [in]

A pointer to a copy of the <a href="wdf.wdf_child_identification_description_header">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER</a> structure that the driver specified when it called <a href="wdf.wdfchildlistaddorupdatechilddescriptionaspresent">WdfChildListAddOrUpdateChildDescriptionAsPresent</a>.


### -param ChildInit [in]

A pointer to a <a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a> structure.


## -returns
The <i>EvtChildListCreateDevice</i> callback function must return STATUS_SUCCESS, or another status value for which <a href="https://msdn.microsoft.com/fe823930-e3ff-4c95-a640-bb6470c95d1d">NT_SUCCESS</a>(<i>status</i>) equals <b>TRUE</b>, if the operation succeeds. Otherwise, this function must return a status value for which NT_SUCCESS(<i>status</i>) equals <b>FALSE</b>.

If the operation failed but you think your driver should try again later, and if the driver's <i>EvtChildListCreateDevice</i> callback function has not called <a href="wdf.wdfdevicecreate">WdfDeviceCreate</a>, the driver can return STATUS_RETRY. As a result, the framework calls the <i>EvtChildListCreateDevice</i> callback function again later. If your driver returns STATUS_RETRY more than a few times, the framework will stop calling the callback function for the failing device.


## -remarks
If a bus driver is using <a href="wdf.dynamic_enumeration">dynamic enumeration</a>, it can register an <i>EvtChildListCreateDevice</i> callback function by calling <a href="wdf.wdffdoinitsetdefaultchildlistconfig">WdfFdoInitSetDefaultChildListConfig</a> or <a href="wdf.wdfchildlistcreate">WdfChildListCreate</a>.

After a driver calls <a href="wdf.wdfchildlistaddorupdatechilddescriptionaspresent">WdfChildListAddOrUpdateChildDescriptionAsPresent</a> or <a href="wdf.wdfchildlistupdateallchilddescriptionsaspresent">WdfChildListUpdateAllChildDescriptionsAsPresent</a>, the framework calls the driver's <i>EvtChildListCreateDevice</i> callback function. The callback function must call <a href="wdf.wdfdevicecreate">WdfDeviceCreate</a> to create a framework device object (a PDO).

Before calling <a href="wdf.wdfdevicecreate">WdfDeviceCreate</a>, the driver must call framework-supplied functions that initialize the WDFDEVICE_INIT structure. For more information about these functions, see <a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a>.

For more information about calling <a href="wdf.wdfdevicecreate">WdfDeviceCreate</a>, see <a href="wdf.creating_a_framework_device_object">Creating a Framework Device Object</a>.

For more information about dynamic enumeration, see <a href="wdf.enumerating_the_devices_on_a_bus">Enumerating the Devices on a Bus</a>.

To define an <i>EvtChildListCreateDevice</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="https://msdn.microsoft.com/2F3549EF-B50F-455A-BDC7-1F67782B8DCA">Code Analysis for Drivers</a>, <a href="https://msdn.microsoft.com/74feeb16-387c-4796-987a-aff3fb79b556">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.

For example, to define an <i>EvtChildListCreateDevice</i> callback function that is named <i>MyChildListCreateDevice</i>, use the <b>EVT_WDF_CHILD_LIST_CREATE_DEVICE</b> type as shown in this code example:

Then, implement your callback function as follows:

The <b>EVT_WDF_CHILD_LIST_CREATE_DEVICE</b> function type is defined in the WdfChildlist.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_CHILD_LIST_CREATE_DEVICE</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/73a408ba-0219-4fde-8dad-ca330e4e67c3">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.


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
<dt>WdfChildlist.h (include Wdf.h)</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdf_child_identification_description_header">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER</a>
</dt>
<dt>
<a href="wdf.wdfchildlistaddorupdatechilddescriptionaspresent">WdfChildListAddOrUpdateChildDescriptionAsPresent</a>
</dt>
<dt>
<a href="wdf.wdfchildlistcreate">WdfChildListCreate</a>
</dt>
<dt>
<a href="wdf.wdfchildlistupdateallchilddescriptionsaspresent">WdfChildListUpdateAllChildDescriptionsAsPresent</a>
</dt>
<dt>
<a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a>
</dt>
<dt>
<a href="wdf.wdfdevicecreate">WdfDeviceCreate</a>
</dt>
<dt>
<a href="wdf.wdffdoinitsetdefaultchildlistconfig">WdfFdoInitSetDefaultChildListConfig</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20EVT_WDF_CHILD_LIST_CREATE_DEVICE callback function%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

