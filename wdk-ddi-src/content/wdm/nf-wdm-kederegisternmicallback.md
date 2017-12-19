---
UID: NF.wdm.KeDeregisterNmiCallback
title: KeDeregisterNmiCallback function
author: windows-driver-content
description: The KeDeregisterNmiCallback routine deregisters a nonmaskable interrupt (NMI) callback registered by KeRegisterNmiCallback.
old-location: kernel\kederegisternmicallback.htm
old-project: kernel
ms.assetid: 45022490-8130-449c-8ec9-380be0a3a03d
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: KeDeregisterNmiCallback
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Server 2003 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeDeregisterNmiCallback
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlKeApcLte2, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= APC_LEVEL
req.product: Windows 10 or later.
---

# KeDeregisterNmiCallback function



## -description
The <b>KeDeregisterNmiCallback</b> routine deregisters a nonmaskable interrupt (NMI) callback registered by <a href="kernel.keregisternmicallback">KeRegisterNmiCallback</a>.



## -syntax

````
NTSTATUS KeDeregisterNmiCallback(
  _In_ PVOID Handle
);
````


## -parameters

### -param Handle [in]

Specifies the value returned by <a href="kernel.keregisternmicallback">KeRegisterNmiCallback</a> when the NMI callback was registered. 


## -returns
The <b>KeDeregisterNmiCallback</b> routine returns STATUS_SUCCESS if the callback is successfully removed. It returns STATUS_INVALID_HANDLE if no callback matching the provided <i>Handle</i> value is found.


## -remarks


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
Version

</th>
<td width="70%">
Available in Windows Server 2003 and later versions of Windows.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= APC_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.wdm_irqlkeapclte2">IrqlKeApcLte2</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.keregisternmicallback">KeRegisterNmiCallback</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeDeregisterNmiCallback routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

