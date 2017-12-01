---
UID: NF.wdm.ExUnregisterCallback
title: ExUnregisterCallback
author: windows-driver-content
description: The ExUnregisterCallback routine removes a callback routine previously registered with a callback object from the list of routines to be called during the notification process.
old-location: kernel\exunregistercallback.htm
old-project: kernel
ms.assetid: a7631732-fac5-458a-b644-eaffd5e53c31
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ExUnregisterCallback
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
req.alt-api: ExUnregisterCallback
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlExApcLte2, HwStorPortProhibitedDDIs
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
req.product: Windows 10 or later.
---

# ExUnregisterCallback function



## -description
<p>The <b>ExUnregisterCallback</b> routine removes a callback routine previously registered with a callback object from the list of routines to be called during the notification process.</p>


## -syntax

````
VOID ExUnregisterCallback(
  _Inout_ PVOID CbRegistration
);
````


## -parameters
<dl>

### -param <i>CbRegistration</i> [in, out]

<dd>
<p>Specifies the callback routine to unregister. This must be the value returned by <b>ExRegisterCallback</b> when the callback was registered. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>For more information about callback objects, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540718">Callback Objects</a>. </p>

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
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.wdm_irqlexapclte2">IrqlExApcLte2</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-excreatecallback.md">ExCreateCallback</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-exregistercallback.md">ExRegisterCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ExUnregisterCallback routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
