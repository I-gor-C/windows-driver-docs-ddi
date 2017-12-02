---
UID: NF.ntifs.PoRegisterSystemState
title: PoRegisterSystemState
author: windows-driver-content
description: The PoRegisterSystemState routine registers the system as busy due to certain activity.
old-location: kernel\poregistersystemstate.htm
old-project: kernel
ms.assetid: 851c694f-6c47-498c-8035-132a63c0fa62
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PoRegisterSystemState
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PoRegisterSystemState
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
req.irql: <=APC_LEVEL
req.iface: 
---

# PoRegisterSystemState function



## -description
<p>The <b>PoRegisterSystemState</b> routine registers the system as busy due to certain activity.</p>


## -syntax

````
PVOID PoRegisterSystemState(
  _Inout_ PVOID           StateHandle,
  _In_    EXECUTION_STATE Flags
);
````


## -parameters
<dl>

### -param StateHandle [in, out]

<dd>
<p>A pointer to a caller-supplied buffer for a registration state handle. The size, in bytes, of the buffer is <b>sizeof</b>(ULONG). If <b>NULL</b>, this is a new registration. If non-<b>NULL</b>, this parameter points to a handle that was returned by a previous call to <b>PoRegisterSystemState</b>.</p>
</dd>

### -param Flags [in]

<dd>
<p>Indicates the type of activity, as specified by a bitwise OR of one or more of the following values:</p>
<p></p>
<dl>

### -param ES_SYSTEM_REQUIRED

<dd>
<p>The system is not idle, regardless of apparent load.</p>
</dd>

### -param ES_DISPLAY_REQUIRED

<dd>
<p>Use of the display is required.</p>
</dd>

### -param ES_USER_PRESENT

<dd>
<p>A user is present.</p>
</dd>

### -param ES_CONTINUOUS

<dd>
<p>The settings are continuous and should remain in effect until explicitly changed.</p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p><b>PoRegisterSystemState</b> returns a handle to be used later to change or unregister the system busy state. It returns <b>NULL</b> if the handle could not be allocated.</p>

## -remarks
<p><b>PoRegisterSystemState</b> registers the system busy state as indicated by the flags. The registration persists until the caller explicitly changes it with another call to <b>PoRegisterSystemState</b> or cancels it with a call to <a href="..\wdm\nf-wdm-pounregistersystemstate.md">PoUnregisterSystemState</a>.</p>

<p>The <i>Flags</i> parameter specifies the type of activity in progress. Drivers can specify any combination of the flags.</p>

<p>Setting ES_CONTINUOUS makes the busy state persist until a driver explicitly changes or cancels it by calling <b>PoRegisterSystemState</b> or <b>PoUnregisterSystemState</b>.</p>

<p>A driver can set the system busy state to request that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559829">power manager</a> avoid system power state transitions out of the system working state (S0) while driver activity is occurring. Note, however, that under some circumstances (such as a critically low battery) the power manager may override this request and put the system to sleep anyway.</p>

<p>To set the system power state, call <a href="..\wdm\nf-wdm-posetsystemstate.md">PoSetSystemState</a>.</p>

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
<p>Available starting with Windows 2000.</p>
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
<p>&lt;=APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-posetsystemstate.md">PoSetSystemState</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-pounregistersystemstate.md">PoUnregisterSystemState</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PoRegisterSystemState routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
