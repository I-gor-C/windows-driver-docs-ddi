---
UID: NF.wdm.PoUnregisterPowerSettingCallback
title: PoUnregisterPowerSettingCallback
author: windows-driver-content
description: The PoUnregisterPowerSettingCallback routine unregisters a power-setting callback routine that a driver previously registered by calling the PoRegisterPowerSettingCallback routine.
old-location: kernel\pounregisterpowersettingcallback.htm
old-project: kernel
ms.assetid: 900db70b-4cdb-41e7-a4cf-0dc435b9fe7d
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PoUnregisterPowerSettingCallback
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PoUnregisterPowerSettingCallback
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
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# PoUnregisterPowerSettingCallback function



## -description
<p>The <b>PoUnregisterPowerSettingCallback</b> routine unregisters a power-setting callback routine that a driver previously registered by calling the <a href="..\wdm\nf-wdm-poregisterpowersettingcallback.md">PoRegisterPowerSettingCallback</a> routine.</p>


## -syntax

````
NTSTATUS PoUnregisterPowerSettingCallback(
  _Inout_ PVOID Handle
);
````


## -parameters
<dl>

### -param Handle [in, out]

<dd>
<p>A handle to a callback routine that a driver registered by calling <b>PoRegisterPowerSettingCallback</b>.</p>
</dd>
</dl>

## -returns
<p><b>PoUnregisterPowerSettingCallback</b> returns one of the following:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The callback routine was unregistered.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The <i>Handle</i> value is not a valid handle to a power setting callback routine.</p>

<p> </p>

## -remarks
<p>A driver calls <b>PoUnregisterPowerSettingCallback</b> to unregister a power setting callback routine that the driver previously registered by calling <b>PoRegisterPowerSettingCallback</b>.</p>

<p>A driver must call <b>PoUnregisterPowerSettingCallback</b> to unregister each callback routine that it previously registered. All callback routines registered by a driver should be unregistered in the <i>Unload</i> routine of the driver.</p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-poregisterpowersettingcallback.md">PoRegisterPowerSettingCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PoUnregisterPowerSettingCallback routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
