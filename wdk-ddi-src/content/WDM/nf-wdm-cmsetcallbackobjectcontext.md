---
UID: NF.wdm.CmSetCallbackObjectContext
title: CmSetCallbackObjectContext
author: windows-driver-content
description: The CmSetCallbackObjectContext routine associates specified context information with a specified registry object.
old-location: kernel\cmsetcallbackobjectcontext.htm
ms.assetid: 69e85037-5c60-404a-b251-dc1622c7d818
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CmSetCallbackObjectContext
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= APC_LEVEL
ms.keywords: CmSetCallbackObjectContext
req.iface: 
req.product: Windows 10 or later.
---

# CmSetCallbackObjectContext function



## -description
<p>The <b>CmSetCallbackObjectContext</b> routine associates specified context information with a specified registry object.</p>


## -syntax

````
NTSTATUS CmSetCallbackObjectContext(
  _Inout_   PVOID          Object,
  _In_      PLARGE_INTEGER Cookie,
  _In_      PVOID          NewContext,
  _Out_opt_ PVOID          *OldContext
);
````


## -parameters
<dl>

### -param <i>Object</i> [in, out]

<dd>
<p>A pointer to the registry key object that the driver is providing context information for. The driver obtains this pointer from the <b>ResultObject</b> member of one of the following structures:</p>
<dl>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560920">REG_CREATE_KEY_INFORMATION</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560922">REG_CREATE_KEY_INFORMATION_V1</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560957">REG_OPEN_KEY_INFORMATION</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560959">REG_OPEN_KEY_INFORMATION_V1</a>
</dd>
</dl>
</dd>

### -param <i>Cookie</i> [in]

<dd>
<p>A pointer to a LARGE_INTEGER value that identifies the callback routine to associate the context with. The <a href="https://msdn.microsoft.com/library/windows/hardware/ff541921">CmRegisterCallbackEx</a> routine provided this value when you registered the callback routine.</p>
</dd>

### -param <i>NewContext</i> [in]

<dd>
<p>A pointer to driver-defined context information.</p>
</dd>

### -param <i>OldContext</i> [out, optional]

<dd>
<p>A pointer to a location that receives a pointer to context information that the driver previously associated with the specified object and cookie. This parameter is optional and can be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p><b>CmSetCallbackObjectContext</b> returns STATUS_SUCCESS or another appropriate <a href="https://msdn.microsoft.com/fe823930-e3ff-4c95-a640-bb6470c95d1d">NTSTATUS</a>-typed value. </p>

## -remarks
<p>The <b>CmSetCallbackObjectContext</b> routine is available starting with Windows Vista.</p>

<p>A driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff560903">RegistryCallback</a> routine can call <b>CmSetCallbackObjectContext</b> for any registry key object after the object has been created or opened (that is, during a post-notification for a create operation, an open operation, or any subsequent notification up to the pre-notification of handle closure).</p>

<p>If a driver calls <b>CmSetCallbackObjectContext</b>, the driver's <i>RegistryCallback</i> routine will receive a <b>RegNtCallbackObjectContextCleanup</b> notification after the key object's handle has been closed or after the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff541928">CmUnRegisterCallback</a> to unregister the <i>RegistryCallback</i> routine. When the <i>RegistryCallback</i> routine receives this notification, the routine should release any resources that it allocated for the object's context.</p>

<p>For more information about <b>CmSetCallbackObjectContext</b> and filtering registry operations, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545879">Filtering Registry Calls</a>.</p>

<p>The <b>CmSetCallbackObjectContext</b> routine is available starting with Windows Vista.</p>

<p>A driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff560903">RegistryCallback</a> routine can call <b>CmSetCallbackObjectContext</b> for any registry key object after the object has been created or opened (that is, during a post-notification for a create operation, an open operation, or any subsequent notification up to the pre-notification of handle closure).</p>

<p>If a driver calls <b>CmSetCallbackObjectContext</b>, the driver's <i>RegistryCallback</i> routine will receive a <b>RegNtCallbackObjectContextCleanup</b> notification after the key object's handle has been closed or after the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff541928">CmUnRegisterCallback</a> to unregister the <i>RegistryCallback</i> routine. When the <i>RegistryCallback</i> routine receives this notification, the routine should release any resources that it allocated for the object's context.</p>

<p>For more information about <b>CmSetCallbackObjectContext</b> and filtering registry operations, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545879">Filtering Registry Calls</a>.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows Vista.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541921">CmRegisterCallbackEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541928">CmUnRegisterCallback</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560920">REG_CREATE_KEY_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560922">REG_CREATE_KEY_INFORMATION_V1</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560903">RegistryCallback</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560957">REG_OPEN_KEY_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560959">REG_OPEN_KEY_INFORMATION_V1</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20CmSetCallbackObjectContext routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
