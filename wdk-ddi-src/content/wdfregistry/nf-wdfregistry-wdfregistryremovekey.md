---
UID: NF.wdfregistry.WdfRegistryRemoveKey
title: WdfRegistryRemoveKey
author: windows-driver-content
description: The WdfRegistryRemoveKey method removes the registry key that is associated with a specified framework registry-key object and then deletes the registry-key object.
old-location: wdf\wdfregistryremovekey.htm
old-project: wdf
ms.assetid: b23d1c2f-15f0-4b9e-8a10-9b81056fa509
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfRegistryRemoveKey
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfregistry.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfRegistryRemoveKey
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
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
req.iface: 
req.product: Windows 10 or later.
---

# WdfRegistryRemoveKey function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfRegistryRemoveKey</b> method removes the registry key that is associated with a specified framework registry-key object and then deletes the registry-key object.</p>


## -syntax

````
NTSTATUS WdfRegistryRemoveKey(
  _In_ WDFKEY Key
);
````


## -parameters
<dl>

### -param <i>Key</i> [in]

<dd>
<p>A handle to a registry-key object that represents an opened registry key.</p>
</dd>
</dl>

## -returns
<p><b>WdfRegistryRemoveKey</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, the method might return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549930">WdfRegistryRemoveKey</a> was not called at IRQL = PASSIVE_LEVEL. </p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The driver did not open the registry key with deletion access.</p><dl>
<dt><b>STATUS_NOT_IMPLEMENTED</b></dt>
</dl><p>See the Remarks section.</p>

<p> </p>

<p>This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p class="note">From a KMDF driver, do not call <b>WdfRegistryRemoveKey</b> and then <a href="https://msdn.microsoft.com/library/windows/hardware/ff549914">WdfRegistryClose</a> on the same key. The WDFKEY is no longer valid after <b>WdfRegistryRemoveKey</b> returns.</p>

<p>While it is legal for a UMDF driver to call <b>WdfRegistryRemoveKey</b>, the call always returns <b>STATUS_NOT_IMPLEMENTED</b>.   To delete the WDFKEY object, a UMDF driver should instead call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549914">WdfRegistryClose</a>.</p>

<p><b>WdfRegistryRemoveKey</b> does not return STATUS_SUCCESS if the specified key object represents a registry key that has subkeys. In other words, the driver must remove the subkeys first.</p>

<p>For more information about registry-key objects, see <a href="wdf.using_the_registry_in_kmdf_drivers">Using the Registry in Framework-Based Drivers</a>.</p>

<p>The following code example removes a registry key and deletes the registry-key object.</p><p class="note">From a KMDF driver, do not call <b>WdfRegistryRemoveKey</b> and then <a href="https://msdn.microsoft.com/library/windows/hardware/ff549914">WdfRegistryClose</a> on the same key. The WDFKEY is no longer valid after <b>WdfRegistryRemoveKey</b> returns.</p>

<p>While it is legal for a UMDF driver to call <b>WdfRegistryRemoveKey</b>, the call always returns <b>STATUS_NOT_IMPLEMENTED</b>.   To delete the WDFKEY object, a UMDF driver should instead call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549914">WdfRegistryClose</a>.</p>

<p><b>WdfRegistryRemoveKey</b> does not return STATUS_SUCCESS if the specified key object represents a registry key that has subkeys. In other words, the driver must remove the subkeys first.</p>

<p>For more information about registry-key objects, see <a href="wdf.using_the_registry_in_kmdf_drivers">Using the Registry in Framework-Based Drivers</a>.</p>

<p>The following code example removes a registry key and deletes the registry-key object.</p>

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
<dt>Wdfregistry.h (include Wdf.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>