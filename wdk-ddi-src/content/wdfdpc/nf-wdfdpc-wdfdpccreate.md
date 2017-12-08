---
UID: NF.wdfdpc.WdfDpcCreate
title: WdfDpcCreate function
author: windows-driver-content
description: The WdfDpcCreate method creates a framework DPC object and registers an EvtDpcFunc callback function.
old-location: wdf\wdfdpccreate.htm
old-project: wdf
ms.assetid: 46c6ffd1-4c01-4d1d-b7da-8f97f728ac71
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfDpcCreate
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdpc.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfDpcCreate
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
req.irql: <=DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfDpcCreate function



## -description
<p class="CCE_Message">[Applies to KMDF only]
The <b>WdfDpcCreate</b> method creates a framework DPC object and registers an <a href="wdf.evtdpcfunc">EvtDpcFunc</a> callback function. 


## -syntax

````
NTSTATUS WdfDpcCreate(
  _In_  PWDF_DPC_CONFIG        Config,
  _In_  PWDF_OBJECT_ATTRIBUTES Attributes,
  _Out_ WDFDPC                 *Dpc
);
````


## -parameters

### -param Config [in]

A pointer to a caller-allocated <a href="wdf.wdf_dpc_config">WDF_DPC_CONFIG</a> structure.

### -param Attributes [in]

A pointer to a caller-allocated <a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a> structure that specifies attributes for the new DPC object. 

### -param Dpc [out]

A pointer to a location that receives a handle to the new framework DPC object.

## -returns
<b>WdfDpcCreate</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, the method might return one of the following values:
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>An invalid parameter was specified.
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>A DPC object could not be allocated.
<dl>
<dt><b>STATUS_WDF_PARENT_NOT_SPECIFIED</b></dt>
</dl>A parent object was not specified in the <a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a> structure.
<dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl>The <b>ParentObject</b> member of the <a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a> structure does not reference a framework device object or an object whose chain of parents leads to a framework device object.
<dl>
<dt><b>STATUS_WDF_INCOMPATIBLE_EXECUTION_LEVEL</b></dt>
</dl>The <b>AutomaticSerialization</b> member of the <a href="wdf.wdf_dpc_config">WDF_DPC_CONFIG</a> structure is set to <b>TRUE</b>, but the parent object's <a href="wdf.wdf_execution_level">execution level</a> is set to <b>WdfExecutionLevelPassive</b>.

 

For a list of other return values that the <b>WdfDpcCreate</b> method might return, see <a href="wdf.framework_object_creation_errors">Framework Object Creation Errors</a>.

This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.

## -remarks
A driver typically calls <b>WdfDpcCreate</b> from within its <a href="..\wdfdriver\nc-wdfdriver-evt_wdf_driver_device_add.md">EvtDriverDeviceAdd</a> callback function.

When a driver creates a DPC object, it must specify a parent object in the <b>ParentObject</b> member of the <a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a> structure. The parent object can be a framework device object or any object whose chain of parents leads to a framework device object. The framework will delete the DPC object when it deletes the device object.

Calling <b>WdfDpcCreate</b> creates a framework DPC object and registers an <a href="wdf.evtdpcfunc">EvtDpcFunc</a> callback function. To schedule execution of the callback function, the driver must call <a href="wdf.wdfdpcenqueue">WdfDpcEnqueue</a>. 

If your driver provides <a href="..\wdfobject\nc-wdfobject-evt_wdf_object_context_cleanup.md">EvtCleanupCallback</a> or <a href="..\wdfobject\nc-wdfobject-evt_wdf_object_context_destroy.md">EvtDestroyCallback</a> callback functions for the framework timer object, note that the framework calls these callback functions at IRQL = PASSIVE_LEVEL.

For more information about using DPC objects, see <a href="wdf.servicing_an_interrupt">Servicing an Interrupt</a>.

The following code example initializes a <a href="wdf.wdf_dpc_config_init">WDF_DPC_CONFIG_INIT</a> structure and then creates a DPC object. 

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
<dt>Wdfdpc.h (include Wdf.h)</dt>
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
&lt;=DISPATCH_LEVEL
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
<a href="wdf.wdfdpcenqueue">WdfDpcEnqueue</a>
</dt>
<dt>
<a href="wdf.wdf_dpc_config">WDF_DPC_CONFIG</a>
</dt>
<dt>
<a href="wdf.wdf_dpc_config_init">WDF_DPC_CONFIG_INIT</a>
</dt>
<dt>
<a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="wdf.wdf_object_attributes_init">WDF_OBJECT_ATTRIBUTES_INIT</a>
</dt>
<dt>
<a href="wdf.evtdpcfunc">EvtDpcFunc</a>
</dt>
<dt>
<a href="..\wdfdriver\nc-wdfdriver-evt_wdf_driver_device_add.md">EvtDriverDeviceAdd</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDpcCreate method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
