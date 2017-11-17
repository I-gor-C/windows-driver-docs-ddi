---
UID: NF.wdfdriver.WdfDriverCreate
title: WdfDriverCreate
author: windows-driver-content
description: The WdfDriverCreate method creates a framework driver object for the calling driver.
old-location: wdf\wdfdrivercreate.htm
ms.assetid: 2b8cea0f-bca0-4ffa-834b-d7c079cf93d8
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfdriver.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfDriverCreate
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: ChangeQueueState, DriverAttributeChanged, DriverCreate, KmdfIrql, KmdfIrql2, MiniportOnlyWdmDevice
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); 
WUDFx02000.dll (UMDF)
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: WdfDriverCreate
req.iface: 
req.product: Windows 10 or later.
---

# WdfDriverCreate function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfDriverCreate</b> method creates a framework driver object for the calling driver.</p>


## -syntax

````
NTSTATUS WdfDriverCreate(
  _In_      PDRIVER_OBJECT         DriverObject,
  _In_      PCUNICODE_STRING       RegistryPath,
  _In_opt_  PWDF_OBJECT_ATTRIBUTES DriverAttributes,
  _In_      PWDF_DRIVER_CONFIG     DriverConfig,
  _Out_opt_ WDFDRIVER              *Driver
);
````


## -parameters
<dl>

### -param <i>DriverObject</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544174">DRIVER_OBJECT</a> structure that represents a Windows Driver Model (WDM) driver object. The driver receives this pointer as input to its <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine.</p>
</dd>

### -param <i>RegistryPath</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> structure that contains the registry path string that the driver received as input to its <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine. </p>
</dd>

### -param <i>DriverAttributes</i> [in, optional]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure. (The structure's <b>ParentObject</b> member must be <b>NULL</b>.) This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES. </p>
</dd>

### -param <i>DriverConfig</i> [in]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff551300">WDF_DRIVER_CONFIG</a> structure.</p>
</dd>

### -param <i>Driver</i> [out, optional]

<dd>
<p>A pointer to a location that receives a handle to the new framework driver object. This parameter is optional and can be WDF_NO_HANDLE.</p>
</dd>
</dl>

## -returns
<p><b>WdfDriverCreate</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one of the following values:</p><dl>
<dt><b>STATUS_DRIVER_INTERNAL_ERROR</b></dt>
</dl><p>The driver called <a href="https://msdn.microsoft.com/library/windows/hardware/ff547175">WdfDriverCreate</a> more than once.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>A <a href="wdf.using_kernel_mode_driver_framework_with_non_pnp_drivers">non-Plug and Play (PnP) driver</a> specified an <a href="https://msdn.microsoft.com/b20db029-ee2c-4fb1-bd69-ccd2e37fdc9a">EvtDriverDeviceAdd</a> callback function.</p>

<p> </p>

<p>For more information about return values, see <a href="wdf.framework_object_creation_errors">Framework Object Creation Errors</a>.</p>

<p>This method might also return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A system bug check occurs if the <i>DriverObject</i>, <i>RegistryPath</i>, or <i>DriverConfig</i> parameter is <b>NULL</b>.</p>

## -remarks
<p>A driver that uses Kernel-Mode Driver Framework must call <b>WdfDriverCreate</b> from within its <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine, before calling any other framework routines. For more information about <b>DriverEntry</b>, see <b>DriverEntry for Framework-based Drivers</b>. </p>

<p>Before your driver calls <b>WdfDriverCreate</b>, the driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff551302">WDF_DRIVER_CONFIG_INIT</a> to initialize its <a href="https://msdn.microsoft.com/library/windows/hardware/ff551300">WDF_DRIVER_CONFIG</a> structure.</p>

<p>The framework driver object is the top of your driver's tree of framework objects and therefore does not have a parent object.</p>

<p>If your driver provides <a href="https://msdn.microsoft.com/aba2efca-7d1f-4594-af65-13356f0e3f8b">EvtCleanupCallback</a> or <a href="https://msdn.microsoft.com/4c3b08d2-bb25-40bd-b2fc-1b9ea2d452b3">EvtDestroyCallback</a> callback functions for the driver object, note that the framework calls these callback functions at IRQL = PASSIVE_LEVEL.</p>

<p>The following code example is a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine that initializes a WDF_DRIVER_CONFIG structure and then creates a framework driver object.</p>

<p>A driver that uses Kernel-Mode Driver Framework must call <b>WdfDriverCreate</b> from within its <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine, before calling any other framework routines. For more information about <b>DriverEntry</b>, see <b>DriverEntry for Framework-based Drivers</b>. </p>

<p>Before your driver calls <b>WdfDriverCreate</b>, the driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff551302">WDF_DRIVER_CONFIG_INIT</a> to initialize its <a href="https://msdn.microsoft.com/library/windows/hardware/ff551300">WDF_DRIVER_CONFIG</a> structure.</p>

<p>The framework driver object is the top of your driver's tree of framework objects and therefore does not have a parent object.</p>

<p>If your driver provides <a href="https://msdn.microsoft.com/aba2efca-7d1f-4594-af65-13356f0e3f8b">EvtCleanupCallback</a> or <a href="https://msdn.microsoft.com/4c3b08d2-bb25-40bd-b2fc-1b9ea2d452b3">EvtDestroyCallback</a> callback functions for the driver object, note that the framework calls these callback functions at IRQL = PASSIVE_LEVEL.</p>

<p>The following code example is a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine that initializes a WDF_DRIVER_CONFIG structure and then creates a framework driver object.</p>

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
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdriver.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975067">ChangeQueueState</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544951">DriverAttributeChanged</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975092">MiniportOnlyWdmDevice</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544174">DRIVER_OBJECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b20db029-ee2c-4fb1-bd69-ccd2e37fdc9a">EvtDriverDeviceAdd</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551300">WDF_DRIVER_CONFIG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551302">WDF_DRIVER_CONFIG_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDriverCreate method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
