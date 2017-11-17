---
UID: NF.wdfregistry.WdfRegistryWdmGetHandle
title: WdfRegistryWdmGetHandle
author: windows-driver-content
description: The WdfRegistryWdmGetHandle method returns a Windows Driver Model (WDM) handle to the registry key that a specified framework registry-key object represents.
old-location: wdf\wdfregistrywdmgethandle.htm
ms.assetid: 60638048-9009-4943-ba61-b724612852df
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfregistry.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfRegistryWdmGetHandle
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate
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
ms.keywords: WdfRegistryWdmGetHandle
req.iface: 
req.product: Windows 10 or later.
---

# WdfRegistryWdmGetHandle function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfRegistryWdmGetHandle</b> method returns a Windows Driver Model (WDM) handle to the registry key that a specified framework registry-key object represents.</p>


## -syntax

````
HANDLE WdfRegistryWdmGetHandle(
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
<p><b>WdfRegistryWdmGetHandle</b> returns a WDM handle to a registry key. </p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>A KMDF driver can pass the returned WDM handle to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557342">ZwXxx routines</a> that accept a WDM handle as input.</p>

<p>A UMDF driver can pass the returned handle to APIs that require an HKEY, such as <a href="base.regenumkeyex">RegEnumKeyEx</a>.</p>

<p>The handle that the <b>WdfRegistryWdmGetHandle</b> method returns is valid until the registry-key object is deleted. If the driver provides an <a href="https://msdn.microsoft.com/aba2efca-7d1f-4594-af65-13356f0e3f8b">EvtCleanupCallback</a> function for the registry-key object, the pointer is valid until the callback function returns.</p>

<p>For more information about registry-key objects, see <a href="wdf.using_the_registry_in_kmdf_drivers">Using the Registry in Framework-Based Drivers</a>.</p>

<p>The following code example obtains a WDM handle to the registry key that a specified framework registry-key object represents.</p>

<p>A KMDF driver can pass the returned WDM handle to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557342">ZwXxx routines</a> that accept a WDM handle as input.</p>

<p>A UMDF driver can pass the returned handle to APIs that require an HKEY, such as <a href="base.regenumkeyex">RegEnumKeyEx</a>.</p>

<p>The handle that the <b>WdfRegistryWdmGetHandle</b> method returns is valid until the registry-key object is deleted. If the driver provides an <a href="https://msdn.microsoft.com/aba2efca-7d1f-4594-af65-13356f0e3f8b">EvtCleanupCallback</a> function for the registry-key object, the pointer is valid until the callback function returns.</p>

<p>For more information about registry-key objects, see <a href="wdf.using_the_registry_in_kmdf_drivers">Using the Registry in Framework-Based Drivers</a>.</p>

<p>The following code example obtains a WDM handle to the registry key that a specified framework registry-key object represents.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>
</td>
</tr>
</table>