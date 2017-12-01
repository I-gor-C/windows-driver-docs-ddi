---
UID: NF.wdm.PoSetSystemState
title: PoSetSystemState
author: windows-driver-content
description: Drivers call the PoSetSystemState routine to indicate that the system is active.
old-location: kernel\posetsystemstate.htm
old-project: kernel
ms.assetid: b62db582-381a-457f-9755-d8667c7561af
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PoSetSystemState
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PoSetSystemState
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
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# PoSetSystemState function



## -description
<p>Drivers call the <b>PoSetSystemState</b> routine to indicate that the system is active.</p>


## -syntax

````
VOID PoSetSystemState(
  _In_ EXECUTION_STATE Flags
);
````


## -parameters
<dl>

### -param <i>Flags</i> [in]

<dd>
<p>Indicates the system activity, as specified by a bitwise OR of one or more of the following values:</p>
<p></p>
<dl>

### -param <a id="ES_SYSTEM_REQUIRED"></a><a id="es_system_required"></a>ES_SYSTEM_REQUIRED

<dd>
<p>The system is not idle, regardless of apparent load.</p>
</dd>

### -param <a id="ES_DISPLAY_REQUIRED"></a><a id="es_display_required"></a>ES_DISPLAY_REQUIRED

<dd>
<p>Use of the display is required.</p>
</dd>

### -param <a id="ES_USER_PRESENT"></a><a id="es_user_present"></a>ES_USER_PRESENT

<dd>
<p>A user is present.</p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A driver calls <b>PoSetSystemState</b> to set flags indicating that system activity is occurring. Unlike <a href="..\ntifs\nf-ntifs-poregistersystemstate.md">PoRegisterSystemState</a>, this routine does not allow the driver to set a persistent busy state. </p>

<p>The <i>Flags</i> parameter specifies the type of activity occurring. Drivers can specify any combination of the flags.</p>

<p>Drivers can set the system busy state to request that the system avoid leaving of the working state while driver activity is occurring. Note, however, that under some circumstances (such as a critically low battery) the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559829">power manager</a> may override this request and put the system to sleep anyway. </p>

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
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntifs\nf-ntifs-poregistersystemstate.md">PoRegisterSystemState</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-pounregistersystemstate.md">PoUnregisterSystemState</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PoSetSystemState routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
